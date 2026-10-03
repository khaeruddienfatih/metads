# CLAUDE.md

Repo ini dipakai untuk mengelola iklan Meta (Umroh/Haji) Elharamain Wisata.

**Sebelum mengerjakan apa pun, baca memory chat sebelumnya:**

@memory/chat-memory.md

Teks iklan (primary text) per paket ada di `memory/primary-texts.md`.
Riwayat percakapan ada di `memory/chat-log.md`.

## Wajib: simpan setiap chat

User ingin bisa melanjutkan dari komputer mana pun. Jadi **di akhir setiap jawaban** (setiap
permintaan user yang selesai dikerjakan):

1. Tambahkan entri baru di **akhir** `memory/chat-log.md` dengan format:
   `### YYYY-MM-DD — <ringkasan permintaan user>` lalu poin-poin singkat: apa yang diminta,
   apa yang dikerjakan (akun, ID, jumlah iklan, angka budget), hasilnya, dan apa yang tertunda.
2. Kalau ada aturan baru, status akun berubah, atau budget berubah, perbarui juga
   `memory/chat-memory.md`.
3. Commit lalu push langsung ke `main` (`git pull origin main` dulu, lalu `git push origin main`).

Jangan simpan token, password, atau kredensial di file memory.
