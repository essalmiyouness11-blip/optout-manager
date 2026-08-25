import random


def random_email_form(token: str) -> str:
    templates = [
        _ocean_form(token),
        _sunset_form(token),
        _dark_form(token),
        _forest_form(token),
        _purple_form(token),
        _clean_form(token),
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
h1{{color:#0f2027;font-size:1.5rem;margin-bottom:0.5rem}}
p{{color:#5a6a75;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.5}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #d1e3eb;border-radius:10px;font-size:1rem;margin-bottom:1rem;transition:border-color .2s}}
input:focus{{outline:none;border-color:#2c5364;box-shadow:0 0 0 3px rgba(44,83,100,0.15)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#0f2027,#2c5364);color:white;border:none;border-radius:10px;font-size:1rem;font-weight:600;cursor:pointer;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-1px);box-shadow:0 6px 20px rgba(44,83,100,0.4)}}
button:active{{transform:translateY(0)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#9aa}}
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


def _ocean_success() -> str:
    return _success_base(
        "#0f2027,#203a43,#2c5364",
        "#0f2027", "#2c5364",
        "#e8f4f8", "#0f2027",
        "rgba(0,0,0,0.3)",
    )


# ── Theme 2: Sunset ──

def _sunset_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#ff512f,#dd2476);padding:1rem}}
.card{{background:white;padding:2.5rem 2rem;border-radius:16px;max-width:420px;width:100%;box-shadow:0 25px 60px rgba(0,0,0,0.25);text-align:center;animation:popIn .4s ease}}
@keyframes popIn{{from{{opacity:0;transform:scale(0.9)}}to{{opacity:1;transform:scale(1)}}}}
h1{{color:#333;font-size:1.4rem;margin-bottom:0.5rem}}
p{{color:#666;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:2px solid #eee;border-radius:12px;font-size:1rem;margin-bottom:1rem;transition:border-color .2s}}
input:focus{{outline:none;border-color:#dd2476;box-shadow:0 0 0 3px rgba(221,36,118,0.15)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#ff512f,#dd2476);color:white;border:none;border-radius:12px;font-size:1rem;font-weight:600;cursor:pointer;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(221,36,118,0.4)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#aaa}}
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


def _sunset_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#ff512f,#dd2476)",
        "#333", "#dd2476",
        "#fff0f5", "#dd2476",
        "rgba(0,0,0,0.25)",
    )


# ── Theme 3: Dark Minimal ──

def _dark_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#111;padding:1rem}}
.card{{background:#1e1e1e;padding:2.5rem 2rem;max-width:420px;width:100%;text-align:center;animation:fadeIn .5s ease}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
h1{{color:#f5f5f5;font-size:1.4rem;margin-bottom:0.75rem;font-weight:300;letter-spacing:0.5px}}
p{{color:#888;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;background:#2a2a2a;border:1px solid #333;border-radius:4px;font-size:1rem;color:#f5f5f5;margin-bottom:1rem;transition:border-color .2s}}
input::placeholder{{color:#666}}
input:focus{{outline:none;border-color:#f5f5f5}}
button{{width:100%;padding:0.9rem;background:#f5f5f5;color:#111;border:none;border-radius:4px;font-size:0.95rem;font-weight:500;cursor:pointer;transition:background .2s;letter-spacing:0.3px}}
button:hover{{background:#e0e0e0}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:#555}}
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


def _dark_success() -> str:
    return _success_base(
        "#111",
        "#f5f5f5", "#f5f5f5",
        "#1e1e1e",
        "#4caf50",
        "none",
    )


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
h1{{color:#134e5e;font-size:1.45rem;margin-bottom:0.5rem}}
p{{color:#5a6b5a;font-size:0.92rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.8rem 1rem;border:2px solid #c8dcc8;border-radius:8px;font-size:1rem;margin-bottom:1rem;font-family:inherit;transition:border-color .2s}}
input:focus{{outline:none;border-color:#134e5e;box-shadow:0 0 0 3px rgba(19,78,94,0.12)}}
button{{width:100%;padding:0.9rem;background:linear-gradient(135deg,#134e5e,#71b280);color:white;border:none;border-radius:8px;font-size:1rem;font-weight:600;cursor:pointer;font-family:inherit;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-1px);box-shadow:0 6px 18px rgba(19,78,94,0.35)}}
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


def _forest_success() -> str:
    return _success_base(
        "linear-gradient(160deg,#134e5e,#71b280)",
        "#333", "#134e5e",
        "#e8f5e9",
        "#2e7d32",
        "0 15px 50px rgba(0,0,0,0.2)",
    )


# ── Theme 5: Purple Haze ──

def _purple_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:linear-gradient(135deg,#667eea,#764ba2);padding:1rem}}
.card{{background:rgba(255,255,255,0.15);backdrop-filter:blur(20px);border:1px solid rgba(255,255,255,0.25);padding:2.5rem 2rem;border-radius:20px;max-width:420px;width:100%;text-align:center;color:white;animation:scaleIn .4s ease}}
@keyframes scaleIn{{from{{opacity:0;transform:scale(0.92)}}to{{opacity:1;transform:scale(1)}}}}
h1{{font-size:1.5rem;margin-bottom:0.5rem;font-weight:600}}
p{{color:rgba(255,255,255,0.8);font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;background:rgba(255,255,255,0.15);border:1px solid rgba(255,255,255,0.3);border-radius:12px;font-size:1rem;color:white;margin-bottom:1rem;transition:border-color .2s}}
input::placeholder{{color:rgba(255,255,255,0.5)}}
input:focus{{outline:none;border-color:white;background:rgba(255,255,255,0.2)}}
button{{width:100%;padding:0.9rem;background:white;color:#764ba2;border:none;border-radius:12px;font-size:1rem;font-weight:700;cursor:pointer;transition:transform .15s,box-shadow .15s}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(0,0,0,0.2)}}
.footer{{margin-top:1.25rem;font-size:0.75rem;color:rgba(255,255,255,0.5)}}
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


def _purple_success() -> str:
    return _success_base(
        "linear-gradient(135deg,#667eea,#764ba2)",
        "#fff", "white",
        "rgba(255,255,255,0.15)",
        "#4caf50",
        "none",
        glass=True,
        glass_border="1px solid rgba(255,255,255,0.25)",
        glass_blur="blur(20px)",
    )


# ── Theme 6: Clean White ──

def _clean_form(token: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Unsubscribe</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;background:#fafafa;padding:1rem}}
.card{{background:white;padding:3rem 2rem;border:1px solid #e5e5e5;max-width:440px;width:100%;text-align:center;animation:fadeIn .4s ease}}
@keyframes fadeIn{{from{{opacity:0}}to{{opacity:1}}}}
h1{{color:#222;font-size:1.3rem;margin-bottom:0.5rem;font-weight:500}}
p{{color:#888;font-size:0.9rem;margin-bottom:1.5rem;line-height:1.6}}
input{{width:100%;padding:0.85rem 1rem;border:1px solid #ddd;border-radius:6px;font-size:1rem;margin-bottom:1rem;transition:border-color .2s;appearance:none}}
input:focus{{outline:none;border-color:#555}}
button{{width:100%;padding:0.85rem;background:#222;color:white;border:none;border-radius:6px;font-size:0.95rem;font-weight:500;cursor:pointer;transition:background .2s}}
button:hover{{background:#333}}
.footer{{margin-top:1.5rem;font-size:0.75rem;color:#bbb}}
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


def _clean_success() -> str:
    return _success_base(
        "#fafafa",
        "#222", "#2e7d32",
        "white", "#2e7d32",
        "0 1px 3px rgba(0,0,0,0.08)",
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
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif);min-height:100vh;display:flex;align-items:center;justify-content:center;background:{bg};padding:1rem}}
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
