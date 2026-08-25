# Suppression Manager

A stateless, self-hosted opt-out and suppression manager for affiliate marketers. Collect unsubscribe requests, manage suppression lists per offer/network/global, and serve permanent suppression feeds to ESPs — all without a database.

## Architecture

```
┌─────────────────────────────────────────────────┐
│                  Nginx + Certbot                 │
│         (TLS termination, reverse proxy)         │
└──────┬──────────────┬───────────────┬───────────┘
       │              │               │
       ▼              ▼               ▼
  unsubpanel.      supp.         unsubscribe.
  remobtracks.com  remobtracks.  remobtracks.com
                   com
       │              │               │
       │  Admin UI    │  Feed API     │  Unsubscribe
       │  Auth/Setup  │  CSV Export   │  Status Check
       └──────┬───────┴──────┬────────┘
              │              │
              ▼              ▼
         ┌──────────────────────┐
         │   FastAPI (Python)   │
         │   No database        │
         │   Encrypted JSON     │
         └──────────┬───────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │  data/suppressions   │
         │  .enc (Fernet AES)   │
         └──────────────────────┘
```

### Subdomains

| Subdomain                  | Purpose               | Allowed Paths                       |
|----------------------------|-----------------------|-------------------------------------|
| `unsubpanel.remobtracks.com` | Admin panel         | `/`, `/admin`, `/auth`, `/health`  |
| `supp.remobtracks.com`       | Suppression feeds  | `/feed`, `/health`                 |
| `unsubscribe.remobtracks.com`| Unsubscribe flow   | `/u`, `/check`, `/status`, `/health`|

---

## Prerequisites

- An **EC2 instance** (Ubuntu 22.04/24.04/26.04) — `t3a.nano` or `t3a.micro` is sufficient
- **Ports 80 and 443** open in your EC2 security group
- **DNS A records** pointing your 3 subdomains to the EC2 public IP
- **SSH key** for the EC2 instance

---

## Step-by-Step Deployment Guide

### Step 1: Launch an EC2 Instance

1. Go to **AWS Console → EC2 → Launch Instance**
2. Choose **Ubuntu 22.04 LTS** (or 24.04 / 26.04)
3. Instance type: **t3a.micro** (free tier) or **t3a.small**
4. Key pair: create or select your existing key (e.g. `ubuntiVirgin.pem`)
5. Security Group — add these inbound rules:

| Type | Port | Source     |
|------|------|------------|
| SSH  | 22   | Your IP    |
| HTTP | 80   | 0.0.0.0/0 |
| HTTPS| 443  | 0.0.0.0/0 |

6. Storage: **8 GB** gp3 is enough
7. Launch and note the **Public IPv4** (e.g. `35.153.176.232`)

### Step 2: Set Up DNS

Create 3 **A records** at your domain registrar, all pointing to the EC2 public IP:

| Record                             | Type | Value         |
|------------------------------------|------|---------------|
| `unsubpanel.remobtracks.com`       | A    | `35.153.176.232` |
| `supp.remobtracks.com`             | A    | `35.153.176.232` |
| `unsubscribe.remobtracks.com`      | A    | `35.153.176.232` |

Wait for DNS propagation (usually 1–5 minutes). Verify with:

```bash
dig +short unsubpanel.remobtracks.com
# Should return: 35.153.176.232
```

### Step 3: Clone the Repository

SSH into your EC2 instance:

```bash
ssh -i ubuntiVirgin.pem ubuntu@ec2-35-153-176-232.compute-1.amazonaws.com
```

Clone the app:

```bash
sudo git clone https://github.com/essalmiyouness11-blip/optout-manager.git /opt/suppression-manager
sudo chown -R ubuntu:ubuntu /opt/suppression-manager
```

### Step 4: Run the Automated Deploy Script

The setup script handles **everything** automatically — system dependencies, Python venv, nginx, systemd, and firewall:

```bash
cd /opt/suppression-manager
sudo bash deploy/setup.sh
```

This script will:

1. **Install system deps** — python3, nginx, certbot, git, rustc (for pydantic-core on Python 3.14+)
2. **Create Python venv** and install all pip dependencies
3. **Generate `.env`** with random `SECRET_KEY` and `ADMIN_API_KEY` (only if `.env` doesn't exist)
4. **Create systemd service** (`suppression-manager.service`) running uvicorn with 2 workers
5. **Configure nginx** as reverse proxy for all 3 subdomains
6. **Open firewall** ports 80, 443, SSH
7. **Verify** the app is responding

When done, you'll see:

```
══════════════════════════════════════════════════════
  Deployment complete!
══════════════════════════════════════════════════════

  App running at:  http://127.0.0.1:8000
  EC2 Public IP:   35.153.176.232

  Next steps:
  3. Once DNS propagates, run certbot for SSL:
     certbot --nginx -d unsubpanel.remobtracks.com -d supp.remobtracks.com -d unsubscribe.remobtracks.com

  4. Complete initial admin setup at:
     https://unsubpanel.remobtracks.com/auth/setup
```

### Step 5: Enable HTTPS with Certbot

Once DNS A records are live and resolving to your EC2 IP, run certbot to get free SSL certificates:

```bash
sudo certbot --nginx \
  -d unsubpanel.remobtracks.com \
  -d supp.remobtracks.com \
  -d unsubscribe.remobtracks.com \
  --non-interactive \
  --agree-tos \
  --email your@email.com \
  --redirect
```

Certbot will:
- Obtain SSL certificates from Let's Encrypt
- Auto-configure nginx with HTTPS + HTTP→HTTPS redirects
- Set up automatic certificate renewal

### Step 6: Create Your Admin Account

Open **https://unsubpanel.remobtracks.com/auth/setup** in your browser.

Create your admin username and password. You'll be redirected to the login page after setup.

**Done!** Your app is live and ready.

---

## Configuration Reference

### Environment Variables

The `.env` file at `/opt/suppression-manager/.env`:

| Variable                | Required | Description                                                                 |
|-------------------------|----------|-----------------------------------------------------------------------------|
| `SECRET_KEY`            | Yes      | 64-char hex string. Encrypts all data. **Lose this = lose all data.**      |
| `ADMIN_API_KEY`         | No       | Legacy API key for admin operations.                                       |
| `BASE_URL`              | Yes      | Admin panel URL, e.g. `https://unsubpanel.remobtracks.com`                 |
| `UNSUBSCRIBE_BASE_URL`  | Yes      | Unsubscribe page URL, e.g. `https://unsubscribe.remobtracks.com`           |
| `DOWNLOAD_BASE_URL`     | Yes      | Feed download URL, e.g. `https://supp.remobtracks.com`                     |
| `SUPPRESSION_FILE`      | No       | Path to encrypted data file. Default: `data/suppressions.enc`              |
| `SECURE_COOKIE`         | No       | Override cookie security. Auto-detected from `BASE_URL` (https = true).    |

---

## Backup & Restore

### What to Back Up

All data lives in two files:

| File                        | Purpose                          |
|-----------------------------|----------------------------------|
| `/opt/suppression-manager/.env`               | Secret keys + config     |
| `/opt/suppression-manager/data/suppressions.enc` | All encrypted data      |

### Manual Backup

```bash
# From your local machine:
scp -i ubuntiVirgin.pem ubuntu@EC2_IP:/opt/suppression-manager/.env ./
scp -i ubuntiVirgin.pem ubuntu@EC2_IP:/opt/suppression-manager/data/suppressions.enc ./
```

> **IMPORTANT**: The `SECRET_KEY` in `.env` is required to decrypt `suppressions.enc`. Back up both files together and keep them safe.

### Automated Restore

The project includes `deploy/restore.sh` for automated data restoration:

#### Restore to the same EC2

```bash
# SSH into the EC2, then:
sudo bash deploy/restore.sh \
  --local \
  --env /path/to/backed-up/.env \
  --data /path/to/backed-up/suppressions.enc
```

#### Restore to a new EC2 (from your machine)

```bash
# Upload backup + restart service
bash deploy/restore.sh \
  --remote ubuntu@NEW_EC2_IP \
  --key /path/to/your-key.pem \
  --env backups/.env \
  --data backups/suppressions.enc
```

#### Full deploy + restore on a fresh EC2

This installs everything from scratch AND restores your data:

```bash
# First, clone the repo on the new EC2:
ssh -i key.pem ubuntu@NEW_EC2_IP
sudo git clone https://github.com/essalmiyouness11-blip/optout-manager.git /opt/suppression-manager
sudo chown -R ubuntu:ubuntu /opt/suppression-manager
exit

# Then restore from your machine:
bash deploy/restore.sh \
  --remote ubuntu@NEW_EC2_IP \
  --key /path/to/your-key.pem \
  --env backups/.env \
  --data backups/suppressions.enc \
  --deploy
```

### Using the CLI for Backup/Restore

You can also use the CLI for a clean JSON export/import:

```bash
# Export decrypted JSON (run on the EC2)
cd /opt/suppression-manager
source venv/bin/activate
python cli/manage.py export > backup.json

# Import from JSON
python cli/manage.py import-cmd backup.json
```

---

## Updating the App

```bash
ssh -i key.pem ubuntu@EC2_IP
cd /opt/suppression-manager
sudo bash deploy/setup.sh
```

The deploy script is idempotent — it pulls the latest code, updates dependencies, and restarts the service. Your `.env` and `data/suppressions.enc` are never overwritten.

---

## Usage Guide

### Admin Panel

Access at **https://unsubpanel.remobtracks.com**

| Tab             | Purpose                                                          |
|-----------------|------------------------------------------------------------------|
| **Generate**    | Create unsubscribe links (global, network, or offer level)       |
| **Networks**    | Manage affiliate networks                                        |
| **Offers**      | Manage offers (linked to networks)                               |
| **Unsubscribers** | Browse unsubscribers per offer with counts, export, TLD stats  |
| **Dashboard**   | Summary stats: global/network/offer counts, feed links           |
| **Users**       | Manage admin users (create, delete)                              |

### Generating Unsubscribe Links

Go to **Generate** tab and select a level:

- **Global** — opts user out of everything
- **Network** — opts user out of all offers in a network
- **Offer** — opts user out of a specific offer

You get two link types:

- **Standard** (`?t=TOKEN`) — shows a themed email form (50 random designs)
- **Auto-unsubscribe** (`?t=TOKEN&e=EMAIL`) — immediately unsubscribes, no form shown

### Suppression Feeds

Each offer/network has a **permanent feed URL** (shown on the details page and dashboard):

```
# JSON feed
GET https://supp.remobtracks.com/feed/unsubscribers/{target}?token={token}&level=offer

# CSV (plain emails)
GET https://supp.remobtracks.com/feed/unsubscribers/{target}/csv?token={token}&level=offer&format=plain

# CSV (MD5 hashes)
GET https://supp.remobtracks.com/feed/unsubscribers/{target}/csv?token={token}&level=offer&format=md5
```

Feed tokens are **persistent** — the same URL works forever unless explicitly regenerated.

**Query parameters:**

| Param   | Description                                     |
|---------|-------------------------------------------------|
| `since` | Unix timestamp — only return entries after this  |
| `token` | Authentication token (included in URL)           |

### Checking Suppression Status

```bash
curl "https://unsubscribe.remobtracks.com/check" \
  -H "Content-Type: application/json" \
  -d '{"h":"sha256_of_email","network":"network_id","offer":"offer_id"}'
```

### What Users See

When a user clicks an unsubscribe link:

1. They land on `https://unsubscribe.remobtracks.com/u?t=TOKEN`
2. A themed form appears (randomly selected from 50 designs)
3. No offer or network information is revealed
4. After submitting → success page with confirmation
5. Email is stored as SHA256 + MD5 hashes in the encrypted file

---

## API Reference

### Public (unsubscribe subdomain)

| Method | Path                  | Description                                |
|--------|-----------------------|--------------------------------------------|
| GET    | `/u`                  | Unsubscribe form (requires `?t=`)         |
| POST   | `/u`                  | Submit email for unsubscription            |
| GET    | `/u/success`          | Success page after unsubscribing           |
| GET    | `/status`             | Check suppression status (`?h=`)           |

### Feed (supp subdomain)

| Method | Path                                       | Description                       |
|--------|--------------------------------------------|-----------------------------------|
| GET    | `/feed/unsubscribers/{target}`             | JSON feed (requires `?token=`)   |
| GET    | `/feed/unsubscribers/{target}/csv`         | CSV feed (requires `?token=`)    |

### Admin (unsubpanel subdomain, requires auth)

| Method | Path                                               | Description                    |
|--------|----------------------------------------------------|--------------------------------|
| GET    | `/admin/generate`                                  | Link generator page            |
| POST   | `/admin/generate`                                  | Generate unsubscribe links     |
| GET    | `/admin/networks`                                  | Networks list                  |
| GET    | `/admin/offers`                                    | Offers list                    |
| GET    | `/admin/offers/{id}`                               | Offer details                  |
| GET    | `/admin/offers/{id}/stats`                         | Offer stats (TLD breakdown)    |
| GET    | `/admin/offers/{id}/unsubscribers/csv`             | Download offer unsubscribers   |
| GET    | `/admin/offers/{id}/export-tld/{domain}`           | Download per-TLD unsubscribers |
| GET    | `/admin/unsubscribers`                             | Unsubscribers overview         |
| GET    | `/admin/unsubscribers/data`                        | Unsubscribers JSON data        |
| GET    | `/admin/unsubscribers/data/offer/{id}`             | Per-offer unsubscriber data    |
| GET    | `/admin/unsubscribers/export`                      | Download filtered CSV          |
| GET    | `/admin/dashboard`                                 | Dashboard page                 |
| GET    | `/admin/users`                                     | Users management               |
| POST   | `/admin/users`                                     | Create user                    |
| DELETE | `/admin/users/{email}`                             | Delete user                    |
| POST   | `/admin/feed/generate`                             | Generate / reuse feed token    |
| POST   | `/admin/feed/regenerate`                           | Rotate feed token              |

### Auth

| Method | Path           | Description                  |
|--------|----------------|------------------------------|
| GET    | `/auth/setup`  | Initial admin setup page     |
| POST   | `/auth/setup`  | Create first admin account   |
| GET    | `/auth/login`  | Login page                   |
| POST   | `/auth/login`  | Login                        |
| POST   | `/auth/logout` | Logout                       |

### Health

| Method | Path      | Description                   |
|--------|-----------|-------------------------------|
| GET    | `/health` | Returns `{"status": "ok"}`    |

---

## CLI Tools

```bash
cd /opt/suppression-manager
source venv/bin/activate

# Generate SECRET_KEY and ADMIN_API_KEY
python cli/manage.py keygen

# List / create / delete users
python cli/manage.py user list
python cli/manage.py user create admin@example.com mypassword --role admin
python cli/manage.py user delete admin@example.com

# Export all suppressions (decrypted JSON)
python cli/manage.py export > backup.json

# Import suppressions from JSON
python cli/manage.py import-cmd backup.json

# Show statistics
python cli/manage.py stats
```

---

## Security

- **Passwords**: bcrypt hashed before storage
- **Session tokens**: JWT (HS256), 24-hour expiry, HTTP-only cookies
- **Unsubscribe tokens**: JWT (HS256), permanent, contain level + target + optional email hash
- **Feed tokens**: random hex, stored encrypted, permanent (reused unless regenerated)
- **Data at rest**: AES-128-CBC + HMAC-SHA256 via Fernet
- **Rate limiting**: 20 requests/60s on `/u` and `/check`
- **Security headers**: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`
- **Host routing**: each subdomain only serves its allowed paths

---

## Useful Commands

```bash
# Service management
sudo systemctl status suppression-manager
sudo systemctl restart suppression-manager
sudo systemctl stop suppression-manager
sudo journalctl -u suppression-manager -f          # live logs
sudo journalctl -u suppression-manager -n 100       # last 100 lines

# Nginx
sudo nginx -t                                       # test config
sudo systemctl reload nginx                         # reload after changes

# SSL / Certbot
sudo certbot certificates                           # view certificates
sudo certbot renew --dry-run                        # test renewal
sudo certbot renew                                  # force renewal

# Full redeploy (idempotent — safe to re-run)
sudo bash /opt/suppression-manager/deploy/setup.sh
```

---

## Troubleshooting

### App not responding on domain

```bash
# Check service is running
sudo systemctl status suppression-manager

# Test locally
curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8000/

# Test via nginx
curl -s -o /dev/null -w '%{http_code}' -H 'Host: unsubpanel.remobtracks.com' http://127.0.0.1/

# Check nginx config
sudo nginx -t
```

### SSL / certificate errors

- Ensure DNS A records resolve to your EC2 IP: `dig +short unsubpanel.remobtracks.com`
- Ensure ports 80 and 443 are open in the EC2 security group
- Re-run certbot: `sudo certbot --nginx -d unsubpanel.remobtracks.com -d supp.remobtracks.com -d unsubscribe.remobtracks.com`

### "Invalid or expired link" on unsubscribe

- The token was generated with a different `SECRET_KEY`
- The URL was mangled (check for `&` being encoded as `&amp;` in HTML)

### Data file corruption

If the encrypted file gets corrupted:
1. Restore from backup: `python cli/manage.py import-cmd backup.json`
2. If no backup exists, delete `data/suppressions.enc` and start fresh (all data lost)

### 403 "Not available on this subdomain"

You're accessing a path from the wrong subdomain. Check the routing rules:

| Subdomain    | Allowed paths                              |
|--------------|---------------------------------------------|
| `unsubpanel` | `/`, `/admin`, `/auth`, `/health`          |
| `supp`       | `/feed`, `/health`                         |
| `unsubscribe`| `/u`, `/check`, `/status`, `/health`       |

---

## File Structure

```
suppression-manager/
├── app/
│   ├── main.py              # FastAPI app assembly
│   ├── auth.py              # bcrypt + JWT session auth
│   ├── crypto.py            # JWT tokens, SHA256/MD5 hashing, Fernet
│   ├── models.py            # Pydantic models
│   ├── store.py             # Thread-safe encrypted JSON CRUD
│   ├── templates.py         # 50 random unsubscribe page themes
│   ├── middleware.py         # Rate limiting + host routing
│   └── routes/
│       ├── admin.py         # Admin panel pages & API
│       ├── auth.py          # Setup / login / logout
│       ├── feed.py          # Suppression feed API
│       ├── status.py        # Suppression status check
│       └── unsubscribe.py   # Unsubscribe form + submission
├── cli/
│   └── manage.py            # CLI tools (keygen, users, export/import)
├── deploy/
│   ├── setup.sh             # Automated EC2 deployment script
│   ├── restore.sh           # Automated backup restore script
│   ├── suppression-manager.service  # Systemd unit file
│   └── nginx.conf           # Nginx reverse proxy config
├── data/                    # Encrypted data (gitignored)
├── backups/                 # Local backups (gitignored)
├── .env.example             # Environment template
├── requirements.txt         # Python dependencies
├── Caddyfile                # Caddy config (alternative)
├── Dockerfile               # Docker build (alternative)
└── README.md                # This file
```
