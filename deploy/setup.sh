#!/bin/bash
set -e

APP_DIR="/opt/suppression-manager"
REPO="https://github.com/essalmiyouness11-blip/optout-manager.git"

echo "=== Suppression Manager — EC2 Setup (no Docker) ==="

# Install system deps
apt update && apt install -y python3 python3-venv python3-pip nginx certbot python3-certbot-nginx git

# Clone or update app
if [ -d "$APP_DIR" ]; then
    cd "$APP_DIR" && git pull origin main
else
    git clone "$REPO" "$APP_DIR"
    cd "$APP_DIR"
fi

# Python venv
python3 -m venv venv
./venv/bin/pip install -r requirements.txt

# Create data dir
mkdir -p data

# Create .env if missing
if [ ! -f .env ]; then
    SECRET=$(python3 -c "import secrets; print(secrets.token_hex(32))")
    API_KEY=$(python3 -c "import secrets; print(secrets.token_hex(24))")
    cat > .env <<EOF
SECRET_KEY=$SECRET
ADMIN_API_KEY=$API_KEY
BASE_URL=https://unsubmepanel.remobtracks.com
UNSUBSCRIBE_BASE_URL=https://optout.remobtracks.com
DOWNLOAD_BASE_URL=https://dlx.remobtracks.com
SUPPRESSION_FILE=data/suppressions.enc
EOF
    echo ".env created — edit BASE_URL/UNSUBSCRIBE_BASE_URL/DOWNLOAD_BASE_URL before proceeding"
    echo "  Then re-run this script to continue with nginx + SSL"
    exit 0
fi

# Systemd service
cp deploy/suppression-manager.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable suppression-manager
systemctl restart suppression-manager

# Nginx
cp deploy/nginx.conf /etc/nginx/sites-available/suppression.conf
ln -sf /etc/nginx/sites-available/suppression.conf /etc/nginx/sites-enabled/suppression.conf
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl restart nginx

# SSL with certbot (dry run first — actual certs need DNS to point here)
echo ""
echo "=== App running on http://127.0.0.1:8000 ==="
echo "=== Nginx configured for 3 subdomains ==="
echo ""
echo "Once DNS A records are set, run:"
echo "  certbot --nginx -d unsubmepanel.remobtracks.com -d dlx.remobtracks.com -d optout.remobtracks.com"
echo ""
echo "Check status: systemctl status suppression-manager"
echo "View logs:    journalctl -u suppression-manager -f"
