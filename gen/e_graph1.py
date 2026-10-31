from enrich_lib import *
from sims import *

G1_EDGES = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 5), (4, 6), (5, 6)]
A1 = adj_from(G1_EDGES, 6)


def pathto(par, v):
    out = []
    while v is not None:
        out.append(v); v = par[v]
    return out[::-1]


def bsnap(snaps, k, caption, note=None):
    cur, q, order, lvl = snaps[k]
    st = {v: "v" for v in order}
    st[cur] = "a"
    for v in q: st[v] = "q"
    sub = {v: "L%d" % lvl[v] for v in lvl}
    return g1(caption, st, sub, note=note)


# ───────────── Adjacency Matrix ─────────────
mat = [[1 if j in A1[i] else 0 for j in range(1, 7)] for i in range(1, 7)]
MAT1 = MV("6 × 6 Adjacency Matrix — সবুজ ঘর = edge আছে", [[(v, "o" if v else "z") for v in r] for r in mat], cols=list(range(1, 7)), rowLabels=list(range(1, 7)), note="ছকটা কর্ণ বরাবর আয়নার মতো (graph[i][j] = graph[j][i]) কারণ graph undirected")
qs = [(1, 2), (1, 6), (5, 6), (3, 4)]
MAT2 = MV("যে ঘরগুলোয় প্রশ্ন করা হয়েছে সেগুলো হলুদ", [[(mat[i][j], "a" if ((i + 1, j + 1) in qs or (j + 1, i + 1) in qs) else ("o" if mat[i][j] else "z")) for j in range(6)] for i in range(6)], cols=list(range(1, 7)), rowLabels=list(range(1, 7)))

EN("graph-adj-matrix",
   "ধরো ৬ টা শহর আর তাদের মধ্যে কিছু রাস্তা। একটা ৬ × ৬ ছক আঁকো। u শহর থেকে v শহরে রাস্তা থাকলে ছকের (u, v) ঘরে 1 লেখো, না থাকলে 0। এই ছকটাই **Adjacency Matrix**। দুই শহরের মধ্যে রাস্তা আছে কিনা এক নজরেই (O(1)) বলা যায়। শুধু দাম দিতে হয় জায়গায়: n টা শহরের জন্য n × n ঘর লাগে।",
   "n ছোট হলে (≤ ১০০০) • edge আছে কিনা বারবার জানতে হলে • Floyd–Warshall • প্রায় সব জোড়ায় edge থাকলে (dense graph)",
   ["node ১ থেকে গুনলে array এর size `n + 1` বা তার বেশি রাখো, নাহলে `graph[n][n]` এ out-of-bound হবে।",
    "undirected graph এ দুই দিকেই (`graph[u][v]` ও `graph[v][u]`) 1 বসাতে হয়। directed হলে শুধু এক দিকে।",
    "n = 10⁵ হলে matrix এ 10¹⁰ ঘর লাগে, memory এ আঁটবে না। বড় graph এ Adjacency List ব্যবহার করো।",
    "weighted graph এ 1 এর জায়গায় cost রাখা হয়, আর 'edge নেই' বোঝাতে 0 বা INF (প্রশ্ন দেখে ঠিক করো)।"],
   X(["input `6 7` মানে 6 টা node, 7 টা edge। `graph[101][101]` global তাই শুরুতে সব ঘর 0।",
      "প্রথম edge `1 2`: `graph[1][2] = 1` আর `graph[2][1] = 1`। দুই দিকেই বসানো হলো কারণ রাস্তাটা দুই দিকেই চলে।",
      "একইভাবে 1-3, 2-4, 2-5, 3-5, 4-6, 5-6 এর জন্যও দুই দিকে করে 1 বসে। মোট 7 × 2 = 14 টা ঘরে 1।",
      "তারপর দুইটা লুপে প্রতিটা সারি ছাপা। যেমন সারি 2 এ 1 আছে 1, 4, 5 নম্বর ঘরে, মানে node 2 এর প্রতিবেশী 1, 4, 5।"],
     viz=[g1("এই graph টার matrix বানানো হলো"), MAT1],
     tables=[T(["সারি (node)", "ছাপা সারি", "1 গুলো কোথায়", "প্রতিবেশী"], [[i, " ".join(map(str, mat[i - 1])), ", ".join(str(j) for j in A1[i]), "%d জন" % len(A1[i])] for i in range(1, 7)], "প্রতিটা সারির 1 গুলোই ঐ node এর প্রতিবেশী")]),
   X(["edge বানানো আগের মতোই। তারপর `q = 4` টা প্রশ্ন পড়া হয়।",
      "প্রতিটা প্রশ্নে `graph[a][b]` একবার দেখলেই উত্তর। কোনো loop নেই, তাই প্রতি প্রশ্ন O(1)।",
      "(1, 2) → 1 তাই YES। (1, 6) → 0 তাই NO (সরাসরি রাস্তা নেই, ঘুরে যাওয়া যায় কিন্তু সরাসরি না)।",
      "(5, 6) → YES। (3, 4) → NO। প্রশ্ন ১০⁶ টা হলেও এই কোড এক মুহূর্তে শেষ, কিন্তু Adjacency List এ প্রতিটা প্রশ্নে প্রতিবেশী খুঁজতে হতো।"],
     viz=[MAT2],
     tables=[T(["প্রশ্ন", "graph[a][b]", "উত্তর"], [["1 - 2", 1, "YES"], ["1 - 6", 0, "NO"], ["5 - 6", 1, "YES"], ["3 - 4", 0, "NO"]], "চারটা প্রশ্নের উত্তর")]))

# ───────────── Adjacency List ─────────────
D4 = GV("Directed graph — তীর যেদিকে, edge শুধু সেদিকে",
        [(1, 60, 60), (2, 200, 60), (3, 130, 150), (4, 280, 150)],
        [(1, 2, "n", None, True), (1, 3, "n", None, True), (3, 2, "n", None, True), (4, 3, "n", None, True)], w=340, h=200)
EN("graph-adj-list",
   "প্রতিটা শহরের জন্য একটা তালিকা রাখো: 'আমার সাথে কারা জোড়া?'। পুরো graph হয়ে যায় তালিকার তালিকা, মানে `vector<vector<int>>`। যত edge আছে ঠিক ততটুকুই জায়গা লাগে (O(N + E)), তাই n = 10⁵ হলেও সমস্যা নেই। BFS বা DFS প্রতিবার শুধু প্রতিবেশীদের ওপর ঘুরলেই হয়। Competitive Programming এর প্রায় সব graph প্রশ্নে এই পদ্ধতিই চলে।",
   "BFS, DFS • বড় n (১০⁵ পর্যন্ত) • যেসব graph এ edge কম (sparse) • Dijkstra, MST, topological sort সবকিছুর ভিত্তি",
   ["`graph[N]` এর N, node সংখ্যার চেয়ে অন্তত 1 বেশি রাখো (১ থেকে গুনলে)।",
    "একাধিক test case এ প্রতি test এর শুরুতে সব `graph[i].clear()` করো। না করলে আগের test এর edge থেকে যাবে।",
    "প্রতিবেশীদের ক্রম input এর edge ক্রম অনুযায়ী। BFS/DFS এর visit ক্রম এই ক্রমের ওপর নির্ভর করে।",
    "ঘুরতে `for (auto &neighbor : graph[i])` লিখলে copy হয় না, বড় object হলে এটাই ভালো।"],
   X(["input `6 7`। `graph(N)` মানে N টা খালি vector, প্রতিটা node এর জন্য একটা করে।",
      "edge `1 2` এলে `graph[1]` এর শেষে 2 আর `graph[2]` এর শেষে 1 বসে। undirected তাই দুই দিকেই।",
      "সব edge শেষে `graph[2] = {1, 4, 5}`। কারণ 2 জড়িত edge গুলো input এ এসেছিল 1-2, 2-4, 2-5 এই ক্রমে।",
      "শেষ লুপে প্রতিটা node এর তালিকা ছাপা হয়। `\"Node i is connected to : \"` এর পরে প্রতিটা প্রতিবেশীর আগে একটা করে space যায়, তাই `:` এর পরে দুইটা space দেখা যায়।"],
     viz=[g1("এই graph এর list গুলো বানানো হলো")],
     tables=[T(["node", "graph[node]", "সাইজ"], [[i, "{ " + ", ".join(map(str, A1[i])) + " }", len(A1[i])] for i in range(1, 7)], "প্রতিটা node এর প্রতিবেশীর তালিকা")]),
   X(["এবার directed graph। edge `u v` মানে শুধু u থেকে v এ যাওয়া যাবে। তাই `graph[u].push_back(v)` একবারই।",
      "edge গুলো: 1→2, 1→3, 3→2, 4→3। `graph[1] = {2, 3}`, `graph[3] = {2}`, `graph[4] = {3}`।",
      "node 2 থেকে কোনো edge বের হয়নি, তাই `graph[2]` ফাঁকা। ছাপার সময় `2 -> ` এর পর কিছু নেই।",
      "undirected এ push দুইবার, directed এ একবার। কোডে শুধু এই একটা লাইনই বদলায়।"],
     viz=[D4],
     tables=[T(["node", "graph[node]", "মন্তব্য"], [[1, "{ 2, 3 }", "1 থেকে বের হয় 2 আর 3 এ"], [2, "{ }", "কোথাও যাওয়া যায় না"], [3, "{ 2 }", "3 থেকে শুধু 2 এ"], [4, "{ 3 }", "4 থেকে শুধু 3 এ"]], "directed graph এর তালিকা")]),
   X(["node এর **degree** মানে তার সাথে কয়টা edge লেগে আছে। Adjacency List এ সেটা `graph[i].size()`, কোনো বাড়তি গণনা লাগে না।",
      "node 2 এর প্রতিবেশী 1, 4, 5 তাই degree 3। node 5 এর প্রতিবেশী 2, 3, 6 তাই degree 3। বাকিদের 2।",
      "সব degree এর যোগফল = 2 + 3 + 2 + 2 + 3 + 2 = 14। এটা ঠিক edge সংখ্যার (7) দ্বিগুণ, কারণ প্রতিটা edge দুই মাথায় একবার করে গোনা হয়। (Handshaking Lemma)"],
     viz=[g1("degree বেশি যাদের (3), তারা হলুদ", {2: "a", 5: "a"})],
     tables=[T(["node", "degree"], [[i, len(A1[i])] for i in range(1, 7)] + [["যোগফল", "14 = 2 × 7"]], "প্রতিটা node এর degree", hl=[6])]),
   truth=T(["", "Adjacency Matrix", "Adjacency List"],
           [["জায়গা", "O(N²)", "O(N + E)"], ["u - v edge আছে কিনা", "O(1)", "O(degree)"], ["সব প্রতিবেশী দেখা", "O(N)", "O(degree)"], ["কখন ভালো", "n ছোট, edge অনেক", "n বড়, edge কম (বেশিরভাগ প্রশ্ন)"]],
           "দুই পদ্ধতির তুলনা"))

# ───────────── Weighted list ─────────────
W5 = GV("weighted graph — edge এর গায়ে cost",
        [(1, 50, 105), (2, 175, 45), (3, 175, 165), (4, 320, 105), (5, 420, 105)],
        [(1, 2, "n", 4), (1, 3, "n", 2), (2, 3, "n", 1), (2, 4, "n", 5), (3, 4, "n", 8), (4, 5, "n", 3)], h=210)
EN("graph-adj-list-weighted",
   "edge এর সাথে যদি ওজন (cost, দূরত্ব বা সময়) থাকে, তাহলে vector এ শুধু node রাখলে চলে না। node আর cost একসাথে `pair<int, int>` এ রাখা হয় (`{প্রতিবেশী, cost}`)। shortest path (Dijkstra) আর minimum spanning tree (Kruskal, Prim) এই ধরনের graph এই ভাবেই রাখে।",
   "Dijkstra • MST • যেকোনো cost/distance যুক্ত graph",
   ["pair এর কোনটা আগে (`first`) আর কোনটা পরে (`second`) সেটা ঠিক করে রাখো। Dijkstra তে সাধারণত `{cost, node}` রাখা হয় যাতে sort এ cost আগে আসে। এখানে `{node, cost}`।",
    "cost 10⁹ পর্যন্ত হলেও যোগফল int এ আঁটবে না। দূরত্ব রাখতে `long long` নাও।",
    "multiple edge বা self-loop থাকতে পারে কিনা প্রশ্নে দেখে নাও। থাকলে ওগুলো আলাদাভাবে সামলাতে হতে পারে।",
    "Kruskal এ list এর চেয়ে `vector<tuple<cost, u, v>>` (edge list) সুবিধার।"],
   X(["input `5 6`। প্রতিটা edge এ তিনটা সংখ্যা: `u v cost`। যেমন `1 2 4` মানে 1 আর 2 এর মধ্যে রাস্তা, cost 4।",
      "`graph[u].push_back({v, cost})` আর `graph[v].push_back({u, cost})`। দুই দিকেই একই cost।",
      "ফলে `graph[1] = {(2, 4), (3, 2)}`, `graph[2] = {(1, 4), (3, 1), (4, 5)}` ইত্যাদি।",
      "ছাপার সময় `edge.first` হলো প্রতিবেশী node আর `edge.second` হলো cost।"],
     viz=[W5],
     tables=[T(["node", "graph[node] = { (প্রতিবেশী, cost), ... }"], [[1, "(2, 4)  (3, 2)"], [2, "(1, 4)  (3, 1)  (4, 5)"], [3, "(1, 2)  (2, 1)  (4, 8)"], [4, "(2, 5)  (3, 8)  (5, 3)"], [5, "(4, 3)"]], "weighted adjacency list")]),
   X(["এই input এ node 1 আর 2 এর মধ্যে তিনটা আলাদা edge (cost 10, 13, 14) আছে। একে **multiple edge** বলে।",
      "vector এ কোনো duplicate আটকানো নেই, তাই তিনটাই জমা হয়েছে। shortest path এর ক্ষেত্রে শুধু ছোটটা কাজে লাগবে (10)।",
      "`2 2 2` একটা **self-loop** (node 2 থেকে নিজেই 2 এ)। কোডে `graph[u]` আর `graph[v]` দুটোই graph[2], তাই (2, 2) দুইবার ঢুকেছে।",
      "প্রশ্নে এসব থাকতে পারে কিনা আগে পড়ে নাও। থাকলে shortest path/MST এ self-loop বাদ দিতে হয়।"],
     tables=[T(["node", "graph[node]"], [[1, "(2, 10) (2, 13) (2, 14)"], [2, "(1, 10) (1, 13) (1, 14) (4, 3) (3, 2) (2, 2) (2, 2)"], [3, "(2, 2)"], [4, "(2, 3)"]], "মজার input এর list")]))

# ───────────── BFS ─────────────
r1, o1, l1, p1, s1 = bfs_trace(A1, 1)
r4, o4, l4, p4, s4 = bfs_trace(A1, 4)
EN("graph-bfs",
   "পুকুরে ঢিল ফেললে ঢেউ যেমন চারদিকে সমানভাবে বাড়ে, BFS ও তেমনি source থেকে আগে ১ ধাপ দূরের সবাইকে, তারপর ২ ধাপ দূরের সবাইকে ছোঁয়। এই ঢেউ সামলায় **queue** (লাইনে দাঁড়ানোর নিয়ম: যে আগে এসেছে সে আগে যাবে)। প্রতিটা node কে একবারই queue এ ঢোকাতে `vis[]` ব্যবহার হয়।",
   "unweighted graph এ shortest path • node গুলোর level/দূরত্ব বের করা • grid এ maze solve • connected component",
   ["`vis[child] = 1` করো queue তে **push করার সময়ই**, pop করার সময় না। নাহলে একই node একাধিকবার queue তে ঢুকে যাবে।",
    "visit এর ক্রম input এর edge ক্রমের ওপর নির্ভর করে। ক্রম আলাদা হতে পারে, কিন্তু level গুলো সবসময় একই থাকে।",
    "একাধিক test case এ `vis` আর `g` আবার খালি করতে ভুলো না।",
    "graph connected না হলে একটা `bfs(1)` সব node ছোঁবে না। সব node এ ঘুরে যেটা unvisited, তাতে bfs চালাও।"],
   X(["input গুলো পড়ে `g` এ adjacency list বানানো হলো (আগের পেজের মতো)। তারপর `bfs(1)`।",
      "শুরুতে `q = [1]` আর `vis[1] = 1`। loop চলে যতক্ষণ queue খালি না হয়: সামনের node কে `front()` দিয়ে নাও, `pop()` করো, তারপর ছাপো।",
      "1 কে নিয়ে প্রতিবেশী 2, 3 কে queue তে ঢোকালাম (দুজনেই unvisited ছিল)। এখন `q = [2, 3]`।",
      "এরপর 2 কে নিলাম। তার প্রতিবেশী 1 (visited, বাদ), 4 আর 5 নতুন। `q = [3, 4, 5]`। এভাবে চলতে চলতে 6 পর্যন্ত যাওয়া হলো।",
      "ছবি দেখো: হলুদ = এখন যাকে নিয়েছি, নীল = queue তে অপেক্ষায়, সবুজ = শেষ। L0, L1 ... হলো source থেকে দূরত্ব (level)।"],
     viz=[bsnap(s1, 0, "ধাপ ১: 1 কে নিলাম, 2 ও 3 queue তে ঢুকলো"), bsnap(s1, 1, "ধাপ ২: 2 কে নিলাম, 4 ও 5 queue তে ঢুকলো"), bsnap(s1, 5, "শেষ: সব node ছোঁয়া হয়ে গেছে", "level (L) অনুযায়ী ঢেউ: L0 → L1 → L2 → L3")],
     tables=[T(["ধাপ", "pop করা node", "নতুন ঢুকলো", "queue (এরপর)", "এ পর্যন্ত ছাপা"], r1, "queue এর পুরো চলা", hl=[6])]),
   X(["এবার source `4`। শুরুতে `q = [4]`।",
      "4 এর প্রতিবেশী 2 আর 6 (input এ edge 2-4 আগে, 4-6 পরে ছিল)। `q = [2, 6]`।",
      "2 কে নিয়ে নতুন পেলাম 1 আর 5। `q = [6, 1, 5]`। (4 আগেই visited, তাই বাদ)",
      "6 কে নিয়ে কিছু নতুন নেই (4, 5 দুটোই আগে থেকে ঢোকা)। 1 কে নিয়ে নতুন 3। শেষে 5, 3।",
      "ক্রম: **4 2 6 1 5 3**। source বদলালেই BFS এর ঢেউ নতুন জায়গা থেকে শুরু হয়, কিন্তু নিয়ম একই।"],
     viz=[bsnap(s4, 0, "ধাপ ১: 4 কে নিলাম, 2 ও 6 queue তে ঢুকলো"), bsnap(s4, 5, "শেষ: 4 থেকে সবার দূরত্ব (L)")],
     tables=[T(["ধাপ", "pop করা node", "নতুন ঢুকলো", "queue (এরপর)", "এ পর্যন্ত ছাপা"], r4, "source = 4 হলে queue এর চলা", hl=[6])]))

# ───────────── BFS level ─────────────
def lvlfig(caption, lv, note=None):
    return g1(caption, {v: ("a" if lv[v] == 0 else "v") for v in lv}, {v: "L%d" % lv[v] for v in lv}, note=note)

M2_1 = GV("Test 1: 1 — 2 — 3 (রাস্তা সোজা)", [(1, 70, 60, "a", None, "L0"), (2, 220, 60, "v", None, "L1"), (3, 370, 60, "v", None, "L2")], [(1, 2), (2, 3)], w=440, h=130)
M2_2 = GV("Test 2: 4 টা দ্বীপ, 1 আর 4 সরাসরি জোড়া", [(1, 80, 40, "a", None, "L0"), (2, 280, 40, "v", None, "L1"), (3, 280, 150, "v", None, "L2"), (4, 80, 150, "v", None, "L1")],
          [(1, 2), (2, 3), (3, 4), (1, 4)], w=360, h=205, note="দুই দিক দিয়েই যাওয়া যায়, কিন্তু সরাসরি 1 → 4 এ মাত্র 1 bridge")
EN("graph-bfs-level",
   "BFS এ প্রতিটা node কে প্রথমবার যখন পাই, তখন `level[child] = level[parent] + 1` লিখে রাখলে `level[v]` হয়ে যায় source থেকে v এ যেতে **সবচেয়ে কম কয়টা edge** পার হতে হয়। BFS কাছের node আগে ছোঁয় বলে কোনো node এ প্রথম পৌঁছানোই সবচেয়ে ছোট পথ। unweighted graph এ এটাই shortest path।",
   "unweighted graph এ shortest path • 'সবচেয়ে কম ধাপে' ধরনের প্রশ্ন • level wise কাজ",
   ["level শুধু unweighted graph এ shortest path দেয়। edge এ cost থাকলে Dijkstra লাগবে।",
    "`level` array এর মান নতুন test এর আগে 0 (বা -1) করতে ভুলো না। -1 দিলে 'পৌঁছানো যায়নি' আলাদা করে বোঝা যায়।",
    "source এ পৌঁছানো না গেলে `level[target]` এ আগের মান (0) থেকে যাবে। এমন হলে -1 ছাপতে `level` কে -1 দিয়ে শুরু করো।",
    "পথটাও (path) দরকার হলে `parent[child] = current_vertex` রেখে শেষ থেকে পিছিয়ে এসো।"],
   X(["input গুলো পড়ে আগের মতো `bfs(1)` চালানো হলো, শুধু এবার `level[]` ও ভরছে।",
      "`level[1] = 0`। 1 কে pop করে 2 আর 3 কে পেলাম, তাই `level[2] = level[3] = 0 + 1 = 1`।",
      "2 কে pop করে 4 আর 5 কে পেলাম, `level[4] = level[5] = 1 + 1 = 2`। 4 কে pop করে 6 কে পেলাম, `level[6] = 3`।",
      "5 এর মাধ্যমেও 6 এ যাওয়া যেত (1→2→5→6 অথবা 1→3→5→6), সেখানেও 3 ধাপ। কিন্তু 6 আগেই visited, তাই level আর বদলায়নি।"],
     viz=[lvlfig("প্রতিটা node এর নিচে লাল L = source (1) থেকে দূরত্ব", l1)],
     tables=[T(["node", "level", "পথ (একটা)"], [[v, l1[v], "→".join(map(str, pathto(p1, v)))] for v in range(1, 7)], "1 থেকে প্রতিটা node এর সবচেয়ে ছোট দূরত্ব")]),
   X(["প্রশ্ন (HackerEarth, Monk and the Islands): দ্বীপ 1 থেকে দ্বীপ n এ যেতে সবচেয়ে কম কয়টা bridge পার হতে হবে। অর্থাৎ ঠিক `level[n]`।",
      "`t = 2` টা test। প্রতিটা test এর শুরুতে `g`, `vis`, `level` পরিষ্কার করা হয়, নাহলে আগের test এর বাকি তথ্য গুলিয়ে ফেলবে।",
      "test 1: 1-2, 2-3। 1 → 2 → 3, level[3] = 2।",
      "test 2: 1-2, 2-3, 3-4, 1-4। 1 থেকে 4 এ সরাসরি একটা bridge আছে, তাই level[4] = 1 (ঘুরে 3 bridge লাগতো না)। BFS নিজে থেকেই সবচেয়ে কমটা খুঁজে পায়।"],
     viz=[M2_1, M2_2],
     tables=[T(["test", "node সংখ্যা n", "edge", "level[n]", "উত্তর"], [[1, 3, "1-2, 2-3", 2, 2], [2, 4, "1-2, 2-3, 3-4, 1-4", 1, 1]], "দুই test এর ফল")]))

# ───────────── BFS grid ─────────────
dirs8 = [["0", "-1", "0", "উপরে"], ["1", "+1", "0", "নিচে"], ["2", "0", "-1", "বামে"], ["3", "0", "+1", "ডানে"], ["4", "-1", "-1", "উপরে-বামে (কোনাকুনি)"], ["5", "-1", "+1", "উপরে-ডানে"], ["6", "+1", "-1", "নিচে-বামে"], ["7", "+1", "+1", "নিচে-ডানে"]]
cheb = [[(max(abs(i - 2), abs(j - 2)), "s" if (i, j) == (2, 2) else "v") for j in range(5)] for i in range(5)]
maze = ["S..#.", ".#...", ".#.#.", "...#.", ".#..E"]
# maze BFS
from collections import deque
dist = {(0, 0): 0}; par = {(0, 0): None}; dq = deque([(0, 0)])
while dq:
    x, y = dq.popleft()
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5 and maze[nx][ny] != "#" and (nx, ny) not in dist:
            dist[(nx, ny)] = dist[(x, y)] + 1; par[(nx, ny)] = (x, y); dq.append((nx, ny))
path = []; c = (4, 4)
while c: path.append(c); c = par[c]
MZ = MV("প্রতিটা ঘরে লেখা সংখ্যা = S থেকে কত ধাপে পৌঁছানো যায়। গোলাপি = একটা সবচেয়ে ছোট পথ, কালো = দেয়াল",
        [[(("#" if maze[i][j] == "#" else dist.get((i, j), "-")), "w" if maze[i][j] == "#" else ("s" if (i, j) == (0, 0) else ("p" if (i, j) in path else "v"))) for j in range(5)] for i in range(5)],
        cols=list(range(5)), rowLabels=list(range(5)))
EN("graph-bfs-grid",
   "grid (ছক) কেও graph ভাবা যায়: প্রতিটা ঘর একটা node, আর পাশের ঘরগুলো তার প্রতিবেশী। আলাদা করে adjacency list বানাতে হয় না। দুইটা ছোট array `dx[]` আর `dy[]` দিয়ে উপর-নিচ-বাম-ডান (বা কোনাকুনিসহ ৮ দিকে) যাওয়া যায়। প্রতিবার নতুন ঘর grid এর ভেতরে আছে কিনা আর আগে visited কিনা `valid()` দিয়ে দেখা হয়।",
   "maze এ সবচেয়ে ছোট পথ • flood fill • knight move • island গোনা • '#' দেয়ালসহ grid এর প্রশ্ন",
   ["`row` আর `column` এ মান না বসালে `valid()` সবসময় false দেবে (0 < 0 মিথ্যা), BFS শুরুর ঘর ছাড়া কোথাও যাবে না। এই ভুল খুব হয়।",
    "`dx[i]` আর `dy[i]` একই index এ জোড়ায় কাজ করে। জোড়া ঠিক না থাকলে কোনাকুনি দিক ভুল হবে।",
    "শুধু 4 দিক চাইলে লুপ `i < 4`, ৮ দিক চাইলে `i < 8`। knight এর চাল হলে `dx = {2, 2, -2, -2, 1, 1, -1, -1}` ধরনের আলাদা array।",
    "ঘর visited করার সময় (queue তে ঢোকানোর সময়ই) `vis` বা `dist` সেট করো, pop এর সময় নয়।"],
   X(["`row = column = 5` বসানো হলো। grid এ কোনো দেয়াল নেই, কেবল ঘর। শুরু ঘর (2, 2), মানে ঠিক মাঝখানে।",
      "`dx[]`/`dy[]` এর ৮টা জোড়া ৮ দিক বোঝায় (নিচের টেবিল দেখো)। প্রতিটা ঘরের জন্য ৮ প্রতিবেশী পরীক্ষা হয়।",
      "`valid(nx, ny)` সত্য হয় যদি ঘরটা grid এর ভেতরে আর এখনো visited না। সত্য হলে `vis = 1` করে queue তে ঢোকানো হয়।",
      "ফাঁকা grid এ কোনাকুনি যাওয়া যায় বলে প্রথম ধাপেই চারপাশের ৮ ঘর, পরের ধাপে বাকি ১৬ ঘর। মোট ২৫ ঘরই visited, তাই সব 1।",
      "নিচের ছবিতে প্রতিটা ঘরে লেখা সংখ্যা মানে ওই ঘরে পৌঁছাতে কত ধাপ লাগে (কোড এই সংখ্যা রাখে না, শুধু visited রাখে। চাইলে `dist` রাখলে এমন সংখ্যা পেতে)।"],
     viz=[MV("5 × 5 grid, শুরু (2, 2) (নীল)। সংখ্যা = কত ধাপে পৌঁছানো যায় (৮ দিকে)", cheb, cols=list(range(5)), rowLabels=list(range(5)))],
     tables=[T(["i", "dx[i]", "dy[i]", "দিক"], dirs8, "৮ দিকের জোড়া")]),
   X(["এবার ৪ দিকের maze। `#` দেয়াল, `S` শুরু, `E` শেষ। `dist[i][j]` কে -1 দিয়ে শুরু করা হলো, মানে 'এখনো পৌঁছাইনি'।",
      "`valid()` এখন তিনটা শর্ত দেখে: grid এর ভেতরে, দেয়াল না (`!= '#'`) আর `dist == -1` (visited না)।",
      "`dist[S] = 0`। queue এর সামনের ঘর (x, y) থেকে চারদিকে যে ঘর valid তার `dist = dist[x][y] + 1` হয়।",
      "BFS ঢেউয়ের মতো ছড়ায়, তাই E তে প্রথমবার পৌঁছানোই সবচেয়ে ছোট পথ। ছবিতে সবচেয়ে ছোট একটা পথ গোলাপি।",
      "শেষে `dist[E]` = **8**। মনে রাখো, S থেকে E এর সরাসরি দূরত্ব (Manhattan) ও 4 + 4 = 8, দেয়াল এড়িয়েও এর চেয়ে কম হতো না।"],
     viz=[MZ],
     tables=[T(["ধাপ", "ঘর (সারি, কলাম)"], [[i, "(%d, %d)" % c] for i, c in enumerate(reversed(path))], "একটা সবচেয়ে ছোট পথ (S থেকে E, মোট %d ধাপ)" % (len(path) - 1))]))

# ───────────── DFS ─────────────
rd1, od1, tin1, tout1, pd1, back1 = dfs_trace(A1, 1)
rd3, od3, tin3, tout3, pd3, back3 = dfs_trace(A1, 3)


def dfsfig(caption, order, par, back, src):
    st = {v: "v" for v in order}; st[src] = "a"
    sub = {v: "#%d" % (i + 1) for i, v in enumerate(order)}
    es = {}
    for v, p in par.items():
        if p: es[(p, v)] = "t"
    for a, b in back: es[(a, b)] = "x"
    return g1(caption, st, sub, es, note="সবুজ মোটা = DFS যে edge ধরে গভীরে গেছে, গোলাপি ড্যাশ = ফিরতি edge (আগেই visited node)। # = visit এর ক্রম")


EN("graph-dfs",
   "গোলকধাঁধায় হাঁটার কথা ভাবো: একটা পথ ধরে যতদূর যাওয়া যায় যাও, আটকে গেলে (সব প্রতিবেশী আগেই দেখা) এক ধাপ পিছিয়ে এসে অন্য পথ ধরো। এটাই **DFS**। এটা recursion দিয়ে করা সহজ, কারণ recursion এর call stack নিজেই 'কোথা থেকে এসেছি' মনে রাখে। `vis[]` না থাকলে cycle এ ঘুরে ঘুরে অসীম loop হবে।",
   "connected component • cycle detection • topological sort • সব পথ খোঁজা (backtracking) • tree এর কাজ",
   ["`vis[v] = 1` সবসময় function এর শুরুতেই করো, নাহলে একই node এ বারবার ঢুকে পড়বে।",
    "n খুব বড় (১০⁵ বা তার বেশি) আর graph লম্বা chain এর মতো হলে recursion এর গভীরতা অনেক বেড়ে stack overflow হতে পারে। তখন stack নিজে বানাও বা BFS ব্যবহার করো।",
    "DFS shortest path দেয় না। শুধু 'পৌঁছানো যায় কিনা' বা 'সব ঘুরে দেখা' তে কাজে লাগে।",
    "ক্রম input edge এর ক্রমের ওপর নির্ভর করে, তাই একই graph এ ক্রম আলাদা হতে পারে। সঠিক DFS এর শর্ত মেনে চললেই হলো।"],
   X(["`adj` এ graph বানিয়ে `dfs(1)` ডাকা হলো। function ঢুকেই `vis[1] = 1` করে 1 ছাপলো।",
      "1 এর প্রতিবেশী {2, 3}। প্রথম unvisited 2, তাই 3 এর জন্য অপেক্ষা না করে সাথে সাথে `dfs(2)`। 2 এর প্রতিবেশী {1, 4, 5}, 1 visited, তাই `dfs(4)`। 4 এর পর `dfs(6)`।",
      "6 এর প্রতিবেশী {4, 5}। 4 visited, তাই `dfs(5)`। 5 এর প্রতিবেশী {2, 3, 6}। 2 visited, 3 নতুন, তাই `dfs(3)`।",
      "3 এর সব প্রতিবেশী (1, 5) visited। কিছু করার নেই, 3 ফিরে গেলো। একে একে 5, 6, 4, 2, 1 ও ফিরে এলো। মাঝে 2 আর 1 এর বাকি প্রতিবেশীও আগেই visited ছিল।",
      "ক্রম: **1 2 4 6 5 3**। BFS এর (1 2 3 4 5 6) সাথে তুলনা করো, এখানে গভীরে আগে গেছে।"],
     viz=[dfsfig("DFS এর পথ (source = 1)", od1, pd1, back1, 1)],
     tables=[T(["ঘটনা", "call stack (ভেতরে আছি)", "এ পর্যন্ত ছাপা"], rd1, "recursion এ ঢোকা (IN) ও ফেরা (OUT)")]),
   X(["এবার `start = 3`। `dfs(3)`: 3 এর প্রতিবেশী {1, 5}। প্রথম unvisited 1, তাই `dfs(1)`।",
      "1 এর প্রতিবেশী {2, 3}। 2 নতুন, তাই `dfs(2)`। 2 এর {1, 4, 5}: 4 নতুন, তাই `dfs(4)`, তারপর 6।",
      "6 এর {4, 5}: 5 নতুন, `dfs(5)`। 5 এর সবাই (2, 3, 6) visited। তাই ফিরে আসা শুরু।",
      "ক্রম: **3 1 2 4 6 5**। source ভেদে একই graph এ DFS এর ক্রম ও গঠন বদলায়।"],
     viz=[dfsfig("DFS এর পথ (source = 3)", od3, pd3, back3, 3)],
     tables=[T(["ঘটনা", "call stack (ভেতরে আছি)", "এ পর্যন্ত ছাপা"], rd3, "source = 3 হলে")]),
   truth=T(["", "BFS", "DFS"],
           [["ব্যবহার করে", "queue", "recursion (stack)"], ["এগোয়", "স্তরে স্তরে (ঢেউ)", "গভীরে, আটকালে পিছিয়ে"], ["shortest path (unweighted)", "✅ দেয়", "❌ দেয় না"], ["cycle / component / topo sort", "চলে", "সবচেয়ে সুবিধার"], ["বিপদ", "queue বড় হতে পারে", "গভীর হলে stack overflow"]],
           "BFS বনাম DFS"))

# ───────────── DFS 4 sections ─────────────
TREE_E = [(1, 2), (1, 3), (2, 4), (2, 5)]
AT = adj_from(TREE_E, 5)
rt, ot, tint, toutt, pt, bt = dfs_trace(AT, 1)
TP = {1: (230, 30), 2: (130, 100), 3: (330, 100), 4: (60, 170), 5: (200, 170)}
def treefig(caption, sub, st=None, note=None):
    return GV(caption, [(i, TP[i][0], TP[i][1], (st or {}).get(i, "n"), None, sub.get(i)) for i in TP], [(a, b) for a, b in TREE_E], w=390, h=215, note=note)
sz = {4: 1, 5: 1, 3: 1, 2: 3, 1: 5}; dp_ = {1: 0, 2: 1, 3: 1, 4: 2, 5: 2}
luv_rows = []
for k, line in enumerate(rt):
    pass
EN("graph-dfs-luv",
   "DFS function এ কাজ বসানোর চারটা আলাদা জায়গা আছে, আর কোন কাজ কোথায় বসবে সেটাই DFS এর আসল কৌশল। (১) vertex এ **ঢুকেই** (২) child এ **ঢোকার আগে** (৩) child থেকে **ফিরে এসে** (৪) vertex থেকে **বেরোনোর আগে**। subtree এর size, depth, tin/tout, cycle, topological sort, bridge, সবই এই চার জায়গার কোনো না কোনোটায় একটা-দুটো লাইন বসিয়েই হয়।",
   "subtree size • depth • entry/exit time • topological sort • bridge ও articulation point • DP on tree",
   ["**ঢোকার সময়ের তথ্য** (depth, parent) child এ ঢোকার আগে আর **ফেরার সময়ের তথ্য** (subtree size, sum) child থেকে ফিরে এসে হিসাব হয়। উল্টো করলে ভুল ফল আসবে।",
    "tree এ parent কে আলাদা করে বাদ দিতে `par` পাঠাও (`if (child == par) continue;`)। `vis[]` ও চলে, কিন্তু par দিলে বাড়তি array লাগে না।",
    "main এ shortcut: সবসময় নিজের কাজ চারটা জায়গার কোনটায় পড়ে আগে ভেবে নাও, তারপর কোড লেখো।",
    "recursion এর গভীরতা বড় হলে (১০⁵) stack overflow এর কথা মনে রাখো।"],
   X(["input একটা ছোট tree: 1-2, 1-3, 2-4, 2-5। `dfs(1)` ডাকা হলো।",
      "function এ ঢুকেই `IN vertex` ছাপা হয় (জায়গা ১) আর `vis` সেট হয়। এরপর প্রতিবেশীদের ওপর লুপ।",
      "প্রতিটা child এর জন্য আগে `parent .., child ..` ছাপা হয়। যদি child আগেই visited হয় (যেমন parent নিজে), `continue` করে পরেরটায় চলে যায়।",
      "unvisited child পেলে `dfs(child)` ডাকা হয়। ফিরে আসার পর (জায়গা ৩) পরের child এ যাওয়া হয়। সব child শেষ হলে (জায়গা ৪) `OUT vertex` ছাপা হয়।",
      "ছবিতে প্রতিটা node এর নিচে `ঢোকার সময় / বেরোনোর সময়` (tin / tout) লেখা আছে। যে node এর সময়ের ব্যবধান যত বড়, তার subtree তত বড়।"],
     viz=[treefig("tree এর ছবি: নিচের লেখা = ঢোকার সময় / বেরোনোর সময়", {v: "%d / %d" % (tint[v], toutt[v]) for v in TP})],
     tables=[T(["ঘটনা", "call stack", "এ পর্যন্ত ঢোকা ক্রম"], rt, "IN / OUT এর পুরো ক্রম")]),
   X(["এখানে দুটো হিসাব করা হচ্ছে। `depth[v]` (root থেকে কত নিচে) আর `sz[v]` (v এর subtree তে কয়টা node, নিজেসহ)।",
      "**depth** child এ ঢোকার আগের জায়গায় বসানো: `depth[child] = depth[v] + 1`। কারণ parent এর depth আগে থেকেই জানা আছে।",
      "**sz** child থেকে ফিরে এসে বসানো: `sz[v] += sz[child]`। কারণ child এর subtree এর size জানতে হলে child এর কাজ শেষ হওয়া দরকার।",
      "node 4 আর 5 এর size 1 (পাতা)। node 2 = 1 + 1 + 1 = 3। node 3 = 1। node 1 = 1 + 3 + 1 = 5।",
      "এই দুই জায়গার পার্থক্য বোঝাই এই পেজের মূল শিক্ষা। পরে tree DP, LCA, Euler tour এ হুবহু এই ছাঁচ কাজে লাগে।"],
     viz=[treefig("প্রতিটা node এর নিচে d = depth, s = subtree size", {v: "d%d s%d" % (dp_[v], sz[v]) for v in TP})],
     tables=[T(["node", "depth", "subtree size", "কীভাবে"], [[1, 0, 5, "1 + sz[2] + sz[3] = 1 + 3 + 1"], [2, 1, 3, "1 + sz[4] + sz[5] = 1 + 1 + 1"], [3, 1, 1, "পাতা"], [4, 2, 1, "পাতা"], [5, 2, 1, "পাতা"]], "ফলাফল")]))

# ───────────── DFS grid ─────────────
GP = ["....#.", ".....#", "......", "..@..."]
reach = set(); stk = [(3, 2)]
while stk:
    x, y = stk.pop()
    if (x, y) in reach: continue
    reach.add((x, y))
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 4 and 0 <= ny < 6 and GP[nx][ny] != "#" and (nx, ny) not in reach: stk.append((nx, ny))
GF = MV("ছবি: গোলাপি = ঢোকা যায়নি (ঘেরা), সবুজ = ঘুরে আসা ঘর, নীল = @, কালো = #",
        [[("#" if GP[i][j] == "#" else ("@" if GP[i][j] == "@" else "."), "w" if GP[i][j] == "#" else ("s" if GP[i][j] == "@" else ("v" if (i, j) in reach else "p"))) for j in range(6)] for i in range(4)],
        cols=list(range(6)), rowLabels=list(range(4)), note="ঘর (0, 5) ফাঁকা কিন্তু দুই দিকে '#' দিয়ে ঘেরা, তাই DFS সেখানে যেতে পারেনি। reachable ঘর = %d" % len(reach))
EN("graph-dfs-grid",
   "grid এ DFS মানে কোনো ঘর থেকে শুরু করে হেঁটে যতগুলো ঘরে যাওয়া যায় সবগুলো ছুঁয়ে আসা। একে **Flood Fill** ও বলে (রং এর বালতি ঢেলে দিলে যেমন ছড়ায়)। BFS এর মতোই `dx`, `dy` আর `valid()` লাগে। শুধু queue এর জায়গায় recursion।",
   "island/connected area গোনা • maze এ পৌঁছানো যায় কিনা • reachable ঘর গোনা • flood fill",
   ["recursion এ ঢোকার প্রথম কাজ: ঘর আগে visited হলে `return`, নাহলে `vis = 1`। এতে একই ঘরে দুইবার ঢোকা আটকায়।",
    "প্রতি test এ `vis` আবার 0 করো (`memset(vis, 0, sizeof(vis))`) আর গণনার `cnt` ও 0 করো।",
    "input এ আগে column (c) তারপর row (r) আসে কিনা লক্ষ করো। LightOJ এ `W H` মানে প্রথমে চওড়া (c), তারপর উচ্চতা (r)।",
    "grid অনেক বড় (১০³ × ১০³) হলে recursion এর গভীরতায় stack overflow হতে পারে। তখন BFS নাও।"],
   X(["`row = column = 5` বসিয়ে `dfs(2, 2)`। DFS এ প্রতিবার ৮ দিকের প্রথম valid ঘরে ঢুকে যায়, আটকে গেলে পিছায়।",
      "ফাঁকা 5 × 5 grid এ কোনাকুনিও যাওয়া যায়, তাই সব ঘরেই পৌঁছানো সম্ভব। সব ঘর visited, তাই সব 1।",
      "BFS এর output এর সাথে হুবহু মিল, শুধু ঘরগুলো ছোঁয়ার ক্রম আলাদা। কোন ঘর visited সেটাই এখানে মূল।"],
     viz=[MV("5 × 5 grid, সব ঘর visited (সবুজ), শুরুর ঘর নীল", [[("1", "s" if (i, j) == (2, 2) else "v") for j in range(5)] for i in range(5)], cols=list(range(5)), rowLabels=list(range(5)))]),
   X(["প্রশ্ন (LightOJ, Guilty Prince): '@' হলো রাজপুত্রের শুরুর ঘর, '#' দেয়াল, '.' ফাঁকা ঘর। রাজপুত্র কয়টা ঘরে যেতে পারবে (নিজের ঘরসহ)?",
      "`@` ঘর খুঁজে বের করা হয় input পড়ার সময়ই। তারপর `dfs(x, y)` ডাকা হয়। DFS এ প্রতিবার **চার** দিকে চেষ্টা (`i < 4`)।",
      "`valid()` এখন দেয়ালও দেখে: `g[x][y] != '#'`। প্রতিটা নতুন ঘরে ঢুকেই `cnt++`।",
      "test 1 এ 4 × 6 grid। দেয়াল আছে (0, 4) আর (1, 5) এ। ঘর (0, 5) ফাঁকা কিন্তু দুই দেয়ালে ঘেরা, তাই DFS সেখানে ঢুকতে পারে না। ফলে 24 - 2 (দেয়াল) - 1 (ঘেরা ঘর) = **21**।",
      "test 2 এ @ এর চারপাশেই '#', তাই শুধু নিজের ঘর: **1**।"],
     viz=[GF],
     tables=[T(["test", "grid", "পৌঁছানো ঘর"], [[1, "4 × 6", 21], [2, "3 × 3 (চারদিকে দেয়াল)", 1]], "দুই test এর ফল")]))
