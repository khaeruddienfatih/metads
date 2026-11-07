# Aturan Otomatis Iklan Meta — per 3 Nov 2026

## Cara mengubah aturan
1. Edit angka atau kalimat di kolom **Kalau**, **Maka**, atau **Angka**.
2. Kirim pesan ke Claude: **"sesuaikan routine dengan routine-tabel.md"**.
3. Claude memperbarui routine di cloud.

> ⚠️ Mengedit file ini saja **belum** mengubah cara kerja routine. Langkah 2 wajib.

## Istilah
- **Hasil** = chat WhatsApp yang masuk dari iklan.
- **CPR** = biaya per hasil, yaitu biaya untuk mendapat 1 chat WA (spend ÷ jumlah chat).
- **Hari ini** = sejak 00:00 sampai saat pengecekan.
- **Sepanjang waktu** = sejak iklan pertama kali jalan.
- **Ad set** = kelompok iklan (berisi anggaran & target). **Iklan** = materi iklan di dalam ad set.

---

## A. Pengecekan otomatis (tiap 15 menit, jam 04:00–21:59; Minggu hanya 04:00–13:59)

| No | Untuk | Kalau (syarat) | Maka | Angka |
|---|---|---|---|---|
| 1 | Ad set | Sedang mati, sudah ada ≥ 1 chat hari ini, dan CPR hari ini murah | NYALAKAN ad set | CPR < Rp30.000 |
| 2 | Ad set | Sedang aktif, spend hari ini sudah tinggi, tapi belum ada chat | MATIKAN ad set | Spend > Rp25.000 |
| 2b | Ad set | Sedang aktif, spend hari ini sudah tinggi, tapi chat hari ini kurang dari 2 | MATIKAN ad set | Spend ≥ Rp45.000 dan chat < 2 |
| 3 | Iklan | Sedang aktif, CPR sepanjang waktu mahal | MATIKAN iklan | CPR > Rp50.000 |
| 4 | Iklan | Sedang mati, CPR sepanjang waktu murah | NYALAKAN iklan | CPR < Rp30.000 |

Catatan:
- Akun **elharamain Profile** (873443374652541) tidak ikut aturan no 1–4 dan 2b, karena hasilnya bukan chat WA (juga tidak ikut bagian B).
- No 2 & 2b hanya untuk ad set chat WA. Ad set lain (mis. **Haji 4**) tidak ikut dimatikan.
- No 1 & 4 tetap menyalakan walau yang mematikan sebelumnya adalah orang, bukan routine.

## B. Jadwal harian

| No | Jam | Kalau (syarat) | Maka | Angka |
|---|---|---|---|---|
| 5 | 22:00 | Ada ad set yang aktif | MATIKAN semua ad set (istirahat malam) | – |
| 5b | Minggu 14:00 | Hari Minggu, ada ad set yang aktif | MATIKAN semua ad set (libur Minggu siang) | – |
| 6 | 03:00 | CPR tiap hari selama 3 hari terakhir murah | NAIKKAN anggaran campaign | CPR < Rp30.000 · naik +10% · maksimal Rp300.000/hari |
| 7 | 04:00 | Ada ad set yang mati | NYALAKAN semua ad set | – |

Catatan:
- No 5b (7 Nov 2026, perintah user "tambah satu aturan khusus di hari minggu adset off di jam 2 siang, elharamain profile tetep berjalan"): Minggu 14:00 WIB semua ad set ACTIVE di 14 akun di-PAUSE. Setelah itu sampai Senin 03:59 tidak ada yang menyalakan (aturan no 1 & 4 libur). Senin 04:00 no 7 menyalakan lagi seperti biasa.
- Akun **elharamain Profile** (873443374652541) tidak ikut no 5, 5b, 6, 7 (tidak dimatikan malam, tidak dinaikkan anggarannya, tidak dinyalakan pagi).
- No 6: campaign **Allif tidak pernah dinaikkan**. Setiap campaign minimal **jeda 3 hari** antar kenaikan.
- No 7 tetap menyalakan walau yang mematikan adalah orang.

## C. Email laporan

| No | Jam | Isi laporan | Dikirim ke |
|---|---|---|---|
| 8 | 06:00 | Hasil kemarin | elharamainwisata |
| 9 | 08:00 | Hasil kemarin | dhiyaaelhaq01 (pimpinan) |
| 10 | 12:00, 16:00, 21:00 | Hasil hari ini sampai jam tersebut | elharamainwisata |

---

## Batasan yang berlaku untuk semua aturan
- **Jam tenang 22:00–03:59, dan hari Minggu sejak 14:00:** tidak ada aturan yang jalan, kecuali no 5, 5b, 6, dan 7 (no 6 jalan 03:00 supaya tidak bentrok dengan no 7 jam 04:00).
- Yang dinyalakan hanya campaign yang **aktif** dan iklan yang **belum diarsipkan**.
- Routine **tidak pernah** menghapus iklan, dan **tidak mengubah** targeting maupun kreatif.

## Ringkasan satu hari
```
03:00  Naikkan anggaran yang layak (no 6)
04:00  Nyalakan semua ad set (no 7)
04:00–21:59  Cek tiap 15 menit (no 1–4)
06:00  Email rekap kemarin → elharamainwisata (no 8)
08:00  Email rekap kemarin → pimpinan (no 9)
12:00 / 16:00 / 21:00  Email laporan hari ini (no 10)
22:00  Matikan semua ad set (no 5)
22:00–03:59  Jam tenang
```

---

## Di balik layar (tidak perlu diedit)

| Aturan | Routine cloud | ID |
|---|---|---|
| 1–4 (+2b) | Cek 15 menit: empat routine, masing-masing sekali per jam | :13 trig_01PExMLpwLUtZxVRsi4R6e8H · :28 trig_01K5FuVYv9LfbFm6adDaxPBV · :43 trig_013WfwoGnfBo14J4EupZGgtx · :58 trig_014noZbx2jsJHWH7w52P2UFf |
| 5 | Jadwal malam | trig_01FPcdHh57QKkum5LoEAwj2k |
| 6 | Naik anggaran 03:00 | trig_0169Dw65vf7mZiGkufKqdoRf |
| 7 | Jadwal pagi 04:00 | trig_01KLe5sJc8N6MQMEYKUpzNqB |
| 8 | Email rekap pagi | trig_01Ci9E1ffEGZ97CAaxiyqCBY |
| 9 | Email rekap pimpinan | trig_01NydaDZaZmHdb68jLxpn13R |
| 10 | Email laporan harian | trig_01D9NHsCepUj6rvi7cs5nt77 |
