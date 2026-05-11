import os

from fastapi import APIRouter, Depends, HTTPException, Query, Request
from fastapi.responses import HTMLResponse, JSONResponse

from ..auth import get_current_user, require_admin, hash_password
from ..crypto import make_fernet, sign_unsubscribe_token
from ..store import (
    export_suppressions, import_suppressions,
    list_users, create_user, delete_user,
    create_network, get_network, list_networks, update_network, delete_network,
    create_offer, get_offer, list_offers, update_offer, delete_offer,
    get_dashboard, get_all_statistics,
    get_unsubscribers_for_target,
    generate_feed_token,
    get_offer_csv_data,
    get_offer_csv_data_by_tld,
    get_offer_statistics,
)
from ..models import (
    GenerateLinkRequest, GenerateLinkResponse, GenerateFeedRequest,
    CreateUserRequest, UserResponse,
    CreateNetworkRequest, UpdateNetworkRequest, NetworkResponse,
    CreateOfferRequest, UpdateOfferRequest, OfferResponse,
)

router = APIRouter()
BASE_URL = os.environ.get("BASE_URL", "http://localhost:8000")
fernet = make_fernet(os.environ["SECRET_KEY"])


# ── Layout ──

_ADMIN_TABS = """
<div class="tabs">
  <a href="/admin/generate" class="tab %s">Generate</a>
  <a href="/admin/networks" class="tab %s">Networks</a>
  <a href="/admin/offers" class="tab %s">Offers</a>
  <a href="/admin/unsubscribers" class="tab %s">Unsubscribers</a>
  <a href="/admin/dashboard" class="tab %s">Dashboard</a>
  <a href="/admin/users" class="tab %s">Users</a>
</div>
"""

_PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<style>
*{box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;background:#f5f5f5;margin:0;padding:0;font-size:16px}
.nav{background:#1a1a2e;color:white;padding:0.6rem 1rem;display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:0.5rem}
.nav .user{font-size:0.75rem;color:#999;word-break:break-all}
.nav a{color:#ccc;text-decoration:none;margin-left:0.75rem;font-size:0.8rem;white-space:nowrap}
.nav a:hover{color:white}
.tabs{display:flex;flex-wrap:wrap;background:#fff;border-bottom:1px solid #ddd;padding:0 0.5rem;overflow-x:auto;-webkit-overflow-scrolling:touch}
.tab{padding:0.6rem 0.8rem;text-decoration:none;color:#666;font-size:0.8rem;border-bottom:2px solid transparent;white-space:nowrap}
.tab.active{color:#1976d2;border-bottom-color:#1976d2;font-weight:600}
.tab:hover{color:#333}
.container{max-width:960px;margin:1rem auto;padding:0 0.75rem}
.card{background:white;padding:1rem 1.25rem;border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,0.08);margin-bottom:1rem;overflow:hidden}
.card h2{margin:0 0 0.75rem;font-size:1.1rem;color:#333;word-wrap:break-word}
.btn{padding:0.5rem 0.9rem;background:#1976d2;color:white;border:none;border-radius:5px;cursor:pointer;font-size:0.85rem;min-height:36px;touch-action:manipulation}
.btn:hover{background:#1565c0}
.btn-sm{padding:0.35rem 0.55rem;font-size:0.75rem;background:#1976d2;color:white;border:none;border-radius:4px;cursor:pointer;min-height:30px;touch-action:manipulation;white-space:nowrap}
.btn-sm:hover{background:#1565c0}
.btn-del{padding:0.35rem 0.55rem;font-size:0.75rem;background:#d32f2f;color:white;border:none;border-radius:4px;cursor:pointer;min-height:30px;touch-action:manipulation}
.btn-del:hover{background:#b71c1c}
input,select{width:100%%;padding:0.5rem;border:1px solid #ccc;border-radius:5px;font-size:0.9rem;margin-bottom:0.75rem;min-height:38px}
input:focus,select:focus{outline:none;border-color:#1976d2;box-shadow:0 0 0 2px rgba(25,118,210,0.15)}
.table-wrap{width:100%%;overflow-x:auto;-webkit-overflow-scrolling:touch}
table{width:100%%;border-collapse:collapse;min-width:auto}
th,td{text-align:left;padding:0.5rem 0.4rem;border-bottom:1px solid #eee;font-size:0.82rem;word-wrap:break-word;word-break:break-word}
th{font-weight:600;color:#555;font-size:0.75rem;text-transform:uppercase;white-space:nowrap}
.flex{display:flex;gap:0.35rem;align-items:center;flex-wrap:wrap}
.msg{padding:0.5rem 0.6rem;border-radius:5px;margin-bottom:0.75rem;display:none;font-size:0.82rem;word-wrap:break-word}
.msg.ok{background:#e8f5e9;color:#2e7d32;display:block}
.msg.err{background:#ffebee;color:#d32f2f;display:block}
.muted{color:#999;font-size:0.78rem}
.hidden{display:none}
code{word-break:break-all;font-size:0.7rem}
@media(max-width:600px){.container{padding:0 0.5rem}.card{padding:0.75rem 0.9rem;border-radius:8px}.card h2{font-size:1rem}.nav{padding:0.5rem 0.75rem;flex-direction:column;align-items:stretch;text-align:center}.nav>div{display:flex;justify-content:center;flex-wrap:wrap}.tabs{padding:0 0.25rem}.tab{padding:0.5rem 0.6rem;font-size:0.75rem}th,td{padding:0.4rem 0.3rem;font-size:0.75rem}input,select{font-size:0.85rem;min-height:40px}.btn,.btn-sm,.btn-del{min-height:34px;padding:0.4rem 0.6rem;font-size:0.75rem}.flex{gap:0.25rem}table{font-size:0.75rem}}
</style>
</head>
<body>
<div class="nav">
  <strong>Suppression Manager</strong>
  <div>
    <span class="user">%s (%s)</span>
    <a href="/auth/logout" onclick="fetch('/auth/logout',{method:'POST'}).then(()=>location.href='/auth/login');return false">Logout</a>
  </div>
</div>
%s
<div class="container">
%s
</div>
</body>
</html>"""


def _page(title, user_email, user_role, active_tab, content):
    tabs = _ADMIN_TABS % tuple(active_tab if i == ["generate","networks","offers","unsubscribers","dashboard","users"].index(active_tab) else "" for i in range(6))
    return _PAGE % (title, user_email, user_role, tabs, content)


# ── Helpers ──

def _json_ok(data):
    return JSONResponse(content=data)


# ── Root ──

@router.get("/admin", response_class=HTMLResponse)
def admin_root():
    from fastapi.responses import RedirectResponse
    return RedirectResponse(url="/admin/generate")


# ── Generate ──

@router.get("/admin/generate", response_class=HTMLResponse)
def generate_page(payload: dict = Depends(get_current_user)):
    nets = list_networks(fernet)
    net_opts = "".join(f'<option value="{n.id}">{n.name} ({n.id})</option>' for n in nets)
    offers_json = {}
    for n in nets:
        offs = list_offers(fernet, n.id)
        offers_json[n.id] = [{"id": o.id, "name": o.name} for o in offs]
    import json
    offers_data = json.dumps(offers_json)

    content = f"""
<div class="card">
  <h2>Generate Unsubscribe Link</h2>
  <div id="msg" class="msg"></div>
  <form id="form">
    <label>Network</label>
    <select id="network" name="network_id">
      <option value="">-- Select Network --</option>
      {net_opts}
    </select>
    <div id="offer-field" class="hidden">
      <label>Offer</label>
      <select id="offer" name="offer_id">
        <option value="">-- Select Offer --</option>
      </select>
    </div>
    <button type="submit" class="btn" style="margin-top:0.5rem">Generate Link</button>
  </form>
  <div id="result" style="display:none;margin-top:1rem;padding:1rem;background:#e8f5e9;border-radius:6px;word-break:break-all">
    <strong>Unsubscribe URL:</strong><br>
    <a id="result-url" href="#" target="_blank"></a><br><br>
    <strong>Token:</strong><br>
    <code id="result-token" style="font-size:0.75rem;word-break:break-all"></code><br><br>
    <button class="btn" onclick="navigator.clipboard.writeText(document.getElementById('result-url').href).then(()=>alert('Copied!'))">Copy URL</button>
  </div>
</div>
<script>
const offers = {offers_data};
document.getElementById('network').addEventListener('change',function(){{
  const sel = document.getElementById('offer');
  sel.innerHTML = '<option value="">-- Select Offer --</option>';
  const list = offers[this.value]||[];
  for(const o of list) sel.innerHTML += '<option value="'+o.id+'">'+o.name+' ('+o.id+')</option>';
  document.getElementById('offer-field').classList.toggle('hidden',!this.value);
}});
document.getElementById('form').addEventListener('submit',async function(e){{
  e.preventDefault();
  const nid = document.getElementById('network').value;
  const oid = document.getElementById('offer').value;
  if(!nid){{msg('Select a network','err');return;}}
  const body = oid ? {{level:'offer',network_id:nid,offer_id:oid}} : {{level:'network',network_id:nid}};
  const res=await fetch('/admin/generate',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify(body)}});
  if(!res.ok){{const d=await res.json();msg(d.detail||'Error','err');return;}}
  const data=await res.json();
  document.getElementById('result-url').href=data.unsubscribe_url;
  document.getElementById('result-url').textContent=data.unsubscribe_url;
  document.getElementById('result-token').textContent=data.token;
  document.getElementById('result').style.display='block';
  document.getElementById('msg').style.display='none';
}});
function msg(t,c){{const el=document.getElementById('msg');el.textContent=t;el.className='msg '+c;el.style.display='block'}}
</script>"""
    return _page("Generate Link", payload["sub"], payload["role"], "generate", content)


@router.post("/admin/generate", response_model=GenerateLinkResponse)
def generate_link(req: GenerateLinkRequest, _=Depends(get_current_user)):
    secret = os.environ["SECRET_KEY"]
    if req.level == "network":
        net = get_network(fernet, req.network_id)
        if not net:
            raise HTTPException(400, "Network not found")
        target = net.id
        token = sign_unsubscribe_token(secret, req.level, target)
    elif req.level == "offer":
        off = get_offer(fernet, req.offer_id)
        if not off:
            raise HTTPException(400, "Offer not found")
        target = off.id
        token = sign_unsubscribe_token(secret, req.level, target)
    else:
        raise HTTPException(400, "Invalid level")
    url = f"{BASE_URL}/u?t={token}"
    return GenerateLinkResponse(unsubscribe_url=url, token=token)


# ── Networks ──

@router.get("/admin/networks", response_class=HTMLResponse)
def networks_page(payload: dict = Depends(require_admin)):
    nets = list_networks(fernet)
    rows = "".join(
        f'<tr><td>{n.id}</td><td>{n.name}</td><td>{n.created_at}</td>'
        f'<td class="flex">'
        f'<button class="btn-sm" onclick="editNet(\'{n.id}\',\'{n.name}\')">Edit</button>'
        f'<button class="btn-del" onclick="delNet(\'{n.id}\')">Delete</button></td></tr>'
        for n in nets
    )
    content = f"""
<div class="card">
  <h2>Add Network</h2>
  <div id="msg" class="msg"></div>
  <form id="form">
    <label>Network ID</label>
    <input type="text" id="net-id" placeholder="e.g. clickbank" required>
    <label>Network Name</label>
    <input type="text" id="net-name" placeholder="e.g. ClickBank" required>
    <button type="submit" class="btn">Add Network</button>
  </form>
</div>
<div class="card">
  <h2>All Networks</h2>
  <div class="table-wrap"><table><thead><tr><th>ID</th><th>Name</th><th>Created</th><th></th></tr></thead>
  <tbody>{rows or '<tr><td colspan="4" class="muted">No networks yet</td></tr>'}</tbody></table></div>
</div>
<script>
document.getElementById('form').addEventListener('submit',async function(e){{
  e.preventDefault();
  const id=document.getElementById('net-id').value.trim();
  const name=document.getElementById('net-name').value.trim();
  const res=await fetch('/admin/networks',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{id,name}})}});
  if(!res.ok){{const d=await res.json();msg(d.detail||'Error','err');return;}}
  location.reload();
}});
async function delNet(id){{
  if(!confirm('Delete network '+id+'? All its offers will also be deleted.'))return;
  const res=await fetch('/admin/networks/'+encodeURIComponent(id),{{method:'DELETE'}});
  if(!res.ok){{const d=await res.json();msg(d.detail||'Error','err');return;}}
  location.reload();
}}
async function editNet(id,name){{
  const newName=prompt('New name for '+id+':',name);
  if(!newName||newName===name)return;
  const res=await fetch('/admin/networks/'+encodeURIComponent(id),{{method:'PUT',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{name:newName}})}});
  if(!res.ok){{const d=await res.json();msg(d.detail||'Error','err');return;}}
  location.reload();
}}
function msg(t,c){{const el=document.getElementById('msg');el.textContent=t;el.className='msg '+c;el.style.display='block'}}
</script>"""
    return _page("Networks", payload["sub"], payload["role"], "networks", content)


@router.post("/admin/networks")
def create_network_endpoint(req: CreateNetworkRequest, _=Depends(require_admin)):
    try:
        net = create_network(fernet, req.id, req.name)
        return NetworkResponse(id=net.id, name=net.name, created_at=net.created_at)
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.put("/admin/networks/{net_id}")
def update_network_endpoint(net_id: str, req: UpdateNetworkRequest, _=Depends(require_admin)):
    net = update_network(fernet, net_id, req.name)
    if not net:
        raise HTTPException(404, "Network not found")
    return NetworkResponse(id=net.id, name=net.name, created_at=net.created_at)


@router.delete("/admin/networks/{net_id}")
def delete_network_endpoint(net_id: str, _=Depends(require_admin)):
    if not delete_network(fernet, net_id):
        raise HTTPException(404, "Network not found")
    return {"status": "deleted"}


@router.get("/admin/networks/{net_id}/offers")
def get_network_offers(net_id: str, _=Depends(require_admin)):
    offs = list_offers(fernet, net_id)
    return [{"id": o.id, "name": o.name} for o in offs]


# ── Offers ──

@router.get("/admin/offers", response_class=HTMLResponse)
def offers_page(payload: dict = Depends(require_admin)):
    nets = list_networks(fernet)
    net_opts = "".join(f'<option value="{n.id}">{n.name}</option>' for n in nets)
    offs = list_offers(fernet)
    rows = "".join(
        f'<tr><td>{o.id}</td><td>{o.name}</td><td>{o.network_id}</td><td>{o.created_at}</td>'
        f'<td class="flex">'
        f'<a href="/admin/offers/{o.id}" class="btn-sm" style="background:#6a1b9a;color:white;text-decoration:none">Details</a>'
        f'<button class="btn-sm" onclick="editOff(\'{o.id}\',\'{o.name}\')">Edit</button>'
        f'<button class="btn-del" onclick="delOff(\'{o.id}\')">Delete</button></td></tr>'
        for o in offs
    )
    content = f"""
<div class="card">
  <h2>Add Offer</h2>
  <div id="msg" class="msg"></div>
  <form id="form">
    <label>Offer ID</label>
    <input type="text" id="off-id" placeholder="e.g. premium-plan" required>
    <label>Offer Name</label>
    <input type="text" id="off-name" placeholder="e.g. Premium Plan" required>
    <label>Network</label>
    <select id="off-net">{net_opts}</select>
    <button type="submit" class="btn">Add Offer</button>
  </form>
</div>
<div class="card">
  <h2>All Offers</h2>
  <div class="table-wrap"><table><thead><tr><th>ID</th><th>Name</th><th>Network</th><th>Created</th><th></th></tr></thead>
  <tbody>{rows or '<tr><td colspan="5" class="muted">No offers yet</td></tr>'}</tbody></table></div>
</div>
<script>
document.getElementById('form').addEventListener('submit',async function(e){{
  e.preventDefault();
  const id=document.getElementById('off-id').value.trim();
  const name=document.getElementById('off-name').value.trim();
  const net=document.getElementById('off-net').value;
  const res=await fetch('/admin/offers',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{id,name,network_id:net}})}});
  if(!res.ok){{const d=await res.json();msg(d.detail||'Error','err');return;}}
  location.reload();
}});
async function delOff(id){{
  if(!confirm('Delete offer '+id+'?'))return;
  const res=await fetch('/admin/offers/'+encodeURIComponent(id),{{method:'DELETE'}});
  if(!res.ok){{const d=await res.json();msg(d.detail||'Error','err');return;}}
  location.reload();
}}
async function editOff(id,name){{
  const newName=prompt('New name for '+id+':',name);
  if(!newName||newName===name)return;
  const res=await fetch('/admin/offers/'+encodeURIComponent(id),{{method:'PUT',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{name:newName}})}});
  if(!res.ok){{const d=await res.json();msg(d.detail||'Error','err');return;}}
  location.reload();
}}
function msg(t,c){{const el=document.getElementById('msg');el.textContent=t;el.className='msg '+c;el.style.display='block'}}
</script>"""
    return _page("Offers", payload["sub"], payload["role"], "offers", content)


@router.post("/admin/offers")
def create_offer_endpoint(req: CreateOfferRequest, _=Depends(require_admin)):
    try:
        off = create_offer(fernet, req.id, req.name, req.network_id)
        return OfferResponse(id=off.id, name=off.name, network_id=off.network_id, created_at=off.created_at)
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.put("/admin/offers/{offer_id}")
def update_offer_endpoint(offer_id: str, req: UpdateOfferRequest, _=Depends(require_admin)):
    off = update_offer(fernet, offer_id, req.name)
    if not off:
        raise HTTPException(404, "Offer not found")
    return OfferResponse(id=off.id, name=off.name, network_id=off.network_id, created_at=off.created_at)


@router.delete("/admin/offers/{offer_id}")
def delete_offer_endpoint(offer_id: str, _=Depends(require_admin)):
    if not delete_offer(fernet, offer_id):
        raise HTTPException(404, "Offer not found")
    return {"status": "deleted"}


# ── Offer Details ──

@router.get("/admin/offers/{offer_id}/stats")
def offer_stats_json(offer_id: str, _=Depends(require_admin)):
    off = get_offer(fernet, offer_id)
    if not off:
        raise HTTPException(404, "Offer not found")
    net = get_network(fernet, off.network_id)
    net_name = net.name if net else ""
    stats = get_offer_statistics(fernet, offer_id)
    return {
        "id": off.id,
        "name": off.name,
        "network_id": off.network_id,
        "network_name": net_name,
        "created_at": off.created_at,
        "total": stats["total"],
        "tlds": stats["tlds"],
    }


@router.get("/admin/offers/{offer_id}/export-tld/{domain:path}")
def offer_tld_csv(
    offer_id: str,
    domain: str,
    format: str = "plain",
    _=Depends(require_admin),
):
    from fastapi.responses import Response
    csv = get_offer_csv_data_by_tld(fernet, offer_id, domain, format)
    suffix = "md5" if format == "md5" else "plain"
    safe_domain = domain.replace(".", "_").replace("@", "_")
    return Response(
        content=csv,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=offer_{offer_id}_{safe_domain}_{suffix}.csv"},
    )


@router.get("/admin/offers/{offer_id}", response_class=HTMLResponse)
def offer_details_page(offer_id: str, payload: dict = Depends(require_admin)):
    off = get_offer(fernet, offer_id)
    if not off:
        raise HTTPException(404, "Offer not found")
    net = get_network(fernet, off.network_id)
    net_name = net.name if net else ""

    content = f"""
<p><a href="/admin/offers" style="color:#1976d2;text-decoration:none;font-size:0.85rem">&larr; Back to Offers</a></p>
<div class="card">
  <h2>Offer: {off.name}</h2>
  <div class="table-wrap"><table>
    <tr><td><strong>ID</strong></td><td>{off.id}</td></tr>
    <tr><td><strong>Network</strong></td><td>{net_name} ({off.network_id})</td></tr>
    <tr><td><strong>Created</strong></td><td>{off.created_at}</td></tr>
  </table></div>
</div>

<div class="card">
  <h2>Suppression Links <span class="muted">(permanent, auto-update)</span></h2>
  <p style="margin-bottom:0.75rem;font-size:0.85rem;color:#666">These links never change and always return the latest unsubscriber list.</p>
  <div style="display:flex;gap:0.5rem;flex-wrap:wrap">
    <button class="btn" style="background:#43a047" onclick="copyLink('plain')">Copy Plain TEXT Link</button>
    <button class="btn" style="background:#e65100" onclick="copyLink('md5')">Copy MD5 Link</button>
  </div>
  <div id="link-msg" style="margin-top:0.5rem" class="msg"></div>
</div>

<div class="card">
  <h2>Unsubscriber Statistics</h2>
  <p style="font-size:1.5rem;font-weight:700;color:#d32f2f" id="stat-total">Loading...</p>
  <p class="muted">Total unsubscribed emails</p>
  <h3 style="margin-top:1rem;font-size:1rem">Per TLD / Email Domain</h3>
  <div class="table-wrap"><table><thead><tr><th>Domain</th><th>Count</th><th>Download</th></tr></thead>
    <tbody id="tld-body"><tr><td colspan="3" class="muted">Loading...</td></tr></tbody>
  </table></div>
</div>

<script>
async function copyLink(format){{
  const res=await fetch('/admin/feed/generate',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{level:'offer',target:'{off.id}'}})}});
  if(!res.ok){{const d=await res.json();linkMsg(d.detail||'Error','err');return;}}
  const data=await res.json();
  const url=window.location.origin+'/feed/unsubscribers/'+encodeURIComponent('{off.id}')+'/csv?token='+data.token+'&level=offer&format='+format;
  navigator.clipboard.writeText(url).then(()=>linkMsg('Suppression link copied!','ok'));
}}
function linkMsg(t,c){{const el=document.getElementById('link-msg');el.textContent=t;el.className='msg '+c;el.style.display='block';setTimeout(()=>el.style.display='none',5000)}}

fetch('/admin/offers/{off.id}/stats').then(r=>r.json()).then(data=>{{
  document.getElementById('stat-total').textContent=data.total;
  const tb=document.getElementById('tld-body');
  if(data.tlds.length===0){{tb.innerHTML='<tr><td colspan="3" class="muted">No unsubscribers yet</td></tr>';return;}}
  tb.innerHTML=data.tlds.map(t=>'<tr><td>'+t.domain+'</td><td>'+t.count+'</td>'
    +'<td class="flex">'
    +'<a href="/admin/offers/{off.id}/export-tld/'+encodeURIComponent(t.domain)+'?format=plain" class="btn-sm" style="background:#43a047;color:white;text-decoration:none">Plain</a>'
    +'<a href="/admin/offers/{off.id}/export-tld/'+encodeURIComponent(t.domain)+'?format=md5" class="btn-sm" style="background:#e65100;color:white;text-decoration:none">MD5</a>'
    +'</td></tr>'
  ).join('');
}});
</script>"""

    return _page(f"Offer: {off.name}", payload["sub"], payload["role"], "offers", content)


# ── Dashboard ──

@router.get("/admin/dashboard", response_class=HTMLResponse)
def dashboard_page(payload: dict = Depends(require_admin)):
    data = get_dashboard(fernet)
    net_rows = "".join(
        f'<tr><td>{n["name"]}</td><td>{n["id"]}</td><td>{n["unsubscribers"]}</td></tr>'
        for n in data["networks"]
    )
    off_rows = "".join(
        f'<tr><td>{o["name"]}</td><td>{o["id"]}</td><td>{o["unsubscribers"]}</td></tr>'
        for o in data["offers"]
    )
    content = f"""
<div class="card">
  <h2>Global Opt-Outs</h2>
  <p style="font-size:1.5rem;font-weight:700;color:#d32f2f">{data["global_count"]}</p>
</div>
<div class="card">
  <h2>Unsubscribers per Network</h2>
  <div class="table-wrap"><table><thead><tr><th>Network</th><th>ID</th><th>Unsubscribers</th></tr></thead>
  <tbody>{net_rows or '<tr><td colspan="3" class="muted">No network unsubscribers yet</td></tr>'}</tbody></table></div>
</div>
<div class="card">
  <h2>Unsubscribers per Offer</h2>
  <div class="table-wrap"><table><thead><tr><th>Offer</th><th>ID</th><th>Unsubscribers</th></tr></thead>
  <tbody>{off_rows or '<tr><td colspan="3" class="muted">No offer unsubscribers yet</td></tr>'}</tbody></table></div>
</div>"""
    return _page("Dashboard", payload["sub"], payload["role"], "dashboard", content)


# ── Users ──

@router.get("/admin/users", response_class=HTMLResponse)
def users_page(payload: dict = Depends(require_admin)):
    users = list_users(fernet)
    rows = "".join(
        f'<tr><td>{u.email}</td><td>{u.role}</td><td><code style="font-size:0.75rem">{u.api_key[:16]}...</code></td>'
        f'<td>{u.created_at}</td>'
        f'<td><button class="btn-del" onclick="delUser(\'{u.email}\')">Delete</button></td></tr>'
        for u in users
    )
    content = f"""
<div class="card">
  <h2>Add User</h2>
  <div id="msg" class="msg"></div>
  <div style="display:flex;gap:0.5rem;flex-wrap:wrap">
    <input type="email" id="new-email" placeholder="Email" style="flex:2;min-width:150px">
    <input type="password" id="new-pw" placeholder="Password" style="flex:1;min-width:100px">
    <select id="new-role" style="flex:0.5;min-width:80px">
      <option value="user">User</option>
      <option value="admin">Admin</option>
    </select>
    <button class="btn" onclick="addUser()">Add</button>
  </div>
</div>
<div class="card">
  <h2>All Users</h2>
  <div class="table-wrap"><table><thead><tr><th>Email</th><th>Role</th><th>API Key</th><th>Created</th><th></th></tr></thead>
  <tbody>{rows}</tbody></table></div>
</div>
<script>
async function addUser(){{
  const email=document.getElementById('new-email').value;
  const pw=document.getElementById('new-pw').value;
  const role=document.getElementById('new-role').value;
  if(!email||!pw)return;
  const res=await fetch('/admin/users',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{email,password:pw,role}})}});
  if(!res.ok){{const d=await res.json();msg(d.detail||'Error','err');return;}}
  location.reload();
}}
async function delUser(email){{
  if(!confirm('Delete '+email+'?'))return;
  const res=await fetch('/admin/users/'+encodeURIComponent(email),{{method:'DELETE'}});
  if(!res.ok){{const d=await res.json();msg(d.detail||'Error','err');return;}}
  location.reload();
}}
function msg(t,c){{const el=document.getElementById('msg');el.textContent=t;el.className='msg '+c;el.style.display='block'}}
</script>"""
    return _page("Users", payload["sub"], payload["role"], "users", content)


@router.post("/admin/users")
def create_user_endpoint(req: CreateUserRequest, _=Depends(require_admin)):
    pw_hash = hash_password(req.password)
    user = create_user(fernet, req.email, pw_hash, req.role)
    return UserResponse(email=user.email, role=user.role, api_key=user.api_key, created_at=user.created_at)


@router.delete("/admin/users/{email}")
def delete_user_endpoint(email: str, _=Depends(require_admin)):
    if not delete_user(fernet, email):
        raise HTTPException(404, "User not found")
    return {"status": "deleted"}


# ── Unsubscribers page ──

@router.get("/admin/unsubscribers", response_class=HTMLResponse)
def unsubscribers_page(payload: dict = Depends(require_admin)):
    nets = list_networks(fernet)
    offs = list_offers(fernet)
    net_opts = "".join(f'<option value="{n.id}">{n.name}</option>' for n in nets)
    off_opts = "".join(f'<option value="{o.id}" data-net="{o.network_id}">{o.name}</option>' for o in offs)

    content = f"""
<div class="card">
  <h2>Filter Unsubscribers</h2>
  <form id="filter-form" style="display:flex;gap:0.5rem;flex-wrap:wrap;align-items:end">
    <div style="flex:1;min-width:120px">
      <label class="muted">Type</label>
      <select id="filter-level">
        <option value="offer">Offer</option>
        <option value="network">Network</option>
        <option value="global">Global</option>
      </select>
    </div>
    <div style="flex:1;min-width:150px" id="filter-net-div">
      <label class="muted">Network</label>
      <select id="filter-net">{net_opts}</select>
    </div>
    <div style="flex:1;min-width:150px" id="filter-off-div">
      <label class="muted">Offer</label>
      <select id="filter-off">{off_opts}</select>
    </div>
    <button type="submit" class="btn">Search</button>
    <select id="export-format" style="flex:0.5;min-width:80px;margin-bottom:0">
      <option value="plain">Plain Emails</option>
      <option value="md5">MD5 Hashes</option>
    </select>
    <button type="button" class="btn" id="export-btn" style="background:#43a047">Export</button>
  </form>
</div>
<div class="card">
  <h2>Results <span id="result-count" class="muted"></span></h2>
  <div id="loading" style="text-align:center;padding:2rem;color:#999">Select filters and click Search</div>
  <div id="result-table" style="display:none">
    <div class="table-wrap"><table><thead><tr><th>Email</th><th>MD5</th><th>SHA256</th><th>Date</th></tr></thead>
    <tbody id="result-body"></tbody></table></div>
  </div>
</div>
<script>
document.getElementById('filter-level').addEventListener('change',function(){{
  const v=this.value;
  document.getElementById('filter-net-div').style.display=v==='global'?'none':'block';
  document.getElementById('filter-off-div').style.display=v==='offer'?'block':'none';
}});
document.getElementById('filter-form').addEventListener('submit',async function(e){{
  e.preventDefault();search();}});
document.getElementById('export-btn').addEventListener('click',function(){{
  const level=document.getElementById('filter-level').value;
  const format=document.getElementById('export-format').value;
  const params=new URLSearchParams({{level,format}});
  if(level==='network') params.set('network_id',document.getElementById('filter-net').value);
  if(level==='offer') params.set('offer_id',document.getElementById('filter-off').value);
  window.location.href='/admin/unsubscribers/export?'+params.toString();
}});
async function search(){{
  const level=document.getElementById('filter-level').value;
  const params=new URLSearchParams({{level}});
  if(level==='network') params.set('target',document.getElementById('filter-net').value);
  if(level==='offer') params.set('target',document.getElementById('filter-off').value);
  if(level==='global') params.set('target','*');
  document.getElementById('loading').textContent='Loading...';
  document.getElementById('loading').style.display='block';
  document.getElementById('result-table').style.display='none';
  const res=await fetch('/admin/unsubscribers/data?'+params.toString());
  const data=await res.json();
  document.getElementById('loading').style.display='none';
  if(data.length===0){{
    document.getElementById('loading').textContent='No results';
    document.getElementById('loading').style.display='block';
    document.getElementById('result-count').textContent='';
    return;
  }}
  document.getElementById('result-count').textContent='('+data.length+' records)';
  document.getElementById('result-body').innerHTML=data.map(r=>
    '<tr><td style="font-size:0.8rem">'+(r.email||'')+'</td><td style="font-family:monospace;font-size:0.7rem">'+(r.md5||'')+'</td><td style="font-family:monospace;font-size:0.7rem">'+r.email_hash+'</td><td style="font-size:0.8rem">'+new Date(r.timestamp*1000).toLocaleString()+'</td></tr>'
  ).join('');
  document.getElementById('result-table').style.display='block';
}}
</script>"""
    return _page("Unsubscribers", payload["sub"], payload["role"], "unsubscribers", content)


@router.get("/admin/unsubscribers/data")
def unsubscribers_data(
    level: str = "offer",
    target: str = "",
    _=Depends(require_admin),
):
    if level == "global":
        target = "*"
    results = get_unsubscribers_for_target(fernet, level, target)
    return JSONResponse(content=results)


@router.get("/admin/unsubscribers/export")
def unsubscribers_export(
    level: str = "offer",
    offer_id: str = "",
    network_id: str = "",
    format_: str = Query("plain", alias="format"),
    _=Depends(require_admin),
):
    from fastapi.responses import Response
    target = offer_id or network_id or "*"
    if level == "global":
        target = "*"
    results = get_unsubscribers_for_target(fernet, level, target)

    lines = []
    for r in results:
        if format_ == "md5":
            val = r.get("md5") or ""
            if not val and r.get("email"):
                from ..crypto import md5_email
                val = md5_email(r["email"])
        else:
            val = r.get("email") or ""
        if val:
            lines.append(val)

    csv = "\n".join(lines) + ("\n" if lines else "")
    suffix = "md5" if format_ == "md5" else "plain"
    return Response(
        content=csv,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=unsubscribers_{level}_{target}_{suffix}.csv"},
    )


# ── Feed management ──

@router.post("/admin/feed/generate")
def generate_feed(req: GenerateFeedRequest, _=Depends(require_admin)):
    try:
        token = generate_feed_token(fernet, req.level, req.target)
        feed_url = f"{BASE_URL}/feed/unsubscribers/{req.target}?token={token}&level={req.level}"
        return {"feed_url": feed_url, "token": token}
    except ValueError as e:
        raise HTTPException(400, str(e))


@router.get("/admin/offers/{offer_id}/unsubscribers/csv")
def offer_unsubscribers_csv(
    offer_id: str,
    format: str = "plain",
    _=Depends(require_admin),
):
    from fastapi.responses import Response
    csv = get_offer_csv_data(fernet, offer_id, format)
    suffix = "md5" if format == "md5" else "full"
    return Response(
        content=csv,
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=offer_{offer_id}_unsubscribers_{suffix}.csv"},
    )


# ── Enhanced dashboard ──

@router.get("/admin/dashboard", response_class=HTMLResponse)
def dashboard_page(payload: dict = Depends(require_admin)):
    data = get_all_statistics(fernet)
    net_rows = "".join(
        f'<tr><td>{n["name"]}</td><td>{n["id"]}</td><td>{n["count"]}</td>'
        f'<td class="flex">'
        f'<button class="btn-sm" onclick="copyFeed(\'{n["id"]}\',\'network\')">JSON</button>'
        f'<button class="btn-sm" style="background:#43a047" onclick="copySuppressionLink(\'{n["id"]}\',\'network\',\'plain\')">Plain</button>'
        f'<button class="btn-sm" style="background:#e65100" onclick="copySuppressionLink(\'{n["id"]}\',\'network\',\'md5\')">MD5</button>'
        f'</td></tr>'
        for n in data["networks"]["details"]
    )
    off_rows = "".join(
        f'<tr><td><a href="/admin/offers/{o["id"]}" style="color:#1976d2;text-decoration:none;font-weight:600">{o["name"]}</a></td><td>{o["id"]}</td><td>{o["network"]}</td><td>{o["count"]}</td>'
        f'<td class="flex">'
        f'<button class="btn-sm" onclick="copyFeed(\'{o["id"]}\',\'offer\')">JSON</button>'
        f'<button class="btn-sm" style="background:#43a047" onclick="copySuppressionLink(\'{o["id"]}\',\'offer\',\'plain\')">Plain</button>'
        f'<button class="btn-sm" style="background:#e65100" onclick="copySuppressionLink(\'{o["id"]}\',\'offer\',\'md5\')">MD5</button>'
        f'</td></tr>'
        for o in data["offers"]["details"]
    )
    content = f"""
<div class="card">
  <h2>Global Opt-Outs</h2>
  <p style="font-size:1.5rem;font-weight:700;color:#d32f2f">{data["global"]["count"]}</p>
</div>
<div class="card">
  <h2>Network Suppression Links</h2>
  <p class="muted">Links are permanent and auto-update when new unsubscribers are added</p>
  <div class="table-wrap"><table><thead><tr><th>Network</th><th>ID</th><th>Count</th><th>Links</th></tr></thead>
  <tbody>{net_rows or '<tr><td colspan="4" class="muted">No data</td></tr>'}</tbody></table></div>
</div>
<div class="card">
  <h2>Offer Suppression Links</h2>
  <p class="muted">Each link is unique per offer, stays the same, always returns latest unsubscribers</p>
  <div class="table-wrap"><table><thead><tr><th>Offer</th><th>ID</th><th>Network</th><th>Count</th><th>Links</th></tr></thead>
  <tbody>{off_rows or '<tr><td colspan="5" class="muted">No data</td></tr>'}</tbody></table></div>
</div>
<div id="feed-msg" class="msg"></div>
<script>
async function copyFeed(id,level){{
  const res=await fetch('/admin/feed/generate',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{level,target:id}})}});
  if(!res.ok){{const d=await res.json();msg(d.detail||'Error','err');return;}}
  const data=await res.json();
  navigator.clipboard.writeText(data.feed_url).then(()=>msg('JSON feed URL copied!','ok'));
}}
async function copySuppressionLink(id,level,format){{
  const res=await fetch('/admin/feed/generate',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{level,target:id}})}});
  if(!res.ok){{const d=await res.json();msg(d.detail||'Error','err');return;}}
  const data=await res.json();
  const url=window.location.origin+'/feed/unsubscribers/'+encodeURIComponent(id)+'/csv?token='+data.token+'&level='+level+'&format='+format;
  navigator.clipboard.writeText(url).then(()=>msg('Suppression link copied! Link is permanent and auto-updates.','ok'));
}}
function msg(t,c){{const el=document.getElementById('feed-msg');el.textContent=t;el.className='msg '+c;el.style.display='block';setTimeout(()=>el.style.display='none',5000)}}
</script>"""
    return _page("Dashboard", payload["sub"], payload["role"], "dashboard", content)


# ── Export/Import ──

@router.get("/admin/export")
def admin_export(_=Depends(require_admin)):
    return JSONResponse(content=export_suppressions(fernet))


@router.post("/admin/import")
def admin_import(data: dict, _=Depends(require_admin)):
    count = import_suppressions(fernet, data)
    return {"imported": count}
