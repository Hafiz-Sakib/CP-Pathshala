"""গ্রাফ algorithm এর ছোট simulation — ধাপের টেবিল ও ছবির জন্য (আসল output এর সাথে মেলানো হয়)"""
import heapq, math


def adj_from(edges, n, w=False, directed=False):
    a = {i: [] for i in range(0, n + 1)}
    for e in edges:
        if w:
            u, v, c = e
            a[u].append((v, c))
            if not directed: a[v].append((u, c))
        else:
            u, v = e
            a[u].append(v)
            if not directed: a[v].append(u)
    return a


def bfs_trace(adj, src):
    vis, q, order, lvl, par = {src}, [src], [], {src: 0}, {src: None}
    rows, snaps = [["শুরু", "—", "—", "[%d]" % src, "—"]], []
    while q:
        u = q.pop(0)
        order.append(u)
        new = []
        for c in adj[u]:
            if c not in vis:
                vis.add(c); q.append(c); new.append(c); lvl[c] = lvl[u] + 1; par[c] = u
        rows.append([len(order), u, ", ".join(map(str, new)) or "—", "[" + " ".join(map(str, q)) + "]", " ".join(map(str, order))])
        snaps.append((u, list(q), list(order), dict(lvl)))
    return rows, order, lvl, par, snaps


def dfs_trace(adj, src):
    vis, order, stack, rows, tin, tout, par, back = set(), [], [], [], {}, {}, {}, []
    t = [0]

    def go(v, p):
        vis.add(v); order.append(v); stack.append(v); t[0] += 1; tin[v] = t[0]; par[v] = p
        rows.append(["IN %d" % v, "→".join(map(str, stack)), " ".join(map(str, order))])
        for c in adj[v]:
            if c not in vis:
                go(c, v)
            elif c != p and (c, v) not in back and (v, c) not in back:
                back.append((v, c))
        stack.pop(); t[0] += 1; tout[v] = t[0]
        rows.append(["OUT %d" % v, "→".join(map(str, stack)) or "(খালি)", " ".join(map(str, order))])
    go(src, None)
    return rows, order, tin, tout, par, back


def dijkstra(adj, n, src, inf=10 ** 7):
    dist = [inf] * (n + 1); dist[src] = 0; par = {src: None}
    st = {(0, src)}; vis = set(); rows = []
    while st:
        c, u = min(st); st.remove((c, u))
        if u in vis:
            rows.append(["(%d, %d)" % (c, u), "আগেই শেষ, বাদ", "—"]); continue
        vis.add(u); upd = []
        for v, w in adj[u]:
            if c + w < dist[v]:
                dist[v] = c + w; par[v] = u; st.add((dist[v], v)); upd.append("dist[%d] = %d" % (v, c + w))
        rows.append(["(%d, %d)" % (c, u), ", ".join(upd) or "কিছু কমলো না", " ".join("%d:%s" % (i, "∞" if dist[i] >= inf else dist[i]) for i in range(len(dist)) if i in vis or dist[i] < inf)])
    return dist, par, rows


def kruskal(n, edges):
    p = list(range(n + 1)); sz = [1] * (n + 1)

    def f(x):
        while p[x] != x:
            p[x] = p[p[x]]; x = p[x]
        return x
    rows, tot, took = [], 0, []
    for w, u, v in sorted((w, u, v) for u, v, w in edges):
        a, b = f(u), f(v)
        if a == b:
            rows.append(["%d - %d" % (u, v), w, "হ্যাঁ (আগেই জোড়া)", "বাদ ❌ (cycle হতো)", tot])
        else:
            if sz[a] < sz[b]: a, b = b, a
            p[b] = a; sz[a] += sz[b]; tot += w; took.append((u, v, w))
            rows.append(["%d - %d" % (u, v), w, "না", "নিলাম ✅", tot])
    return rows, tot, took


def prim(n, edges, start=1):
    adj = {i: [] for i in range(n + 1)}
    for u, v, w in edges:
        adj[u].append((w, v)); adj[v].append((w, u))
    h = [(0, start, 0)]; mark = set(); tot = 0; took = []; rows = []
    while h:
        c, x, fr = heapq.heappop(h)
        if x in mark:
            continue
        mark.add(x); tot += c
        if fr: took.append((fr, x, c))
        for w, y in adj[x]:
            if y not in mark: heapq.heappush(h, (w, y, x))
        rows.append(["(%d, %d)" % (c, x), c, tot, " ".join(str(i) for i in sorted(mark))])
    return rows, tot, took


def circ(ids, cx, cy, rad, start=-90):
    out = {}
    for k, i in enumerate(ids):
        a = math.radians(start + 360 * k / len(ids))
        out[i] = (round(cx + rad * math.cos(a)), round(cy + rad * math.sin(a)))
    return out
