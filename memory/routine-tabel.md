# Tabel routine (bisa diedit) — 3 Nov 2026

Edit kolom "Aturan" atau "Angka", lalu beri tahu Claude: "sesuaikan routine dengan routine-tabel.md". Claude akan memperbarui prompt routine cloud sesuai tabel ini.

| No | Routine | ID routine | Jam (WIB) | Bagian | Aturan | Angka | Siapa yang mematikan | Status |
|---|---|---|---|---|---|---|---|---|
| 1 | Cek 30 menit (:13) | trig_01PExMLpwLUtZxVRsi4R6e8H | Tiap jam menit :13, lewati 22:00–03:59 | A | NYALAKAN ad set PAUSED kalau chat hari ini ≥ 1 dan CPR hari ini di bawah angka | CPR hari ini < Rp30.000; tanpa batas berapa kali | Siapa pun | Aktif, prompt baru 3 Nov |
| 1 | Cek 30 menit (:13) | trig_01PExMLpwLUtZxVRsi4R6e8H | sama | B | PAUSE ad set ACTIVE kalau spend hari ini di atas angka dan 0 chat | Spend hari ini > Rp25.000 dan 0 chat | – | Aktif |
| 1 | Cek 30 menit (:13) | trig_01PExMLpwLUtZxVRsi4R6e8H | sama | C | PAUSE iklan ACTIVE kalau CPR sepanjang waktu di atas angka | CPR sepanjang waktu > Rp50.000 (atau 0 chat dan spend ≥ Rp35.000) | – | Aktif |
| 1 | Cek 30 menit (:13) | trig_01PExMLpwLUtZxVRsi4R6e8H | sama | D | NYALAKAN iklan PAUSED kalau CPR sepanjang waktu di bawah angka | CPR sepanjang waktu < Rp30.000 (chat ≥ 1) | Siapa pun | Aktif, baru |
| 2 | Cek 30 menit (:43) | trig_013WfwoGnfBo14J4EupZGgtx | Tiap jam menit :43, lewati 22:00–03:59 | A, B, C, D | Sama persis dengan routine 1 | Sama dengan routine 1 | Sama | Aktif, prompt baru 3 Nov |
| 3 | Jadwal pagi | trig_01KLe5sJc8N6MQMEYKUpzNqB | 04:00 | Langkah 1 | NAIK ANGGARAN campaign chat WA kalau CPR 3 hari berturut-turut di bawah angka | CPR tiap hari (H-1, H-2, H-3) < Rp30.000; naik +10%; maks Rp300.000/hari/campaign; jeda 3 hari; Allif dikecualikan | – | Aktif |
| 3 | Jadwal pagi | trig_01KLe5sJc8N6MQMEYKUpzNqB | 04:00 | Langkah 2 | NYALAKAN SEMUA ad set PAUSED di campaign ACTIVE | – | Siapa pun | Aktif, prompt baru 3 Nov |
| 4 | Jadwal malam | trig_01FPcdHh57QKkum5LoEAwj2k | 22:00 | – | PAUSE semua ad set ACTIVE di 14 akun, simpan daftar | – | – | Aktif, tidak diubah |
| 5 | Email rekap pagi | trig_01Ci9E1ffEGZ97CAaxiyqCBY | 06:00 | – | Email laporan KEMARIN (chat, biaya, CPR; Umroh per akun, Haji per CS) ke elharamainwisata@gmail.com | Urut biaya terbesar | – | Aktif |
| 6 | Email rekap pimpinan | trig_01NydaDZaZmHdb68jLxpn13R | 08:00 | – | Email laporan yang sama ke dhiyaaelhaq01@gmail.com (tidak dikirim kalau gagal cek) | Urut biaya terbesar | – | Aktif |
| 7 | Email laporan harian | trig_01D9NHsCepUj6rvi7cs5nt77 | 12:00, 16:00, 21:00 | – | Email laporan HARI INI sampai jam itu ke elharamainwisata@gmail.com, tanpa pembanding | Urut biaya terbesar | – | Aktif |
| 8 | Naik anggaran 07:00 (lama) | trig_01XvAgB4noayYxfMXZgoiruc | 07:00 | – | Digantikan routine 3 langkah 1 | – | – | NONAKTIF |

## Catatan

- 14 akun: Diana, Tira, Nida, Hanif, Allif, Fikri, AIni, Irfan, Fifi, Elharamain Haji, Haji 2, Haji 3, Haji 4, haji (ID lengkap di `auto-reaktivasi.md`).
- Hasil = chat WA (messaging conversation started). Ad set non-chat (pixel/add-to-cart, mis. Haji 4) dikecualikan dari B.
- Larangan: routine tidak mengubah targeting, kreatif, atau budget di luar aturan; tidak menghapus iklan.
