import random


def random_email_form(token: str) -> str:
    templates = [
        _ocean_form(token),
        _sunset_form(token),
        _dark_form(token),
        _forest_form(token),
        _purple_form(token),
        _clean_form(token),
        _midnight_form(token),
        _neonpink_form(token),
        _mint_form(token),
        _coral_form(token),
        _charcoal_form(token),
        _lavender_form(token),
        _emerald_form(token),
        _ruby_form(token),
        _sapphire_form(token),
        _amber_form(token),
        _rosequartz_form(token),
        _arctic_form(token),
        _tropical_form(token),
        _cosmic_form(token),
        _autumn_form(token),
        _storm_form(token),
        _bamboo_form(token),
        _cherryblossom_form(token),
        _deepsea_form(token),
        _sunsetblvd_form(token),
        _northernlights_form(token),
        _concrete_form(token),
        _orchid_form(token),
        _cloud_form(token),
        _royal_form(token),
        _palmbeach_form(token),
        _volcano_form(token),
        _glacier_form(token),
        _sahara_form(token),
        _neongreen_form(token),
        _plum_form(token),
        _iceblue_form(token),
        _burntorange_form(token),
        _indigonight_form(token),
        _peach_form(token),
        _steelblue_form(token),
        _mahogany_form(token),
        _cerulean_form(token),
        _olive_form(token),
        _crimson_form(token),
        _periwinkle_form(token),
        _tangerine_form(token),
        _gunmetal_form(token),
        _maraungold_form(token),
    ]
    return random.choice(templates)


def random_success() -> str:
    templates = [
        _ocean_success(),
        _sunset_success(),
        _dark_success(),
        _forest_success(),
        _purple_success(),
        _clean_success(),
        _midnight_success(),
        _neonpink_success(),
        _mint_success(),
        _coral_success(),
        _charcoal_success(),
        _lavender_success(),
        _emerald_success(),
        _ruby_success(),
        _sapphire_success(),
        _amber_success(),
        _rosequartz_success(),
        _arctic_success(),
        _tropical_success(),
        _cosmic_success(),
        _autumn_success(),
        _storm_success(),
        _bamboo_success(),
        _cherryblossom_success(),
        _deepsea_success(),
        _sunsetblvd_success(),
        _northernlights_success(),
        _concrete_success(),
        _orchid_success(),
        _cloud_success(),
        _royal_success(),
        _palmbeach_success(),
        _volcano_success(),
        _glacier_success(),
        _sahara_success(),
        _neongreen_success(),
        _plum_success(),
        _iceblue_success(),
        _burntorange_success(),
        _indigonight_success(),
        _peach_success(),
        _steelblue_success(),
        _mahogany_success(),
        _cerulean_success(),
        _olive_success(),
        _crimson_success(),
        _periwinkle_success(),
        _tangerine_success(),
        _gunmetal_success(),
        _maraungold_success(),
    ]
    return random.choice(templates)


# ── Theme 1: Ocean Blue ──

def _ocean_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);padding:1rem}}
.card{{background:rgba(255,255,255,0.95);backdrop-filter:blur(10px);padding:2.5rem 2rem;border-radius:20px;max-width:420px;width:100%;box-shadow:0 20px 60px rgba(0,0,0,0.3);text-align:center;animation:slideUp .5s ease}}
@keyframes slideUp{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#0f2027;font-size:1.5rem;margin-bottom:0.5rem;}}
p{{color:#5a6a75;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #d1e3eb;border-radius:10px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#2c5364;box-shadow:0 0 0 3px rgba(44,83,100,0.15)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#0f2027,#2c5364);color:white;border:none;border-radius:10px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 6px 20px rgba(44,83,100,0.4)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#9aa;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>You will be removed from our mailing list and will no longer receive emails from us.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="Enter your email address" required>
<button type="submit">Unsubscribe Me</button>
</form>
<p class="footer">This action is permanent and cannot be undone.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe Me';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe Me';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 2: Sunset ──

def _sunset_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#ff512f,#dd2476);padding:1rem}}
.card{{background:white;padding:2.5rem 2rem;border-radius:16px;max-width:420px;width:100%;box-shadow:0 25px 60px rgba(0,0,0,0.25);text-align:center;animation:popIn .5s ease}}
@keyframes popIn{{from{{opacity:0;transform:scale(0.9)}}to{{opacity:1;transform:scale(1)}}}}
h1{{color:#333;font-size:1.5rem;margin-bottom:0.5rem;}}
p{{color:#666;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #eee;border-radius:12px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#dd2476;box-shadow:0 0 0 3px rgba(221,36,118,0.15)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#ff512f,#dd2476);color:white;border:none;border-radius:12px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(221,36,118,0.4)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#aaa;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>We're sorry to see you go. Enter your email below to be removed from our list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">You won't receive any more emails from us.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 3: Dark Minimal ──

def _dark_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#111;padding:1rem}}
.card{{background:#1e1e1e;padding:2.5rem 2rem;border-radius:0;max-width:420px;width:100%;box-shadow:none;text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
h1{{color:#f5f5f5;font-size:1.5rem;margin-bottom:0.5rem;font-weight:300;letter-spacing:0.5px}}
p{{color:#888;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid #333;border-radius:4px;font-size:1rem;margin-bottom:1rem;background:#2a2a2a;transition:border-color .2s;color:#f5f5f5}}
input:focus{{outline:none;border-color:#f5f5f5;box-shadow:none}}
button{{width:100%;padding:0.9rem;background:#f5f5f5;color:#111;border:none;border-radius:4px;font-size:1rem;cursor:pointer;font-weight:500;letter-spacing:0.3px;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:none}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#555;}}
</style></head>
<body>
<div class="card">
<h1>OPT OUT</h1>
<p>Enter your email address and we'll remove you from all communications.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="email@example.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Immediate. Permanent. No questions asked.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 4: Forest ──

def _forest_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Georgia,'Times New Roman',serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(160deg,#134e5e,#71b280);padding:1rem}}
.card{{background:rgba(255,255,255,0.96);padding:2.5rem 2rem;border-radius:12px;max-width:420px;width:100%;box-shadow:0 15px 50px rgba(0,0,0,0.2);text-align:center;animation:fadeUp .5s ease}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(15px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#134e5e;font-size:1.5rem;margin-bottom:0.5rem;}}
p{{color:#5a6b5a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #c8dcc8;border-radius:8px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;font-family:inherit}}
input:focus{{outline:none;border-color:#134e5e;box-shadow:0 0 0 3px rgba(19,78,94,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#134e5e,#71b280);color:white;border:none;border-radius:8px;font-size:1rem;cursor:pointer;font-weight:600;font-family:inherit;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 6px 18px rgba(19,78,94,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#999;font-style:italic}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>We respect your inbox. Enter your email to be removed from our mailing list permanently.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe Me</button>
</form>
<p class="footer">We'll miss you, but we respect your choice.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe Me';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe Me';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 5: Purple Haze ──

def _purple_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#667eea,#764ba2);padding:1rem}}
.card{{background:rgba(255,255,255,0.15);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.25);padding:2.5rem 2rem;border-radius:20px;max-width:420px;width:100%;box-shadow:none;text-align:center;animation:scaleIn .5s ease}}
@keyframes scaleIn{{from{{opacity:0;transform:scale(0.92)}}to{{opacity:1;transform:scale(1)}}}}
h1{{color:#fff;font-size:1.5rem;margin-bottom:0.5rem;font-weight:600}}
p{{color:rgba(255,255,255,0.8);font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid rgba(255,255,255,0.3);border-radius:12px;font-size:1rem;margin-bottom:1rem;background:rgba(255,255,255,0.15);transition:border-color .2s;color:white}}
input:focus{{outline:none;border-color:white;box-shadow:none}}
button{{width:100%;padding:0.9rem;background:white;color:#764ba2;border:none;border-radius:12px;font-size:1rem;cursor:pointer;font-weight:700;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(0,0,0,0.2)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:rgba(255,255,255,0.5);}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Want to stop receiving emails? Enter your email address below and you'll be removed immediately.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">This cannot be undone.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 6: Clean White ──

def _clean_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#fafafa;padding:1rem}}
.card{{background:white;padding:2.5rem 2rem;border-radius:0;max-width:420px;width:100%;box-shadow:0 1px 3px rgba(0,0,0,0.08);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
h1{{color:#222;font-size:1.5rem;margin-bottom:0.5rem;font-weight:500}}
p{{color:#888;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid #ddd;border-radius:6px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;appearance:none}}
input:focus{{outline:none;border-color:#555;box-shadow:none}}
button{{width:100%;padding:0.9rem;background:#222;color:white;border:none;border-radius:6px;font-size:1rem;cursor:pointer;font-weight:500;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:none}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#bbb;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Enter your email to be removed from our mailing list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">We respect your privacy.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 7: Midnight Blue ──

def _midnight_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(180deg,#0a1628,#162447,#1f4068);padding:1rem}}
.card{{background:#ffffff;padding:2.5rem 2rem;border-radius:0;max-width:420px;width:100%;box-shadow:0 30px 60px rgba(0,0,0,0.4);text-align:center;animation:slideRight .5s ease}}
@keyframes slideRight{{from{{opacity:0;transform:translateX(-30px)}}to{{opacity:1;transform:translateX(0)}}}}
h1{{color:#0a1628;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700;letter-spacing:-0.5px}}
p{{color:#4a5568;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #e2e8f0;border-radius:0;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;font-family:monospace}}
input:focus{{outline:none;border-color:#1f4068;box-shadow:none}}
button{{width:100%;padding:0.9rem;background:#1f4068;color:white;border:none;border-radius:0;font-size:1rem;cursor:pointer;font-weight:700;text-transform:uppercase;letter-spacing:1px;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:none}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#a0aec0;text-transform:uppercase;letter-spacing:0.5px}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Remove your email from our mailing list. You will stop receiving all future communications.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">This action is immediate</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 8: Neon Pink ──

def _neonpink_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Courier New',monospace;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#0d0d0d;padding:1rem}}
.card{{background:#1a1a1a;border:2px solid #ff006e;box-shadow:0 0 30px rgba(255,0,110,0.3),0 0 60px rgba(255,0,110,0.1);padding:2.5rem 2rem;border-radius:8px;max-width:420px;width:100%;box-shadow:none;text-align:center;animation:glow .5s ease}}
@keyframes glow{{from{{opacity:0;box-shadow:0 0 0 rgba(255,0,110,0)}}to{{opacity:1;box-shadow:0 0 30px rgba(255,0,110,0.3)}}}}
h1{{color:#ff006e;font-size:1.5rem;margin-bottom:0.5rem;text-transform:uppercase;letter-spacing:3px}}
p{{color:#888;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid #333;border-radius:4px;font-size:1rem;margin-bottom:1rem;background:#0d0d0d;transition:border-color .2s;color:#ff006e;font-family:inherit}}
input:focus{{outline:none;border-color:#ff006e;box-shadow:0 0 10px rgba(255,0,110,0.3)}}
button{{width:100%;padding:0.9rem;background:#ff006e;color:#0d0d0d;border:none;border-radius:4px;font-size:1rem;cursor:pointer;font-weight:700;text-transform:uppercase;letter-spacing:2px;border:2px solid #ff006e;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 0 20px rgba(255,0,110,0.4)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#444;text-transform:uppercase;letter-spacing:1px}}
</style></head>
<body>
<div class="card">
<h1>Opt Out</h1>
<p>Enter your email below to unsubscribe from all future communications.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">// no more emails</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 9: Mint Fresh ──

def _mint_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#e0f7fa,#b2dfdb,#80cbc4);padding:1rem}}
.card{{background:white;padding:2.5rem 2rem;border-radius:24px;max-width:420px;width:100%;box-shadow:0 12px 40px rgba(0,77,64,0.15);text-align:center;animation:bounceIn .5s ease}}
@keyframes bounceIn{{from{{opacity:0;transform:scale(0.85)}}50%{{transform:scale(1.02)}}to{{opacity:1;transform:scale(1)}}}}
h1{{color:#00695c;font-size:1.5rem;margin-bottom:0.5rem;font-weight:600}}
p{{color:#607d8b;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #b2dfdb;border-radius:14px;font-size:1rem;margin-bottom:1rem;background:#f0faf8;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#00897b;box-shadow:0 0 0 3px rgba(0,137,123,0.12)}}
button{{width:100%;padding:0.9rem;background:#00897b;color:white;border:none;border-radius:14px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 20px rgba(0,137,123,0.3)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#b0bec5;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Ready to opt out? We'll remove your email from our list right away.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe Me</button>
</form>
<p class="footer">No more emails, promise.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe Me';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe Me';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 10: Coral Reef ──

def _coral_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#ff9a9e,#fecfef,#fad0c4);padding:1rem}}
.card{{background:rgba(255,255,255,0.9);backdrop-filter:blur(10px);padding:2.5rem 2rem;border-radius:18px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(255,107,107,0.2);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#e55353;font-size:1.5rem;margin-bottom:0.5rem;}}
p{{color:#7a6060;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #fdd;border-radius:12px;font-size:1rem;margin-bottom:1rem;background:rgba(255,255,255,0.7);transition:border-color .2s;}}
input:focus{{outline:none;border-color:#ff6b6b;box-shadow:0 0 0 3px rgba(255,107,107,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#ff6b6b,#ee5a24);color:white;border:none;border-radius:12px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(238,90,36,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#c4a0a0;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>We're sad to see you leave. Enter your email to opt out of our mailing list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">You're free as a fish.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 11: Charcoal ──

def _charcoal_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Helvetica Neue',Arial,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#2d2d2d;padding:1rem}}
.card{{background:#3a3a3a;border-left:4px solid #666;padding:2.5rem 2rem;border-radius:0;max-width:420px;width:100%;box-shadow:none;text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
h1{{color:#e0e0e0;font-size:1.5rem;margin-bottom:0.5rem;font-weight:400;text-transform:uppercase;letter-spacing:2px}}
p{{color:#999;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid #555;border-radius:0;font-size:1rem;margin-bottom:1rem;background:#2d2d2d;transition:border-color .2s;color:#e0e0e0;text-transform:uppercase;letter-spacing:0.5px}}
input:focus{{outline:none;border-color:#888;box-shadow:none}}
button{{width:100%;padding:0.9rem;background:#666;color:#fff;border:none;border-radius:0;font-size:1rem;cursor:pointer;font-weight:500;text-transform:uppercase;letter-spacing:2px;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:none}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#666;text-transform:uppercase;letter-spacing:1px}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Enter your email address and we'll remove you from all future mailings.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Done. No more emails.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 12: Lavender Dream ──

def _lavender_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#e8d5f5,#d5c8f0,#c4b5e8);padding:1rem}}
.card{{background:rgba(255,255,255,0.85);backdrop-filter:blur(12px);padding:2.5rem 2rem;border-radius:20px;max-width:420px;width:100%;box-shadow:0 15px 45px rgba(120,80,180,0.15);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(15px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#5b3a8c;font-size:1.5rem;margin-bottom:0.5rem;font-weight:600}}
p{{color:#7a6a8a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #d5c8f0;border-radius:16px;font-size:1rem;margin-bottom:1rem;background:rgba(255,255,255,0.6);transition:border-color .2s;}}
input:focus{{outline:none;border-color:#7c5cbf;box-shadow:0 0 0 3px rgba(124,92,191,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#9b72cf,#7c5cbf);color:white;border:none;border-radius:16px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(124,92,191,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#b0a0c0;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>We understand. Enter your email and we'll take care of the rest.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe Me</button>
</form>
<p class="footer">Thanks for being with us.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe Me';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe Me';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 13: Emerald City ──

def _emerald_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#004d40,#00695c,#00897b);padding:1rem}}
.card{{background:#ffffff;padding:2.5rem 2rem;border-radius:16px;max-width:420px;width:100%;box-shadow:0 25px 55px rgba(0,0,0,0.3);text-align:center;animation:flipIn .5s ease}}
@keyframes flipIn{{from{{opacity:0;transform:perspective(400px) rotateX(20deg)}}to{{opacity:1;transform:perspective(400px) rotateX(0)}}}}
h1{{color:#004d40;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#546e7a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #c8e6c9;border-radius:8px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#00695c;box-shadow:0 0 0 3px rgba(0,105,92,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#004d40,#00897b);color:white;border:none;border-radius:8px;font-size:1rem;cursor:pointer;font-weight:700;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(0,77,64,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#a0b0a0;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Enter your email and we'll remove you from our mailing list permanently.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">We respect your decision.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 14: Ruby Red ──

def _ruby_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#8b0000,#b71c1c,#d32f2f);padding:1rem}}
.card{{background:rgba(255,255,255,0.95);padding:2.5rem 2rem;border-radius:12px;max-width:420px;width:100%;box-shadow:0 25px 50px rgba(139,0,0,0.3);text-align:center;animation:rotateIn .5s ease}}
@keyframes rotateIn{{from{{opacity:0;transform:rotate(-3deg) scale(0.95)}}to{{opacity:1;transform:rotate(0) scale(1)}}}}
h1{{color:#8b0000;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#666;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #ffcdd2;border-radius:8px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#d32f2f;box-shadow:0 0 0 3px rgba(211,47,47,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#8b0000,#d32f2f);color:white;border:none;border-radius:8px;font-size:1rem;cursor:pointer;font-weight:700;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(139,0,0,0.4)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#c0a0a0;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>We don't want to see you go, but we'll remove you from our list immediately.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe Me</button>
</form>
<p class="footer">Farewell, friend.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe Me';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe Me';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 15: Sapphire ──

def _sapphire_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#0d47a1,#1565c0,#1976d2);padding:1rem}}
.card{{background:rgba(255,255,255,0.92);padding:2.5rem 2rem;border-radius:14px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(13,71,161,0.25);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#0d47a1;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#546e7a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #bbdefb;border-radius:10px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#1976d2;box-shadow:0 0 0 3px rgba(25,118,210,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#0d47a1,#1976d2);color:white;border:none;border-radius:10px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(13,71,161,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#90a4ae;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Enter your email address below and we'll remove you from our mailing list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Your privacy matters to us.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 16: Amber Gold ──

def _amber_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#f57f17,#ff8f00,#ffa000);padding:1rem}}
.card{{background:#ffffff;padding:2.5rem 2rem;border-radius:16px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(245,127,23,0.25);text-align:center;animation:popIn .5s ease}}
@keyframes popIn{{from{{opacity:0;transform:scale(0.9)}}to{{opacity:1;transform:scale(1)}}}}
h1{{color:#e65100;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#6d5b4b;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #ffe0b2;border-radius:12px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#ff8f00;box-shadow:0 0 0 3px rgba(255,143,0,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#f57f17,#ffa000);color:white;border:none;border-radius:12px;font-size:1rem;cursor:pointer;font-weight:700;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(255,160,0,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#bfa580;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>It's been great having you. Enter your email to opt out of our list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Wishing you all the best.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 17: Rose Quartz ──

def _rosequartz_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Georgia',serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#fdf2f0;padding:1rem}}
.card{{background:white;border:1px solid #f0d5cc;padding:2.5rem 2rem;border-radius:4px;max-width:420px;width:100%;box-shadow:0 4px 20px rgba(0,0,0,0.05);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
h1{{color:#a0605a;font-size:1.5rem;margin-bottom:0.5rem;font-weight:400;font-style:italic}}
p{{color:#b08a85;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid #e8c5be;border-radius:4px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;font-family:inherit;font-style:italic}}
input:focus{{outline:none;border-color:#c08070;box-shadow:none}}
button{{width:100%;padding:0.9rem;background:#a0605a;color:white;border:none;border-radius:4px;font-size:1rem;cursor:pointer;font-family:inherit;font-style:italic;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:none}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#d0b0a8;font-style:italic}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Enter your email to leave our mailing list. We'll miss your presence.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Until we meet again.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 18: Arctic ──

def _arctic_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(180deg,#e3f2fd,#bbdefb,#90caf9);padding:1rem}}
.card{{background:rgba(255,255,255,0.8);backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,0.6);padding:2.5rem 2rem;border-radius:16px;max-width:420px;width:100%;box-shadow:0 10px 40px rgba(66,165,245,0.15);text-align:center;animation:slideRight .5s ease}}
@keyframes slideRight{{from{{opacity:0;transform:translateX(-20px)}}to{{opacity:1;transform:translateX(0)}}}}
h1{{color:#1565c0;font-size:1.5rem;margin-bottom:0.5rem;}}
p{{color:#607d8b;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid rgba(21,101,192,0.2);border-radius:10px;font-size:1rem;margin-bottom:1rem;background:rgba(255,255,255,0.5);transition:border-color .2s;}}
input:focus{{outline:none;border-color:#42a5f5;box-shadow:0 0 0 3px rgba(66,165,245,0.12)}}
button{{width:100%;padding:0.9rem;background:#1976d2;color:white;border:none;border-radius:10px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(25,118,210,0.3)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#90a4ae;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Cold feet? No problem. Enter your email to unsubscribe from our list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Stay cool out there.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 19: Tropical ──

def _tropical_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#00b09b,#96c93d);padding:1rem}}
.card{{background:white;padding:2.5rem 2rem;border-radius:20px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(0,0,0,0.2);text-align:center;animation:bounceIn .5s ease}}
@keyframes bounceIn{{from{{opacity:0;transform:scale(0.85)}}50%{{transform:scale(1.03)}}to{{opacity:1;transform:scale(1)}}}}
h1{{color:#00897b;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#689f63;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #c8e6c9;border-radius:14px;font-size:1rem;margin-bottom:1rem;background:#f1f8e9;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#7cb342;box-shadow:0 0 0 3px rgba(124,179,66,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#00b09b,#7cb342);color:white;border:none;border-radius:14px;font-size:1rem;cursor:pointer;font-weight:700;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(0,176,155,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#a5d6a7;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Time to leave the island? Enter your email and we'll set you free.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe Me</button>
</form>
<p class="footer">Paradise awaits elsewhere.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe Me';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe Me';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 20: Cosmic ──

def _cosmic_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Courier New',monospace;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#0c0c1d;padding:1rem}}
.card{{background:rgba(22,33,62,0.85);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.1);padding:2.5rem 2rem;border-radius:8px;max-width:420px;width:100%;box-shadow:0 0 30px rgba(206,147,216,0.15);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#e1bee7;font-size:1.5rem;margin-bottom:0.5rem;}}
p{{color:rgba(255,255,255,0.6);font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid rgba(255,255,255,0.15);border-radius:4px;font-size:1rem;margin-bottom:1rem;background:rgba(255,255,255,0.05);transition:border-color .2s;color:white;font-family:inherit}}
input:focus{{outline:none;border-color:#ce93d8;box-shadow:0 0 10px rgba(206,147,216,0.2)}}
button{{width:100%;padding:0.9rem;background:rgba(206,147,216,0.2);color:#e1bee7;border:none;border-radius:4px;font-size:1rem;cursor:pointer;font-weight:600;font-family:inherit;border:1px solid rgba(206,147,216,0.4);transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 0 20px rgba(206,147,216,0.2)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:rgba(255,255,255,0.3);}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Enter your email to leave our orbit. You'll drift away from our mailing list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Safe travels through the cosmos.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 21: Autumn ──

def _autumn_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Georgia,'Times New Roman',serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#bf360c,#e65100,#f57f17);padding:1rem}}
.card{{background:rgba(255,248,240,0.95);padding:2.5rem 2rem;border-radius:12px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(0,0,0,0.25);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(15px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#bf360c;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#8d6e63;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #ffccbc;border-radius:8px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;font-family:Georgia,serif}}
input:focus{{outline:none;border-color:#e65100;box-shadow:0 0 0 3px rgba(230,81,0,0.1)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#bf360c,#e65100);color:white;border:none;border-radius:8px;font-size:1rem;cursor:pointer;font-weight:600;font-family:Georgia,serif;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(191,54,12,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#bcaaa4;font-style:italic}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>As the leaves fall, so too shall your subscription. Enter your email below.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe Me</button>
</form>
<p class="footer">Every ending is a new beginning.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe Me';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe Me';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 22: Storm ──

def _storm_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(180deg,#263238,#37474f,#455a64);padding:1rem}}
.card{{background:rgba(255,255,255,0.9);padding:2.5rem 2rem;border-radius:2px;max-width:420px;width:100%;box-shadow:0 30px 60px rgba(0,0,0,0.4);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
h1{{color:#263238;font-size:1.5rem;margin-bottom:0.5rem;font-weight:300;letter-spacing:1px}}
p{{color:#607d8b;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid #b0bec5;border-radius:2px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#455a64;box-shadow:none}}
button{{width:100%;padding:0.9rem;background:#263238;color:white;border:none;border-radius:2px;font-size:1rem;cursor:pointer;font-weight:600;border:2px solid #263238;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:none}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#90a4ae;}}
</style></head>
<body>
<div class="card">
<h1>UNSUBSCRIBE</h1>
<p>Weather the storm and opt out. Enter your email to stop receiving messages.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Clear skies ahead.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 23: Bamboo ──

def _bamboo_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#c0ca33,#9e9d24,#827717);padding:1rem}}
.card{{background:#fffff0;border:2px solid #c5e1a5;padding:2.5rem 2rem;border-radius:12px;max-width:420px;width:100%;box-shadow:0 12px 35px rgba(0,0,0,0.15);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(10px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#558b2f;font-size:1.5rem;margin-bottom:0.5rem;font-weight:600}}
p{{color:#7c8560;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #dce775;border-radius:8px;font-size:1rem;margin-bottom:1rem;background:#fafde8;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#9e9d24;box-shadow:0 0 0 3px rgba(158,157,36,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#827717,#9e9d24);color:white;border:none;border-radius:8px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 20px rgba(130,119,23,0.3)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#c5ca8a;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Like bamboo swaying in the wind, you're free to go. Enter your email to opt out.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Nature calls you onward.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 24: Cherry Blossom ──

def _cherryblossom_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Hiragino Mincho ProN','Yu Mincho',serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#fff5f5;padding:1rem}}
.card{{background:white;border:1px solid #fce4ec;padding:2.5rem 2rem;border-radius:4px;max-width:420px;width:100%;box-shadow:0 4px 25px rgba(0,0,0,0.06);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
h1{{color:#c2185b;font-size:1.5rem;margin-bottom:0.5rem;font-weight:400}}
p{{color:#ad6a7a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid #f8bbd0;border-radius:2px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;font-family:inherit}}
input:focus{{outline:none;border-color:#e91e63;box-shadow:none}}
button{{width:100%;padding:0.9rem;background:#e91e63;color:white;border:none;border-radius:2px;font-size:1rem;cursor:pointer;font-family:inherit;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:none}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#e8b4bc;font-style:italic}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Like petals falling from a cherry blossom, it's time to part ways. Enter your email below.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Until the blossoms return.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 25: Deep Sea ──

def _deepsea_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(180deg,#001f3f,#003366,#004080);padding:1rem}}
.card{{background:rgba(0,50,80,0.7);backdrop-filter:blur(15px);border:1px solid rgba(0,150,200,0.2);padding:2.5rem 2rem;border-radius:14px;max-width:420px;width:100%;box-shadow:none;text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(25px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#80deea;font-size:1.5rem;margin-bottom:0.5rem;}}
p{{color:rgba(255,255,255,0.6);font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid rgba(0,150,200,0.3);border-radius:10px;font-size:1rem;margin-bottom:1rem;background:rgba(0,0,0,0.3);transition:border-color .2s;color:white}}
input:focus{{outline:none;border-color:#4dd0e1;box-shadow:0 0 10px rgba(77,208,225,0.2)}}
button{{width:100%;padding:0.9rem;background:rgba(0,150,200,0.3);color:#80deea;border:none;border-radius:10px;font-size:1rem;cursor:pointer;font-weight:600;border:1px solid rgba(0,150,200,0.4);transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 0 20px rgba(0,150,200,0.2)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:rgba(255,255,255,0.3);}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Deep beneath the surface, your privacy matters. Enter your email to opt out.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Dive back to calm waters.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 26: Sunset Boulevard ──

def _sunsetblvd_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Trebuchet MS',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#f093fb,#f5576c,#fda085);padding:1rem}}
.card{{background:rgba(255,255,255,0.92);padding:2.5rem 2rem;border-radius:20px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(245,87,108,0.25);text-align:center;animation:popIn .5s ease}}
@keyframes popIn{{from{{opacity:0;transform:scale(0.92)}}to{{opacity:1;transform:scale(1)}}}}
h1{{color:#f5576c;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#8a6070;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #f8bbd0;border-radius:16px;font-size:1rem;margin-bottom:1rem;background:#fff5f5;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#f5576c;box-shadow:0 0 0 3px rgba(245,87,108,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#f5576c,#fda085);color:white;border:none;border-radius:16px;font-size:1rem;cursor:pointer;font-weight:700;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(245,87,108,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#d4a0b0;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Walking down the boulevard one last time? Enter your email to opt out.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Catch you on the flip side.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 27: Northern Lights ──

def _northernlights_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#0f0c29,#302b63,#24243e);padding:1rem}}
.card{{background:rgba(255,255,255,0.1);backdrop-filter:blur(25px);border:1px solid rgba(0,255,200,0.15);box-shadow:0 0 40px rgba(0,255,200,0.08);padding:2.5rem 2rem;border-radius:20px;max-width:420px;width:100%;box-shadow:none;text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#00ff88;font-size:1.5rem;margin-bottom:0.5rem;}}
p{{color:rgba(255,255,255,0.6);font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid rgba(0,255,200,0.2);border-radius:12px;font-size:1rem;margin-bottom:1rem;background:rgba(255,255,255,0.08);transition:border-color .2s;color:white}}
input:focus{{outline:none;border-color:rgba(0,255,200,0.5);box-shadow:0 0 15px rgba(0,255,200,0.1)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,rgba(0,255,136,0.3),rgba(0,212,255,0.3));color:#00ff88;border:none;border-radius:12px;font-size:1rem;cursor:pointer;font-weight:600;border:1px solid rgba(0,255,200,0.3);transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 0 25px rgba(0,255,200,0.15)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:rgba(255,255,255,0.25);}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Let the aurora guide you out. Enter your email to leave our mailing list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">May the lights find your way.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 28: Concrete ──

def _concrete_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Arial Narrow',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#9e9e9e;padding:1rem}}
.card{{background:#e0e0e0;border:3px solid #757575;padding:2.5rem 2rem;border-radius:0;max-width:420px;width:100%;box-shadow:none;text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
h1{{color:#212121;font-size:1.5rem;margin-bottom:0.5rem;font-weight:900;text-transform:uppercase;letter-spacing:3px}}
p{{color:#616161;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #9e9e9e;border-radius:0;font-size:1rem;margin-bottom:1rem;background:#f5f5f5;transition:border-color .2s;text-transform:uppercase;letter-spacing:1px}}
input:focus{{outline:none;border-color:#424242;box-shadow:none}}
button{{width:100%;padding:0.9rem;background:#424242;color:white;border:none;border-radius:0;font-size:1rem;cursor:pointer;font-weight:900;text-transform:uppercase;letter-spacing:3px;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:none}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#9e9e9e;text-transform:uppercase;letter-spacing:1px}}
</style></head>
<body>
<div class="card">
<h1>Opt Out</h1>
<p>Remove your email from our list. No frills, just results.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="YOUR@EMAIL.COM" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Done.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 29: Orchid ──

def _orchid_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#e040fb,#d500f9,#aa00ff);padding:1rem}}
.card{{background:rgba(255,255,255,0.95);padding:2.5rem 2rem;border-radius:20px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(170,0,255,0.3);text-align:center;animation:flipIn .5s ease}}
@keyframes flipIn{{from{{opacity:0;transform:perspective(400px) rotateY(15deg)}}to{{opacity:1;transform:perspective(400px) rotateY(0)}}}}
h1{{color:#aa00ff;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#8a6a8a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #e1bee7;border-radius:16px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#d500f9;box-shadow:0 0 0 3px rgba(213,0,249,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#e040fb,#aa00ff);color:white;border:none;border-radius:16px;font-size:1rem;cursor:pointer;font-weight:700;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(170,0,255,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#ce93d8;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>We're exotic but not your thing? Enter your email to unsubscribe.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Orchids will bloom without you.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 30: Cloud ──

def _cloud_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(180deg,#f5f7fa,#c3cfe2);padding:1rem}}
.card{{background:white;padding:2.5rem 2rem;border-radius:30px;max-width:420px;width:100%;box-shadow:0 15px 40px rgba(0,0,0,0.08);text-align:center;animation:bounceIn .5s ease}}
@keyframes bounceIn{{from{{opacity:0;transform:translateY(30px) scale(0.95)}}to{{opacity:1;transform:translateY(0) scale(1)}}}}
h1{{color:#5a6a7a;font-size:1.5rem;margin-bottom:0.5rem;font-weight:500}}
p{{color:#90a4ae;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #e8edf2;border-radius:25px;font-size:1rem;margin-bottom:1rem;background:#f8f9fb;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#90a4ae;box-shadow:0 0 0 3px rgba(144,164,174,0.1)}}
button{{width:100%;padding:0.9rem;background:#78909c;color:white;border:none;border-radius:25px;font-size:1rem;cursor:pointer;font-weight:500;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 20px rgba(120,144,156,0.3)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#b0bec5;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Float away from our mailing list. Enter your email and you're free as a cloud.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Clouds drift, emails stop.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 31: Royal Purple ──

def _royal_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Georgia,'Times New Roman',serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#311b92,#4a148c,#6a1b9a);padding:1rem}}
.card{{background:#fffde7;border:3px solid #ffd54f;padding:2.5rem 2rem;border-radius:4px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(0,0,0,0.3);text-align:center;animation:rotateIn .5s ease}}
@keyframes rotateIn{{from{{opacity:0;transform:rotate(-2deg) scale(0.95)}}to{{opacity:1;transform:rotate(0) scale(1)}}}}
h1{{color:#4a148c;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700;text-shadow:1px 1px 0 #ffd54f}}
p{{color:#6a6a4a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #ffd54f;border-radius:4px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;font-family:Georgia,serif}}
input:focus{{outline:none;border-color:#6a1b9a;box-shadow:0 0 0 3px rgba(106,27,154,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#4a148c,#6a1b9a);color:#ffd54f;border:none;border-radius:4px;font-size:1rem;cursor:pointer;font-weight:700;font-family:Georgia,serif;border:2px solid #ffd54f;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(74,20,140,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#b0a0c0;font-style:italic}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Your royal departure awaits. Enter your email to be removed from our court.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Long live the king.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 32: Palm Beach ──

def _palmbeach_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#00b4db,#0083b0);padding:1rem}}
.card{{background:white;padding:2.5rem 2rem;border-radius:16px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(0,0,0,0.2);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(15px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#0083b0;font-size:1.5rem;margin-bottom:0.5rem;font-weight:600}}
p{{color:#6a8fa0;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #b2ebf2;border-radius:12px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#00acc1;box-shadow:0 0 0 3px rgba(0,172,193,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#f4516b,#ff8a65);color:white;border:none;border-radius:12px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(244,81,107,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#b0c4cc;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Leaving paradise? Enter your email to unsubscribe from our beach-side updates.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">See you under the palm trees.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 33: Volcano ──

def _volcano_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(180deg,#1a1a1a,#b71c1c,#ff6f00);padding:1rem}}
.card{{background:rgba(30,30,30,0.9);backdrop-filter:blur(15px);border:1px solid rgba(255,111,0,0.3);box-shadow:0 0 40px rgba(255,111,0,0.15);padding:2.5rem 2rem;border-radius:4px;max-width:420px;width:100%;box-shadow:none;text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:scale(0.95)}}to{{opacity:1;transform:scale(1)}}}}
h1{{color:#ff6f00;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700;text-transform:uppercase;letter-spacing:2px}}
p{{color:rgba(255,255,255,0.6);font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid rgba(255,111,0,0.3);border-radius:4px;font-size:1rem;margin-bottom:1rem;background:rgba(255,111,0,0.1);transition:border-color .2s;color:white}}
input:focus{{outline:none;border-color:#ff6f00;box-shadow:0 0 15px rgba(255,111,0,0.2)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#b71c1c,#ff6f00);color:white;border:none;border-radius:4px;font-size:1rem;cursor:pointer;font-weight:700;text-transform:uppercase;letter-spacing:2px;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(255,111,0,0.4)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:rgba(255,255,255,0.25);text-transform:uppercase;letter-spacing:1px}}
</style></head>
<body>
<div class="card">
<h1>Erupt</h1>
<p>Blaze your own trail. Enter your email to escape our mailing list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">The heat is off.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 34: Glacier ──

def _glacier_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#e8f4f8,#d1ecf1,#bee5eb);padding:1rem}}
.card{{background:white;border:1px solid #b8d4e3;padding:2.5rem 2rem;border-radius:8px;max-width:420px;width:100%;box-shadow:0 10px 35px rgba(0,0,0,0.08);text-align:center;animation:slideUp .5s ease}}
@keyframes slideUp{{from{{opacity:0;transform:translateY(15px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#2c7a7b;font-size:1.5rem;margin-bottom:0.5rem;font-weight:600}}
p{{color:#718096;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #bee5eb;border-radius:6px;font-size:1rem;margin-bottom:1rem;background:#f0f9ff;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#3182ce;box-shadow:0 0 0 3px rgba(49,130,206,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#2c7a7b,#3182ce);color:white;border:none;border-radius:6px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 20px rgba(49,130,206,0.3)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#a0aec0;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Enter your email and we'll gently remove you from our glacier of messages.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Stay frosty.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 35: Sahara ──

def _sahara_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Georgia,'Times New Roman',serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#e6a817,#d4910a,#c2790a);padding:1rem}}
.card{{background:rgba(255,250,235,0.95);padding:2.5rem 2rem;border-radius:12px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(0,0,0,0.2);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(15px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#8b6914;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#8a7a5a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #e0c88a;border-radius:8px;font-size:1rem;margin-bottom:1rem;background:rgba(255,255,255,0.6);transition:border-color .2s;font-family:Georgia,serif}}
input:focus{{outline:none;border-color:#c2790a;box-shadow:0 0 0 3px rgba(194,121,10,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#c2790a,#e6a817);color:white;border:none;border-radius:8px;font-size:1rem;cursor:pointer;font-weight:700;font-family:Georgia,serif;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(194,121,10,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#c0a870;font-style:italic}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Cross the desert of no return. Enter your email to unsubscribe from our list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe Me</button>
</form>
<p class="footer">The oasis awaits.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe Me';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe Me';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 36: Neon Green ──

def _neongreen_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Courier New',monospace;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#0a0a0a;padding:1rem}}
.card{{background:#111;border:2px solid #00ff41;box-shadow:0 0 20px rgba(0,255,65,0.2),0 0 40px rgba(0,255,65,0.1);padding:2.5rem 2rem;border-radius:0;max-width:420px;width:100%;box-shadow:none;text-align:center;animation:glow .5s ease}}
@keyframes glow{{from{{opacity:0;box-shadow:0 0 0 rgba(0,255,65,0)}}to{{opacity:1;box-shadow:0 0 20px rgba(0,255,65,0.2)}}}}
h1{{color:#00ff41;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700;text-transform:uppercase;letter-spacing:4px}}
p{{color:#00cc33;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid #00ff41;border-radius:0;font-size:1rem;margin-bottom:1rem;background:#0a0a0a;transition:border-color .2s;color:#00ff41;font-family:inherit}}
input:focus{{outline:none;border-color:#00ff41;box-shadow:0 0 10px rgba(0,255,65,0.3)}}
button{{width:100%;padding:0.9rem;background:#00ff41;color:#0a0a0a;border:none;border-radius:0;font-size:1rem;cursor:pointer;font-weight:700;font-family:inherit;text-transform:uppercase;letter-spacing:3px;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 0 20px rgba(0,255,65,0.4)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#006622;}}
</style></head>
<body>
<div class="card">
<h1>OPT OUT</h1>
<p>Hack your inbox. Enter your email to unsubscribe from the matrix.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">UNSUBSCRIBE</button>
</form>
<p class="footer">>> system.unsubscribed</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='UNSUBSCRIBE';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='UNSUBSCRIBE';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 37: Plum ──

def _plum_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#4a0e4e,#6b1a5a,#8b2252);padding:1rem}}
.card{{background:rgba(255,255,255,0.93);padding:2.5rem 2rem;border-radius:16px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(74,14,78,0.3);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#4a0e4e;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#7a5a7a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #d1a0d1;border-radius:10px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#8b2252;box-shadow:0 0 0 3px rgba(139,34,82,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#4a0e4e,#8b2252);color:white;border:none;border-radius:10px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(74,14,78,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#c0a0c0;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Rich decisions deserve respect. Enter your email to leave our list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">A plum farewell.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 38: Ice Blue ──

def _iceblue_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#e0f7fa,#b3e5fc,#81d4fa);padding:1rem}}
.card{{background:rgba(255,255,255,0.75);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.8);padding:2.5rem 2rem;border-radius:20px;max-width:420px;width:100%;box-shadow:0 10px 35px rgba(0,0,0,0.06);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:scale(0.97)}}to{{opacity:1;transform:scale(1)}}}}
h1{{color:#0277bd;font-size:1.5rem;margin-bottom:0.5rem;font-weight:500}}
p{{color:#5a8a9a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid rgba(2,119,189,0.2);border-radius:14px;font-size:1rem;margin-bottom:1rem;background:rgba(255,255,255,0.6);transition:border-color .2s;}}
input:focus{{outline:none;border-color:#0288d1;box-shadow:0 0 0 3px rgba(2,136,209,0.1)}}
button{{width:100%;padding:0.9rem;background:#0288d1;color:white;border:none;border-radius:14px;font-size:1rem;cursor:pointer;font-weight:500;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 20px rgba(2,136,209,0.3)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#90caf9;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>A frozen moment to say goodbye. Enter your email to leave our list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe Me</button>
</form>
<p class="footer">Winter is passing.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe Me';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe Me';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 39: Burnt Orange ──

def _burntorange_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#bf360c,#e65100,#ef6c00);padding:1rem}}
.card{{background:#fef3e8;border:2px solid #ffcc80;padding:2.5rem 2rem;border-radius:12px;max-width:420px;width:100%;box-shadow:0 15px 40px rgba(191,54,12,0.2);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(15px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#bf360c;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#8a6a4a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #ffcc80;border-radius:8px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#ef6c00;box-shadow:0 0 0 3px rgba(239,108,0,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#bf360c,#ef6c00);color:white;border:none;border-radius:8px;font-size:1rem;cursor:pointer;font-weight:700;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(191,54,12,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#c0a070;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Earthy goodbyes are the warmest. Enter your email to opt out.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Keep it real.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 40: Indigo Night ──

def _indigonight_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#1a0033,#2d0066,#3f0099);padding:1rem}}
.card{{background:rgba(255,255,255,0.08);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.12);padding:2.5rem 2rem;border-radius:16px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(0,0,0,0.4);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(20px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#b388ff;font-size:1.5rem;margin-bottom:0.5rem;font-weight:600}}
p{{color:rgba(255,255,255,0.5);font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid rgba(179,136,255,0.3);border-radius:10px;font-size:1rem;margin-bottom:1rem;background:rgba(255,255,255,0.05);transition:border-color .2s;color:white}}
input:focus{{outline:none;border-color:#b388ff;box-shadow:0 0 12px rgba(179,136,255,0.2)}}
button{{width:100%;padding:0.9rem;background:rgba(179,136,255,0.25);color:#b388ff;border:none;border-radius:10px;font-size:1rem;cursor:pointer;font-weight:600;border:1px solid rgba(179,136,255,0.4);transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 0 20px rgba(179,136,255,0.2)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:rgba(255,255,255,0.2);}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>The night is dark and full of unsubscribes. Enter your email below.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Shadows fade, emails end.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 41: Peach ──

def _peach_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#ffecd2,#fcb69f);padding:1rem}}
.card{{background:white;padding:2.5rem 2rem;border-radius:20px;max-width:420px;width:100%;box-shadow:0 15px 40px rgba(252,182,159,0.25);text-align:center;animation:bounceIn .5s ease}}
@keyframes bounceIn{{from{{opacity:0;transform:translateY(20px) scale(0.95)}}to{{opacity:1;transform:translateY(0) scale(1)}}}}
h1{{color:#d4614a;font-size:1.5rem;margin-bottom:0.5rem;font-weight:600}}
p{{color:#a08070;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #f8d5c0;border-radius:16px;font-size:1rem;margin-bottom:1rem;background:#fff8f8;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#f08060;box-shadow:0 0 0 3px rgba(240,128,96,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#f08060,#e06050);color:white;border:none;border-radius:16px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(224,96,80,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#d4b0a0;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>A gentle parting of ways. Enter your email to leave our mailing list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe Me</button>
</form>
<p class="footer">Peachy keen without us.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe Me';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe Me';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 42: Steel Blue ──

def _steelblue_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#4a6fa5,#607d9a,#78909c);padding:1rem}}
.card{{background:#f8f9fa;border:1px solid #dee2e6;padding:2.5rem 2rem;border-radius:8px;max-width:420px;width:100%;box-shadow:0 8px 30px rgba(0,0,0,0.1);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
h1{{color:#34495e;font-size:1.5rem;margin-bottom:0.5rem;font-weight:600}}
p{{color:#6c757d;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid #ced4da;border-radius:6px;font-size:1rem;margin-bottom:1rem;background:white;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#4a6fa5;box-shadow:0 0 0 3px rgba(74,111,165,0.12)}}
button{{width:100%;padding:0.9rem;background:#4a6fa5;color:white;border:none;border-radius:6px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 6px 20px rgba(74,111,165,0.3)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#adb5bd;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Professional and clean. Enter your email to unsubscribe from our communications.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Corporate courtesy.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 43: Mahogany ──

def _mahogany_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Georgia,'Times New Roman',serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#4e2a04,#6b3a1f,#8b4513);padding:1rem}}
.card{{background:#faf3eb;border:2px solid #c9a96e;padding:2.5rem 2rem;border-radius:8px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(78,42,4,0.3);text-align:center;animation:rotateIn .5s ease}}
@keyframes rotateIn{{from{{opacity:0;transform:rotate(-2deg) scale(0.96)}}to{{opacity:1;transform:rotate(0) scale(1)}}}}
h1{{color:#4e2a04;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#7a6040;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #c9a96e;border-radius:6px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;font-family:Georgia,serif}}
input:focus{{outline:none;border-color:#8b4513;box-shadow:0 0 0 3px rgba(139,69,19,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#4e2a04,#8b4513);color:#c9a96e;border:none;border-radius:6px;font-size:1rem;cursor:pointer;font-weight:700;font-family:Georgia,serif;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(78,42,4,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#b09070;font-style:italic}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Fine furniture, fine choices. Enter your email to leave our mailing list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Crafted with care.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 44: Cerulean ──

def _cerulean_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#007ba7,#0288d1,#29b6f6);padding:1rem}}
.card{{background:white;padding:2.5rem 2rem;border-radius:20px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(0,123,167,0.2);text-align:center;animation:popIn .5s ease}}
@keyframes popIn{{from{{opacity:0;transform:scale(0.9)}}to{{opacity:1;transform:scale(1)}}}}
h1{{color:#007ba7;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#5a8a9a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #b3e5fc;border-radius:14px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#0288d1;box-shadow:0 0 0 3px rgba(2,136,209,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#007ba7,#29b6f6);color:white;border:none;border-radius:14px;font-size:1rem;cursor:pointer;font-weight:700;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(0,123,167,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#90caf9;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Clear as a cerulean sky. Enter your email to opt out of our list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe Me</button>
</form>
<p class="footer">The sky's the limit.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe Me';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe Me';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 45: Olive ──

def _olive_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Arial Narrow',sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#3e4a1e,#556b2f,#6b8e23);padding:1rem}}
.card{{background:#f5f5dc;border:2px solid #9e9e5a;padding:2.5rem 2rem;border-radius:4px;max-width:420px;width:100%;box-shadow:0 15px 40px rgba(0,0,0,0.2);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
h1{{color:#3e4a1e;font-size:1.5rem;margin-bottom:0.5rem;font-weight:900;text-transform:uppercase;letter-spacing:2px}}
p{{color:#6b7a4a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #9e9e5a;border-radius:4px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;text-transform:uppercase}}
input:focus{{outline:none;border-color:#556b2f;box-shadow:none}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#3e4a1e,#6b8e23);color:#f5f5dc;border:none;border-radius:4px;font-size:1rem;cursor:pointer;font-weight:900;text-transform:uppercase;letter-spacing:2px;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:none}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#9e9e5a;text-transform:uppercase;letter-spacing:1px}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Duty calls. Enter your email to be removed from our roster permanently.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Mission complete.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 46: Crimson ──

def _crimson_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#dc143c,#b91c1c,#991b1b);padding:1rem}}
.card{{background:white;border-left:6px solid #dc143c;padding:2.5rem 2rem;border-radius:8px;max-width:420px;width:100%;box-shadow:0 25px 60px rgba(220,20,60,0.25);text-align:center;animation:scaleIn .5s ease}}
@keyframes scaleIn{{from{{opacity:0;transform:scale(0.9)}}to{{opacity:1;transform:scale(1)}}}}
h1{{color:#dc143c;font-size:1.5rem;margin-bottom:0.5rem;font-weight:800;text-transform:uppercase;letter-spacing:1px}}
p{{color:#666;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #fecaca;border-radius:6px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#dc143c;box-shadow:0 0 0 3px rgba(220,20,60,0.12)}}
button{{width:100%;padding:0.9rem;background:#dc143c;color:white;border:none;border-radius:6px;font-size:1rem;cursor:pointer;font-weight:800;text-transform:uppercase;letter-spacing:1px;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(220,20,60,0.4)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#e57373;font-weight:600}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Urgent and bold. Enter your email to stop receiving our communications immediately.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">UNSUBSCRIBE NOW</button>
</form>
<p class="footer">No turning back.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='UNSUBSCRIBE NOW';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='UNSUBSCRIBE NOW';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 47: Periwinkle ──

def _periwinkle_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#7c73e6,#9d8df1,#b8a9e8);padding:1rem}}
.card{{background:rgba(255,255,255,0.92);padding:2.5rem 2rem;border-radius:18px;max-width:420px;width:100%;box-shadow:0 15px 45px rgba(124,115,230,0.2);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0;transform:translateY(12px)}}to{{opacity:1;transform:translateY(0)}}}}
h1{{color:#5b4fcf;font-size:1.5rem;margin-bottom:0.5rem;font-weight:600}}
p{{color:#7a7a9a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #c5bfe8;border-radius:12px;font-size:1rem;margin-bottom:1rem;background:rgba(255,255,255,0.6);transition:border-color .2s;}}
input:focus{{outline:none;border-color:#7c73e6;box-shadow:0 0 0 3px rgba(124,115,230,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#5b4fcf,#9d8df1);color:white;border:none;border-radius:12px;font-size:1rem;cursor:pointer;font-weight:600;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(91,79,207,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#b0a0d0;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Soft and unique, just like your choice. Enter your email to leave our list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Until our paths cross again.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 48: Tangerine ──

def _tangerine_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#ff8c00,#ff6b00,#ff4500);padding:1rem}}
.card{{background:white;padding:2.5rem 2rem;border-radius:20px;max-width:420px;width:100%;box-shadow:0 20px 50px rgba(255,140,0,0.25);text-align:center;animation:bounceIn .5s ease}}
@keyframes bounceIn{{from{{opacity:0;transform:scale(0.85) rotate(-2deg)}}to{{opacity:1;transform:scale(1) rotate(0)}}}}
h1{{color:#e65100;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700}}
p{{color:#8a6a4a;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #ffcc80;border-radius:14px;font-size:1rem;margin-bottom:1rem;background:#fff8ee;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#ff8c00;box-shadow:0 0 0 3px rgba(255,140,0,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#ff8c00,#ff4500);color:white;border:none;border-radius:14px;font-size:1rem;cursor:pointer;font-weight:700;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(255,69,0,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#d4a060;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Energetic goodbye! Enter your email to opt out and juice up your inbox.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Squeeze you later.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 49: Gunmetal ──

def _gunmetal_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#2c3539,#3a4a4e,#4a5c62);padding:1rem}}
.card{{background:#f0f2f3;border:1px solid #c0c8cc;padding:2.5rem 2rem;border-radius:2px;max-width:420px;width:100%;box-shadow:0 15px 40px rgba(0,0,0,0.15);text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
h1{{color:#2c3539;font-size:1.5rem;margin-bottom:0.5rem;font-weight:600;letter-spacing:0.5px}}
p{{color:#6a7a80;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #c0c8cc;border-radius:2px;font-size:1rem;margin-bottom:1rem;background:white;transition:border-color .2s;}}
input:focus{{outline:none;border-color:#3a4a4e;box-shadow:none}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#2c3539,#4a5c62);color:white;border:none;border-radius:2px;font-size:1rem;cursor:pointer;font-weight:600;letter-spacing:0.5px;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 6px 20px rgba(44,53,57,0.3)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#a0a8ac;}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>Sleek and modern exit. Enter your email to unsubscribe from our platform.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Stay sharp.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""


# ── Theme 50: Maroon & Gold ──

def _maraungold_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Georgia,'Times New Roman',serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#5a0a0a,#800020,#a02020);padding:1rem}}
.card{{background:#fffbf0;border:2px solid #c9a94e;padding:2.5rem 2rem;border-radius:4px;max-width:420px;width:100%;box-shadow:0 25px 60px rgba(90,10,10,0.3);text-align:center;animation:rotateIn .5s ease}}
@keyframes rotateIn{{from{{opacity:0;transform:rotate(-2deg) scale(0.96)}}to{{opacity:1;transform:rotate(0) scale(1)}}}}
h1{{color:#800020;font-size:1.5rem;margin-bottom:0.5rem;font-weight:700;font-style:italic}}
p{{color:#6a5030;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #c9a94e;border-radius:4px;font-size:1rem;margin-bottom:1rem;background:transparent;transition:border-color .2s;font-family:Georgia,serif}}
input:focus{{outline:none;border-color:#800020;box-shadow:0 0 0 3px rgba(128,0,32,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#800020,#a02020);color:#c9a94e;border:none;border-radius:4px;font-size:1rem;cursor:pointer;font-weight:700;font-family:Georgia,serif;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(128,0,32,0.35)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#c9a94e;font-style:italic}}
</style></head>
<body>
<div class="card">
<h1>Unsubscribe</h1>
<p>A classic departure. Enter your email to leave our distinguished mailing list.</p>
<form id="f" onsubmit="return submitForm(event)">
<input type="email" id="e" placeholder="your@email.com" required>
<button type="submit">Unsubscribe</button>
</form>
<p class="footer">Class never fades.</p>
</div>
<script>
async function submitForm(ev){{ev.preventDefault();const b=document.querySelector('button');b.disabled=true;b.textContent='Processing...';try{{const r=await fetch('/u',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{token:'{token}',email:document.getElementById('e').value.toLowerCase()}})}});if(r.ok){{window.location.href='/u/success';return}}const d=await r.json();b.disabled=false;b.textContent='Unsubscribe';alert(d.detail||'Error occurred')}}catch(e){{b.disabled=false;b.textContent='Unsubscribe';alert('Network error')}}}}
</script>
</body></html>"""

def _ocean_success() -> str:
    return _success_base(
        "#0f2027,#203a43,#2c5364",
        "#0f2027", "#2c5364",
        "#e8f4f8", "#0f2027",
        "rgba(0,0,0,0.3)",
    )

def _sunset_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#ff512f,#dd2476)",
        "#333", "#dd2476",
        "#fff0f5", "#dd2476",
        "rgba(0,0,0,0.25)",
    )

def _dark_success() -> str:
    return _success_base(
        "#111",
        "#f5f5f5", "#f5f5f5",
        "#1e1e1e", "#4caf50",
        "none",
    )

def _forest_success() -> str:
    return _success_base(
        "linear-gradient(160deg,#134e5e,#71b280)",
        "#333", "#134e5e",
        "#e8f5e9", "#2e7d32",
        "0 15px 50px rgba(0,0,0,0.2)",
    )

def _purple_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#667eea,#764ba2)",
        "#fff", "white",
        "rgba(255,255,255,0.15)", "#4caf50",
        "none",
        glass=True,
        glass_border="1px solid rgba(255,255,255,0.25)",
        glass_blur="blur(20px)",
    )

def _clean_success() -> str:
    return _success_base(
        "#fafafa",
        "#222", "#2e7d32",
        "white", "#2e7d32",
        "0 1px 3px rgba(0,0,0,0.08)",
    )

def _midnight_success() -> str:
    return _success_base(
        "linear-gradient(180deg,#0a1628,#162447,#1f4068)",
        "#ffffff", "#48bb78",
        "#ffffff", "#1f4068",
        "0 30px 60px rgba(0,0,0,0.4)",
    )

def _neonpink_success() -> str:
    return _success_base(
        "#0d0d0d",
        "#ff006e", "#ff006e",
        "#1a1a1a", "#ff006e",
        "0 0 30px rgba(255,0,110,0.3)",
    )

def _mint_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#e0f7fa,#b2dfdb,#80cbc4)",
        "#00695c", "#00897b",
        "#ffffff", "#00897b",
        "0 12px 40px rgba(0,77,64,0.15)",
    )

def _coral_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#ff9a9e,#fecfef,#fad0c4)",
        "#e55353", "#ff6b6b",
        "rgba(255,255,255,0.9)", "#ff6b6b",
        "0 20px 50px rgba(255,107,107,0.2)",
    )

def _charcoal_success() -> str:
    return _success_base(
        "#2d2d2d",
        "#e0e0e0", "#66bb6a",
        "#3a3a3a", "#66bb6a",
        "none",
    )

def _lavender_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#e8d5f5,#d5c8f0,#c4b5e8)",
        "#5b3a8c", "#7c5cbf",
        "rgba(255,255,255,0.85)", "#7c5cbf",
        "0 15px 45px rgba(120,80,180,0.15)",
    )

def _emerald_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#004d40,#00695c,#00897b)",
        "#ffffff", "#69f0ae",
        "#ffffff", "#004d40",
        "0 25px 55px rgba(0,0,0,0.3)",
    )

def _ruby_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#8b0000,#b71c1c,#d32f2f)",
        "#ffffff", "#ef5350",
        "rgba(255,255,255,0.95)", "#d32f2f",
        "0 25px 50px rgba(139,0,0,0.3)",
    )

def _sapphire_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#0d47a1,#1565c0,#1976d2)",
        "#ffffff", "#42a5f5",
        "rgba(255,255,255,0.92)", "#1976d2",
        "0 20px 50px rgba(13,71,161,0.25)",
    )

def _amber_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#f57f17,#ff8f00,#ffa000)",
        "#e65100", "#ff8f00",
        "#ffffff", "#ffa000",
        "0 20px 50px rgba(245,127,23,0.25)",
    )

def _rosequartz_success() -> str:
    return _success_base(
        "#fdf2f0",
        "#a0605a", "#c08070",
        "white", "#a0605a",
        "0 4px 20px rgba(0,0,0,0.05)",
    )

def _arctic_success() -> str:
    return _success_base(
        "linear-gradient(180deg,#e3f2fd,#bbdefb,#90caf9)",
        "#1565c0", "#42a5f5",
        "rgba(255,255,255,0.8)", "#1976d2",
        "0 10px 40px rgba(66,165,245,0.15)",
    )

def _tropical_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#00b09b,#96c93d)",
        "#00897b", "#7cb342",
        "#ffffff", "#00b09b",
        "0 20px 50px rgba(0,0,0,0.2)",
    )

def _cosmic_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#0c0c1d,#1a0a2e,#16213e)",
        "#e1bee7", "#ce93d8",
        "rgba(22,33,62,0.85)", "#ce93d8",
        "0 0 30px rgba(206,147,216,0.15)",
        glass=True,
        glass_border="1px solid rgba(255,255,255,0.1)",
        glass_blur="blur(20px)",
    )

def _autumn_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#bf360c,#e65100,#f57f17)",
        "#ffffff", "#ffab40",
        "rgba(255,248,240,0.95)", "#bf360c",
        "0 20px 50px rgba(0,0,0,0.25)",
    )

def _storm_success() -> str:
    return _success_base(
        "linear-gradient(180deg,#263238,#37474f,#455a64)",
        "#ffffff", "#90a4ae",
        "rgba(255,255,255,0.9)", "#263238",
        "0 30px 60px rgba(0,0,0,0.4)",
    )

def _bamboo_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#c0ca33,#9e9d24,#827717)",
        "#ffffff", "#aed581",
        "#fffff0", "#558b2f",
        "0 12px 35px rgba(0,0,0,0.15)",
    )

def _cherryblossom_success() -> str:
    return _success_base(
        "#fff5f5",
        "#c2185b", "#e91e63",
        "white", "#f8bbd0",
        "0 4px 25px rgba(0,0,0,0.06)",
    )

def _deepsea_success() -> str:
    return _success_base(
        "linear-gradient(180deg,#001f3f,#003366,#004080)",
        "#80deea", "#4dd0e1",
        "rgba(0,50,80,0.7)", "#80deea",
        "none",
        glass=True,
        glass_border="1px solid rgba(0,150,200,0.2)",
        glass_blur="blur(15px)",
    )

def _sunsetblvd_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#f093fb,#f5576c,#fda085)",
        "#ffffff", "#fda085",
        "rgba(255,255,255,0.92)", "#f5576c",
        "0 20px 50px rgba(245,87,108,0.25)",
    )

def _northernlights_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#0f0c29,#302b63,#24243e)",
        "#00ff88", "#00d4ff",
        "rgba(255,255,255,0.1)", "#00ff88",
        "0 0 40px rgba(0,255,200,0.08)",
        glass=True,
        glass_border="1px solid rgba(0,255,200,0.15)",
        glass_blur="blur(25px)",
    )

def _concrete_success() -> str:
    return _success_base(
        "#9e9e9e",
        "#212121", "#424242",
        "#e0e0e0", "#424242",
        "none",
    )

def _orchid_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#e040fb,#d500f9,#aa00ff)",
        "#ffffff", "#ea80fc",
        "rgba(255,255,255,0.95)", "#d500f9",
        "0 20px 50px rgba(170,0,255,0.3)",
    )

def _cloud_success() -> str:
    return _success_base(
        "linear-gradient(180deg,#f5f7fa,#c3cfe2)",
        "#5a6a7a", "#78909c",
        "white", "#90a4ae",
        "0 15px 40px rgba(0,0,0,0.08)",
    )

def _royal_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#311b92,#4a148c,#6a1b9a)",
        "#ffd54f", "#ffd54f",
        "#fffde7", "#4a148c",
        "0 20px 50px rgba(0,0,0,0.3)",
    )

def _palmbeach_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#00b4db,#0083b0)",
        "#ffffff", "#4dd0e1",
        "#ffffff", "#0083b0",
        "0 20px 50px rgba(0,0,0,0.2)",
    )

def _volcano_success() -> str:
    return _success_base(
        "linear-gradient(180deg,#1a1a1a,#b71c1c,#ff6f00)",
        "#ff6f00", "#ff9800",
        "rgba(30,30,30,0.9)", "#ff6f00",
        "0 0 40px rgba(255,111,0,0.15)",
        glass=True,
        glass_border="1px solid rgba(255,111,0,0.3)",
        glass_blur="blur(15px)",
    )

def _glacier_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#e8f4f8,#d1ecf1,#bee5eb)",
        "#2c7a7b", "#3182ce",
        "white", "#3182ce",
        "0 10px 35px rgba(0,0,0,0.08)",
    )

def _sahara_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#e6a817,#d4910a,#c2790a)",
        "#ffffff", "#e6a817",
        "rgba(255,250,235,0.95)", "#c2790a",
        "0 20px 50px rgba(0,0,0,0.2)",
    )

def _neongreen_success() -> str:
    return _success_base(
        "#0a0a0a",
        "#00ff41", "#00ff41",
        "#111", "#00ff41",
        "0 0 20px rgba(0,255,65,0.2)",
    )

def _plum_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#4a0e4e,#6b1a5a,#8b2252)",
        "#ffffff", "#d1a0d1",
        "rgba(255,255,255,0.93)", "#8b2252",
        "0 20px 50px rgba(74,14,78,0.3)",
    )

def _iceblue_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#e0f7fa,#b3e5fc,#81d4fa)",
        "#0277bd", "#0288d1",
        "rgba(255,255,255,0.75)", "#0288d1",
        "0 10px 35px rgba(0,0,0,0.06)",
        glass=True,
        glass_border="1px solid rgba(255,255,255,0.8)",
        glass_blur="blur(20px)",
    )

def _burntorange_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#bf360c,#e65100,#ef6c00)",
        "#ffffff", "#ffcc80",
        "#fef3e8", "#bf360c",
        "0 15px 40px rgba(191,54,12,0.2)",
    )

def _indigonight_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#1a0033,#2d0066,#3f0099)",
        "#b388ff", "#b388ff",
        "rgba(255,255,255,0.08)", "#b388ff",
        "0 20px 50px rgba(0,0,0,0.4)",
        glass=True,
        glass_border="1px solid rgba(255,255,255,0.12)",
        glass_blur="blur(20px)",
    )

def _peach_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#ffecd2,#fcb69f)",
        "#d4614a", "#f08060",
        "white", "#f08060",
        "0 15px 40px rgba(252,182,159,0.25)",
    )

def _steelblue_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#4a6fa5,#607d9a,#78909c)",
        "#ffffff", "#90caf9",
        "#f8f9fa", "#4a6fa5",
        "0 8px 30px rgba(0,0,0,0.1)",
    )

def _mahogany_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#4e2a04,#6b3a1f,#8b4513)",
        "#faf3eb", "#c9a96e",
        "#faf3eb", "#4e2a04",
        "0 20px 50px rgba(78,42,4,0.3)",
    )

def _cerulean_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#007ba7,#0288d1,#29b6f6)",
        "#ffffff", "#29b6f6",
        "white", "#007ba7",
        "0 20px 50px rgba(0,123,167,0.2)",
    )

def _olive_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#3e4a1e,#556b2f,#6b8e23)",
        "#f5f5dc", "#6b8e23",
        "#f5f5dc", "#556b2f",
        "0 15px 40px rgba(0,0,0,0.2)",
    )

def _crimson_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#dc143c,#b91c1c,#991b1b)",
        "#ffffff", "#ef5350",
        "white", "#dc143c",
        "0 25px 60px rgba(220,20,60,0.25)",
    )

def _periwinkle_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#7c73e6,#9d8df1,#b8a9e8)",
        "#ffffff", "#b8a9e8",
        "rgba(255,255,255,0.92)", "#5b4fcf",
        "0 15px 45px rgba(124,115,230,0.2)",
    )

def _tangerine_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#ff8c00,#ff6b00,#ff4500)",
        "#ffffff", "#ffcc80",
        "white", "#ff8c00",
        "0 20px 50px rgba(255,140,0,0.25)",
    )

def _gunmetal_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#2c3539,#3a4a4e,#4a5c62)",
        "#ffffff", "#90a4ae",
        "#f0f2f3", "#2c3539",
        "0 15px 40px rgba(0,0,0,0.15)",
    )

def _maraungold_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#5a0a0a,#800020,#a02020)",
        "#c9a94e", "#c9a94e",
        "#fffbf0", "#800020",
        "0 25px 60px rgba(90,10,10,0.3)",
    )



# ── Shared success base ──

def _success_base(
    bg,
    h1_color,
    accent,
    card_bg,
    icon_color,
    shadow,
    glass=False,
    glass_border="",
    glass_blur="",
) -> str:
    card_style = f"background:{card_bg};"
    if glass:
        card_style += f"backdrop-filter:{glass_blur};border:{glass_border};"
    else:
        card_style += "border-radius:16px;"

    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribed</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:{bg};padding:1rem}}
.card{{{card_style}padding:2.5rem 2rem;max-width:420px;width:100%;box-shadow:{shadow};text-align:center;animation:popIn .5s ease}}
@keyframes popIn{{from{{opacity:0;transform:translateY(12px) scale(0.96)}}to{{opacity:1;transform:translateY(0) scale(1)}}}}
.icon{{width:64px;height:64px;border-radius:50%;background:{icon_color};display:flex;align-items:center;justify-content:center;margin:0 auto 1.25rem}}
.icon svg{{width:32px;height:32px}}
h1{{color:{h1_color};font-size:1.35rem;margin-bottom:0.5rem;font-weight:600}}
p{{color:#666;font-size:0.9rem;line-height:1.6;margin:0}}
</style></head>
<body>
<div class="card">
<div class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg></div>
<h1>You're unsubscribed</h1>
<p>You have been successfully removed from our mailing list. You will no longer receive emails from us.</p>
</div>
</body></html>"""
