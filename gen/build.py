import json, lib, p_stl1, p_stl2, p_stl3, p_bits, p_nt, p_rec, p_graph
import enrich_lib, e_bits, e_nt1, e_nt2, e_rec, e_graph1, e_graph2

lib.run_all()
enrich_lib.merge(lib.pages)

# sanity: every table row must match its column count; every bits/nt page must be enriched
bad = []
for p in lib.pages:
    if p["grp"] in ("bits", "nt", "rec", "graph") and "intro" not in p:
        bad.append(("NOT ENRICHED", p["id"]))
    tabs = ([p["truth"]] if p.get("truth") else [])
    for e in p["examples"]:
        tabs += e.get("tables", [])
        for g in e.get("viz", []):
            if g["kind"] == "bits":
                for r in g["rows"]:
                    assert all(len(r["bits"]) == len(x["bits"]) for x in g["rows"]), (p["id"], "bit width mismatch")
    for t in tabs:
        for r in t["rows"]:
            if len(r) != len(t["cols"]):
                bad.append(("COL MISMATCH", p["id"], t["caption"], len(r), len(t["cols"])))
if bad:
    raise SystemExit(bad)

json.dump(lib.pages, open("../src/data/pages.json", "w", encoding="utf-8"), ensure_ascii=False)
print(len(lib.pages), "pages")
for p in lib.pages:
    for i, e in enumerate(p["examples"]):
        if e["output"] in ("", "(compile error)"): print("EMPTY/ERR", p["id"], i)
