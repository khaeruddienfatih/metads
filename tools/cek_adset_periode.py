#!/usr/bin/env python3
# Tarik spend & chat semua ad set ACTIVE (13 akun, tanpa Haji 2) untuk last_3d/7d/30d lewat Graph API bot (telegram/.env).
# Pemakaian: python3 tools/cek_adset_periode.py /tmp/adset.json  (5 Nov 2026, user: "coba juga kamu cek per 7 hari dan 30 hari")
import sys, json
sys.path.insert(0, "/home/khaeruddien/metaads/telegram")
import auto_rules as ar
out = {}
for nama, akun in ar.AKUN.items():
    if nama == "Haji 2":
        continue
    for preset in ("today", "last_3d", "last_7d", "last_30d"):
        rows = ar.semua(f"act_{akun}/insights", {
            "level": "adset", "date_preset": preset, "limit": 500,
            "fields": "adset_id,adset_name,campaign_name,spend,actions",
            "filtering": json.dumps([{"field": "adset.effective_status", "operator": "IN", "value": ["ACTIVE"]}])})
        for r in rows:
            chat = sum(int(float(a["value"])) for a in r.get("actions", []) if a["action_type"] == ar.CHAT)
            k = r["adset_id"]
            o = out.setdefault(k, {"akun": nama, "campaign": r["campaign_name"], "adset": r["adset_name"]})
            o[preset] = (round(float(r.get("spend", 0))), chat)
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False)
print(len(out), "ad set aktif")
