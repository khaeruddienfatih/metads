# Routine baku (aturan resmi dari user, 3 Nov 2026)

Sumber: pesan user 3 Nov 2026 (rincian di bawah dikutip dari perintahnya). Kalau ada beda dengan file lain, file ini yang dipakai.
Jam = WIB. Akun: 14 (Naik anggaran: 13, Allif dikecualikan). Hasil = chat WA. Semua CPR "hari ini" kecuali disebut lain.

## Jadwal

| Jam | Pekerjaan |
|---|---|
| Tiap 30 menit (:13, :43), kecuali 22:00–03:59 | Cek ad set dan iklan (A, B, C, D di bawah) |
| 22:00 | Semua ad set aktif di-PAUSE, daftarnya disimpan |
| 04:00 | Naik anggaran +10%, lalu nyalakan ad set yang OFF |
| 06:00 dan 08:00 | Email rekap kemarin |
| 12:00, 16:00, 21:00 | Email laporan hari ini sampai jam itu |

## Aturan cek tiap 30 menit

- **A — NYALAKAN ad set** yang kena OFF otomatis kalau CPR hari ini < **Rp30rb** (chat ≥ 1). **Tidak ada batas berapa kali**; yang penting CPR < Rp30rb.
- **B — PAUSE ad set** kalau spend hari ini > **Rp25rb** dan **0 hasil** hari ini. (Menggantikan aturan lama Rp30rb/0 chat dan Rp40rb/<2 chat.) Ad set non-chat dikecualikan.
- **C — PAUSE iklan** kalau CPR sepanjang waktu > **Rp50rb** (atau 0 chat dan spend ≥ Rp35rb). Hanya PAUSE, tidak menghapus.
- **D — NYALAKAN iklan** yang kena OFF kalau CPR sepanjang waktu < **Rp30rb** (chat ≥ 1). Iklan yang diarsipkan/dihapus user tidak dinyalakan.

## Naik anggaran (04:00)

Campaign chat WA ACTIVE dengan H-1, H-2, H-3 masing-masing chat ≥ 1 dan CPR < Rp30rb → budget +10% (dibulatkan ke atas Rp1.000),
maks Rp300rb/hari per campaign, jeda 3 hari antar kenaikan. Allif dikecualikan.

## Larangan

Jangan ubah targeting, iklan, atau budget di luar aturan di atas. Jangan menghapus iklan lewat routine.
Jangan simpan token/kredensial di file memory.

## Perlu dipastikan dengan user

- "Kena off otomatis" (A/D): hanya yang dimatikan auto rule Meta, atau juga yang dimatikan routine (B/C)? Perhatikan: kalau B/C ikut, bisa saling bolak-balik.
- 04:00 "nyalakan semua adset off": semua ad set PAUSED, atau hanya yang dimatikan jadwal malam? (Sekarang hanya daftar malam.)
- Laporan "ad set/iklan CPR bagus tapi PAUSED" dan auto rule via token Meta belum ada.
- Prompt routine cloud (`trig_...`) mungkin perlu disamakan dengan file ini; teks `/routine` di bot.py juga masih lama.
