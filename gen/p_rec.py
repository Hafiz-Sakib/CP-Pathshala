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
