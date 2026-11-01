from lib import *

R1 = "০১ Recursion"
R2 = "০২ Memoization ও Basic DP"

FIBO = """int fibo(int n)
{
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibo(n - 1) + fibo(n - 2);
}"""

CALLS = """int calls = 0;
int fibo(int n)
{
    calls++;
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibo(n - 1) + fibo(n - 2);
}"""

MEMO = """int dp[1000];
int fibo(int n)
{
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (dp[n] != -1) return dp[n];
    dp[n] = fibo(n - 1) + fibo(n - 2);
    return dp[n];
}"""

MEMOC = """int calls = 0;
long long dp[1000];
long long fibo(int n)
{
    calls++;
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (dp[n] != -1) return dp[n];
    dp[n] = fibo(n - 1) + fibo(n - 2);
    return dp[n];
}"""

P("rec", R1, "rec-fibo", "Recursive Function (Fibonacci)",
  "যে function নিজের ভেতর থেকেই নিজেকে ডাকে, তাকে recursive function বলে। থামার জন্য একটা base case লাগে। Fibonacci হলো এর সবচেয়ে ভালো প্রথম উদাহরণ: fibo(n) = fibo(n-1) + fibo(n-2)।",
  "int f(int n)\n{\n    if (base case) return মান;   // থামার শর্ত\n    return f(ছোট n) ...;       // নিজেকে ডাকা\n}", "O(2ⁿ)",
  E("fibo(0) থেকে fibo(n) পর্যন্ত ছাপো", "int n;\ncin >> n;\nfor (int i = 0; i <= n; i++)\n    cout << fibo(i) << ' ';",
    "fibo(0) = 0, fibo(1) = 1 হলো base case। এর পর প্রতিটা সংখ্যা আগের দুইটার যোগফল।", "10", FIBO),
  E("কতবার function ডাকা হলো? (n = 5)", "int n;\ncin >> n;\ncout << \"fibo(\" << n << \") = \" << fibo(n) << endl;\ncout << \"total calls = \" << calls;",
    "fibo(5) বের করতে fibo ডাকা হয়েছে মোট ১৫ বার। অথচ উত্তর মাত্র একটা সংখ্যা।", "5", CALLS),
  E("n = 30 হলে কী হয়?", "int n;\ncin >> n;\ncout << \"fibo(\" << n << \") = \" << fibo(n) << endl;\ncout << \"total calls = \" << calls;",
    "n = 30 তে ২৬ লক্ষের বেশি বার function ডাকা হয়েছে। n = 50 দিলে কয়েক মিনিটেও শেষ হবে না। এই সমস্যার সমাধান পরের পেজে (Memoization)।", "30", CALLS))

P("rec", R2, "rec-memo", "Memoization (Top-Down DP)",
  "একবার যে উত্তর বের করেছি সেটা একটা array তে লিখে রাখি (dp[n])। পরের বার একই n এলে আবার হিসাব না করে array থেকে সরাসরি নিয়ে নেই। এতে O(2ⁿ) কমে O(n) হয়ে যায়।",
  "int dp[N];              // শুরুতে সব -1\nint f(int n)\n{\n    if (base case) return ...;\n    if (dp[n] != -1) return dp[n];   // আগেই করা আছে\n    dp[n] = f(n-1) + f(n-2);         // করে রাখো\n    return dp[n];\n}", "O(n)",
  E("fibo(0) থেকে fibo(n)", "for (int i = 0; i < 1000; i++) dp[i] = -1;\nint n;\ncin >> n;\nfor (int i = 0; i <= n; i++)\n    cout << fibo(i) << ' ';",
    "dp[i] কে শুরুতে -1 করা হয়েছে, মানে \"এখনো জানি না\"। একবার জানা হয়ে গেলে dp[i] তে আসল মান থাকে।", "10", MEMO),
  E("n = 30 — এবার কত বার ডাকা হলো?", "for (int i = 0; i < 1000; i++) dp[i] = -1;\nint n;\ncin >> n;\ncout << \"fibo(\" << n << \") = \" << fibo(n) << endl;\ncout << \"total calls = \" << calls;",
    "আগে যেখানে ২৬ লক্ষের বেশি call লাগছিল, এখন লাগলো মাত্র ৫৯টা (2n - 1)। উত্তর একই, গতি কয়েক হাজার গুণ বেশি।", "30", MEMOC),
  E("Bottom-Up: loop দিয়ে একই কাজ", "int n;\ncin >> n;\nvector<long long> dp(n + 2);\ndp[0] = 0;\ndp[1] = 1;\nfor (int i = 2; i <= n; i++)\n    dp[i] = dp[i - 1] + dp[i - 2];\nfor (int i = 0; i <= n; i++)\n    cout << dp[i] << ' ';",
    "Recursion ছাড়াই ছোট থেকে বড় দিকে loop চালিয়ে dp ভরা যায়। একে Bottom-Up (Tabulation) বলে। দুই পদ্ধতির উত্তর একই।", "10"))

P("rec", R2, "rec-dp-array", "memset, int বনাম long long",
  "dp array কে -1 দিয়ে ভরতে সবচেয়ে সহজ উপায় memset। আর Fibonacci খুব দ্রুত বড় হয়, তাই dp এর type ঠিক না হলে উত্তর ভুল আসে। এই পেজে দুইটাই হাতে-কলমে দেখবে।",
  "memset(dp, -1, sizeof(dp));\nint dp[N];        // n ≤ 46 পর্যন্ত\nlong long dp[N];  // n ≤ 92 পর্যন্ত", "O(n)",
  E("memset দিয়ে dp ভরা (n = 40)", "int n;\ncin >> n;\nmemset(dp, -1, sizeof(dp));\nint result = fibonaccidp(n);\ncout << \"Fibonacci(\" << n << \") = \" << result << endl;",
    "memset(dp, -1, sizeof(dp)) এক লাইনেই পুরো array -1 হয়ে যায়। fibo(40) = 102334155, int এর সীমার ভেতরেই।", "40",
    "const int MAXN = 1000;\nint dp[MAXN];\nint fibonaccidp(int n)\n{\n    if (n <= 0) return 0;\n    if (n == 1) return 1;\n    if (dp[n] != -1) return dp[n];\n    dp[n] = fibonaccidp(n - 1) + fibonaccidp(n - 2);\n    return dp[n];\n}"),
  E("int এ n = 47 — ভুল উত্তর!", "int n;\ncin >> n;\nmemset(dp, -1, sizeof(dp));\nint result = fibonaccidp(n);\ncout << \"Fibonacci(\" << n << \") = \" << result << endl;",
    "fibo(47) = 2971215073, কিন্তু int এর সর্বোচ্চ মান 2147483647। তাই overflow হয়ে ঋণাত্মক সংখ্যা এসেছে। কোড ঠিক থাকলেও type ভুল হওয়ায় উত্তর ভুল।", "47",
    "const int MAXN = 1000;\nint dp[MAXN];\nint fibonaccidp(int n)\n{\n    if (n <= 0) return 0;\n    if (n == 1) return 1;\n    if (dp[n] != -1) return dp[n];\n    dp[n] = fibonaccidp(n - 1) + fibonaccidp(n - 2);\n    return dp[n];\n}"),
  E("long long এ n = 90 — ঠিক উত্তর", "int n;\ncin >> n;\nmemset(dp, -1, sizeof(dp));\nlong long result = fibonaccidp(n);\ncout << \"Fibonacci(\" << n << \") = \" << result << endl;",
    "dp আর return দুটোই long long করায় fibo(90) = 2880067194370816120 ঠিকঠাক এসেছে। long long এ fibo(92) পর্যন্ত নিরাপদ।", "90",
    "const int MAXN = 1000;\nlong long dp[MAXN];\nlong long fibonaccidp(int n)\n{\n    if (n <= 0) return 0;\n    if (n == 1) return 1;\n    if (dp[n] != -1) return dp[n];\n    dp[n] = fibonaccidp(n - 1) + fibonaccidp(n - 2);\n    return dp[n];\n}"))


# ───────────── ০৩ Knapsack — Real Life উদাহরণ সহ ─────────────
R3 = "০৩ Knapsack — Real Life উদাহরণ সহ"
K_IN = "4 8\n2 3\n3 4\n4 5\n5 8"
F_IN = "3 50\n10 60\n20 100\n30 120"
K_BIG = "10 12\n1 1\n2 3\n2 2\n3 4\n1 2\n2 2\n3 5\n1 1\n2 3\n1 1"

K_READ = """int n, W;
cin >> n >> W;
vector<int> w(n + 1), v(n + 1);
for (int i = 1; i <= n; i++)
    cin >> w[i] >> v[i];
"""

K_PRE_MEMO = """int n, W;
int w[105], v[105];
int dp[105][1005];
int calls = 0;

int solve(int i, int cap)
{
    calls++;
    if (i == n + 1 || cap == 0) return 0;
    if (dp[i][cap] != -1) return dp[i][cap];
    int ans = solve(i + 1, cap);                          // না নিলে
    if (w[i] <= cap)
        ans = max(ans, v[i] + solve(i + 1, cap - w[i]));  // নিলে
    return dp[i][cap] = ans;
}"""

P("rec", R3, "rec-knapsack-01", "0/1 Knapsack (Classical DP)",
  "n টা জিনিস, প্রতিটার একটা ওজন (w) আর একটা মূল্য (v)। ব্যাগে সর্বোচ্চ W ওজন ধরে। প্রতিটা জিনিস হয় পুরোটা নেওয়া যাবে, নয়তো একদম না (0 বা 1)। কোন জিনিসগুলো নিলে মোট মূল্য সবচেয়ে বেশি হবে? এটা Dynamic Programming এর সবচেয়ে বিখ্যাত ক্লাসিক সমস্যা।",
  "dp[i][j] = dp[i-1][j];                                  // জিনিস i না নিলে\nif (j >= w[i])\n    dp[i][j] = max(dp[i][j], dp[i-1][j - w[i]] + v[i]);  // নিলে\n// উত্তর: dp[n][W]", "O(n × W)",
  E("Bottom-Up: পুরো dp টেবিল ছাপো",
    K_READ + """
vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));
for (int i = 1; i <= n; i++)
{
    for (int j = 0; j <= W; j++)
    {
        dp[i][j] = dp[i - 1][j];                                // না নিলে
        if (j >= w[i])
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i]);  // নিলে
    }
}
for (int i = 0; i <= n; i++)
{
    for (int j = 0; j <= W; j++)
        cout << dp[i][j] << (j == W ? '\\n' : ' ');
}
cout << "Max value = " << dp[n][W];""",
    "dp[i][j] মানে প্রথম i টা জিনিস থেকে j ওজনের ব্যাগে সর্বোচ্চ মূল্য। প্রতিটা ঘরে 'না নিলে' আর 'নিলে' এর বড়টা বসে। শেষ ঘর dp[4][8] = 12 ই উত্তর।", K_IN),
  E("কোন কোন জিনিস নিলাম? (Traceback)",
    K_READ + """
vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));
for (int i = 1; i <= n; i++)
    for (int j = 0; j <= W; j++)
    {
        dp[i][j] = dp[i - 1][j];
        if (j >= w[i])
            dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i]);
    }

int j = W, totalW = 0;
cout << "Taken items:";
for (int i = n; i >= 1; i--)
{
    if (dp[i][j] != dp[i - 1][j])   // মান বদলেছে মানে i নম্বর জিনিস নেওয়া হয়েছে
    {
        cout << ' ' << i;
        j -= w[i];
        totalW += w[i];
    }
}
cout << endl << "Total weight = " << totalW << endl;
cout << "Total value = " << dp[n][W];""",
    "শুধু উত্তরের সংখ্যা না, কোন জিনিসগুলো নেওয়া হলো সেটাও জানা যায়। শেষ ঘর থেকে উল্টো দিকে হাঁটতে হয়: উপরের ঘরের সাথে মান আলাদা হলে ঐ জিনিসটা নেওয়া হয়েছে, তখন ওজন কমিয়ে ওপরে যাও।", K_IN),
  E("Top-Down: Recursion + Memoization",
    """memset(dp, -1, sizeof(dp));
cin >> n >> W;
for (int i = 1; i <= n; i++)
    cin >> w[i] >> v[i];
cout << "Max value = " << solve(1, W) << endl;
cout << "total calls = " << calls;""",
    "solve(i, cap) মানে i নম্বর জিনিস থেকে শেষ পর্যন্ত, cap ওজনের জায়গা থাকলে সর্বোচ্চ মূল্য কত। Fibonacci এর মতোই dp[i][cap] এ উত্তর লিখে রাখা হয়েছে, তাই একই (i, cap) জোড়া দ্বিতীয়বার এলে সাথে সাথে ফেরত যায়। এবার ১০ টা জিনিস আর ১২ কেজির ব্যাগ নিয়েছি, যাতে memo এর সুবিধা চোখে পড়ে।", K_BIG, K_PRE_MEMO),
  E("Space কমাও: 1D array (লুপ উল্টো দিকে!)",
    K_READ + """
vector<int> dp(W + 1, 0);
for (int i = 1; i <= n; i++)
{
    for (int j = W; j >= w[i]; j--)          // ডান থেকে বামে!
        dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
}
for (int j = 0; j <= W; j++)
    cout << dp[j] << ' ';
cout << endl << "Max value = " << dp[W];""",
    "প্রতিটা সারি শুধু ঠিক আগের সারি থেকে হিসাব হয়, তাই পুরো 2D টেবিল না রেখে একটা সারিই বারবার বদলানো যায়। মেমরি O(n × W) থেকে O(W) হয়ে যায়। কিন্তু j কে অবশ্যই বড় থেকে ছোটর দিকে চালাতে হবে।", K_IN),
  E("ভুল: লুপ সামনের দিকে চালালে কী হয়? (1 টা জিনিস, 3 বার!)",
    K_READ + """
vector<int> dp(W + 1, 0);
for (int i = 1; i <= n; i++)
{
    for (int j = w[i]; j <= W; j++)          // ভুল দিক: বাম থেকে ডানে
        dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
}
cout << "Max value = " << dp[W];""",
    "ব্যাগে ধরে ১০ কেজি, জিনিস মাত্র একটা (৩ কেজি, মূল্য ৫)। ঠিক উত্তর ৫। কিন্তু সামনের দিকে লুপ চালালে ঐ একই জিনিস বারবার নেওয়া হয়ে যায় আর উত্তর ১৫ আসে। এটা আসলে Unbounded Knapsack (যত খুশি নেওয়া যায়) এর হিসাব।", "1 10\n3 5"))

P("rec", R3, "rec-knapsack-fractional", "Fractional Knapsack (Greedy)",
  "এবার জিনিস ভাগ করে নেওয়া যায়: পুরোটা না ধরলে যতটুকু ধরে ততটুকু (ভগ্নাংশ) নেওয়া চলে, আর মূল্যও আনুপাতিক হারে পাওয়া যায়। এখানে DP লাগে না, Greedy ই যথেষ্ট: প্রতি কেজিতে সবচেয়ে বেশি মূল্য যার, তাকে আগে নাও। 0/1 Knapsack এর পাশাপাশি রাখলে দুটোর পার্থক্য পরিষ্কার বোঝা যায়, তাই এই বিভাগেই রাখা হয়েছে।",
  "sort করো  value / weight  বেশি থেকে কম ক্রমে\nপ্রতিটা জিনিসের জন্য:\n    পুরোটা ধরলে → পুরোটা নাও\n    না ধরলে     → যতটুকু ধরে (W / weight) ভাগ নাও, তারপর থামো", "O(n log n)",
  E("Greedy: value / weight এর অনুপাতে sort",
    """int n;
double W;
cin >> n >> W;
vector<pair<double, double>> a(n);      // {ওজন, মূল্য}
for (auto &p : a)
    cin >> p.first >> p.second;

sort(a.begin(), a.end(), [](const pair<double, double> &x, const pair<double, double> &y)
{
    return x.second / x.first > y.second / y.first;   // প্রতি কেজির মূল্য বেশি আগে
});

double total = 0;
for (auto &p : a)
{
    if (W >= p.first)
    {
        W -= p.first;
        total += p.second;                  // পুরোটাই নিলাম
    }
    else
    {
        total += p.second * (W / p.first);  // যতটুকু ধরে ততটুকু
        break;
    }
}
cout << fixed << setprecision(2) << total;""",
    "অনুপাতে বড় জিনিস আগে বসানো হয়েছে। পুরো জিনিস ধরলে পুরোটা, না ধরলে বাকি জায়গার ভগ্নাংশটুকু নিয়ে থেমে গেছি। ৫০ কেজির ট্রলিতে সর্বোচ্চ মূল্য ২৪০।", F_IN),
  E("কোন জিনিস কতটুকু নিলাম, ধাপে ধাপে ছাপো",
    """int n;
double W;
cin >> n >> W;
vector<Item> a(n);
for (int i = 0; i < n; i++)
{
    a[i].id = i + 1;
    cin >> a[i].w >> a[i].v;
}
sort(a.begin(), a.end(), [](const Item &x, const Item &y)
{
    return x.v / x.w > y.v / y.w;
});

double total = 0;
for (auto &p : a)
{
    if (W <= 0) break;
    double take = min(W, p.w);              // কত কেজি নিতে পারছি
    double gain = p.v * (take / p.w);
    W -= take;
    total += gain;
    cout << "Item " << p.id << ": took " << take << " of " << p.w << " kg, gain " << gain << endl;
}
cout << "Total value = " << total;""",
    "take = min(বাকি জায়গা, জিনিসের ওজন) লিখলে if-else ছাড়াই একই কাজ হয়। পুরো জিনিস ধরলে take = ওজন, না ধরলে take = বাকি জায়গা। বাকি জায়গা ০ হয়ে গেলে লুপ থামে।", F_IN,
    "struct Item { int id; double w, v; };"),
  E("একই জিনিস 0/1 হলে? (ভাগ করা যায় না)",
    """int n, W;
cin >> n >> W;
vector<int> w(n), v(n);
for (int i = 0; i < n; i++)
    cin >> w[i] >> v[i];

vector<int> dp(W + 1, 0);
for (int i = 0; i < n; i++)
    for (int j = W; j >= w[i]; j--)
        dp[j] = max(dp[j], dp[j - w[i]] + v[i]);
cout << "0/1 Knapsack = " << dp[W];""",
    "একই তিনটা জিনিস, একই ৫০ কেজির ট্রলি, কিন্তু এবার ভাগ করা যায় না (সিল করা বস্তা)। উত্তর নেমে এলো ২২০ এ। ভাগ করতে পারার সুবিধার দাম ২৪০ − ২২০ = ২০।", F_IN),
  E("কেন অনুপাত? 'সবচেয়ে দামি আগে' নিলে কী হয়?",
    """int n;
double W;
cin >> n >> W;
vector<Item> a(n);
for (auto &p : a)
    cin >> p.w >> p.v;

sort(a.begin(), a.end(), [](const Item &x, const Item &y) { return x.v > y.v; });
cout << fixed << setprecision(2);
cout << "Highest value first: " << grab(a, W) << endl;

sort(a.begin(), a.end(), [](const Item &x, const Item &y) { return x.v / x.w > y.v / y.w; });
cout << "Highest value/weight first: " << grab(a, W);""",
    "একই greedy কাজ, শুধু sort এর নিয়ম আলাদা। শুধু মূল্য দেখে বাছলে ২২০ আসে, আর প্রতি কেজির মূল্য দেখে বাছলে ২৪০ (সঠিক)। ঠিক sort এর নিয়মটাই পুরো অ্যালগরিদমের প্রাণ।", F_IN,
    """struct Item { double w, v; };

double grab(const vector<Item> &a, double W)
{
    double total = 0;
    for (auto &p : a)
    {
        if (W >= p.w) { W -= p.w; total += p.v; }
        else { total += p.v * (W / p.w); break; }
    }
    return total;
}"""))
