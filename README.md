# Suppression Manager

A stateless, self-hosted opt-out and suppression manager for affiliate marketers. Collect unsubscribe requests, manage suppression lists per offer/network/global, and serve permanent suppression feeds to ESPs — all without a database.

## Architecture

```
┌─────────────────────────────────────────────────┐
│                   Caddy / Nginx                  │
│  (TLS termination, reverse proxy, auto-HTTPS)   │
└──────┬──────────────┬───────────────┬───────────┘
       │              │               │
       ▼              ▼               ▼
  unsubmepanel.    dlx.          optout.
  remobtracks.com  remobtracks.  remobtracks.
                   com           com
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

| Subdomain              | Purpose           | Paths allowed             |
|------------------------|-------------------|---------------------------|
| `unsubmepanel.*`       | Admin panel       | `/`, `/admin`, `/auth`    |
| `dlx.*`                | Suppression feeds | `/feed`, `/health`        |
| `optout.*`             | Unsubscribe flow  | `/u`, `/check`, `/status` |

## Prerequisites

- Python 3.10+ or Docker
- A domain with three subdomain DNS A records pointing to your server IP
- Ports 80 and 443 open in your firewall / security group

## Configuration

Copy `.env.example` to `.env` and fill in:

```bash
cp .env.example .env
```

| Variable                | Required | Description                                     |
|-------------------------|----------|-------------------------------------------------|
| `SECRET_KEY`            | Yes      | 64-character hex string. Used for Fernet AES encryption (persisted data), JWT session tokens, and unsubscribe tokens. **Keep this safe — if lost, all data is unrecoverable.** |
| `ADMIN_API_KEY`         | No       | Legacy API key for admin operations (optional). |
| `BASE_URL`              | Yes      | Base URL of the admin panel, e.g. `https://unsubmepanel.remobtracks.com`. |
| `UNSUBSCRIBE_BASE_URL`  | Yes      | Public unsubscribe page URL, e.g. `https://optout.remobtracks.com`. Used in generated unsubscribe links. |
| `DOWNLOAD_BASE_URL`     | Yes      | Public feed download URL, e.g. `https://dlx.remobtracks.com`. Used in generated suppression feed links. |
| `SUPPRESSION_FILE`      | No       | Path to the encrypted data file. Default: `data/suppressions.enc`. Inside Docker, this is `/data/suppressions.enc`. |

### Generate keys

```bash
python cli/manage.py keygen
```

This outputs a secure `SECRET_KEY` and `ADMIN_API_KEY`. Copy the `SECRET_KEY` into your `.env`.

---

## Quick Start (Local Development)

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create .env (see Configuration above)
cp .env.example .env
# Edit .env with your secret key and URLs

# 3. Run the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 4. Open http://localhost:8000 — you'll be redirected to /auth/setup
#    to create the initial admin user.
```

---

## EC2 Deployment

### Option A: Caddy (recommended — auto-HTTPS, zero config)

#### 1. Launch an EC2 instance

- **AMI**: Ubuntu 22.04 LTS or Amazon Linux 2023
- **Instance type**: `t3a.nano` or `t3a.micro` (free tier eligible) — sufficient for thousands of suppressions
- **Storage**: 8 GB gp3 is plenty
- **Security Group**: open ports **22** (SSH), **80** (HTTP), **443** (HTTPS)

#### 2. Install Docker and Compose

```bash
# Ubuntu
sudo apt update && sudo apt install -y docker.io docker-compose-v2
sudo systemctl enable --now docker
sudo usermod -aG docker ubuntu
# Log out and back in for group changes to take effect
```

#### 3. Clone the repository

```bash
git clone https://github.com/YOUR_USER/optout-manager.git
cd optout-manager
```

#### 4. Configure environment

```bash
cp .env.example .env
nano .env
```

Fill in your values:

```ini
SECRET_KEY=<generated 64-hex string>
BASE_URL=https://unsubmepanel.YOURDOMAIN.com
UNSUBSCRIBE_BASE_URL=https://optout.YOURDOMAIN.com
DOWNLOAD_BASE_URL=https://dlx.YOURDOMAIN.com
```

> **Important**: `SUPPRESSION_FILE` is already set to `/data/suppressions.enc` in the Dockerfile. Do not change it unless you know what you're doing.

#### 5. Update Caddyfile

Edit `Caddyfile` to use your domain:

```
unsubmepanel.YOURDOMAIN.com {
    reverse_proxy app:8000
}

dlx.YOURDOMAIN.com {
    reverse_proxy app:8000
}

optout.YOURDOMAIN.com {
    reverse_proxy app:8000
}
```

#### 6. Set up DNS

Create three **A records** in your DNS provider, all pointing to your EC2 instance's public IP:

| Record                  | Type | Value      |
|-------------------------|------|------------|
| `unsubmepanel.YOURDOMAIN.com` | A    | `<EC2_IP>` |
| `dlx.YOURDOMAIN.com`          | A    | `<EC2_IP>` |
| `optout.YOURDOMAIN.com`       | A    | `<EC2_IP>` |

DNS propagation can take a few minutes to hours.

#### 7. Launch

```bash
docker compose -f docker-compose.caddy.yml up -d --build
```

Caddy automatically provisions and renews TLS certificates for all three subdomains via Let's Encrypt.

#### 8. First-time setup

Open `https://unsubmepanel.YOURDOMAIN.com` in your browser. You'll be redirected to `/auth/setup` to create the initial admin account.

---

### Option B: Nginx + Certbot (alternative)

This project includes `docker-compose.yml` and `nginx.conf` for a Nginx-based setup with manual Let's Encrypt certificates.

**Changes required before deploying:**

1. Set your domain names in `nginx.conf` (replace `server_name _;` with your actual subdomains, or add separate `server` blocks)
2. Place your SSL certificate and key at `ssl/fullchain.pem` and `ssl/privkey.pem` (or modify paths)
3. Launch: `docker compose up -d --build`

For a fresh certificate:
```bash
docker compose run --rm certbot certonly --webroot -w /var/www/certbot \
  -d unsubmepanel.YOURDOMAIN.com \
  -d dlx.YOURDOMAIN.com \
  -d optout.YOURDOMAIN.com
```

Then copy the certificates to `ssl/` and launch the stack.

---

## Updating

```bash
git pull
docker compose -f docker-compose.caddy.yml up -d --build
```

The encrypted data file persists in the `suppression_data` Docker volume — it survives container rebuilds.

---

## Usage Guide

### 1. Admin Panel

Access the admin panel at `https://unsubmepanel.YOURDOMAIN.com`.

**Tabs:**

| Tab            | Purpose                                                   |
|----------------|-----------------------------------------------------------|
| **Generate**   | Create unsubscribe links for global, network, or offer level |
| **Networks**   | CRUD for affiliate networks                               |
| **Offers**     | CRUD for offers (belong to a network)                     |
| **Unsubscribers** | Browse unsubscribers per offer with counts, export, inline expansion |
| **Dashboard**  | Summary stats: global/network/offer unsubscriber counts, suppression feed links |
| **Users**      | Manage admin users (create, delete)                       |

### 2. Generating Unsubscribe Links

Go to **Generate** tab and select a level:

- **Global** — the unsubscribe link opts the user out of everything
- **Network** — opts the user out of a specific affiliate network (all its offers)
- **Offer** — opts the user out of a specific offer only

You'll get two types of links:

- **Standard link** (`?t=TOKEN`) — opens an unsubscribe form where the user enters their email
- **Auto-unsubscribe link** (`?t=TOKEN&e=EMAIL`) — immediately unsubscribes the user without showing a form

### 3. Suppression Feeds

Each offer and network has a **permanent suppression feed URL** (shown on the offer/network details page, and in the Dashboard). These URLs:

- **Never change** — the same token is reused unless explicitly regenerated
- **Auto-update** — always return the latest unsubscriber list
- **Three formats** — JSON, Plain CSV (emails), MD5 CSV (MD5 hashes)

**Supported query parameters on feed URLs:**

| Param   | Values              | Description                                     |
|---------|---------------------|-------------------------------------------------|
| `since` | Unix timestamp      | Only return unsubscribers added after this time  |
| `token` | Feed token          | Authentication token (included in URL)           |

#### Feed endpoint formats

```
JSON:   GET /feed/unsubscribers/{target}?token={token}&level=offer
CSV:    GET /feed/unsubscribers/{target}/csv?token={token}&level=offer&format=plain
MD5:    GET /feed/unsubscribers/{target}/csv?token={token}&level=offer&format=md5
```

These endpoints are served on the `dlx.` subdomain.

### 4. What the User Sees

When a user clicks an unsubscribe link:

1. They land on `https://optout.YOURDOMAIN.com/u?t=TOKEN` (or with `&e=EMAIL` for auto-unsubscribe)
2. No offer/network information is shown — just a clean email input form
3. After submitting, they're redirected to a success page with a confirmation message
4. The email is stored as lowercase SHA256 + MD5 hash in the encrypted data file

### 5. Checking Suppression Status

```http
GET /status?h=<sha256_of_email>
```

Returns whether an email is suppressed at global, network, or offer level. Useful for ESP integration.

**Response:**
```json
{
  "email_hash": "sha256hash",
  "suppressed": true,
  "global_suppressed": false,
  "network_suppressions": [],
  "offer_suppressions": ["offer_123"]
}
```

---

## CLI Tools

The project includes a CLI for managing data and users:

```bash
# Generate SECRET_KEY and ADMIN_API_KEY
python cli/manage.py keygen

# List all users
python cli/manage.py user list

# Create a user
python cli/manage.py user create admin@example.com mypassword --role admin

# Delete a user
python cli/manage.py user delete admin@example.com

# Reset an API key
python cli/manage.py user reset-api-key admin@example.com

# Export all suppressions as JSON (decrypted)
python cli/manage.py export

# Import suppressions from JSON
python cli/manage.py import-cmd backup.json

# Show statistics
python cli/manage.py stats
```

**Note**: CLI commands read `SUPPRESSION_FILE` and `SECRET_KEY` from the environment. You can override the file path with `--file`.

---

## Data Storage

All data is stored in a single encrypted JSON file (default: `data/suppressions.enc`). The file is:

- **Encrypted** with Fernet (AES-128-CBC + HMAC-SHA256) using your `SECRET_KEY`
- **Thread-safe** — all reads/writes are protected by a lock
- **Cached in memory** — the file is re-read only when modified

### Backup

To safely back up your data:

```bash
# Export decrypted JSON
python cli/manage.py export > backup.json

# To restore
python cli/manage.py import-cmd backup.json
```

---

## API Endpoints

### Public (optout subdomain)

| Method | Path                  | Description                          |
|--------|-----------------------|--------------------------------------|
| GET    | `/u`                  | Show unsubscribe form (requires `?t=`) |
| POST   | `/u`                  | Submit email via unsubscribe form    |
| GET    | `/u/success`          | Success page after unsubscribing     |
| GET    | `/status`             | Check suppression status (`?h=`)     |

### Feed (dlx subdomain)

| Method | Path                                       | Description                     |
|--------|--------------------------------------------|---------------------------------|
| GET    | `/feed/unsubscribers/{target}`             | JSON feed (requires `?token=`)  |
| GET    | `/feed/unsubscribers/{target}/csv`         | CSV feed (requires `?token=`)   |

### Admin (unsubmepanel subdomain, requires auth)

| Method | Path                                             | Description                  |
|--------|--------------------------------------------------|------------------------------|
| GET    | `/admin/generate`                                | Link generator page          |
| POST   | `/admin/generate`                                | Generate unsubscribe links   |
| GET    | `/admin/networks`                                | Networks list page           |
| GET    | `/admin/offers`                                  | Offers list page             |
| GET    | `/admin/offers/{id}`                             | Offer details page           |
| GET    | `/admin/offers/{id}/stats`                       | Offer stats (TLD breakdown)  |
| GET    | `/admin/offers/{id}/unsubscribers/csv`           | Download offer unsubscribers |
| GET    | `/admin/offers/{id}/export-tld/{domain}`         | Download per-TLD unsubscribers|
| GET    | `/admin/unsubscribers`                           | Unsubscribers overview page  |
| GET    | `/admin/unsubscribers/data`                      | Unsubscribers JSON data      |
| GET    | `/admin/unsubscribers/data/offer/{id}`           | Per-offer unsubscriber data  |
| GET    | `/admin/unsubscribers/export`                    | Download filtered CSV        |
| GET    | `/admin/dashboard`                               | Dashboard page               |
| GET    | `/admin/users`                                   | Users management page        |
| POST   | `/admin/users`                                   | Create user                  |
| DELETE | `/admin/users/{email}`                           | Delete user                  |
| POST   | `/admin/feed/generate`                           | Generate (or reuse) feed token|
| POST   | `/admin/feed/regenerate`                         | Rotate feed token            |

### Auth

| Method | Path          | Description                |
|--------|---------------|----------------------------|
| GET    | `/auth/setup` | Initial admin setup page   |
| POST   | `/auth/setup` | Create first admin account |
| GET    | `/auth/login` | Login page                 |
| POST   | `/auth/login` | Login                      |
| POST   | `/auth/logout`| Logout                     |

### Health

| Method | Path      | Description          |
|--------|-----------|----------------------|
| GET    | `/health` | Returns `{"status":"ok"}` |

---

## Security

- **Passwords**: hashed with bcrypt before storage
- **Session tokens**: JWT (HS256), 24-hour expiry, stored in HTTP-only cookies
- **Unsubscribe tokens**: JWT (HS256), no expiry (permanent links), contain level + target + optional email hash
- **Feed tokens**: random hex string, stored in encrypted file, permanent (reused) unless explicitly regenerated
- **Data at rest**: AES-128-CBC + HMAC-SHA256 via Fernet
- **Rate limiting**: 20 requests per 60 seconds on `/u` and `/check` endpoints
- **Security headers**: `X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`
- **Host routing**: each subdomain only serves its allowed paths; unknown paths return 403

---

## Troubleshooting

### "Unsubscriber Statistics" showing "Loading..."

The offer details page fetches `/admin/offers/{id}/stats` via JS. Make sure the route is registered before the generic `/admin/offers/{id}` route. If you see "Failed to load stats", check browser dev tools (F12 → Network tab) for the exact error.

### Caddy 404 / Host routing blocks requests

Caddy serves all three subdomains and proxies everything to the app. The **app's middleware** enforces host routing. If you get a 403 `"Not available on this subdomain"`, you're accessing a path from the wrong subdomain.

Check the middleware rules in `app/middleware.py`:

- `unsubmepanel.*` → `/`, `/admin`, `/auth`, `/health`
- `dlx.*` → `/feed`, `/health`
- `optout.*` → `/u`, `/check`, `/status`, `/health`

### Data file corruption

The encrypted data file is read on every request. If it gets corrupted:
1. Restore from backup: `python cli/manage.py import-cmd backup.json`
2. If no backup exists, delete the file and start fresh (you'll lose all data)

### "Invalid or expired link" on unsubscribe

The unsubscribe token is JWT-based and may be invalid if:
- The token was generated with a different `SECRET_KEY`
- The URL was mangled (check for `&` being encoded as `&amp;` in HTML)
- The token was truncated by email client line-wrapping

### Port 80/443 not accessible on EC2

- Check the EC2 security group: must allow inbound TCP on 80 and 443
- Check the instance's firewall: `sudo ufw status` (if using UFW)
- Caddy binds directly to 80/443 on the host (not inside Docker networking)
