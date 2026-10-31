"""Enrichment layer: adds intro / steps / bit-visuals / trace tables to pages
without touching the code examples. build.py merges ENR into lib.pages by page id."""
ENR = {}


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


def merge(pages):
    miss = []
    for p in pages:
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
    unknown = set(ENR) - {p["id"] for p in pages}
    if unknown:
        raise SystemExit("UNKNOWN IDS: %s" % unknown)
