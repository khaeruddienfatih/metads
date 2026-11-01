# Pindah ke akun Claude baru (Max, email beda)

Disiapkan 1 Nov 2026 atas permintaan user ("ya siapkan semua saya mau pakai akun max beda email").
Semua aturan/status/log ada di repo ini — akun baru cukup membuka repo ini. Yang TIDAK ikut pindah: connector, routine cloud, akses GitHub.

## Langkah di akun baru

1. Login Claude akun baru (Max) di Claude Code: `/login` di terminal (atau `claude logout` lalu `claude`).
2. Sambungkan connector di https://claude.ai/customize/connectors:
   - **Meta Ads** — login Facebook yang SAMA (yang punya akses ke 15 akun iklan). Wajib.
   - **Gmail** — untuk email laporan pagi (email terkirim dari akun Gmail yang disambungkan).
   - Opsional: Canva, Cloudinary (cloud `q2xuhm0o`), Google Drive, Google Sheets.
3. Hubungkan GitHub di akun baru (claude.ai/code → GitHub / pasang Claude GitHub App) memakai akun GitHub
   **elharamainwisata** dengan akses ke repo **`elharamainwisata/metads`** — mulai akun baru ini repo UTAMA
   (perintah user 1 Nov: "github yang tersambung adalah elharamainwisata"). `khaeruddienfatih/metads` jadi cadangan.
4. Buka folder `Desktop/metaads` di Claude Code akun baru, lalu ketik:
   **"buat ulang 6 routine dari memory/pindah-akun.md"** — Claude membuat routine dengan isi di bawah (model Sonnet,
   repo **`https://github.com/elharamainwisata/metads`**, environment Default akun baru, connector sesuai tabel).
5. Cek di https://claude.ai/code/routines akun baru: 6 routine aktif.
6. **Setelah itu matikan routine di akun LAMA** (https://claude.ai/code/routines, login akun lama) — kalau dua-duanya jalan,
   semua cek jalan dobel (pause/nyala dua kali, email terkirim dua kali).
7. Ganti repo utama di Mac (SETELAH routine akun lama dimatikan, supaya tidak ada push dari dua arah):
   ```
   git remote set-url origin https://github.com/elharamainwisata/metads.git
   git remote set-url --add --push origin https://github.com/khaeruddienfatih/metads.git
   git pull origin main && git push origin main
   ```
   (`git push origin main` lalu tetap push ke dua repo: elharamainwisata utama + khaeruddienfatih cadangan.)
   Perbarui juga CLAUDE.md langkah 3: repo utama elharamainwisata, cadangan khaeruddienfatih.
8. Di akun baru, catat ID routine baru di `memory/chat-memory.md` (ganti ID lama `trig_…`).

## Status 1 Nov 2026 — routine SUDAH dibuat ulang di akun baru

Repo routine: `https://github.com/khaeruddienfatih/metads` (akun baru belum punya akses GitHub ke `elharamainwisata/metads` → 403 repo_access_denied; GitHub App terpasang di khaeruddienfatih). Push cadangan di prompt tetap ke elharamainwisata (gagal diabaikan).

| # | ID baru |
|---|---|
| 1 (:13) | `trig_01PExMLpwLUtZxVRsi4R6e8H` |
| 2 (:43) | `trig_013WfwoGnfBo14J4EupZGgtx` |
| 3 (22:00 OFF) | `trig_01FPcdHh57QKkum5LoEAwj2k` |
| 4 (04:00 naik+ON) | `trig_01KLe5sJc8N6MQMEYKUpzNqB` |
| 5 (email 06:00) | `trig_01Ci9E1ffEGZ97CAaxiyqCBY` |
| 6 (email 08:00) | `trig_01NydaDZaZmHdb68jLxpn13R` |

Sisa: matikan 6 routine di akun LAMA (langkah 6). Langkah 7 (ganti remote Mac) ditunda — repo utama tetap khaeruddienfatih selama akun baru belum punya akses elharamainwisata.

## Ringkasan 6 routine aktif (akun lama)

| # | Nama | Jadwal | Connector | Tools | ID lama |
|---|---|---|---|---|---|
| 1 | Auto ad set & iklan (menit :13): nyala ulang rule-off, pause boros, pause iklan mahal | tiap jam menit :13 (cron UTC `13 * * * *`) | Meta-Ads | Bash, Read, Write, Edit, Glob, Grep, ToolSearch | `trig_012Qu1YrebVhGGQCXMKv23y5` |
| 2 | Auto ad set & iklan (menit :43): nyala ulang rule-off, pause boros, pause iklan mahal | tiap jam menit :43 (cron UTC `43 * * * *`) | Meta-Ads | Bash, Read, Write, Edit, Glob, Grep, ToolSearch | `trig_01GUvNdBksYcSF5CP1aZarPU` |
| 3 | Jadwal malam: ad set OFF 22:00 WIB | 22:00 WIB (cron UTC `0 15 * * *`) | Meta-Ads | Bash, Read, Write, Edit, Glob, Grep, ToolSearch | `trig_01Tv4htgnxAiipP6ic38dc6X` |
| 4 | Jadwal pagi 04:00 WIB: naik anggaran +10% lalu ad set ON | 04:00 WIB (cron UTC `0 21 * * *`) | Meta-Ads | Bash, Read, Write, Edit, Glob, Grep, ToolSearch | `trig_01ASjPaNeoNDjpJZaALrzVzy` |
| 5 | Email pagi 06:00: chat Umroh & Haji kemarin (khaeruddien) | 06:00 WIB (cron UTC `0 23 * * *`) | Meta-Ads, Gmail | Bash, Read, Glob, Grep, ToolSearch | `trig_015kQ7xrGRj9ZWeKRnha6ia4` |
| 6 | Email pagi 08:00: chat Umroh & Haji kemarin (dhiyaaelhaq01) | 08:00 WIB (cron UTC `0 1 * * *`) | Meta-Ads, Gmail | Bash, Read, Glob, Grep, ToolSearch | `trig_017i6fP6AFjxsRDgiXSPN4nq` |

Routine lama yang sudah NONAKTIF (tidak perlu dibuat ulang): naik anggaran 07:00 `trig_01XvAgB4noayYxfMXZgoiruc`, routine sekali-jalan (cek kampanye/penawaran batch), dan "Meta Ads Auto-Rule - Reset Budget Batch1".

## Isi prompt tiap routine (salin persis)

Saat membuat ulang: di setiap prompt yang menyuruh push cadangan, ganti
`git push https://github.com/elharamainwisata/metads.git main` menjadi
`git push https://github.com/khaeruddienfatih/metads.git main` (karena `origin` di cloud sudah elharamainwisata).
Kalau akun baru tidak punya akses ke khaeruddienfatih, baris itu gagal dan diabaikan — tidak masalah.

### 1. Auto ad set & iklan (menit :13): nyala ulang rule-off, pause boros, pause iklan mahal

- Jadwal: tiap jam menit :13 (cron UTC `13 * * * *`)
- Connector: Meta-Ads
- Model: claude-sonnet-5-5

````text
Scheduled run (every 30 minutes via two routines at :13 and :43) of the user's explicit standing orders: (A, 30 Oct) "aktipan adset ... yang cpr di bawah 30rb dan terkena off oleh auto rules saya" (+ 3-day CPR condition); (B, 30 Oct) "matikan adset yang habis 25ribu tapi tidak ada chat" (threshold later 30ribu) + (B2, 1 Nov) "matikan adset harian jika belanja di atas 40rb dan cpr di bawah 2"; (C, 1 Nov) "matikan iklan jika iklan sudah running sepanjang waktu dan cpr di atas 50rb"; "di cek 30 menit".

You manage Meta Ads for Elharamain Wisata (Umroh/Haji WhatsApp-chat ads). Work on branch main only.

0. NIGHT WINDOW: check `TZ=Asia/Jakarta date +%H`. If the hour is 22, 23, 00, 01, 02 or 03, do NOTHING (no Meta calls, no log, no commit) and finish with "Jendela malam — dilewati".

1. Today in WIB: `TZ=Asia/Jakarta date +%Y-%m-%d`, start 00:00 +07:00.
2. Read memory/auto-reaktivasi.md and follow it EXACTLY (parts A, B, C) for all 14 accounts listed there. Chats = WhatsApp messaging conversations started (missing/"Not available" = 0).

PART A — reactivate ad sets turned off by the user's auto rules today (activity log event_category status, start_time today 00:00+07:00, limit 200; entries "Ad set status updated" with "rule_info" in extra_data and new_value "Inactive"). Reactivate only if ALL: currently not active; campaign ACTIVE; TODAY >=1 chat and spend/chat < Rp30.000; LAST 3 DAYS (date_preset last_3d) >=1 chat with spend/chat < Rp50.000, or spend < Rp35.000; reactivated by "ads MCP server" fewer than 2 times today. ads_activate_entity (object_ids [adset_id], publish_as_active true; if "no staged changes in the draft", retry entity_type ad_set + entity_id). Verify.

PART B — pause wasteful AD SETS today: ACTIVE ad sets (filter effective_status IN [ACTIVE], date_preset today) where (spend today >= Rp30.000 AND 0 chats) OR (spend today > Rp40.000 AND chats < 2). Exclude ad sets whose result is not WhatsApp chats (optimization_goal not CONVERSATIONS, e.g. Haji 4 pixel/add-to-cart). Do not touch an ad set Part A just reactivated. PAUSE via ads_update_entity (ad_account_id, entity_id, entity_type ad_set, fields {"status":"PAUSED"}). Verify.

PART C — pause expensive ADS (lifetime): ACTIVE ads (level ad, filter effective_status IN [ACTIVE], date_preset maximum, fields name, adset_name, campaign_name, amount_spent, results) where (chats >= 1 AND spend/chats > Rp50.000) OR (0 chats AND spend >= Rp35.000). Exclude non-chat results. PAUSE via ads_update_entity (entity_type ad, fields {"status":"PAUSED"}). Verify. Never delete.

Change NOTHING else (no budget, targeting, creatives).

3. Meta Ads tools come from the Meta-Ads connector (load with ToolSearch). Always send client_conversation_id "Hn4fT8qLz2WcP7xR1bVk", client_model "claude-sonnet-5-5", scheduled_task_run true. Verify field names with ads_get_field_context before ads_get_ad_entities. Paginate. Skip optional insight/benchmark next_actions.
4. Only if something changed: append ONE entry at the END of memory/chat-log.md: `### YYYY-MM-DD HH:MM — cek 30 menit (cloud)` with bullets for A (account, ad set ID, name, rule, chats/spend/CPR today and 3 days, verified status), B (account, ad set ID, name, campaign, spend & chats today, which condition, verified status) and C (account, ad ID, name, lifetime spend/chats/CPR, verified status). Then `git add memory/chat-log.md && git commit -m "Chat log: cek 30 menit — A:N nyala, B:M pause adset, C:K pause iklan (DD Mon)"`, `git pull --rebase origin main` (on conflict in chat-log.md keep both sides), `git push origin main`; then try `git push https://github.com/elharamainwisata/metads.git main` and ignore failure. If nothing changed, do not write or commit.
5. Never store tokens or credentials in files.

Final message (Indonesian, concise): A / B / C lists or "tidak ada"; errors verbatim.
````

### 2. Auto ad set & iklan (menit :43): nyala ulang rule-off, pause boros, pause iklan mahal

- Jadwal: tiap jam menit :43 (cron UTC `43 * * * *`)
- Connector: Meta-Ads
- Model: claude-sonnet-5-5

````text
Scheduled run (every 30 minutes via two routines at :13 and :43) of the user's explicit standing orders: (A, 30 Oct) "aktipan adset ... yang cpr di bawah 30rb dan terkena off oleh auto rules saya" (+ 3-day CPR condition); (B, 30 Oct) "matikan adset yang habis 25ribu tapi tidak ada chat" (threshold later 30ribu) + (B2, 1 Nov) "matikan adset harian jika belanja di atas 40rb dan cpr di bawah 2"; (C, 1 Nov) "matikan iklan jika iklan sudah running sepanjang waktu dan cpr di atas 50rb"; "di cek 30 menit".

You manage Meta Ads for Elharamain Wisata (Umroh/Haji WhatsApp-chat ads). Work on branch main only.

0. NIGHT WINDOW: check `TZ=Asia/Jakarta date +%H`. If the hour is 22, 23, 00, 01, 02 or 03, do NOTHING (no Meta calls, no log, no commit) and finish with "Jendela malam — dilewati".

1. Today in WIB: `TZ=Asia/Jakarta date +%Y-%m-%d`, start 00:00 +07:00.
2. Read memory/auto-reaktivasi.md and follow it EXACTLY (parts A, B, C) for all 14 accounts listed there. Chats = WhatsApp messaging conversations started (missing/"Not available" = 0).

PART A — reactivate ad sets turned off by the user's auto rules today (activity log event_category status, start_time today 00:00+07:00, limit 200; entries "Ad set status updated" with "rule_info" in extra_data and new_value "Inactive"). Reactivate only if ALL: currently not active; campaign ACTIVE; TODAY >=1 chat and spend/chat < Rp30.000; LAST 3 DAYS (date_preset last_3d) >=1 chat with spend/chat < Rp50.000, or spend < Rp35.000; reactivated by "ads MCP server" fewer than 2 times today. ads_activate_entity (object_ids [adset_id], publish_as_active true; if "no staged changes in the draft", retry entity_type ad_set + entity_id). Verify.

PART B — pause wasteful AD SETS today: ACTIVE ad sets (filter effective_status IN [ACTIVE], date_preset today) where (spend today >= Rp30.000 AND 0 chats) OR (spend today > Rp40.000 AND chats < 2). Exclude ad sets whose result is not WhatsApp chats (optimization_goal not CONVERSATIONS, e.g. Haji 4 pixel/add-to-cart). Do not touch an ad set Part A just reactivated. PAUSE via ads_update_entity (ad_account_id, entity_id, entity_type ad_set, fields {"status":"PAUSED"}). Verify.

PART C — pause expensive ADS (lifetime): ACTIVE ads (level ad, filter effective_status IN [ACTIVE], date_preset maximum, fields name, adset_name, campaign_name, amount_spent, results) where (chats >= 1 AND spend/chats > Rp50.000) OR (0 chats AND spend >= Rp35.000). Exclude non-chat results. PAUSE via ads_update_entity (entity_type ad, fields {"status":"PAUSED"}). Verify. Never delete.

Change NOTHING else (no budget, targeting, creatives).

3. Meta Ads tools come from the Meta-Ads connector (load with ToolSearch). Always send client_conversation_id "Hn4fT8qLz2WcP7xR1bVk", client_model "claude-sonnet-5-5", scheduled_task_run true. Verify field names with ads_get_field_context before ads_get_ad_entities. Paginate. Skip optional insight/benchmark next_actions.
4. Only if something changed: append ONE entry at the END of memory/chat-log.md: `### YYYY-MM-DD HH:MM — cek 30 menit (cloud)` with bullets for A (account, ad set ID, name, rule, chats/spend/CPR today and 3 days, verified status), B (account, ad set ID, name, campaign, spend & chats today, which condition, verified status) and C (account, ad ID, name, lifetime spend/chats/CPR, verified status). Then `git add memory/chat-log.md && git commit -m "Chat log: cek 30 menit — A:N nyala, B:M pause adset, C:K pause iklan (DD Mon)"`, `git pull --rebase origin main` (on conflict in chat-log.md keep both sides), `git push origin main`; then try `git push https://github.com/elharamainwisata/metads.git main` and ignore failure. If nothing changed, do not write or commit.
5. Never store tokens or credentials in files.

Final message (Indonesian, concise): A / B / C lists or "tidak ada"; errors verbatim.
````

### 3. Jadwal malam: ad set OFF 22:00 WIB

- Jadwal: 22:00 WIB (cron UTC `0 15 * * *`)
- Connector: Meta-Ads
- Model: claude-sonnet-5-5

````text
Scheduled nightly run of the user's explicit standing order (31 Oct 2026): "saya mau setiap jam 11 malam adset off semua dan jam 4 pagi adset on", corrected the same day to "matikan di jam 10 malam". This run = the 22:00 WIB OFF step.

You manage Meta Ads for Elharamain Wisata. Work on branch main only.

1. Date in WIB: `TZ=Asia/Jakarta date +%Y-%m-%d`.
2. Read memory/jadwal-malam.md and follow section "OFF — jam 22:00 WIB" EXACTLY for all 14 accounts listed there:
   - list every ad set with effective_status ACTIVE (all pages) per account;
   - FIRST overwrite memory/jadwal-malam-daftar.md with header `# Daftar ad set dimatikan jadwal malam — YYYY-MM-DD 22:00 WIB` and one line per ad set `- <ad_account_id> | <adset_id> | <ad set name> | <campaign_name>`; commit and push it immediately (so the 04:00 run can find it even if this run is cut short);
   - then PAUSE each with ads_update_entity (ad_account_id, entity_id = ad set id, fields {"status":"PAUSED"}); status only — never touch campaigns, budgets, targeting, ads;
   - verify per account; mark failures in the list as ` | GAGAL: <error>`.
   Accounts that error / can't be read: note and continue.
3. Meta Ads tools come from the Meta-Ads connector (load with ToolSearch). Always send client_conversation_id "Hn4fT8qLz2WcP7xR1bVk", client_model "claude-sonnet-5-5", scheduled_task_run true. Verify field names with ads_get_field_context before ads_get_ad_entities. Skip optional insight/benchmark next_actions.
4. Append ONE entry at the END of memory/chat-log.md: `### YYYY-MM-DD 22:00 — jadwal malam OFF (cloud)` with per-account counts paused / failed and unreadable accounts. Commit (`Chat log: jadwal malam OFF — N ad set (DD Okt)`), `git pull --rebase origin main` (on conflict in chat-log.md keep both sides), `git push origin main`. Then also try `git push https://github.com/elharamainwisata/metads.git main` — if it fails (no access), ignore.
5. Never store tokens or credentials in files.

Final message (Indonesian, concise): jumlah ad set di-OFF per akun, gagal, akun tak terbaca, errors verbatim.
````

### 4. Jadwal pagi 04:00 WIB: naik anggaran +10% lalu ad set ON

- Jadwal: 04:00 WIB (cron UTC `0 21 * * *`)
- Connector: Meta-Ads
- Model: claude-sonnet-5-5

````text
Scheduled 04:00 WIB run of the user's explicit standing orders (31 Oct 2026):
(1) "jika setiap hari dalam 3 hari cpr bagus di bawah 30rb kamu naikan anggaran kampanyenya 10%" + "batas maksimal budget 300rb perkampanye naik anggaran di jam 04 pagi" — this explicitly authorizes budget increases on running campaigns/ad sets (overrides the older "don't change running ad sets" rule for this increase only). EXCEPTION (1 Nov 2026): "khusus akun alif di larang meniakan anggaran walaupun ada pemenang" — NEVER increase any budget in Allif 4678183395742010.
(2) "saya mau setiap jam 11 malam adset off semua dan jam 4 pagi adset on" (OFF later moved to 22:00).
Do PART 1 completely, THEN PART 2. You manage Meta Ads for Elharamain Wisata. Work on branch main only.

Dates in WIB: today = `TZ=Asia/Jakarta date +%Y-%m-%d`; H-1 = `TZ=Asia/Jakarta date -d yesterday +%Y-%m-%d`; H-2 = `TZ=Asia/Jakarta date -d '2 days ago' +%Y-%m-%d`; H-3 = `TZ=Asia/Jakarta date -d '3 days ago' +%Y-%m-%d`.

PART 1 — NAIK ANGGARAN. Read memory/naik-budget.md and follow it EXACTLY for the 13 accounts listed there (Allif excluded):
   - Campaigns with status ACTIVE (ad sets are paused overnight by design — that is normal), level campaign, time_range {since: H-3, until: H-1}, time_increment "1", fields name, amount_spent, results, daily_budget, lifetime_budget, status, effective_status (paginate).
   - Qualify only if result is WhatsApp chats (messaging conversation started; missing/"Not available" = 0) AND on EACH of the 3 days: chats >= 1 and spend/chats < Rp30.000.
   - Cooldown: skip if memory/naik-budget-log.md shows this campaign increased on a date >= H-2.
   - CAP Rp300.000/day per campaign: CBO new = min(ceil(old*1.10 to Rp1.000), 300000); ABO: increase daily_budget of the campaign's ad sets that are in memory/jadwal-malam-daftar.md (were ACTIVE before 22:00) by the same factor so the campaign total <= Rp300.000. Already >= Rp300.000 -> do not change (never decrease). Lifetime budgets: do not change.
   - ads_update_entity (ad_account_id, entity_id, fields {"daily_budget": new}) in the same units as the daily_budget you read. Then READ BACK daily_budget with ads_get_ad_entities and only log the increase if the read-back value equals the new value; if not, report it as failed (do not log it as done). If the CAMPAIGN became PAUSED, re-activate the campaign (ads_activate_entity object_ids [campaign_id], publish_as_active true; if "no staged changes in the draft", retry entity_type campaign + entity_id). If the value did not change (draft-mode account), publish with ads_activate_entity object_ids [id], publish_as_active true — but never activate ad sets in PART 1. Budget only.
   - Log each VERIFIED increase as a line in memory/naik-budget-log.md.

PART 2 — AD SET ON. Read memory/jadwal-malam.md section "ON — jam 04:00 WIB" and follow it EXACTLY:
   - read memory/jadwal-malam-daftar.md; use it ONLY if its header date = H-1 (WIB). Otherwise activate nothing and report.
   - turn ON ONLY the ad sets in that list (skip lines marked GAGAL). Never activate any other ad set, campaign or ad.
   - per ad set: activate only if it is currently PAUSED and its campaign is ACTIVE.
   - ads_activate_entity (object_ids [adset_id], publish_as_active true); if rejected with "no staged changes in the draft", retry with entity_type ad_set + entity_id. Verify.
   - append to memory/jadwal-malam-daftar.md: `## Dinyalakan YYYY-MM-DD 04:00` + counts on / skipped (reason) / failed.

Meta Ads tools come from the Meta-Ads connector (load with ToolSearch). Always send client_conversation_id "Hn4fT8qLz2WcP7xR1bVk", client_model "claude-sonnet-5-5", scheduled_task_run true. Verify field names with ads_get_field_context before ads_get_ad_entities. Skip optional insight/benchmark next_actions.

LOG: append ONE entry at the END of memory/chat-log.md: `### YYYY-MM-DD 04:00 — jadwal pagi: naik anggaran + ON (cloud)` with PART 1 (each verified increase: account, campaign ID, name, CBO/ABO, old -> new, CPR per day; failed increases; campaigns at the cap) and PART 2 (per-account counts on / skipped / failed). Commit (`Jadwal pagi: naik N campaign, ON M ad set (DD Mon)`), `git pull --rebase origin main` (on conflict keep both sides), `git push origin main`; then try `git push https://github.com/elharamainwisata/metads.git main` and ignore failure. Never store tokens or credentials in files.

Final message (Indonesian, concise): campaigns increased (old -> new) or "tidak ada"; ad sets turned on per account; skipped/failed; errors verbatim.
````

### 5. Email pagi 06:00: chat Umroh & Haji kemarin (khaeruddien)

- Jadwal: 06:00 WIB (cron UTC `0 23 * * *`)
- Connector: Meta-Ads, Gmail
- Model: claude-sonnet-5-5

````text
Scheduled daily morning report. User's explicit standing order (30 Oct 2026): "setiap pagi kamu kirim ke email saya khaeruddien@gmail.com brp chat umroh dan haji per harinya" + "dan biaya yang dikeluarkan" + "kirim dalam bentuk table ya".

READ-ONLY on Meta Ads: never change any campaign, ad set, ad, or budget. Do not commit anything to git.

1. Dates in WIB: yesterday = `TZ=Asia/Jakarta date -d yesterday +%Y-%m-%d`, day before = `TZ=Asia/Jakarta date -d '2 days ago' +%Y-%m-%d`.
2. Meta Ads tools come from the Meta-Ads connector (load with ToolSearch, e.g. "ads_get_ad_entities ads_get_field_context"). Always send client_conversation_id "Hn4fT8qLz2WcP7xR1bVk", client_model "claude-sonnet-5-5", scheduled_task_run true. Verify field names with ads_get_field_context first. Skip optional insight/benchmark next_actions.
3. Accounts:
   UMROH: Diana 1076195694707828, Tira 868364731529534, Nida 1019832712800468, Hanif 482252744648260, Allif 4678183395742010, Fikri 1676215979752437, AIni 814396810761205, Irfan 1060984719243481, Fifi 521083143750270.
   HAJI: Elharamain Haji 947788760498911, Haji 2 1032468828178224, Haji 3 794403715776985, Haji 4 1526562231314028, haji 1050343302646341.
   NOTE: Elharamain Haji 947788760498911 also contains an Umroh campaign named "Yoga" — count campaigns whose name contains "Yoga" as UMROH, the rest of that account as HAJI.
4. For each account, at campaign level (ALL campaigns with spend > 0, no minimum filter; paginate if needed), time_range yesterday and separately the day before: fields name, amount_spent, results, cost_per_result. Chats = WhatsApp messaging conversations started (missing/"Not available" = 0). Campaigns whose result is not WhatsApp chats (e.g. Haji 4 pixel/add-to-cart) are excluded from chat counts and CPR, but their spend IS included in total spend and listed separately as "biaya non-chat". If an account errors (billing, access), note it and continue.
5. Compute per account: chats, spend (biaya), CPR (chat spend / chats). Totals for UMROH and HAJI and grand total (chats, spend, CPR), plus change vs the day before (chats, spend, CPR).
6. Send ONE email with the Gmail connector (load its send tool via ToolSearch, e.g. "gmail send_message") to khaeruddien@gmail.com. The body MUST be TABLES:
   Subject: `Laporan chat WA <DD Mon YYYY> — Umroh <N> chat Rp<X> | Haji <M> chat Rp<Y>`
   - Table 1 "Ringkasan": rows Umroh, Haji, Total; columns Chat | Biaya | CPR | Chat kemarin lusa | Biaya kemarin lusa | Perubahan chat.
   - Table 2 "Umroh per akun": columns Akun | Chat | Biaya | CPR, sorted by chat desc, with a total row.
   - Table 3 "Haji per akun": same columns, sorted by chat desc, with a total row.
   - Below the tables, one short line of notes (biaya non-chat, account errors).
   Prefer an HTML email: check the send tool's schema for an HTML body / content-type / mimeType option and use real <table> elements with border-collapse, 1px borders, cell padding 4-6px, right-aligned numbers, bold total rows. If the tool only supports plain text, use aligned monospace text tables (pipe-separated, fixed-width columns). Indonesian labels. Format rupiah like Rp1.234.567 and CPR like Rp28,4rb. Only this recipient; no attachments.
7. Final message: confirm the email was sent (recipient, subject, HTML or plain) and the headline numbers, or the exact error.
````

### 6. Email pagi 08:00: chat Umroh & Haji kemarin (dhiyaaelhaq01)

- Jadwal: 08:00 WIB (cron UTC `0 1 * * *`)
- Connector: Meta-Ads, Gmail
- Model: claude-sonnet-5-5

````text
Scheduled daily morning report (08:00 WIB). User's explicit standing order (30 Oct 2026): "setiap pagi kamu kirim ke email saya ... brp chat umroh dan haji per harinya" + "dan biaya yang dikeluarkan" + "kirim dalam bentuk table ya"; extended 31 Oct 2026: "kirim juga ke dhiyaaelhaq01@gmail.com jam 8 pagi".

READ-ONLY on Meta Ads: never change any campaign, ad set, ad, or budget. Do not commit anything to git.

1. Dates in WIB: yesterday = `TZ=Asia/Jakarta date -d yesterday +%Y-%m-%d`, day before = `TZ=Asia/Jakarta date -d '2 days ago' +%Y-%m-%d`.
2. Meta Ads tools come from the Meta-Ads connector (load with ToolSearch, e.g. "ads_get_ad_entities ads_get_field_context"). Always send client_conversation_id "Hn4fT8qLz2WcP7xR1bVk", client_model "claude-sonnet-5-5", scheduled_task_run true. Verify field names with ads_get_field_context first. Skip optional insight/benchmark next_actions.
3. Accounts:
   UMROH: Diana 1076195694707828, Tira 868364731529534, Nida 1019832712800468, Hanif 482252744648260, Allif 4678183395742010, Fikri 1676215979752437, AIni 814396810761205, Irfan 1060984719243481, Fifi 521083143750270.
   HAJI: Elharamain Haji 947788760498911, Haji 2 1032468828178224, Haji 3 794403715776985, Haji 4 1526562231314028, haji 1050343302646341.
   NOTE: Elharamain Haji 947788760498911 also contains an Umroh campaign named "Yoga" — count campaigns whose name contains "Yoga" as UMROH, the rest of that account as HAJI.
4. For each account, at campaign level (ALL campaigns with spend > 0, no minimum filter; paginate if needed), time_range yesterday and separately the day before: fields name, amount_spent, results, cost_per_result. Chats = WhatsApp messaging conversations started (missing/"Not available" = 0). Campaigns whose result is not WhatsApp chats (e.g. Haji 4 pixel/add-to-cart) are excluded from chat counts and CPR, but their spend IS included in total spend and listed separately as "biaya non-chat". If an account errors (billing, access), note it and continue.
5. Compute per account: chats, spend (biaya), CPR (chat spend / chats). Totals for UMROH and HAJI and grand total (chats, spend, CPR), plus change vs the day before (chats, spend, CPR).
6. Send ONE email with the Gmail connector (load its send tool via ToolSearch, e.g. "gmail send_message") to dhiyaaelhaq01@gmail.com ONLY. The body MUST be TABLES:
   Subject: `Laporan chat WA <DD Mon YYYY> — Umroh <N> chat Rp<X> | Haji <M> chat Rp<Y>`
   - Table 1 "Ringkasan": rows Umroh, Haji, Total; columns Chat | Biaya | CPR | Chat kemarin lusa | Biaya kemarin lusa | Perubahan chat.
   - Table 2 "Umroh per akun": columns Akun | Chat | Biaya | CPR, sorted by chat desc, with a total row.
   - Table 3 "Haji per akun": same columns, sorted by chat desc, with a total row.
   - Below the tables, one short line of notes (biaya non-chat, account errors).
   Use the send tool's htmlBody with real <table> elements (border-collapse, 1px borders, cell padding 4-6px, right-aligned numbers, bold total rows); if HTML is unavailable, use aligned monospace text tables. Indonesian labels. Format rupiah like Rp1.234.567 and CPR like Rp28,4rb. Only this recipient; no attachments.
7. Final message: confirm the email was sent (recipient, subject, HTML or plain) and the headline numbers, or the exact error.
````
