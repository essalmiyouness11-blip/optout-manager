#!/bin/bash
set -euo pipefail

APP_DIR="/opt/suppression-manager"
REPO="https://github.com/essalmiyouness11-blip/optout-manager.git"
SERVICE_NAME="suppression-manager"
NGINX_SITE="suppression-manager"
DOMAIN_PANEL="unsubpanel.remobtracks.com"
DOMAIN_FEED="supp.remobtracks.com"
DOMAIN_UNSUB="unsubscribe.remobtracks.com"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log()  { echo -e "${GREEN}[+]${NC} $1"; }
warn() { echo -e "${YELLOW}[!]${NC} $1"; }
err()  { echo -e "${RED}[x]${NC} $1"; exit 1; }

echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════╗"
echo "║      Suppression Manager — Automated Deploy      ║"
echo "╚══════════════════════════════════════════════════╝"
echo -e "${NC}"

# ── Phase 1: System dependencies ──
log "Phase 1: Installing system dependencies..."

apt-get update -qq

# Core packages
apt-get install -y -qq python3 python3-venv python3-pip nginx certbot python3-certbot-nginx git curl ufw > /dev/null 2>&1

# Install Rust if not present (needed for pydantic-core on Python 3.14+)
PYTHON_VERSION=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
PYTHON_MINOR=$(python3 -c 'import sys; print(sys.version_info.minor)')
if [ "$PYTHON_MINOR" -ge 14 ] && ! command -v rustc &> /dev/null; then
    log "Python ${PYTHON_VERSION} detected — installing Rust for pydantic-core..."
    apt-get install -y -qq rustc cargo gcc > /dev/null 2>&1
fi

# ── Phase 2: App code ──
log "Phase 2: Setting up application code..."

if [ -d "$APP_DIR/.git" ]; then
    cd "$APP_DIR"
    git pull origin main --quiet
    log "Pulled latest code"
else
    rm -rf "$APP_DIR"
    git clone "$REPO" "$APP_DIR" --quiet
    cd "$APP_DIR"
    log "Cloned repository"
fi

# ── Phase 3: Python venv + deps ──
log "Phase 3: Setting up Python environment..."

if [ ! -d "venv" ] || [ ! -f "venv/bin/python3" ]; then
    python3 -m venv venv
    log "Created virtual environment"
fi

./venv/bin/pip install --upgrade pip --quiet 2>/dev/null
./venv/bin/pip install -r requirements.txt --quiet 2>/dev/null
log "Python dependencies installed"

# ── Phase 4: Environment file ──
log "Phase 4: Configuring environment..."

if [ ! -f .env ]; then
    SECRET=$(python3 -c "import secrets; print(secrets.token_hex(32))")
    API_KEY=$(python3 -c "import secrets; print(secrets.token_hex(24))")
    cat > .env <<ENVEOF
SECRET_KEY=$SECRET
ADMIN_API_KEY=$API_KEY
BASE_URL=https://${DOMAIN_PANEL}
UNSUBSCRIBE_BASE_URL=https://${DOMAIN_UNSUB}
DOWNLOAD_BASE_URL=https://${DOMAIN_FEED}
SUPPRESSION_FILE=data/suppressions.enc
ENVEOF
    chmod 600 .env
    log ".env generated with random secrets"
else
    log ".env already exists — skipping (edit manually if domains changed)"
fi

mkdir -p data

# ── Phase 5: Systemd service ──
log "Phase 5: Configuring systemd service..."

# Generate service file dynamically
cat > /etc/systemd/system/${SERVICE_NAME}.service <<SVCEOF
[Unit]
Description=Suppression Manager
After=network.target

[Service]
Type=simple
User=$(whoami)
Group=$(id -gn)
WorkingDirectory=${APP_DIR}
ExecStart=${APP_DIR}/venv/bin/uvicorn app.main:app --host 127.0.0.1 --port 8000 --workers 2
Restart=always
RestartSec=3
Environment="PATH=${APP_DIR}/venv/bin"
EnvironmentFile=${APP_DIR}/.env

[Install]
WantedBy=multi-user.target
SVCEOF

systemctl daemon-reload
systemctl enable ${SERVICE_NAME} --quiet
systemctl restart ${SERVICE_NAME}
sleep 2

if systemctl is-active --quiet ${SERVICE_NAME}; then
    log "Systemd service running"
else
    err "Service failed to start. Check: journalctl -u ${SERVICE_NAME} -n 20"
fi

# ── Phase 6: Nginx ──
log "Phase 6: Configuring nginx..."

# Create nginx config dynamically
cat > /etc/nginx/sites-available/${NGINX_SITE} <<'NGINXEOF'
server {
    listen 80;
    server_name PANEL_DOMAIN;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

server {
    listen 80;
    server_name FEED_DOMAIN;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

server {
    listen 80;
    server_name UNSUB_DOMAIN;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
NGINXEOF

# Replace domain placeholders
sed -i "s|PANEL_DOMAIN|${DOMAIN_PANEL}|g" /etc/nginx/sites-available/${NGINX_SITE}
sed -i "s|FEED_DOMAIN|${DOMAIN_FEED}|g" /etc/nginx/sites-available/${NGINX_SITE}
sed -i "s|UNSUB_DOMAIN|${DOMAIN_UNSUB}|g" /etc/nginx/sites-available/${NGINX_SITE}

ln -sf /etc/nginx/sites-available/${NGINX_SITE} /etc/nginx/sites-enabled/${NGINX_SITE}
rm -f /etc/nginx/sites-enabled/default
mkdir -p /var/www/certbot

if nginx -t 2>&1; then
    systemctl reload nginx
    log "Nginx configured and reloaded"
else
    err "Nginx config test failed"
fi

# ── Phase 7: UFW firewall ──
log "Phase 7: Configuring firewall..."

if command -v ufw &> /dev/null; then
    ufw allow 'Nginx Full' --quiet 2>/dev/null || true
    ufw allow ssh --quiet 2>/dev/null || true
    log "Firewall rules added"
fi

# ── Phase 8: Verify ──
log "Phase 8: Verifying..."

HTTP_CODE=$(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8000/ 2>/dev/null || echo "000")
if [ "$HTTP_CODE" = "307" ] || [ "$HTTP_CODE" = "200" ]; then
    log "App responding locally (HTTP ${HTTP_CODE})"
else
    warn "App returned HTTP ${HTTP_CODE} — check logs: journalctl -u ${SERVICE_NAME}"
fi

HTTP_CODE_NGINX=$(curl -s -o /dev/null -w '%{http_code}' -H "Host: ${DOMAIN_PANEL}" http://127.0.0.1/ 2>/dev/null || echo "000")
if [ "$HTTP_CODE_NGINX" = "307" ] || [ "$HTTP_CODE_NGINX" = "200" ]; then
    log "Nginx proxy working (HTTP ${HTTP_CODE_NGINX})"
else
    warn "Nginx proxy returned HTTP ${HTTP_CODE_NGINX}"
fi

# ── Done ──
EC2_PUBLIC_IP=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4 2>/dev/null || echo "unknown")

echo ""
echo -e "${CYAN}══════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  Deployment complete!${NC}"
echo -e "${CYAN}══════════════════════════════════════════════════════${NC}"
echo ""
echo -e "  App running at:  ${GREEN}http://127.0.0.1:8000${NC}"
echo -e "  EC2 Public IP:   ${YELLOW}${EC2_PUBLIC_IP}${NC}"
echo ""
echo -e "  ${YELLOW}Next steps:${NC}"
echo ""
echo "  1. Open ports 80 and 443 in your EC2 security group"
echo ""
echo "  2. Create DNS A records pointing to ${EC2_PUBLIC_IP}:"
echo "     - ${DOMAIN_PANEL}"
echo "     - ${DOMAIN_FEED}"
echo "     - ${DOMAIN_UNSUB}"
echo ""
echo "  3. Once DNS propagates, run certbot for SSL:"
echo "     ${CYAN}certbot --nginx -d ${DOMAIN_PANEL} -d ${DOMAIN_FEED} -d ${DOMAIN_UNSUB}${NC}"
echo ""
echo "  4. Complete initial admin setup at:"
echo "     https://${DOMAIN_PANEL}/auth/setup"
echo ""
echo -e "  Useful commands:"
echo "    Status:   systemctl status ${SERVICE_NAME}"
echo "    Logs:     journalctl -u ${SERVICE_NAME} -f"
echo "    Restart:  systemctl restart ${SERVICE_NAME}"
echo -e "${CYAN}══════════════════════════════════════════════════════${NC}"
