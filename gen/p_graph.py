from lib import *

GA = "০১ গ্রাফ রাখার উপায়"
GB = "০২ BFS (Breadth First Search)"
GD = "০৩ DFS (Depth First Search)"
GC = "০৪ Component, Cycle ও Bipartite"
GS = "০৫ Shortest Path (Dijkstra)"
GU = "০৬ Disjoint Set Union (DSU)"
GM = "০৭ Minimum Spanning Tree"

G1 = "6 7\n1 2\n1 3\n2 4\n2 5\n3 5\n4 6\n5 6"

# ───────────── গ্রাফ রাখার উপায় ─────────────
MAT = "const int mx = 101;\nint graph[mx][mx];"
MAT_BUILD = """int n, e;
cin >> n >> e;
for (int i = 1; i <= e; i++)
{
    int v1, v2;
    cin >> v1 >> v2;
    graph[v1][v2] = 1;
    graph[v2][v1] = 1;
}
"""
P("graph", GA, "graph-adj-matrix", "Adjacency Matrix",
  "n টা node এর জন্য n × n এর একটা 2D array নেওয়া হয়। u আর v এর মধ্যে edge থাকলে graph[u][v] = 1, না থাকলে 0। কোনো দুটো node জোড়ার মধ্যে edge আছে কিনা এক ধাপেই বলা যায়।",
  "int graph[mx][mx];\ngraph[u][v] = 1;\ngraph[v][u] = 1;   // undirected হলে দুই দিকেই", "Space O(N²), edge check O(1)",
  E("matrix বানিয়ে ছাপো", MAT_BUILD + "for (int i = 1; i <= n; i++)\n{\n    for (int j = 1; j <= n; j++)\n        cout << graph[i][j] << ' ';\n    cout << endl;\n}",
    "6 টা node, 7 টা edge। undirected তাই graph[u][v] আর graph[v][u] দুটোই 1 হয়েছে এবং matrix টা কর্ণ বরাবর (diagonal) আয়নার মতো মিলে যায়।", G1, MAT),
  E("edge আছে কিনা — O(1) এ", MAT_BUILD + "int q;\ncin >> q;\nwhile (q--)\n{\n    int a, b;\n    cin >> a >> b;\n    cout << a << \" - \" << b << \" : \" << (graph[a][b] ? \"YES\" : \"NO\") << endl;\n}",
    "graph[a][b] দেখেই সাথে সাথে উত্তর পাওয়া যায়, কোনো loop লাগে না। এটাই Matrix এর সবচেয়ে বড় সুবিধা।", G1 + "\n4\n1 2\n1 6\n5 6\n3 4", MAT))

ADJ = "const int N = 1e3 + 10;"
P("graph", GA, "graph-adj-list", "Adjacency List (Unweighted)",
  "প্রতিটা node এর জন্য একটা vector রাখা হয়, যেখানে শুধু তার প্রতিবেশী (neighbor) node গুলো থাকে। যত edge আছে ঠিক ততটুকুই জায়গা লাগে, তাই বড় graph এ এটাই সবচেয়ে বেশি ব্যবহার হয়।",
  "vector<vector<int>> graph(N);\ngraph[u].push_back(v);\ngraph[v].push_back(u);   // undirected হলে",
  "Space O(N + E)",
  E("প্রতিটা node এর প্রতিবেশী ছাপো", "vector<vector<int>> graph(N);\nint n, e;\ncin >> n >> e;\nfor (int i = 1; i <= e; i++)\n{\n    int v1, v2;\n    cin >> v1 >> v2;\n    graph[v1].push_back(v2);\n    graph[v2].push_back(v1);\n}\nfor (int i = 1; i <= n; i++)\n{\n    cout << \"Node \" << i << \" is connected to : \";\n    for (auto neighbor : graph[i])\n        cout << \" \" << neighbor;\n    cout << endl;\n}",
    "edge যে ক্রমে input এ এসেছে প্রতিবেশীরা সেই ক্রমেই vector এ বসেছে। যেমন node 2 এর কাছে আগে 1 (edge 1-2), তারপর 4, তারপর 5 এসেছে।", G1, ADJ),
  E("Directed graph — শুধু একদিকে", "vector<vector<int>> graph(N);\nint n, e;\ncin >> n >> e;\nfor (int i = 1; i <= e; i++)\n{\n    int u, v;\n    cin >> u >> v;\n    graph[u].push_back(v);   // শুধু u থেকে v\n}\nfor (int i = 1; i <= n; i++)\n{\n    cout << i << \" -> \";\n    for (auto v : graph[i]) cout << v << ' ';\n    cout << endl;\n}",
    "directed graph এ u → v edge এর জন্য শুধু graph[u].push_back(v) করা হয়। তাই node 2 থেকে বের হওয়ার edge নেই বলে তার তালিকা ফাঁকা।", "4 4\n1 2\n1 3\n3 2\n4 3", ADJ),
  E("প্রতিটা node এর degree", "vector<vector<int>> graph(N);\nint n, e;\ncin >> n >> e;\nfor (int i = 1; i <= e; i++)\n{\n    int v1, v2;\n    cin >> v1 >> v2;\n    graph[v1].push_back(v2);\n    graph[v2].push_back(v1);\n}\nfor (int i = 1; i <= n; i++)\n    cout << \"degree of \" << i << \" = \" << graph[i].size() << endl;",
    "node এর degree মানে তার সাথে কয়টা edge লেগে আছে। graph[i].size() ই সেই সংখ্যা। সব degree এর যোগফল 14 = 2 × 7 (edge সংখ্যার দ্বিগুণ)।", G1, ADJ))

WCODE = "vector<vector<pair<int, int>>> graph(N);\nint n, e;\ncin >> n >> e;\nfor (int i = 1; i <= e; i++)\n{\n    int u, v, cost;\n    cin >> u >> v >> cost;\n    graph[u].push_back({v, cost});\n    graph[v].push_back({u, cost});\n}\nfor (int i = 1; i <= n; i++)\n{\n    cout << \"Node \" << i << \" is connected to : \";\n    for (auto edge : graph[i])\n    {\n        int v = edge.first;\n        int cost = edge.second;\n        cout << \" ( Node : \" << v << \" , Weight : \" << cost << \")\";\n    }\n    cout << endl;\n}"
P("graph", GA, "graph-adj-list-weighted", "Adjacency List (Weighted)",
  "edge এ ওজন (cost বা distance) থাকলে vector এ শুধু node না রেখে pair<node, cost> রাখতে হয়। shortest path (Dijkstra) আর MST (Kruskal/Prim) এই রকম graph এই ভাবেই রাখে।",
  "vector<vector<pair<int,int>>> graph(N);\ngraph[u].push_back({v, cost});\ngraph[v].push_back({u, cost});", "Space O(N + E)",
  E("পরিষ্কার একটা weighted graph", WCODE, "node 1 এর প্রতিবেশী 2 (cost 4) আর 3 (cost 2)। প্রতিটা entry তে node আর cost দুটোই আছে, যা Dijkstra তে লাগবে।", "5 6\n1 2 4\n1 3 2\n2 3 1\n2 4 5\n3 4 8\n4 5 3", ADJ),
  E("Multiple edge ও self-loop", WCODE, "node 1 আর 2 এর মধ্যে তিনটা আলাদা edge (10, 13, 14) আছে, তিনটাই জমা হয়েছে। আর 2 2 2 (self-loop) এ graph[2] তে দুইবার ঢুকে গেছে, কারণ কোডে u ও v দুই দিকেই push হয়। এই ধরনের input এ সাবধান থাকতে হয়।", "4 6\n1 2 10\n1 2 13\n1 2 14\n2 4 3\n2 3 2\n2 2 2", ADJ))

# ───────────── BFS ─────────────
BFS = """const int mx = 1e3;
vector<vector<int>> g(mx);
vector<bool> vis(mx);

void bfs(int source)
{
    queue<int> q;
    q.push(source);
    vis[source] = 1;
    while (!q.empty())
    {
        int current_vertex = q.front();
        q.pop();
        cout << current_vertex << ' ';
        for (auto child : g[current_vertex])
        {
            if (!vis[child])
            {
                q.push(child);
                vis[child] = 1;
            }
        }
    }
}"""
READ = "int nodes, e;\ncin >> nodes >> e;\nfor (int i = 0; i < e; i++)\n{\n    int u, v;\n    cin >> u >> v;\n    g[u].push_back(v);\n    g[v].push_back(u);\n}\n"
P("graph", GB, "graph-bfs", "BFS (Queue দিয়ে)",
  "BFS মানে source থেকে শুরু করে আগে কাছের সব node, তারপর তার পরের স্তরের node — এভাবে ঢেউয়ের মতো ছড়িয়ে যাওয়া। এটা queue দিয়ে করা হয় (যে আগে ঢুকবে সে আগে বের হবে)। vis array দিয়ে একই node দুইবার ঢোকা আটকানো হয়।",
  "queue<int> q;\nq.push(source);  vis[source] = 1;\nwhile (!q.empty()) {\n    int v = q.front();  q.pop();\n    for (auto child : g[v])\n        if (!vis[child]) { q.push(child); vis[child] = 1; }\n}", "O(N + E)",
  E("node 1 থেকে BFS", READ + "bfs(1);", "1 এর প্রতিবেশী 2, 3 আগে। তারপর 2 এর প্রতিবেশী 4, 5। শেষে 6। অর্থাৎ কাছের স্তর আগে, দূরের স্তর পরে।", G1, BFS),
  E("source বদলালে ক্রম বদলায়", READ + "int source;\ncin >> source;\nbfs(source);", "একই graph এ node 4 থেকে শুরু করলে আগে 4 এর প্রতিবেশী 2, 6, তারপর তাদের প্রতিবেশী 1, 5, শেষে 3 আসে।", G1 + "\n4", BFS))

LVL = """const int mx = 1e3;
vector<vector<int>> g(mx);
vector<int> level(mx);
vector<bool> vis(mx);

void bfs(int source)
{
    queue<int> q;
    q.push(source);
    vis[source] = 1;
    level[source] = 0;
    while (!q.empty())
    {
        int current_vertex = q.front();
        q.pop();
        for (auto child : g[current_vertex])
        {
            if (!vis[child])
            {
                q.push(child);
                vis[child] = 1;
                level[child] = level[current_vertex] + 1;
            }
        }
    }
}"""
P("graph", GB, "graph-bfs-level", "BFS এ Level (Shortest Path)",
  "BFS এ প্রতিটা node কে প্রথমবার যখন পাওয়া যায়, তখন level[child] = level[parent] + 1 লিখে রাখলে level[v] হয়ে যায় source থেকে v এ যেতে সবচেয়ে কম কয়টা edge পার হতে হয়। unweighted graph এ এটাই shortest path।",
  "level[source] = 0;\nlevel[child] = level[current_vertex] + 1;", "O(N + E)",
  E("সব node এর level", READ + "bfs(1);\nfor (int i = 1; i <= nodes; i++)\n    cout << i << \" : \" << level[i] << endl;", "1 এর level 0। 2 ও 3 এর level 1। 4 ও 5 এর level 2। 6 এর level 3। অর্থাৎ 1 থেকে 6 এ যেতে অন্তত 3 টা edge লাগে।", G1, LVL),
  E("Monk and the Islands — 1 থেকে n এ সবচেয়ে কম bridge", "int t;\ncin >> t;\nwhile (t--)\n{\n    int nodes, e;\n    cin >> nodes >> e;\n    for (int i = 0; i <= nodes; i++)\n    {\n        g[i].clear();\n        vis[i] = 0;\n        level[i] = 0;\n    }\n    for (int i = 0; i < e; i++)\n    {\n        int u, v;\n        cin >> u >> v;\n        g[u].push_back(v);\n        g[v].push_back(u);\n    }\n    bfs(1);\n    cout << level[nodes] << endl;\n}",
    "প্রশ্নে 1 নম্বর দ্বীপ থেকে n নম্বর দ্বীপে কম সংখ্যক bridge পার হয়ে যেতে হবে। প্রতি test এ আগে g, vis, level পরিষ্কার করা হয়, তারপর bfs(1) চালিয়ে level[n] ছাপা হয়।", "2\n3 2\n1 2\n2 3\n4 4\n1 2\n2 3\n3 4\n1 4", LVL))

PATHB = """const int mx = 1e3;
vector<vector<int>> g(mx);
bool vis[mx];
int level[mx], parent[mx];

void bfs(int source)
{
    queue<int> q;
    q.push(source);
    vis[source] = 1;
    level[source] = 0;
    parent[source] = 0;
    while (!q.empty())
    {
        int u = q.front();
        q.pop();
        for (auto v : g[u])
        {
            if (!vis[v])
            {
                vis[v] = 1;
                level[v] = level[u] + 1;
                parent[v] = u;
                q.push(v);
            }
        }
    }
}"""
PATHMAIN = READ + "int source, target;\ncin >> source >> target;\nbfs(source);\ncout << \"দূরত্ব = \" << level[target] << \"\\n\";\nvector<int> path;\nfor (int v = target; v != 0; v = parent[v])\n    path.push_back(v);\nreverse(path.begin(), path.end());\nfor (int i = 0; i < (int)path.size(); i++)\n{\n    if (i) cout << \" -> \";\n    cout << path[i];\n}\ncout << \"\\n\";"
P("graph", GB, "graph-bfs-path", "BFS দিয়ে আসল পথ বের করা (parent[])",
  "শুধু দূরত্ব জানলে হয় না, অনেক সময় পুরো পথটাও লাগে। BFS এ নতুন node v পাওয়ার সময় parent[v] = u লিখে রাখলে প্রতিটা node জানে সে কোথা থেকে এসেছে। গন্তব্য থেকে parent ধরে ধরে পিছিয়ে সোর্সে পৌঁছালেই পুরো পথ পাওয়া যায় (উল্টো ক্রমে, তাই শেষে reverse করতে হয়)।",
  "parent[child] = current_vertex;\nfor (int v = target; v != 0; v = parent[v])\n    path.push_back(v);\nreverse(path.begin(), path.end());", "O(N + E)",
  E("1 থেকে 6 এ যাওয়ার পথ", PATHMAIN, "level[6] = 3, অর্থাৎ ৩টা edge। parent ধরে 6 → 4 → 2 → 1 এসে reverse করে পাওয়া গেছে পথ।", G1 + "\n1 6", PATHB),
  E("3 থেকে 4 এ যাওয়ার পথ", PATHMAIN, "source বদলালে পথও বদলায়। এখানে 3 → 1 → 2 → 4, আবার ৩টা edge।", G1 + "\n3 4", PATHB))

GRIDPRE = """int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
bool vis[1000][1000];
int row, column;

bool valid(int x, int y)
{
    return (x >= 0 and x < row and y >= 0 and y < column and !vis[x][y]);
}

void bfs(int source_x, int source_y)
{
    queue<pair<int, int>> q;
    q.push({source_x, source_y});
    vis[source_x][source_y] = 1;
    while (!q.empty())
    {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();
        for (int i = 0; i < 8; i++)
        {
            int next_x = x + dx[i];
            int next_y = y + dy[i];
            if (valid(next_x, next_y))
            {
                vis[next_x][next_y] = 1;
                q.push({next_x, next_y});
            }
        }
    }
}"""
MAZE = """int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
int row, column;
vector<string> grid;
int dist[50][50];

bool valid(int x, int y)
{
    return (x >= 0 and x < row and y >= 0 and y < column and grid[x][y] != '#' and dist[x][y] == -1);
}"""
P("graph", GB, "graph-bfs-grid", "BFS on Grid",
  "grid কেও graph ভাবা যায়: প্রতিটা ঘর একটা node, আর পাশের ঘর (উপর, নিচে, বামে, ডানে) তার প্রতিবেশী। dx[] আর dy[] array দিয়ে চার (বা আট) দিকে যাওয়া হয়, আর valid() দিয়ে দেখা হয় ঘরটা grid এর ভেতরে আছে কিনা।",
  "int dx[] = {-1, 1, 0, 0};\nint dy[] = {0, 0, -1, 1};\nnx = x + dx[i];  ny = y + dy[i];\nif (valid(nx, ny)) { ... }", "O(row × column)",
  E("5 × 5 grid, ৮ দিকে BFS", "row = column = 5;\nbfs(2, 2);\nfor (int i = 0; i < 5; i++)\n{\n    for (int j = 0; j < 5; j++)\n        cout << vis[i][j] << ' ';\n    cout << endl;\n}",
    "মাঝের ঘর (2, 2) থেকে শুরু করে আট দিকে ছড়িয়ে পুরো grid এ পৌঁছানো গেছে, তাই সব ঘর 1। লক্ষ করো: row আর column এ মান বসাতে হয়েছে, নাহলে valid() সবসময় false হতো।", "", GRIDPRE),
  E("Maze এ S থেকে E এর সবচেয়ে কম ধাপ (4 দিক)", "cin >> row >> column;\ngrid.resize(row);\nint sx = 0, sy = 0, ex = 0, ey = 0;\nfor (int i = 0; i < row; i++)\n{\n    cin >> grid[i];\n    for (int j = 0; j < column; j++)\n    {\n        dist[i][j] = -1;\n        if (grid[i][j] == 'S') sx = i, sy = j;\n        if (grid[i][j] == 'E') ex = i, ey = j;\n    }\n}\nqueue<pair<int, int>> q;\nq.push({sx, sy});\ndist[sx][sy] = 0;\nwhile (!q.empty())\n{\n    int x = q.front().first, y = q.front().second;\n    q.pop();\n    for (int i = 0; i < 4; i++)\n    {\n        int nx = x + dx[i], ny = y + dy[i];\n        if (valid(nx, ny))\n        {\n            dist[nx][ny] = dist[x][y] + 1;\n            q.push({nx, ny});\n        }\n    }\n}\ncout << dist[ex][ey];",
    "'#' হলো দেয়াল, S শুরু, E শেষ। প্রতিটা ঘরের dist এ শুরু থেকে কত ধাপ লাগে সেটা জমা হয়। শেষে dist[E] ই উত্তর। BFS এ প্রথমবার যে ঘরে পৌঁছানো যায় সেটাই সবচেয়ে কম ধাপের পথ।", "5 5\nS..#.\n.#...\n.#.#.\n...#.\n.#..E", MAZE))

# ───────────── DFS ─────────────
DFS = """vector<vector<int>> adj(1e5);
bool vis[12345];

void dfs(int v)
{
    vis[v] = 1;
    cout << v << ' ';
    for (auto child : adj[v])
    {
        if (!vis[child])
            dfs(child);
    }
}"""
DREAD = "int nodes, e;\ncin >> nodes >> e;\nfor (int i = 0; i < e; i++)\n{\n    int u, v;\n    cin >> u >> v;\n    adj[u].push_back(v);\n    adj[v].push_back(u);\n}\n"
P("graph", GD, "graph-dfs", "DFS (Recursion দিয়ে)",
  "DFS মানে একটা পথ ধরে যতদূর যাওয়া যায় ততদূর গভীরে যাওয়া, আটকে গেলে পিছিয়ে এসে অন্য পথ ধরা। এটা recursion (বা stack) দিয়ে করা হয়। vis array না থাকলে cycle এ পড়ে অসীম loop হয়ে যাবে।",
  "void dfs(int v)\n{\n    vis[v] = 1;\n    for (auto child : adj[v])\n        if (!vis[child]) dfs(child);\n}", "O(N + E)",
  E("node 1 থেকে DFS", DREAD + "dfs(1);", "1 → 2 → 4 → 6 → 5 → 3। প্রতিবার প্রথম unvisited প্রতিবেশীর দিকে গভীরে গেছে। 5 এ এসে 3 পাওয়া গেছে, তারপর সবাই visited তাই ফিরে আসা শুরু।", G1, DFS),
  E("node 3 থেকে DFS", DREAD + "int start;\ncin >> start;\ndfs(start);", "source আলাদা হলে ক্রমও আলাদা। 3 → 1 → 2 → 4 → 6 → 5।", G1 + "\n3", DFS))

LUV = """const int N = 1e5 + 10;
vector<int> g[N];
bool vis[N];

void dfs(int vertex)
{
    /* ১. vertex এ ঢুকেই যা করার */
    cout << "IN  " << vertex << "\\n";
    vis[vertex] = true;
    for (int child : g[vertex])
    {
        cout << "  parent " << vertex << ", child " << child << "\\n";
        if (vis[child]) continue;
        /* ২. child এ ঢোকার আগে যা করার */
        dfs(child);
        /* ৩. child থেকে ফিরে এসে যা করার */
    }
    /* ৪. vertex থেকে বেরোনোর আগে যা করার */
    cout << "OUT " << vertex << "\\n";
}"""
TREE = "5 4\n1 2\n1 3\n2 4\n2 5"
P("graph", GD, "graph-dfs-luv", "DFS এর ৪টা জায়গা (Enter / Exit)",
  "DFS এ কাজ বসানোর চারটা আলাদা জায়গা আছে: vertex এ ঢুকে, child এ ঢোকার আগে, child থেকে ফিরে এসে, আর vertex থেকে বেরোনোর আগে। কোন কাজ কোথায় বসবে বুঝলে subtree size, depth, cycle, topological sort সবই একই কাঠামোতে লেখা যায়।",
  "void dfs(int v) {\n    /* ঢুকে */\n    for (int child : g[v]) {\n        /* child এর আগে */\n        dfs(child);\n        /* child এর পরে */\n    }\n    /* বেরোনোর আগে */\n}", "O(N + E)",
  E("IN / OUT দেখি", "int n, m;\ncin >> n >> m;\nfor (int i = 0; i < m; i++)\n{\n    int v1, v2;\n    cin >> v1 >> v2;\n    g[v1].push_back(v2);\n    g[v2].push_back(v1);\n}\ndfs(1);", "প্রতিটা vertex এ IN একবার আর OUT একবার ছাপা হয়েছে। IN 2 এর পর IN 4 আর OUT 4 হয়ে তবেই 5 এ গেছে। এটাই recursion এর stack এর খেলা।", TREE, LUV),
  E("Depth আর Subtree Size", "int n, m;\ncin >> n >> m;\nfor (int i = 0; i < m; i++)\n{\n    int v1, v2;\n    cin >> v1 >> v2;\n    g[v1].push_back(v2);\n    g[v2].push_back(v1);\n}\ndfs(1, 0);\nfor (int i = 1; i <= n; i++)\n    cout << \"node \" << i << \" : depth = \" << depth[i] << \", subtree size = \" << sz[i] << endl;",
    "depth নির্ধারণ হয় child এ ঢোকার আগে (depth[child] = depth[v] + 1)। আর subtree size নির্ধারণ হয় child থেকে ফিরে এসে (sz[v] += sz[child])। এই দুই জায়গার পার্থক্যই এই পেজের মূল শিক্ষা।", TREE,
    "const int N = 1e5 + 10;\nvector<int> g[N];\nint depth[N], sz[N];\n\nvoid dfs(int v, int par)\n{\n    sz[v] = 1;\n    for (int child : g[v])\n    {\n        if (child == par) continue;\n        depth[child] = depth[v] + 1;\n        dfs(child, v);\n        sz[v] += sz[child];\n    }\n}"))

COLB = """const int N = 1e5 + 10;
vector<int> adj[N];
int color[N];   // 0 = সাদা, 1 = ধূসর, 2 = কালো
bool has_cycle = false;

void dfs(int u)
{
    color[u] = 1;
    for (int v : adj[u])
    {
        if (color[v] == 0)
            dfs(v);
        else if (color[v] == 1)
        {
            cout << "Back edge: " << u << " -> " << v << "\\n";
            has_cycle = true;
        }
    }
    color[u] = 2;
}"""
COLMAIN = "int n, e;\ncin >> n >> e;\nfor (int i = 0; i < e; i++)\n{\n    int u, v;\n    cin >> u >> v;\n    adj[u].push_back(v);\n}\nfor (int i = 1; i <= n; i++)\n    if (color[i] == 0) dfs(i);\ncout << (has_cycle ? \"Cycle আছে\" : \"Cycle নেই\") << \"\\n\";"
P("graph", GD, "graph-dfs-color", "DFS এর ৩ রং ও Back Edge",
  "DFS এ প্রতিটা node কে তিন রঙে ভাবা যায়: সাদা (এখনো দেখিনি), ধূসর (ঢুকেছি কিন্তু এর থেকে যাওয়ার পথগুলো শেষ হয়নি, মানে recursion এখনো চলছে), কালো (পুরো কাজ শেষ)। DFS চলার সময় কোনো ধূসর node থেকে আরেকটা ধূসর node এ যেতে চাইলে সেটা back edge, আর back edge মানেই graph এ cycle আছে।",
  "if (color[v] == 0) dfs(v);          // tree edge\nelse if (color[v] == 1) { /* back edge → cycle */ }", "O(N + E)",
  E("Cycle আছে (directed graph)", COLMAIN, "1 → 2 → 3 → 4 এ নেমে 4 থেকে 2 এ যেতে চেয়েছে, কিন্তু 2 তখনো ধূসর (কাজ চলছে)। তাই 4 → 2 একটা back edge, আর 2 → 3 → 4 → 2 একটা cycle।", "4 4\n1 2\n2 3\n3 4\n4 2", COLB),
  E("Cycle নেই (DAG)", COLMAIN, "3 থেকে 4 এ যেতে চেয়ে দেখা গেল 4 কালো, অর্থাৎ 4 এর কাজ আগেই শেষ। কালো node এ যাওয়া back edge না, তাই cycle ধরা পড়েনি।", "4 4\n1 2\n1 3\n2 4\n3 4", COLB))

DGRID = """int dx[] = {-1, 1, 0, 0, -1, -1, 1, 1};
int dy[] = {0, 0, -1, 1, -1, 1, -1, 1};
int row, column;
bool vis[5][5];

bool valid(int x, int y)
{
    return (x >= 0 and x < row and y >= 0 and y < column and !vis[x][y]);
}

void dfs(int x, int y)
{
    if (vis[x][y]) return;
    vis[x][y] = 1;
    for (int i = 0; i < 8; i++)
    {
        int next_x = x + dx[i];
        int next_y = y + dy[i];
        if (valid(next_x, next_y))
            dfs(next_x, next_y);
    }
}"""
GUILTY = """const int mx = 30;
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};
bool vis[mx][mx];
char g[mx][mx];
int c, r, cnt = 0;

bool valid(int x, int y)
{
    return (x >= 0 and x < r and y >= 0 and y < c and !vis[x][y] and g[x][y] != '#');
}

void dfs(int x, int y)
{
    if (vis[x][y]) return;
    vis[x][y] = 1;
    cnt++;
    for (int i = 0; i < 4; i++)
    {
        int next_x = x + dx[i];
        int next_y = y + dy[i];
        if (valid(next_x, next_y))
            dfs(next_x, next_y);
    }
}"""
P("graph", GD, "graph-dfs-grid", "DFS on Grid (Flood Fill)",
  "grid এ DFS এর কাজ হলো কোনো ঘর থেকে শুরু করে যতগুলো ঘরে হেঁটে যাওয়া যায় সবগুলো ছুঁয়ে আসা। এটাকে Flood Fill ও বলে। BFS এর মতোই dx, dy আর valid() লাগে, শুধু queue এর জায়গায় recursion।",
  "void dfs(int x, int y)\n{\n    if (vis[x][y]) return;\n    vis[x][y] = 1;\n    for (int i = 0; i < 4; i++)\n        if (valid(x + dx[i], y + dy[i]))\n            dfs(x + dx[i], y + dy[i]);\n}", "O(row × column)",
  E("5 × 5 grid, ৮ দিকে DFS", "row = column = 5;\ndfs(2, 2);\nfor (int i = 0; i < 5; i++)\n{\n    for (int j = 0; j < 5; j++)\n        cout << vis[i][j] << ' ';\n    cout << endl;\n}", "ফাঁকা grid এ মাঝের ঘর থেকে DFS চালালে সবগুলো ঘরই visited হয়। ফলাফল BFS এর মতোই, শুধু ঘরগুলো ঘোরার ক্রম আলাদা।", "", DGRID),
  E("Guilty Prince — কয়টা ঘরে যাওয়া যাবে?", "memset(vis, 0, sizeof(vis));\nint t;\ncin >> t;\nfor (int tc = 1; tc <= t; tc++)\n{\n    memset(vis, 0, sizeof(vis));\n    cnt = 0;\n    int x = 0, y = 0;\n    cin >> c >> r;\n    for (int i = 0; i < r; i++)\n    {\n        for (int j = 0; j < c; j++)\n        {\n            cin >> g[i][j];\n            if (g[i][j] == '@') x = i, y = j;\n        }\n    }\n    dfs(x, y);\n    cout << \"Case \" << tc << \": \" << cnt << endl;\n}",
    "'@' হলো রাজপুত্রের অবস্থান, '#' দেয়াল। @ ঘর থেকে DFS চালিয়ে যতগুলো ঘরে পৌঁছানো যায় cnt তে গোনা হয় (@ ঘরসহ)। দ্বিতীয় test এ চারদিকেই দেয়াল, তাই শুধু নিজের ঘরটাই।", "2\n6 4\n....#.\n.....#\n......\n..@...\n3 3\n.#.\n#@#\n.#.", GUILTY))

# ───────────── Component, Cycle, Bipartite ─────────────
CCP = "bool vis[100000];\nvector<int> g[100000];\nvoid dfs(int v)\n{\n    vis[v] = 1;\n    for (auto child : g[v])\n        if (!vis[child]) dfs(child);\n}"
CCREAD = "int n, e, c = 0;\ncin >> n >> e;\nfor (int i = 0; i < e; i++)\n{\n    int u, v;\n    cin >> u >> v;\n    g[u].push_back(v);\n    g[v].push_back(u);\n}\n"
P("graph", GC, "graph-cc-count", "Connected Component গোনা",
  "graph টা যদি এক টুকরোয় না থাকে, প্রতিটা আলাদা টুকরোকে একটা connected component বলে। সব node এর ওপর ঘুরে যেটা এখনো visited না, সেখান থেকে DFS চালাও। কয়বার DFS শুরু করতে হলো, ততগুলোই component।",
  "for (int i = 1; i <= n; i++)\n    if (!vis[i]) { dfs(i); c++; }", "O(N + E)",
  E("৪ টা টুকরো", CCREAD + "for (int i = 1; i <= n; i++)\n{\n    if (vis[i]) continue;\n    dfs(i);\n    c++;\n}\ncout << c << endl;", "{1,2,3}, {4,5,6}, {7}, {8}। একা পড়ে থাকা node (7 ও 8) ও নিজেরা একেকটা component। তাই মোট 4।", "8 4\n1 2\n2 3\n4 5\n5 6", CCP),
  E("পুরোটা জোড়া থাকলে", CCREAD + "for (int i = 1; i <= n; i++)\n{\n    if (vis[i]) continue;\n    dfs(i);\n    c++;\n}\ncout << c << endl;", "আগের পেজের graph এ সব node একে অন্যের সাথে জোড়া, তাই প্রথম DFS (node 1 থেকে) ই সবাইকে ছুঁয়ে ফেলেছে এবং c = 1।", G1, CCP))

STP = "bool vis[100000];\nvector<int> g[100000];\nvector<vector<int>> cc;\nvector<int> curr_cc;\nvoid dfs(int v)\n{\n    vis[v] = 1;\n    curr_cc.push_back(v);\n    for (auto child : g[v])\n        if (!vis[child]) dfs(child);\n}"
P("graph", GC, "graph-cc-store", "Component এর node গুলো জমা রাখা",
  "শুধু সংখ্যা না, কোন component এ কোন কোন node আছে সেটাও দরকার হতে পারে। প্রতিটা DFS এর শুরুতে curr_cc খালি করো, DFS এর সময় node গুলো তাতে জমাও, শেষে cc তে curr_cc টাকে রেখে দাও।",
  "curr_cc.clear();\ndfs(i);              // dfs এর ভেতরে curr_cc.push_back(v)\ncc.push_back(curr_cc);", "O(N + E)",
  E("প্রতিটা component ছাপো", CCREAD + "for (int i = 1; i <= n; i++)\n{\n    if (vis[i]) continue;\n    curr_cc.clear();\n    dfs(i);\n    cc.push_back(curr_cc);\n    c++;\n}\ncout << c << endl;\nfor (int i = 0; i < (int)cc.size(); i++)\n{\n    sort(cc[i].begin(), cc[i].end());\n    cout << \"Component \" << i + 1 << \" :\";\n    for (auto v : cc[i]) cout << ' ' << v;\n    cout << endl;\n}", "প্রতিটা component আলাদা vector এ জমেছে। DFS এর ক্রমে node গুলো আসে, তাই সুন্দর করে দেখাতে sort করা হয়েছে।", "8 4\n1 2\n2 3\n4 5\n5 6", STP))

CYC = "bool vis[100000];\nvector<int> g[100000];\n\nbool cycledet(int node, int par)\n{\n    vis[node] = 1;\n    for (int child : g[node])\n    {\n        if (!vis[child])\n        {\n            if (cycledet(child, node)) return true;\n        }\n        else if (child != par)\n            return true;\n    }\n    return false;\n}"
CYCMAIN = "int n, e;\ncin >> n >> e;\nfor (int i = 0; i < e; i++)\n{\n    int u, v;\n    cin >> u >> v;\n    g[u].push_back(v);\n    g[v].push_back(u);\n}\nbool found = false;\nfor (int i = 1; i <= n && !found; i++)\n    if (!vis[i]) found = cycledet(i, 0);\ncout << (found ? \"Cycle found\" : \"No cycle\");"
P("graph", GC, "graph-cycle", "Cycle Detection (Undirected)",
  "DFS চালানোর সময় যদি এমন একটা প্রতিবেশী পাওয়া যায় যে আগেই visited আর সে আমার parent না, তাহলে ঘুরে আসার একটা পথ আছে, মানে cycle। parent কে বাদ দিতে হয় কারণ undirected graph এ যে edge দিয়ে এসেছি সেই edge দিয়েই পিছনে যাওয়া যায়।",
  "bool cycledet(int node, int par)\n{\n    vis[node] = 1;\n    for (int child : g[node])\n        if (!vis[child]) { if (cycledet(child, node)) return true; }\n        else if (child != par) return true;\n    return false;\n}", "O(N + E)",
  E("cycle আছে", CYCMAIN, "2 → 3 → 4 → 2 একটা চক্র। DFS এ 4 এ এসে প্রতিবেশী 2 পেল যে visited, আবার 4 এর parent (3) ও না। তাই true।", "5 5\n1 2\n2 3\n3 4\n4 2\n4 5", CYC),
  E("Tree তে cycle থাকে না", CYCMAIN, "n টা node আর n - 1 টা edge এর জোড়া graph (tree) এ cycle থাকে না। এখানে প্রতিটা visited প্রতিবেশীই parent, তাই কখনো true হয়নি।", "5 4\n1 2\n1 3\n3 4\n3 5", CYC))

UW = """const int mx = 2e4 + 123;
vector<bool> vis(mx);
vector<bool> is_dual(mx);
vector<vector<int>> g(mx);
int curr_cc_size, color_1;

void dfs(int v, int color)
{
    vis[v] = 1;
    if (color == 1) color_1++;
    curr_cc_size++;
    int new_color = (color == 1 ? 2 : 1);
    for (auto child : g[v])
        if (!vis[child]) dfs(child, new_color);
}

void clear_data()
{
    for (int i = 1; i < mx; i++)
    {
        g[i].clear();
        vis[i] = 0;
        is_dual[i] = 0;
    }
}

void solve(int t)
{
    clear_data();
    int e, ans = 0;
    cin >> e;
    for (int i = 0; i < e; i++)
    {
        int u, v;
        cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u);
        is_dual[u] = 1;
        is_dual[v] = 1;
    }
    for (int i = 1; i < mx; i++)
    {
        if (is_dual[i] and !vis[i])
        {
            curr_cc_size = 0, color_1 = 0;
            dfs(i, 1);
            ans += max(color_1, (curr_cc_size - color_1));
        }
    }
    cout << "Case " << t << ": " << ans << endl;
}"""
P("graph", GC, "graph-bipartite", "Bipartite Coloring (Back to Underworld)",
  "যদি node গুলোকে দুই রঙে এমনভাবে রং করা যায় যেন প্রতিটা edge এর দুই মাথা আলাদা রঙের হয়, তাকে bipartite graph বলে। DFS এ parent এর উল্টো রঙ child কে দিয়ে গেলেই এটা হয়ে যায়। LightOJ এর Back to Underworld এই ধরনের প্রশ্ন।",
  "void dfs(int v, int color)\n{\n    vis[v] = 1;\n    for (auto child : g[v])\n        if (!vis[child]) dfs(child, color == 1 ? 2 : 1);\n}", "O(N + E)",
  E("প্রতিটা component থেকে বড় দলটা নাও", "int t;\ncin >> t;\nfor (int i = 1; i <= t; i++)\n    solve(i);", "প্রতিটা component এ দুই রঙ করলে দুইটা দল হয়। শত্রুরা সবসময় আলাদা দলে, তাই একটা component থেকে বড় দলের সবাইকে নেওয়াই সবচেয়ে ভালো। সব component এর বড় দলের যোগফলই উত্তর।", "2\n2\n1 2\n2 3\n3\n1 2\n3 4\n4 5", UW),
  E("Star graph", "int t;\ncin >> t;\nfor (int i = 1; i <= t; i++)\n    solve(i);", "মাঝে 1 আর চারদিকে 2, 3, 4, 5। 1 এর রঙ আলাদা বলে একদিকে 1 জন, অন্যদিকে 4 জন। বড় দলে 4 জন।", "1\n4\n1 2\n1 3\n1 4\n1 5", UW))

# ───────────── Dijkstra ─────────────
DIJ = """const int inf = 1e7;
const int n = 1e3;
vector<pair<int, int>> g[n];
// { node, cost }

void dijkstra(int source, int nodes)
{
    vector<int> distance(n, inf);
    vector<bool> visited(n, 0);
    set<pair<int, int>> st;
    // { cost, node } : cost আগে থাকে বলে সবচেয়ে কম cost টাই আগে আসে
    st.insert({0, source});
    distance[source] = 0;
    while (!st.empty())
    {
        auto node = *st.begin();
        int parent_node = node.second;
        int parent_node_cost = node.first;
        st.erase(st.begin());
        if (visited[parent_node]) continue;
        visited[parent_node] = 1;
        for (auto child : g[parent_node])
        {
            int child_node = child.first;
            int edge_cost = child.second;
            // Relaxation
            if ((parent_node_cost + edge_cost) < distance[child_node])
            {
                distance[child_node] = (parent_node_cost + edge_cost);
                st.insert({distance[child_node], child_node});
            }
        }
    }
    cout << "Node\\tDistance from " << source << endl;
    for (int i = 0; i <= nodes; i++)
        if (distance[i] != inf)
            cout << i << "\\t" << distance[i] << endl;
}"""
DREAD2 = "int node, edge, source;\ncin >> node >> edge;\nfor (int i = 0; i < edge; i++)\n{\n    int u, v, cost;\n    cin >> u >> v >> cost;\n    g[u].push_back({v, cost});\n    g[v].push_back({u, cost});\n}\ncin >> source;\ndijkstra(source, node);"
P("graph", GS, "graph-dijkstra", "Dijkstra (set দিয়ে)",
  "weighted graph এ source থেকে সব node এর সবচেয়ে কম খরচের দূরত্ব বের করার algorithm। প্রতিবার সবচেয়ে কম দূরত্বের node টাকে নেওয়া হয়, তারপর তার প্রতিবেশীদের দূরত্ব কমানো যায় কিনা দেখা হয় (এটাকে Relaxation বলে)। edge এর cost ঋণাত্মক হলে চলবে না।",
  "set<pair<int,int>> st;      // { cost, node }\nst.insert({0, source});  distance[source] = 0;\nwhile (!st.empty()) {\n    auto [cost, u] = *st.begin();  st.erase(st.begin());\n    for (auto [v, w] : g[u])\n        if (cost + w < distance[v]) { distance[v] = cost + w; st.insert({distance[v], v}); }\n}", "O((N + E) log N)",
  E("ছোট একটা graph (source = 1)", DREAD2, "1 থেকে 3 এ সরাসরি 2। 3 হয়ে 2 এ গেলে 2 + 1 = 3 (সরাসরি 4 এর চেয়ে কম)। 4 এ 2 হয়ে 3 + 5 = 8 (3 হয়ে 2 + 8 = 10 এর চেয়ে কম)। 5 এ 8 + 3 = 11।", "5 6\n1 2 4\n1 3 2\n2 3 1\n2 4 5\n3 4 8\n4 5 3\n1", DIJ),
  E("৮ node এর বড় graph (source = 0)", DREAD2, "0 থেকে বাকি সব node এর shortest distance। যেমন 0 → 1 সরাসরি 9 হলেও 0 → 3 → 4 → ... পথে কম খরচ হতে পারে, algorithm নিজেই সবচেয়ে কম খরচেরটা বেছে নেয়।", "8 17\n0 1 9\n0 4 7\n0 3 3\n1 4 8\n1 5 11\n1 7 6\n1 3 17\n1 2 2\n2 7 3\n2 6 11\n2 5 19\n3 4 5\n4 6 5\n4 5 12\n5 7 13\n5 6 6\n6 7 8\n0", DIJ))

# ───────────── DSU ─────────────
DSU = """const int mx = 1e5 + 10;
vector<int> parent(mx);
vector<int> set_size(mx);

void make(int v)
{
    parent[v] = v;
    set_size[v] = 1;
}

int find(int v)
{
    if (v == parent[v]) return v;
    // path compression
    return parent[v] = find(parent[v]);
}

void union_sets(int a, int b)
{
    a = find(a);
    b = find(b);
    if (a != b)
    {
        // Union by size
        if (set_size[a] < set_size[b]) swap(a, b);
        parent[b] = a;
        set_size[a] += set_size[b];
    }
}"""
P("graph", GU, "graph-dsu", "Disjoint Set Union (Union-Find)",
  "অনেকগুলো আলাদা দল (set) নিয়ে কাজ করার data structure। প্রতিটা দলের একজন নেতা (root) থাকে। find(v) দিয়ে v এর নেতা পাওয়া যায়, আর union_sets(a, b) দিয়ে দুই দল এক করা যায়। Path compression আর Union by size দিয়ে প্রায় O(1) এ কাজ হয়।",
  "make(v);            // v নিজেই নিজের নেতা\nfind(v);            // v এর নেতা কে?\nunion_sets(a, b);   // দুই দল এক করো", "প্রায় O(1) (amortized)",
  E("কয়টা দল তৈরি হলো?", "int n, q;\ncin >> n >> q;\nfor (int i = 1; i <= n; i++) make(i);\nwhile (q--)\n{\n    int u, v;\n    cin >> u >> v;\n    union_sets(u, v);\n}\nint connected_components = 0;\nfor (int i = 1; i <= n; i++)\n    if (find(i) == i) connected_components++;\ncout << connected_components;", "যার নেতা সে নিজেই (find(i) == i), সেই হলো এক একটা দলের প্রতিনিধি। তাই প্রতিনিধি গুনলেই দলের সংখ্যা পাওয়া যায়।", "8 5\n1 2\n3 4\n2 3\n5 6\n4 1", DSU),
  E("parent আর size ভেতরে কেমন বদলায়", "int n, q;\ncin >> n >> q;\nfor (int i = 1; i <= n; i++) make(i);\nwhile (q--)\n{\n    int u, v;\n    cin >> u >> v;\n    union_sets(u, v);\n    cout << \"union(\" << u << \", \" << v << \")  parent :\";\n    for (int i = 1; i <= n; i++) cout << ' ' << parent[i];\n    cout << endl;\n}\ncout << \"size of root 1 = \" << set_size[find(1)];", "প্রতিটা union এর পর parent[] কেমন হলো দেখা যাচ্ছে। বড় দল ছোট দলের নেতা হয়, তাই tree কখনো লম্বা হয় না। শেষে 1 এর দলে 4 জন।", "6 4\n1 2\n3 4\n2 3\n5 6", DSU))

P("graph", GU, "graph-dsu-problems", "DSU এর দুটো প্রশ্ন",
  "DSU তে দল গোনা আর প্রতিটা দলের সাইজ জানা, এই দুটো কাজ হলো সবচেয়ে বেশি আসা প্রশ্ন। HackerEarth এর City and Flood আর City and Campers এই দুটোর সরাসরি উদাহরণ।",
  "union_sets(u, v);\nset_size[find(v)];   // v এর দলের সাইজ", "প্রায় O(1) প্রতি query",
  E("City and Flood — কয়টা আলাদা এলাকা?", "int n, q;\ncin >> n >> q;\nfor (int i = 1; i <= n; i++) make(i);\nwhile (q--)\n{\n    int u, v;\n    cin >> u >> v;\n    union_sets(u, v);\n}\nint c = 0;\nfor (int i = 1; i <= n; i++)\n    if (find(i) == i) c++;\ncout << c << endl;", "n টা শহর, q টা রাস্তা। রাস্তা দিয়ে জোড়া শহরগুলো এক দলে। শেষে দলের সংখ্যাই উত্তর। এখানে {1,2}, {3,4}, {5} মোট 3।", "5 3\n1 2\n3 4\n2 1", DSU),
  E("City and Campers — প্রতি union এ (বড় দল − ছোট দল)", "int n, q;\ncin >> n >> q;\nmultiset<int> camper_group;\nfor (int i = 1; i <= n; i++)\n{\n    make(i);\n    camper_group.insert(1);\n}\nwhile (q--)\n{\n    int u, v;\n    cin >> u >> v;\n    int a = find(u), b = find(v);\n    if (a != b)\n    {\n        camper_group.erase(camper_group.find(set_size[a]));\n        camper_group.erase(camper_group.find(set_size[b]));\n        camper_group.insert(set_size[a] + set_size[b]);\n        union_sets(a, b);\n    }\n    if (camper_group.size() == 1) cout << 0 << endl;\n    else cout << (*camper_group.rbegin() - *camper_group.begin()) << endl;\n}",
    "multiset এ সব দলের সাইজ রাখা হয়েছে। union এর আগে দুই দলের সাইজ তুলে ফেলে যোগফল বসানো হয়। multiset এর begin() সবচেয়ে ছোট আর rbegin() সবচেয়ে বড় দল দেয়। সব এক দল হয়ে গেলে উত্তর 0।", "5 4\n1 2\n3 4\n2 3\n4 5", DSU))

# ───────────── MST ─────────────
KRU = "const int mx = 1e5 + 10;\nvector<int> parent(mx);\nvector<int> set_size(mx);\n\nvoid make(int v)\n{\n    parent[v] = v;\n    set_size[v] = 1;\n}\nint find(int v)\n{\n    if (v == parent[v]) return v;\n    return parent[v] = find(parent[v]);\n}\nvoid union_sets(int a, int b)\n{\n    a = find(a);\n    b = find(b);\n    if (a != b)\n    {\n        if (set_size[a] < set_size[b]) swap(a, b);\n        parent[b] = a;\n        set_size[a] += set_size[b];\n    }\n}"
KMAIN = "int n, e, total_cost = 0;\ncin >> n >> e;\nvector<pair<int, pair<int, int>>> edges;\nfor (int i = 0; i < e; i++)\n{\n    int u, v, wt;\n    cin >> u >> v >> wt;\n    edges.push_back({wt, {u, v}});\n}\nsort(edges.begin(), edges.end());\nfor (int i = 1; i <= n; i++) make(i);\nfor (auto edge : edges)\n{\n    int wt = edge.first;\n    int u = edge.second.first;\n    int v = edge.second.second;\n    if (find(u) == find(v)) continue;\n    union_sets(u, v);\n    total_cost += wt;\n    cout << \"take \" << u << \" - \" << v << \" (\" << wt << \")\" << endl;\n}\ncout << \"Minimum Cost Spanning Tree Cost = \" << total_cost << endl;"
MST1 = "4 5\n1 2 1\n2 3 2\n3 4 3\n4 1 4\n1 3 5"
MST2 = "8 17\n1 2 9\n1 5 7\n1 4 3\n2 5 8\n2 6 11\n2 8 6\n2 4 17\n2 3 2\n3 8 3\n3 7 11\n3 6 19\n4 5 5\n5 7 5\n5 6 12\n6 8 13\n6 7 6\n7 8 8"
P("graph", GM, "graph-kruskal", "Kruskal's Algorithm",
  "সব edge কে cost অনুযায়ী ছোট থেকে বড় সাজাও। একে একে নাও, কিন্তু যে edge নিলে cycle তৈরি হবে (দুই মাথা আগে থেকেই এক দলে) সেটা বাদ দাও। cycle আছে কিনা DSU দিয়ে সাথে সাথে বোঝা যায়। n - 1 টা edge নেওয়া হলে Minimum Spanning Tree তৈরি।",
  "sort(edges.begin(), edges.end());\nfor (auto [wt, uv] : edges)\n    if (find(u) != find(v)) { union_sets(u, v); total_cost += wt; }", "O(E log E)",
  E("ছোট graph (৪ node)", KMAIN, "edge গুলো cost এর ক্রমে: 1, 2, 3, 4, 5। প্রথম তিনটা নেওয়া হয়েছে (1, 2, 3 দিয়ে চারটা node জোড়া হয়ে গেল)। 4 আর 5 নিলে cycle হতো, তাই বাদ। মোট 1 + 2 + 3 = 6।", MST1, KRU),
  E("৮ node, ১৭ edge", KMAIN, "17 টা edge থেকে শুধু 7 টা (= 8 - 1) নেওয়া হয়েছে। ছোট cost আগে নেওয়া হয়, আর যেটা cycle বানায় সেটা বাদ যায়। শেষে মোট cost ই Minimum Spanning Tree এর cost।", MST2, KRU))

PRIM = "const int MAX = 1e4 + 5;\ntypedef pair<long long, int> PII;\nbool marked[MAX];\nvector<PII> adj[MAX];\n\nlong long prim(int x)\n{\n    priority_queue<PII, vector<PII>, greater<PII>> Q;\n    long long minimumCost = 0;\n    Q.push({0, x});\n    while (!Q.empty())\n    {\n        PII p = Q.top();\n        Q.pop();\n        x = p.second;\n        if (marked[x]) continue;\n        minimumCost += p.first;\n        marked[x] = true;\n        for (int i = 0; i < (int)adj[x].size(); ++i)\n        {\n            int y = adj[x][i].second;\n            if (!marked[y]) Q.push(adj[x][i]);\n        }\n    }\n    return minimumCost;\n}"
PMAIN = "int nodes, edges, x, y, weight;\ncin >> nodes >> edges;\nfor (int i = 0; i < edges; ++i)\n{\n    cin >> x >> y >> weight;\n    adj[x].push_back({weight, y});\n    adj[y].push_back({weight, x});\n}\ncout << \"Minimum Cost = \" << prim(1) << endl;"
P("graph", GM, "graph-prim", "Prim's Algorithm",
  "একটা node থেকে শুরু করে একটু একটু করে tree বাড়ানো হয়। প্রতিবার tree এর বাইরের সবচেয়ে সস্তা edge টাই নেওয়া হয়। priority_queue (min-heap) দিয়ে সবচেয়ে ছোট cost এর edge দ্রুত পাওয়া যায়। Kruskal এর মতোই একই MST cost দেয়।",
  "priority_queue<PII, vector<PII>, greater<PII>> Q;   // { cost, node }\nQ.push({0, start});\nwhile (!Q.empty()) { নিয়ে marked না হলে cost যোগ করো, প্রতিবেশী push করো }", "O(E log E)",
  E("ছোট graph (৪ node)", PMAIN, "1 থেকে শুরু। সবচেয়ে সস্তা 1-2 (1), তারপর 2-3 (2), তারপর 3-4 (3)। মোট 6, Kruskal এর সাথে হুবহু মেলে।", MST1, PRIM),
  E("৮ node, ১৭ edge", PMAIN, "Kruskal এর পেজের একই graph এ Prim চালিয়ে একই cost পাওয়া গেছে। দুই algorithm এর পথ আলাদা, কিন্তু MST এর মোট cost সবসময় সমান।", MST2, PRIM))
