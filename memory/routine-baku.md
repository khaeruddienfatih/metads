# Routine baku (aturan resmi dari user, 3 Nov 2026)

Sumber: pesan user 3 Nov 2026 (rincian di bawah dikutip dari perintahnya). Kalau ada beda dengan file lain, file ini yang dipakai.
Jam = WIB. Akun: 14 (Naik anggaran: 13, Allif dikecualikan). Hasil = chat WA. Semua CPR "hari ini" kecuali disebut lain.

## Jadwal

| Jam | Pekerjaan |
|---|---|
| Tiap 30 menit (:13, :43), kecuali 22:00–03:59 | Cek ad set dan iklan (A, B, C, D di bawah) |
| 22:00 | Semua ad set aktif di-PAUSE, daftarnya disimpan |
| 04:00 | Naik anggaran +10%, lalu nyalakan SEMUA ad set yang OFF (siapa pun yang mematikan) |
| 06:00 dan 08:00 | Email rekap kemarin |
| 12:00, 16:00, 21:00 | Email laporan hari ini sampai jam itu |

## Aturan cek tiap 30 menit

- **A — NYALAKAN ad set** yang PAUSED (siapa pun yang mematikan; kecuali campaign-nya dimatikan / ARCHIVED) kalau CPR hari ini < **Rp30rb** (chat ≥ 1). **Tidak ada batas berapa kali**; yang penting CPR < Rp30rb.
- **B — PAUSE ad set** kalau spend hari ini > **Rp25rb** dan **0 hasil** hari ini. (Menggantikan aturan lama Rp30rb/0 chat dan Rp40rb/<2 chat.) Ad set non-chat dikecualikan.
- **C — PAUSE iklan** kalau CPR sepanjang waktu > **Rp50rb** (atau 0 chat dan spend ≥ Rp35rb). Hanya PAUSE, tidak menghapus.
- **D — NYALAKAN iklan** yang PAUSED (siapa pun yang mematikan, ditegaskan user 3 Nov "karena ada iklan bagus malah kena off") kalau CPR sepanjang waktu < **Rp30rb** (chat ≥ 1). Iklan yang diarsipkan/dihapus user tidak dinyalakan.

## Naik anggaran (04:00)

Campaign chat WA ACTIVE dengan H-1, H-2, H-3 masing-masing chat ≥ 1 dan CPR < Rp30rb → budget +10% (dibulatkan ke atas Rp1.000),
maks Rp300rb/hari per campaign, jeda 3 hari antar kenaikan. Allif dikecualikan.

## Larangan

Jangan ubah targeting, iklan, atau budget di luar aturan di atas. Jangan menghapus iklan lewat routine.
Jangan simpan token/kredensial di file memory.

## Sudah dijawab user (3 Nov)

- Nyala ulang berlaku untuk **siapa pun yang mematikan** (auto rule, routine, atau user); 04:00 menyalakan **semua** ad set yang PAUSED.
- Pengecualian aman: campaign PAUSED/ARCHIVED/DELETED tidak dinyalakan; iklan ARCHIVED/DELETED tidak dinyalakan.
- Saling-tabrak dijaga syarat: A/D butuh chat ≥ 1 dan CPR < Rp30rb; B butuh 0 hasil; C butuh CPR > Rp50rb — tidak ada yang tumpang tindih.

## Masih tertunda

- Prompt routine cloud (`trig_...`) disamakan dengan file ini; teks `/routine` di bot.py; laporan "CPR bagus tapi PAUSED"; auto rule via token Meta.
