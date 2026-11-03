# Tabel routine (bisa diedit) — 3 Nov 2026

Edit kolom "Kalau", "Maka" atau "Angka", lalu bilang ke Claude: "sesuaikan routine dengan routine-tabel.md".
Claude akan memperbarui prompt routine cloud sesuai tabel ini. Mengedit file saja belum mengubah cara kerja routine.

| No | Kapan jalan | Kalau (syarat) | Maka | Angka |
|---|---|---|---|---|
| 1 | Tiap 30 menit | Ad set mati, chat hari ini ≥ 1, CPR hari ini di bawah angka | NYALAKAN ad set | CPR < Rp30.000 |
| 2 | Tiap 30 menit | Ad set aktif, spend hari ini di atas angka, 0 chat | MATIKAN ad set | Spend > Rp25.000 |
| 3 | Tiap 30 menit | Iklan aktif, CPR sepanjang waktu di atas angka | MATIKAN iklan | CPR > Rp50.000 |
| 4 | Tiap 30 menit | Iklan mati, CPR sepanjang waktu di bawah angka | NYALAKAN iklan | CPR < Rp30.000 |
| 5 | 22:00 | Semua ad set aktif | MATIKAN semua | – |
| 6 | 04:00 | CPR tiap hari selama 3 hari di bawah angka | NAIKKAN anggaran campaign | CPR < Rp30.000, +10%, maks Rp300.000 |
| 7 | 04:00 (setelah no 6) | Semua ad set mati | NYALAKAN semua | – |
| 8 | 06:00 | – | KIRIM email laporan kemarin ke elharamainwisata | – |
| 9 | 08:00 | – | KIRIM email laporan kemarin ke dhiyaaelhaq01 | – |
| 10 | 12:00, 16:00, 21:00 | – | KIRIM email laporan hari ini ke elharamainwisata | – |

## Pengecualian (berlaku untuk semuanya)

- Tidak ada yang jalan di jam 22:00–03:59, kecuali no 5, 6, 7.
- Ad set bukan chat WA (mis. Haji 4) tidak ikut no 2.
- Allif tidak boleh dinaikkan anggarannya (no 6); jeda 3 hari antar kenaikan.
- Hanya campaign yang aktif dan iklan yang belum diarsipkan yang dinyalakan.
- Penyalaan tidak peduli siapa yang mematikan (no 1, 4, 7).
- Hasil = chat WA. Routine tidak menghapus iklan dan tidak mengubah targeting atau kreatif.

## Di balik layar (tidak perlu diedit)

| No di atas | Routine cloud | ID |
|---|---|---|
| 1–4 | Cek menit :13 dan :43 (dua routine kembar) | trig_01PExMLpwLUtZxVRsi4R6e8H, trig_013WfwoGnfBo14J4EupZGgtx |
| 5 | Jadwal malam | trig_01FPcdHh57QKkum5LoEAwj2k |
| 6–7 | Jadwal pagi | trig_01KLe5sJc8N6MQMEYKUpzNqB |
| 8 | Email rekap pagi | trig_01Ci9E1ffEGZ97CAaxiyqCBY |
| 9 | Email rekap pimpinan | trig_01NydaDZaZmHdb68jLxpn13R |
| 10 | Email laporan harian | trig_01D9NHsCepUj6rvi7cs5nt77 |
