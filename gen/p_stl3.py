from lib import *
A = "algorithm"
P("stl", A, "algo-sort", "sort()", "Array বা vector ছোট থেকে বড় সাজায়। বড় থেকে ছোট করতে greater<int>() দিতে হয়।", "sort(v.begin(), v.end());\nsort(v.begin(), v.end(), greater<int>());\nsort(a, a + n);", "O(n log n)",
  E("vector sort", "vector<int> v = {5, 2, 9, 1, 7};\nsort(v.begin(), v.end());\nfor (auto u : v) cout << u << ' ';\ncout << endl;\nsort(v.begin(), v.end(), greater<int>());\nfor (auto u : v) cout << u << ' ';", "প্রথমে ছোট থেকে বড়: 1 2 5 7 9। greater<int>() দিয়ে বড় থেকে ছোট: 9 7 5 2 1।"),
  E("array sort", "int a[5] = {4, 3, 5, 1, 2};\nsort(a, a + 5);\nfor (int i = 0; i < 5; i++) cout << a[i] << ' ';", "array এর জন্য শুরু a, শেষ a + n। সাজানোর পর 1 2 3 4 5।"))
P("stl", A, "algo-reverse", "reverse()", "vector বা array-র ক্রম উল্টে দেয়।", "reverse(v.begin(), v.end());", "O(n)",
  E("উল্টানো", "vector<int> v = {1, 2, 3, 4, 5};\nreverse(v.begin(), v.end());\nfor (auto u : v) cout << u << ' ';", "ক্রম উল্টে 5 4 3 2 1।"))
P("stl", A, "algo-minmax", "max_element() ও min_element()", "সবচেয়ে বড়/ছোট ডাটার iterator দেয়। মান পেতে সামনে * দিতে হয়।", "*max_element(v.begin(), v.end());\n*min_element(v.begin(), v.end());", "O(n)",
  E("সর্বোচ্চ ও সর্বনিম্ন", "vector<int> v = {4, 9, 2, 7};\ncout << *max_element(v.begin(), v.end()) << \" \" << *min_element(v.begin(), v.end());", "সবচেয়ে বড় 9, সবচেয়ে ছোট 2।"),
  E("কোন index এ আছে", "vector<int> v = {4, 9, 2, 7};\nint idx = max_element(v.begin(), v.end()) - v.begin();\ncout << idx;", "iterator থেকে begin() বিয়োগ করলে index পাওয়া যায়। 9 আছে index 1 এ।"))
P("stl", A, "algo-accumulate", "accumulate()", "রেঞ্জের সব ডাটার যোগফল বের করে। তৃতীয় আর্গুমেন্ট হলো শুরুর মান।", "accumulate(v.begin(), v.end(), 0);\naccumulate(v.begin(), v.end(), 0LL);", "O(n)",
  E("যোগফল", "vector<int> v = {1, 2, 3, 4, 5};\ncout << accumulate(v.begin(), v.end(), 0);", "1+2+3+4+5 = 15।"),
  E("বড় যোগফলে 0LL", "vector<long long> v = {2000000000, 2000000000};\ncout << accumulate(v.begin(), v.end(), 0LL);", "ফল int-এর সীমার বেশি, তাই শুরুর মান 0LL (long long) দিতে হয়। নাহলে ভুল উত্তর আসে।"))
P("stl", A, "algo-binary_search", "binary_search()", "সাজানো ডাটায় কোনো মান আছে কিনা O(log n) এ বলে দেয় (true/false)। ডাটা সাজানো থাকতেই হবে।", "binary_search(v.begin(), v.end(), x);", "O(log n)",
  E("আছে কিনা", "vector<int> v = {1, 3, 5, 7, 9};\ncout << binary_search(v.begin(), v.end(), 7) << \" \" << binary_search(v.begin(), v.end(), 4);", "7 আছে তাই 1 (true), 4 নেই তাই 0 (false)।"))
P("stl", A, "algo-bounds", "lower_bound() ও upper_bound() (vector)", "সাজানো vector-এ lower_bound(x) = x বা বড় প্রথম ডাটার iterator, upper_bound(x) = শুধু বড় প্রথম ডাটার iterator।", "lower_bound(v.begin(), v.end(), x);\nupper_bound(v.begin(), v.end(), x);", "O(log n)",
  E("index বের করা", "vector<int> v = {1, 2, 4, 4, 4, 7};\nint lo = lower_bound(v.begin(), v.end(), 4) - v.begin();\nint up = upper_bound(v.begin(), v.end(), 4) - v.begin();\ncout << lo << \" \" << up << endl << up - lo;", "4 শুরু হয় index 2 থেকে (lower_bound)। 4 এর পরের বড় ডাটা index 5 এ (upper_bound)। তাই 4 আছে 5 - 2 = 3 বার।"))
P("stl", A, "algo-unique", "unique() ও erase() — duplicate মোছা", "সাজানো ডাটায় unique() duplicate গুলো শেষে ঠেলে দেয়। erase() দিয়ে সেই অংশ কেটে ফেলতে হয়।", "v.erase(unique(v.begin(), v.end()), v.end());", "O(n)",
  E("sort + unique", "vector<int> v = {3, 1, 3, 2, 1, 2, 5};\nsort(v.begin(), v.end());\nv.erase(unique(v.begin(), v.end()), v.end());\nfor (auto u : v) cout << u << ' ';", "sort এ 1 1 2 2 3 3 5। unique + erase এ duplicate গিয়ে 1 2 3 5।"))
P("stl", A, "algo-count", "count() ও count_if()", "রেঞ্জে কোনো মান কতবার আছে (count) বা শর্ত মানে এমন কয়টা (count_if) গুনে।", "count(v.begin(), v.end(), x);", "O(n)",
  E("গুনা", "vector<int> v = {1, 2, 2, 3, 2, 4};\ncout << count(v.begin(), v.end(), 2) << endl;\ncout << count_if(v.begin(), v.end(), [](int x) { return x % 2 == 0; });", "2 আছে ৩ বার। জোড় সংখ্যা আছে 2, 2, 2, 4 — মোট ৪টা।"))
P("stl", A, "algo-swap", "swap()", "দুইটা ভ্যারিয়েবলের মান অদলবদল করে।", "swap(a, b);", "O(1)",
  E("মান বদল", "int a = 5, b = 10;\nswap(a, b);\ncout << a << \" \" << b;", "swap এর পর a = 10, b = 5।"))
P("stl", A, "algo-next-permutation", "next_permutation() (সংখ্যা)", "সংখ্যার সব ক্রম (permutation) একে একে বের করে। আগে sort করে নিতে হয়।", "next_permutation(v.begin(), v.end());", "O(n)",
  E("1 2 3 এর সব ক্রম", "vector<int> v = {1, 2, 3};\ndo {\n    for (auto u : v) cout << u << ' ';\n    cout << endl;\n} while (next_permutation(v.begin(), v.end()));", "৩টা ডাটার ৩! = ৬টা ক্রম অভিধানের নিয়মে প্রিন্ট হলো।"))
P("stl", A, "algo-gcd", "__gcd() ও lcm", "দুইটা সংখ্যার গ.সা.গু (GCD) দেয়। ল.সা.গু = (a / gcd) * b।", "__gcd(a, b);\n(a / __gcd(a, b)) * b;", "O(log n)",
  E("GCD ও LCM", "int a = 12, b = 18;\ncout << __gcd(a, b) << endl;\ncout << (a / __gcd(a, b)) * b;", "12 ও 18 এর গ.সা.গু 6, ল.সা.গু 36।"))

BS = "bitset"
P("stl", BS, "bitset-basic", "bitset", "bitset হলো বিটের array — প্রতিটা ঘরে মাত্র ১ বিট। বড় sieve বা true/false array-তে মেমোরি অনেক বাঁচায়।", "bitset<N> b;\nb[i] = 1;\nb.count();", "O(1) / count O(N)",
  E("set ও count", "bitset<8> b;\nb[1] = 1;\nb[3] = 1;\nb[6] = 1;\ncout << b << endl << b.count() << endl << b[3] << b[4];", "বিট ডান থেকে গোনা হয় (index 0 সবচেয়ে ডানে), তাই 01001010। ১ আছে ৩টা। b[3] = 1, b[4] = 0।"))
P("stl", BS, "bitset-functions", "bitset.set(), reset(), flip(), test()", "set() বিট 1 করে, reset() 0 করে, flip() উল্টে, test(i) i নম্বর বিট 1 কিনা বলে।", "b.set(i);\nb.reset(i);\nb.flip(i);\nb.test(i);", "O(1)",
  E("বিট নিয়ে খেলা", "bitset<5> b;\nb.set(0);\nb.set(2);\ncout << b << endl;\nb.flip(0);\ncout << b << endl;\nb.reset();\ncout << b << \" \" << b.test(2);", "set(0), set(2) এ 00101। flip(0) এ index 0 উল্টে 00100। reset() সব 0, তাই test(2) = 0।"))

U = "unordered"
P("stl", U, "unordered_map", "unordered_map", "map-এর মতোই key–value, কিন্তু সাজানো থাকে না। গড়ে O(1) এ কাজ হয়, তাই অনেক সময় map-এর চেয়ে দ্রুত।", "unordered_map<int, int> m;", "গড়ে O(1)",
  E("frequency", "unordered_map<int, int> m;\nint a[] = {1, 2, 2, 3, 3, 3};\nfor (int x : a) m[x]++;\ncout << m[1] << \" \" << m[2] << \" \" << m[3] << \" \" << m.size();", "প্রতিটা সংখ্যা কতবার আছে গোনা হলো: 1 একবার, 2 দুইবার, 3 তিনবার। unique key ৩টা। (প্রিন্টের ক্রম সাজানো থাকে না, তাই এখানে key ধরে প্রিন্ট করেছি।)"))
P("stl", U, "unordered_set", "unordered_set", "set-এর মতোই unique ডাটা, কিন্তু সাজানো থাকে না। insert/find গড়ে O(1)।", "unordered_set<int> s;", "গড়ে O(1)",
  E("unique গোনা", "unordered_set<int> s;\nint a[] = {5, 1, 5, 2, 1, 9};\nfor (int x : a) s.insert(x);\ncout << s.size() << \" \" << s.count(5) << \" \" << s.count(7);", "unique ডাটা 5, 1, 2, 9 — মোট ৪টা। 5 আছে (1), 7 নেই (0)।"))
