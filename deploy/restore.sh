#!/bin/bash
set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

log()  { echo -e "${GREEN}[+]${NC} $1"; }
warn() { echo -e "${YELLOW}[!]${NC} $1"; }
err()  { echo -e "${RED}[x]${NC} $1"; exit 1; }

APP_DIR="/opt/suppression-manager"
SERVICE_NAME="suppression-manager"

usage() {
    echo ""
    echo -e "${CYAN}Usage:${NC}"
    echo ""
    echo "  Local restore (run on the EC2 instance):"
    echo "    sudo bash deploy/restore.sh --local --env /path/to/.env --data /path/to/suppressions.enc"
    echo ""
    echo "  Remote restore (run from your machine via SSH):"
    echo "    bash deploy/restore.sh --remote ubuntu@EC2_IP --key /path/to/pem --env backups/.env --data backups/suppressions.enc"
    echo ""
    echo "  Remote restore with full deploy (fresh EC2):"
    echo "    bash deploy/restore.sh --remote ubuntu@EC2_IP --key /path/to/pem --env backups/.env --data backups/suppressions.enc --deploy"
    echo ""
    exit 1
}

# ── Parse args ──
MODE=""
REMOTE_HOST=""
SSH_KEY=""
ENV_FILE=""
DATA_FILE=""
FULL_DEPLOY=false

while [[ $# -gt 0 ]]; do
    case $1 in
        --local)   MODE="local"; shift ;;
        --remote)  MODE="remote"; REMOTE_HOST="$2"; shift 2 ;;
        --key)     SSH_KEY="$2"; shift 2 ;;
        --env)     ENV_FILE="$2"; shift 2 ;;
        --data)    DATA_FILE="$2"; shift 2 ;;
        --deploy)  FULL_DEPLOY=true; shift ;;
        -h|--help) usage ;;
        *) err "Unknown option: $1" ;;
    esac
done

[ -z "$MODE" ] && err "Must specify --local or --remote"
[ -z "$ENV_FILE" ] && err "Missing --env (path to .env backup)"
[ -z "$DATA_FILE" ] && err "Missing --data (path to suppressions.enc backup)"

[ ! -f "$ENV_FILE" ] && err ".env file not found: $ENV_FILE"
[ ! -f "$DATA_FILE" ] && err "suppressions.enc not found: $DATA_FILE"

if [ "$MODE" = "remote" ]; then
    [ -z "$REMOTE_HOST" ] && err "Missing --remote (user@host)"
    SSH_OPTS=""
    [ -n "$SSH_KEY" ] && SSH_OPTS="-i $SSH_KEY"
    SCP_OPTS="$SSH_OPTS"
    RSH="ssh $SSH_OPTS $REMOTE_HOST"
    RCP="scp $SCP_OPTS"
else
    [ "$(id -u)" -ne 0 ] && err "Local restore requires root — run with sudo"
    RSH=""
fi

echo -e "${CYAN}"
echo "╔══════════════════════════════════════════════════╗"
echo "║      Suppression Manager — Data Restore          ║"
echo "╚══════════════════════════════════════════════════╝"
echo -e "${NC}"

# ── Step 1: Upload backup files ──
log "Step 1: Placing backup files..."

if [ "$MODE" = "remote" ]; then
    log "Uploading .env to ${REMOTE_HOST}:${APP_DIR}/.env"
    $RCP "$ENV_FILE" ${REMOTE_HOST}:/tmp/sm-env-restore
    log "Uploading suppressions.enc to ${REMOTE_HOST}:${APP_DIR}/data/suppressions.enc"
    $RCP "$DATA_FILE" ${REMOTE_HOST}:/tmp/sm-data-restore

    $RSH "sudo mkdir -p ${APP_DIR}/data"
    $RSH "sudo cp /tmp/sm-env-restore ${APP_DIR}/.env"
    $RSH "sudo cp /tmp/sm-data-restore ${APP_DIR}/data/suppressions.enc"
    $RSH "sudo chown \$(id -u):\$(id -g) ${APP_DIR}/.env ${APP_DIR}/data/suppressions.enc 2>/dev/null || true"
    $RSH "sudo chmod 600 ${APP_DIR}/.env"
    $RSH "rm -f /tmp/sm-env-restore /tmp/sm-data-restore"
else
    cp "$ENV_FILE" "${APP_DIR}/.env"
    mkdir -p "${APP_DIR}/data"
    cp "$DATA_FILE" "${APP_DIR}/data/suppressions.enc"
    chmod 600 "${APP_DIR}/.env"
fi

log "Files placed"

# ── Step 2: Full deploy (optional — for fresh EC2) ──
if [ "$FULL_DEPLOY" = true ] && [ "$MODE" = "remote" ]; then
    log "Step 2: Running full deploy on remote..."
    $RSH "cd ${APP_DIR} && sudo bash deploy/setup.sh"
    log "Full deploy complete"
else
    log "Step 2: Restarting service..."
    if [ "$MODE" = "remote" ]; then
        $RSH "sudo systemctl restart ${SERVICE_NAME}"
    else
        systemctl restart "$SERVICE_NAME"
    fi
    sleep 2
    log "Service restarted"
fi

# ── Step 3: Verify ──
log "Step 3: Verifying..."

if [ "$MODE" = "remote" ]; then
    STATUS=$($RSH "sudo systemctl is-active ${SERVICE_NAME}" 2>/dev/null || echo "inactive")
    HTTP=$($RSH "curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8000/ 2>/dev/null" || echo "000")
    DATA_SIZE=$($RSH "stat -c%s ${APP_DIR}/data/suppressions.enc 2>/dev/null" || echo "0")
else
    STATUS=$(systemctl is-active "$SERVICE_NAME" 2>/dev/null || echo "inactive")
    HTTP=$(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:8000/ 2>/dev/null || echo "000")
    DATA_SIZE=$(stat -c%s "${APP_DIR}/data/suppressions.enc" 2>/dev/null || echo "0")
fi

echo ""
echo -e "${CYAN}══════════════════════════════════════════════════════${NC}"

if [ "$STATUS" = "active" ]; then
    echo -e "  Service:   ${GREEN}running${NC}"
else
    echo -e "  Service:   ${RED}${STATUS}${NC}"
fi

if [ "$HTTP" = "307" ] || [ "$HTTP" = "200" ]; then
    echo -e "  App:       ${GREEN}responding (HTTP ${HTTP})${NC}"
else
    echo -e "  App:       ${YELLOW}HTTP ${HTTP}${NC}"
fi

echo -e "  Data:      ${GREEN}${DATA_SIZE} bytes${NC}"
echo ""

if [ "$STATUS" = "active" ] && ([ "$HTTP" = "307" ] || [ "$HTTP" = "200" ]); then
    echo -e "  ${GREEN}Restore successful!${NC}"
else
    echo -e "  ${YELLOW}Restore completed but verification had issues — check logs:${NC}"
    if [ "$MODE" = "remote" ]; then
        echo "    $RSH 'sudo journalctl -u ${SERVICE_NAME} -n 20'"
    else
        echo "    journalctl -u ${SERVICE_NAME} -n 20"
    fi
fi

echo -e "${CYAN}══════════════════════════════════════════════════════${NC}"
