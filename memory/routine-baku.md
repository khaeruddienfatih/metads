# Routine baku (ringkasan tunggal, 3 Nov 2026)

Ringkasan semua yang dikerjakan routine. Rincian langkah ada di file yang ditautkan. Kalau ada beda dengan file lain, file ini
(versi terbaru perintah user) yang dipakai. Jam = WIB. Akun: 14 (Naik anggaran: 13, Allif dikecualikan).

## Jadwal

| Jam | Pekerjaan | Rincian |
|---|---|---|
| tiap 30 menit (:13, :43), kecuali 22:00–03:59 | Bagian A nyala / B pause ad set / C pause iklan | [auto-reaktivasi.md](auto-reaktivasi.md) |
| 22:00 | Semua ad set ACTIVE di-PAUSE, daftar disimpan | [jadwal-malam.md](jadwal-malam.md) |
| 04:00 | 1) Naik anggaran +10%, 2) nyalakan ad set dari daftar malam | [naik-budget.md](naik-budget.md) |
| 06:00, 08:00 | Email Rekap Harian (kemarin) | chat-memory.md |
| 12:00, 16:00, 21:00 | Email laporan hari ini s.d. jam itu | chat-memory.md |

## Aturan cek tiap 30 menit (semua pakai data HARI INI, hasil = chat WA)

- **A — NYALAKAN** ad set yang PAUSED, campaign ACTIVE, chat hari ini ≥ 1 dan CPR hari ini < **Rp35rb**.
  Tanpa batas berapa kali sehari (3 Nov). Syarat CPR 3 hari dihapus.
  *Cakupan saat ini:* hanya ad set yang dimatikan auto rule Meta. **Belum diputuskan:** apakah juga ad set yang dimatikan Bagian B.
- **B — PAUSE ad set** ACTIVE: spend ≥ Rp30rb dan 0 chat; ATAU spend > Rp40rb dan chat < 2. Ad set non-chat dikecualikan.
- **C — PAUSE iklan** (data sepanjang waktu): CPR > Rp50rb, atau 0 chat dan spend ≥ Rp35rb. Hanya PAUSE, tidak menghapus.

## Naik anggaran (04:00)

Campaign chat WA ACTIVE dengan H-1, H-2, H-3 masing-masing chat ≥ 1 dan CPR < Rp30rb → budget +10% (dibulatkan ke atas Rp1.000),
maks Rp300rb/hari per campaign, jeda 3 hari antar kenaikan. Allif dikecualikan.

## Larangan

Jangan ubah targeting, iklan, atau budget di luar aturan di atas. Jangan menghapus iklan lewat routine.
Jangan simpan token/kredensial di file memory.

## Yang belum otomatis / perlu diputuskan

- Laporan "ad set CPR < Rp35rb tapi PAUSED" dan laporan kerja routine ke Telegram/email belum ada.
- Auto rule lewat token Meta belum dibuat (token belum ada).
- Daftar di `bot.py` (`routine()`) masih teks lama; samakan setelah disetujui.
