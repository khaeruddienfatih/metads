#!/usr/bin/env bash
# Setup Mac mini Ubuntu: Claude Code + repo metaads + bot Telegram.
# Jalankan sekali:  bash setup-ubuntu.sh
set -euo pipefail

REPO_URL="https://github.com/khaeruddienfatih/metads.git"
BACKUP_URL="https://github.com/elharamainwisata/metads.git"
DIR="$HOME/metaads"

echo "== 1. Paket dasar (git, python3, curl)"
sudo apt-get update -y
sudo apt-get install -y git python3 curl

echo "== 2. Claude Code"
if ! command -v claude >/dev/null 2>&1; then
  curl -fsSL https://claude.ai/install.sh | bash
fi
export PATH="$HOME/.local/bin:$PATH"
claude --version || true

echo "== 3. Repo metaads -> $DIR"
if [ ! -d "$DIR/.git" ]; then
  git clone "$REPO_URL" "$DIR"
fi
cd "$DIR"
if ! git remote get-url --push --all origin | grep -q "elharamainwisata"; then
  git remote set-url --add --push origin "$REPO_URL"
  git remote set-url --add --push origin "$BACKUP_URL"
fi
git config user.name  >/dev/null || git config user.name  "Elharamain Mac mini"
git config user.email >/dev/null || git config user.email "elharamainwisata@gmail.com"

echo "== 4. File konfigurasi bot"
if [ ! -f telegram/.env ]; then
  cp telegram/.env.example telegram/.env
  chmod 600 telegram/.env
  echo ">> Isi token bot di $DIR/telegram/.env lalu jalankan skrip ini lagi."
fi

echo "== 5. Service systemd (jalan otomatis)"
mkdir -p "$HOME/.config/systemd/user"
cp telegram/elharamain-bot.service "$HOME/.config/systemd/user/"
systemctl --user daemon-reload
systemctl --user enable elharamain-bot.service
sudo loginctl enable-linger "$USER"   # tetap jalan walau user tidak login
if grep -q "isi-token" telegram/.env; then
  echo ">> Token belum diisi — service belum dinyalakan."
else
  systemctl --user restart elharamain-bot.service
  systemctl --user --no-pager status elharamain-bot.service | head -5
fi

cat <<'EOF'

Selesai. Langkah manual yang tersisa (lihat memory/pindah-ubuntu.md):
  a) Login Claude:      claude   lalu ketik /login  (akun Claude yang sama)
  b) Login GitHub:      supaya git push bisa (gh auth login atau token HTTPS)
  c) Isi telegram/.env  (token BotFather + chat ID), lalu:
                        systemctl --user restart elharamain-bot
  d) Tes di Telegram:   kirim /start ke bot
Log bot:  journalctl --user -u elharamain-bot -f
EOF
