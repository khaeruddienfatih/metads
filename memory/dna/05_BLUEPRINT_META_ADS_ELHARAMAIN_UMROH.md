# 05 — BLUEPRINT META ADS — Elharamain Wisata Umroh (9 akun)

**Otak Meta Ads** — dibaca Claude di awal setiap sesi analisis/keputusan harian (Level 2).
Dibangun 22 Okt 2026 dari [01](01_META_ADS_ACCOUNT_DISCOVERY.md) · [02](02_META_ADS_PERFORMANCE_PATTERN.md) ·
[03](03_META_ADS_CREATIVE_AUDIENCE_DISCOVERY.md) · [04](04_META_ADS_SCALING_REFRESH_DISCOVERY.md).
Konversi = **chat WA dimulai**. Aturan user di `chat-memory.md` **selalu menang** atas Blueprint ini bila bertentangan.

## SYNTHESIS AKTIF (sebelum Blueprint)
**5 temuan konsisten di semua file:**
1. CPM adalah driver CPR #1 (Q1 vs Q4 CPM lebih murah di **9/9 akun**).
2. Winner terkonsentrasi: 5,7% iklan = 70% chat, CPR Rp31rb.
3. Iklan < Rp50rb belum bisa divonis (59–96% masih nol chat); ≥ Rp100rb hampir pasti dapat chat.
4. 12 Hari selalu lebih mahal dari 9 Hari (9/9 akun); LAT paling mahal.
5. WA Status/Reels lebih murah dari IG Feed.

**3 temuan bertentangan & penyelesaiannya:**
1. *Kill Rp35rb (aturan user)* vs *data: median biaya 1 chat Rp39rb* → aturan user tetap dipakai; ambang dijadikan eksperimen (Rp35rb vs Rp50rb).
2. *"Gambar baru tiap minggu"* vs *iklan baru Okt CPR Rp48rb, winner lama Rp31rb* → refresh hanya saat ada trigger (lihat Bagian 11).
3. *Frequency rendah = baik* vs *frequency 1,6–2,0 justru termurah* → fatigue baru dianggap > 2,0.

**Data paling tipis (diberi label):** histori scaling, learning phase, hook/angle, komentar, chat per wilayah, data closing.

**1 variabel paling menentukan profitabilitas:** **data closing per iklan** — saat ini tidak ada; tanpa itu CPR hanya proxy.
Variabel terukur paling menentukan: **CPM per chat-klik (pilihan penempatan + kualitas creative)**.

## BAGIAN 1 — QUICK REFERENCE CARD
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
META ADS DNA — Elharamain Umroh (9 akun) — Quick Reference
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Konversi         : chat WA dimulai (bukan purchase)
CPR baseline     : Rp27.900 – Rp39.300   (P25–median iklan)
Target per paket : 9 Hari Rp41rb · Ramadhan Rp42rb · Desember Rp44,6rb · 12 Hari Rp47rb
CPR safe ceiling : Rp54.900 (P75) → cek penempatan & creative, jangan tambah budget
CPR danger       : Rp73.800 (P90) → kurangi budget ad set / ganti creative
CPR kill         : CPR lifetime > Rp73.800, ATAU spend ≥ Rp78.600 dengan 0 chat
Aturan user aktif: hapus spend ≥ Rp35rb & 0 chat; hapus CPR > Rp50rb kecuali ≥5 chat
Min test budget  : Rp39.300/hari per ad set (ideal Rp78.600) × N hari (N: data belum ada)
Winner validation: ≥5 chat & CPR ≤ Rp39.300 & spend ≥ Rp100rb
Scale trigger    : ad set ≥10 chat/7 hari & CPR ≤ Rp39.300 → +20% budget, tunggu 3 hari (HIPOTESIS)
Refresh trigger  : frequency ad set > 2,0  ATAU  CTR < 0,42% (≥ Rp50rb)  ATAU  CPR > Rp54.900
Cannibalism      : maks 3 iklan per ad set · iklan baru tidak masuk ad set winner
Penempatan       : IG (feed/story/reels) + FB Story + WA Status + Threads; tanpa IG Explore
Prioritas akun   : Fifi > Diana > Hanif ≈ AIni ≈ Tira ≈ Nida > Fikri > Irfan > Allif
Attribution      : default percakapan pesan 7 hari
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## BAGIAN 2 — Account operating principles (10)
1. **PRINSIP 1:** Nilai iklan dari CPR & chat/klik, bukan CTR. Dasar: 01 B3. ✓ TERBUKTI. Karena: korelasi CTR–CPR −0,11; testimoni CTR 1,15% CPR Rp64rb.
2. **PRINSIP 2:** Lindungi winner. Dasar: 02 P1. ✓. Karena: 800 iklan ≥5 chat = 70% chat, CPR Rp31rb.
3. **PRINSIP 3:** Iklan belum boleh divonis sebelum ±1× median CPR (Rp39rb). Dasar: 01 B12. ✓. Karena: 59% iklan Rp35–50rb masih nol.
4. **PRINSIP 4:** Penempatan murah (WA Status, Reels, FB Story) wajib ada. Dasar: 01 B6. ✓ (7/8 akun).
5. **PRINSIP 5:** CPM menentukan CPR → kontrol lewat penempatan & wilayah, bukan budget. Dasar: 01 B3. ✓ (9/9 akun).
6. **PRINSIP 6:** 9 Hari = produk utama; 12 Hari target CPR lebih tinggi; LAT berhenti. Dasar: 02 B2. ✓.
7. **PRINSIP 7:** Hanya objective percakapan WA. Dasar: 01 B1. ✓. Karena: Rp161 jt objective lain = 0 chat.
8. **PRINSIP 8:** Maks 3 iklan per ad set, CBO. Dasar: 01 B10. ✓ (433 grup).
9. **PRINSIP 9:** Pakai ulang post winner (By Saudia) sebelum membuat desain baru. Dasar: 03 B5. ~ PROBABLE (5/6 akun).
10. **PRINSIP 10:** Setiap perubahan budget/target dicatat (data scaling belum ada). Dasar: 04 B1. — wajib proses.

## BAGIAN 3 — Framework 10 fase
| Fase | Tujuan | KPI | SOP | Naik fase | Turun fase |
|---|---|---|---|---|---|
| 1 Research | ambil bahan dari CS (pertanyaan WA) & winner lama | 5 pertanyaan teratas tercatat | CS kirim daftar mingguan | daftar ada | — |
| 2 Production | 3 creative/paket/minggu | 9 creative/minggu | pakai visual dasar winner | creative siap | — |
| 3 Sprint testing | uji di ad set baru | spend Rp39–79rb/hari/ad set | 1 CBO · 3 ad set · ≤3 iklan | iklan ≥ Rp39rb spend | — |
| 4 Validation | pilih winner | ≥5 chat, CPR ≤ Rp39,3rb | lihat Bagian 8 | lolos Level 3 | CPR > Rp54,9rb |
| 5 Scaling | tambah volume | CPR ≤ Rp39,3rb setelah +20% | Bagian 9 | 3 hari stabil | CPR naik > 20% |
| 6 Refresh | cegah fatigue | frequency ≤ 2,0 | Bagian 11 | CPR kembali ≤ safe | — |
| 7 Audience expansion | kota baru | CPM ≤ Rp45rb | tambah kota ke ad set baru | CPR ≤ Rp42rb | CPM > Rp104rb |
| 8 Campaign scaling | salin campaign winner ke akun lain | CPR ≤ Rp42rb | post winner via object_story_id | 7 hari stabil | — |
| 9 Maintenance | jaga winner | CPR ≤ Rp39,3rb | jangan edit/pause | — | frequency > 2,0 |
| 10 Retirement | matikan | CPR > Rp73,8rb | aturan kill user | — | — |

## BAGIAN 4 — Creative research system
Sumber: (1) pertanyaan WA dari CS (bahasa jamaah), (2) post winner lama, (3) Meta Ads Library kompetitor umroh,
(4) review Google (6800+). Framework: Problem (antre lama, jadwal tidak pasti) · Desire (umroh tenang, Ramadhan) ·
Objection (harga, DP, cicilan, usia orang tua) · Proof (Google Review, tiket confirm) · Authority (Saudia, hotel bintang 5).
Status: hanya Offer+Proof yang pernah diuji (03 B1).

## BAGIAN 5 — Creative production system
- Volume: 3 creative per paket per minggu (9/minggu per akun) — bukan ±60–75/minggu seperti Sep–Okt (3.072 iklan/bulan).
- Prioritas format: **post winner dipakai ulang → foto paket (saudia_9_hari, januari_) → Desain 2/3 → Desain 7/Musim Dingin (uji)**. Testimoni & Desain 1/4 tidak diproduksi.
- Setiap nama iklan: `<Objektif> <Paket> | <Visual> | H-Review/H-Confirm | <Angle>`.

## BAGIAN 6 — Creative testing system
- Struktur: 1 campaign CBO | 3 ad set (paket) | ≤3 iklan per ad set (pola "(baru)").
- Budget: minimum Rp39.300/hari per ad set, ideal Rp78.600.
- Durasi: sampai tiap iklan ≥ Rp39.300 spend (atau 7 hari bila Meta tidak membelanjakan).
- Stop testing: iklan spend ≥ Rp35rb & 0 chat (aturan user) · CPR > Rp50rb & < 5 chat (aturan user) · CPR > Rp73,8rb.
- Lanjut: ≥1 chat sebelum Rp39rb, atau chat/klik ≥ 25%.

## BAGIAN 7 — Evaluasi harian
| Hari | Lihat | Abaikan | Boleh | Dilarang |
|---|---|---|---|---|
| 1 | delivery jalan, CPM, error | CPR | perbaiki error/target | kill/scale |
| 2 | CPM vs Rp77,9rb median, CTR | CPR | — | kill iklan < Rp35rb |
| 3 | spend per iklan, chat pertama | CTR naik turun | kill iklan ≥ Rp35rb & 0 chat (aturan user) | scale |
| 5 | CPR per ad set vs Rp39,3rb | iklan < Rp20rb | hapus iklan CPR > Rp73,8rb | ubah target |
| 7 | chat/7 hari, frequency | — | scale +20% bila ≥10 chat & CPR ≤ Rp39,3rb | > 1 perubahan/objek |
| 10 | iklan ≥5 chat | — | salin winner ke ad set baru | pause winner |
| 14 | frequency > 2,0? | — | refresh | hapus winner |
| 21 | review: scale/kill ad set | — | kill ad set CPR > Rp54,9rb & < 10 chat | — |

## BAGIAN 8 — Creative validation (5 level)
1. **Potential:** ≥1 chat dengan spend ≤ Rp39,3rb.
2. **Seed:** ≥3 chat, CPR ≤ Rp54,9rb.
3. **Validated:** ≥5 chat, CPR ≤ Rp39,3rb, spend ≥ Rp100rb.
4. **Scale:** ≥15 chat, CPR ≤ Rp35rb (lebih baik dari winner rata-rata Rp31rb +13%).
5. **Legend:** ≥50 chat, CPR ≤ Rp35rb (contoh: Fifi "Januari" 156 chat Rp32,6rb; Fikri "Post" 153 chat Rp34rb; Irfan "post - Salin" 110 chat Rp21,8rb; Diana "new" 136 chat Rp20,7rb).

## BAGIAN 9 — Scaling system
- **Vertikal** (pakai saat ad set ≥10 chat/7 hari & CPR ≤ Rp39,3rb): +20% budget campaign, tunggu 3 hari, ulangi. Hindari bila frequency > 2,0. Risiko: belum ada histori → catat hasil. ? HIPOTESIS.
- **Horizontal** (pakai saat winner sudah Level 4): salin iklan ke ad set/kota baru di akun sama (`source_ad_id`), atau pakai post winner di akun lain (`object_story_id`). Hindari: membuat banyak iklan baru tanpa winner. Risiko: 9 akun berebut audiens. ~ PROBABLE.
- **Hybrid:** naikkan budget akun Fifi/Diana + salin winner mereka ke akun lain.

## BAGIAN 10 — Bid framework
Saat ini lowest cost di semua ad set. Bid/cost cap belum ada data. Jika diuji: konservatif **Rp27.900**, normal **Rp39.300**, agresif **Rp54.900** (cost per chat). Min ROAS: tidak bisa (tanpa nilai konversi). ASC: tidak ada data.

## BAGIAN 11 — Refresh framework
- **Creative refresh:** trigger frequency > 2,0 atau CTR < 0,42% (iklan ≥ Rp50rb) atau CPR > Rp54,9rb. Langkah: 1 creative baru (visual dasar winner) di ad set baru; winner tetap. Timeline: nilai setelah Rp39rb.
- **Campaign refresh:** trigger CPR campaign > Rp54,9rb selama 7 hari. Langkah: salin campaign dengan winner saja. ?
- **Audience refresh:** trigger CPM > Rp104rb (Q4). Langkah: tambah kota ber-CPM rendah (Jateng/Jatim) di ad set baru. ?

## BAGIAN 12 — Cannibalism prevention SOP
1. **Campaign/akun:** trigger: ≥2 akun menjalankan creative + kota sama. Deteksi: CPM naik bersamaan di beberapa akun. Cegah: bagi kota atau paket per akun. Atasi: pause duplikat di akun dengan CPR tertinggi. ? HIPOTESIS.
2. **Ad set:** overlap tidak terukur → hindari 2 ad set paket sama dengan kota sama dalam 1 campaign.
3. **Ads:** trigger > 3 iklan per ad set. Deteksi: iklan ke-4+ spend < Rp10rb. Cegah: maks 3. Atasi: pindahkan iklan baru ke ad set baru. ✓.
4. **Creative:** trigger gambar sama di beberapa ad set satu campaign. Cegah: gambar unik (aturan user). Atasi: ganti gambar.

## BAGIAN 13 — CPR ceiling protection rules
- **GREEN:** Rp27.900 – Rp39.300 → tidak perlu intervensi.
- **YELLOW:** Rp39.300 – Rp54.900 → cek penempatan (WA Status/Reels terbuka?), jangan tambah budget.
- **DANGER:** Rp54.900 – Rp73.800 → turunkan budget ad set / ganti creative; ikuti aturan user (> Rp50rb & < 5 chat = hapus).
- **KILL:** > Rp73.800 lifetime, atau ≥ Rp78.600 spend tanpa chat → hapus. Precedent recovery: DATA TIDAK TERSEDIA.
- **SCALE PROTECTION:** CPR naik > 20% dalam 3 hari setelah naik budget → kembalikan budget. ?

## BAGIAN 14 — Campaign kill rules
- Kill creative: aturan user (≥ Rp35rb & 0 chat; CPR > Rp50rb & < 5 chat) — override: CPR > Rp73,8rb.
- Kill ad set: lifetime ≥ Rp250rb & CPR > Rp54,9rb & < 10 chat.
- Kill campaign: objective bukan percakapan WA; paket LAT; CPR > Rp54,9rb selama 14 hari.

## BAGIAN 15 — 90 day operating system
| Hari | Lakukan | Ukur | Putuskan |
|---|---|---|---|
| 1 | jalankan campaign "(baru)" (sudah aktif 8 akun; Irfan ad set masih PAUSED) | delivery, CPM | perbaiki error |
| 2 | cek CPM tiap akun | CPM ≤ Rp77,9rb | — |
| 3 | kill iklan aturan user | chat pertama | kill |
| 7 | review per paket & akun | CPR vs target paket | +20% untuk ad set ≥10 chat & ≤ Rp39,3rb |
| 14 | review frequency & winner | frequency, ≥5 chat | refresh / salin winner |
| 21 | review ad set | CPR ad set | kill ad set (Bagian 14) |
| 30 | update Blueprint (CPR bulanan) | CPR Okt→Nov | revisi ambang |
| 45 | uji ambang kill Rp35rb vs Rp50rb (2 akun) | chat per Rp | putuskan ambang |
| 60 | evaluasi data closing CS per paket | jamaah / chat | prioritas paket |
| 90 | rebuild DNA (jalankan skill 1–5 lagi) | semua | Blueprint v2 |

## BATTLE TEST (10 rule terpenting)
| Rule | Pembantah | Hasil |
|---|---|---|
| CPM rendah → CPR rendah | 0 dari 9 akun | **RULE KUAT** |
| 12 Hari > 9 Hari | 0 dari 9 akun | **RULE KUAT** |
| Iklan ≥ Rp100rb hampir pasti dapat chat | 24 dari 1.374 (1,7%) | **RULE KUAT** |
| Winner ≥5 chat CPR ±Rp31rb | per definisi | **RULE KUAT** (bukan prediksi) |
| WA Status < IG Feed | 1 dari 8 akun (Allif) = 12,5% | **RULE DENGAN SYARAT** — kecuali akun dengan Feed sudah < Rp32rb |
| LAT lebih mahal dari rata-rata akun | 1 dari 8 akun (Irfan 0,97×) = 12,5% | **RULE DENGAN SYARAT** |
| Post dipakai ulang lebih murah dari rata-rata akun | 1 dari 6 akun (Diana 1,03×) = 17% | **RULE DENGAN SYARAT** |
| IG Feed > Reels | 2 dari 9 akun (Nida, Allif) = 22% | **TURUN ke PROBABLE** |
| Maks 3 iklan per ad set | 1 iklan Rp32,9rb vs 5 iklan Rp41,2rb; 6 iklan Rp35,7rb membantah | **RULE DENGAN SYARAT** |
| Frequency > 2,0 = fatigue | hanya Rp11,9 jt data | **TETAP HIPOTESIS** |

## BAGIAN 16 — Final operating system

**20 rules yang tidak boleh dilanggar**
1. Iklan harus PAUSE saat dibuat; aktivasi hanya dengan perintah user.
2. Jangan sentuh iklan/ad set ACTIVE untuk perbaikan target (aturan user).
3. Objective selalu percakapan WA (CONVERSATIONS → WhatsApp).
4. Tanpa katalog.
5. Penempatan default + target kota default untuk iklan baru.
6. Teks By Saudia + Direct Flight; ice breaker Ramadhan untuk iklan Ramadhan.
7. Maks 5 iklan/ad set (aturan user) — Blueprint menyarankan 3.
8. Kill: ≥ Rp35rb & 0 chat; CPR > Rp50rb kecuali ≥5 chat (aturan user).
9. Kill override: CPR > Rp73,8rb.
10. Jangan pause/hapus iklan ≥5 chat & CPR ≤ Rp39,3rb.
11. Jangan scale sebelum ≥5 chat.
12. Jangan scale ad set dengan frequency > 2,0.
13. 1 perubahan signifikan per objek per hari.
14. Paket LAT tidak dibuat.
15. Paket Riyadh Air/November tidak dibuat (aturan user).
16. Gambar unik antar ad set dalam satu campaign.
17. Ad set < Rp250rb lifetime belum divonis.
18. Semua perubahan budget dicatat dengan CPR sebelum/sesudah.
19. Target CPR per paket (9H Rp41rb, R Rp42rb, Des Rp44,6rb, 12H Rp47rb).
20. Eksekusi apa pun ke Meta hanya setelah konfirmasi user.

**20 formula winner** — 02 B12 (10) + 04 B19 scaling (10).
**20 formula loser** — 02 B12 losing (10) + 04 B19 refresh/kill (10).

**10 risiko terbesar (mitigasi)**
1. Tidak ada data closing → CPR murah ≠ jamaah. *Mitigasi:* CS catat sumber iklan/akun tiap DP.
2. CPR naik Mar→Okt (Rp23rb→Rp48rb). *Mitigasi:* kurangi volume iklan baru, lindungi winner.
3. 9 akun bersaing di audiens sama. *Mitigasi:* bagi paket/kota per akun (uji).
4. Winner ikut di-pause (Allif, Fikri, Nida 7 hari terakhir). *Mitigasi:* aturan 10.
5. Kill Rp35rb terlalu cepat. *Mitigasi:* uji Rp50rb di 2 akun.
6. Rp151,9 jt Nida di objective non-chat. *Mitigasi:* aturan 3.
7. Learning terganggu oleh edit massal target. *Mitigasi:* edit sebelum publish, bukan setelah.
8. Ketergantungan IG Feed (spend terbesar, CPR Rp45rb). *Mitigasi:* pastikan WA Status/Reels dapat porsi.
9. Data scaling nol. *Mitigasi:* aturan 18.
10. Ramadhan tidak konsisten antar akun. *Mitigasi:* budget Ramadhan dulu di Allif & Diana.

**10 peluang terbesar (cara eksploitasi)**
1. Post winner lintas akun (object_story_id) — CPR Rp33,7rb.
2. WA Status (Rp26,6rb) & FB Reels/Stories (Rp29–34rb).
3. Akun Fifi & Diana (CPR Rp34–37rb) sebagai akun scale utama.
4. Paket 9 Hari sebagai produk volume (3.387 chat, Rp41rb).
5. Ramadhan di Allif (Rp34,3rb) & Diana (Rp27,2rb).
6. Laki-laki 25–34 (Rp35,4rb) — jangan dikecualikan.
7. Kota CPM rendah (Jateng/Jatim).
8. Mengurangi iklan baru → anggaran ke winner (70% chat dari 5,7% iklan).
9. Tagging hook/angle → data creative bulan depan.
10. Data closing CS → Blueprint v2 bisa menghitung biaya per jamaah.

**10 prioritas utama untuk scale (urut dampak)**
1. Lindungi & aktifkan kembali ad set winner yang di-pause (minta keputusan user).
2. Matikan objective non-WA.
3. Budget ke Fifi & Diana.
4. Post winner dipakai ulang di akun lain.
5. Paket 9 Hari budget terbesar.
6. Maks 3 iklan per ad set, iklan baru di ad set baru.
7. Uji ambang kill Rp50rb.
8. Uji +20%/3 hari di Fifi.
9. Bagi kota/paket antar akun.
10. Tracking closing per iklan.
