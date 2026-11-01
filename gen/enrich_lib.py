"""Enrichment layer: adds intro / steps / bit-visuals / trace tables to pages
without touching the code examples. build.py merges ENR into lib.pages by page id."""
ENR = {}
BLOG = {}


def bs(n, w=8):
    """n কে w-ঘরের বাইনারি স্ট্রিং বানায় (negative হলে two's complement)"""
    return format(n & ((1 << w) - 1), "0{}b".format(w))


def R(label, bits, dec=None, tone="n", hl=(), sep=False):
    """একটা বিট-সারি। tone: a / b / r / n (রঙ), hl: highlight করা ঘরের index (বাম থেকে ০)"""
    return dict(label=label, bits=bits, dec=dec, tone=tone, hl=list(hl), sep=sep)


def RB(label, n, w=8, tone="n", hl=(), dec=None, sep=False):
    return R(label, bs(n, w), n if dec is None else dec, tone, hl, sep)


def hlv(w, *values):
    """যেসব place-value (যেমন 8, 4) এর ঘর highlight করতে চাই তাদের index"""
    return [w - 1 - (v.bit_length() - 1) for v in values]


def VB(caption, *rows):
    return dict(kind="bits", caption=caption, rows=list(rows))


def VG(caption, cells):
    """cells: [(লেখা, state)]  state: p=prime/ok, x=কাটা, n=সাধারণ, h=highlight"""
    return dict(kind="grid", caption=caption, cells=[dict(t=str(t), s=s) for t, s in cells])


def T(cols, rows, caption=None, hl=(), sums=False):
    return dict(caption=caption, cols=[str(c) for c in cols],
                rows=[[str(c) for c in r] for r in rows], hl=list(hl))


def X(steps, viz=None, tables=None):
    return dict(steps=steps, viz=viz or [], tables=tables or [])


def EN(pid, intro, uses, tips, *ex, truth=None):
    ENR[pid] = dict(intro=intro, uses=uses, tips=tips, truth=truth, ex=list(ex))


def S(h, p=None, ul=None, table=None):
    """ব্লগের একটা অংশ: h = শিরোনাম, p = অনুচ্ছেদের তালিকা, ul = বুলেট তালিকা, table = T(...)"""
    return dict(h=h, p=p or [], ul=ul or [], table=table)


def BL(pid, *sections):
    """পেজের জন্য ব্লগ (গল্প + real life উদাহরণ)। LessonPage এ 'ব্লগ' কার্ড হয়ে দেখায়"""
    BLOG[pid] = list(sections)


def merge(pages):
    miss = []
    for p in pages:
        if p["id"] in BLOG:
            p["blog"] = BLOG[p["id"]]
        e = ENR.get(p["id"])
        if not e:
            continue
        if len(e["ex"]) != len(p["examples"]):
            miss.append((p["id"], len(e["ex"]), len(p["examples"])))
            continue
        for k in ("intro", "uses", "tips", "truth"):
            p[k] = e[k]
        for ex, x in zip(p["examples"], e["ex"]):
            ex["steps"], ex["viz"], ex["tables"] = x["steps"], x["viz"], x["tables"]
    if miss:
        raise SystemExit("EXAMPLE COUNT MISMATCH: %s" % miss)
    unknown = (set(ENR) | set(BLOG)) - {p["id"] for p in pages}
    if unknown:
        raise SystemExit("UNKNOWN IDS: %s" % unknown)


# ───────────── গ্রাফ / গ্রিডের ছবি ─────────────
def GV(caption, nodes, edges, w=460, h=205, note=None, r=20):
    """গ্রাফের ছবি। nodes: (id, x, y, state='n', label=None, sub=None) | edges: (a, b, state='n', weight=None, directed=False)
    node state: n সাধারণ, a এখনকার, v শেষ, q অপেক্ষায়, x বাদ, r ২ নম্বর রঙ | edge state: n, t নেওয়া, x বাদ, a এখনকার"""
    ns = []
    for t in nodes:
        t = list(t) + [None] * (6 - len(t))
        ns.append(dict(id=t[0], x=t[1], y=t[2], s=t[3] or "n", t=t[4], sub=t[5]))
    es = []
    for t in edges:
        t = list(t) + [None] * (5 - len(t))
        es.append(dict(a=t[0], b=t[1], s=t[2] or "n", w=t[3], d=bool(t[4])))
    return dict(kind="graph", caption=caption, nodes=ns, edges=es, w=w, h=h, r=r, note=note)


def MV(caption, rows, cols=None, rowLabels=None, note=None, legend=None):
    """2D ঘরের ছবি। rows: [[(লেখা, state), ...], ...] | state: n z o w a s v p
    legend: [(state, লেখা), ...] দিলে ছবির নিচে সেই অর্থ দেখায় (না দিলে graph এর ডিফল্ট অর্থ)"""
    d = dict(kind="mat", caption=caption, cols=cols, rowLabels=rowLabels, note=note,
             rows=[[dict(t=str(t), s=s) for t, s in r] for r in rows])
    if legend:
        d["legend"] = [list(x) for x in legend]
    return d


# নমুনা গ্রাফ G1 (৬ node, ৭ edge) এর জায়গা
G1P = {1: (50, 100), 2: (160, 45), 3: (160, 155), 4: (290, 45), 5: (290, 155), 6: (410, 100)}
G1E = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (4, 6), (5, 6)]
G1A = {1: [2, 3], 2: [1, 4, 5], 3: [1, 5], 4: [2, 6], 5: [2, 3, 6], 6: [4, 5]}


def g1(caption, st=None, sub=None, es=None, note=None, label=None):
    st, sub, es, label = st or {}, sub or {}, es or {}, label or {}
    nodes = [(i, G1P[i][0], G1P[i][1], st.get(i, "n"), label.get(i), sub.get(i)) for i in G1P]
    edges = [(a, b, es.get((a, b), es.get((b, a), "n"))) for a, b in G1E]
    return GV(caption, nodes, edges, note=note)
