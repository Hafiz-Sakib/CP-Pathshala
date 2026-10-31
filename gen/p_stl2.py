from lib import *
PQ = "priority_queue"
P("stl", PQ, "pq-declare", "priority_queue declare (Max / Min Heap)", "Priority Queue-তে ডাটা নিজে নিজে সাজানো থাকে। ডিফল্টে সবচেয়ে বড় ডাটা আগে বের হয় (Max Heap)। ছোট আগে চাইলে greater<int> দিতে হয় (Min Heap)।", "priority_queue<int> pq;\npriority_queue<int, vector<int>, greater<int>> pq;", "O(1)",
  E("Max ও Min Heap", "priority_queue<int> mx;\npriority_queue<int, vector<int>, greater<int>> mn;\nfor (int x : {5, 8, 7}) { mx.push(x); mn.push(x); }\ncout << mx.top() << \" \" << mn.top();", "একই 5, 8, 7 দুই heap-এ ঢুকিয়েছি। Max Heap-এর top = সবচেয়ে বড় (8), Min Heap-এর top = সবচেয়ে ছোট (5)।"))
P("stl", PQ, "pq-push-emplace", "priority_queue.push() ও emplace()", "ডাটা ঢোকায়, আর ডাটা নিজে সঠিক জায়গায় বসে যায়। emplace() ও একই কাজ করে।", "pq.push(x);\npq.emplace(x);", "O(log n)",
  E("push ও emplace", "priority_queue<int> pq;\npq.push(5);\npq.push(8);\npq.emplace(7);\ncout << pq.size() << \" \" << pq.top();", "৩টা ডাটা ঢুকেছে তাই size 3। এদের মধ্যে সবচেয়ে বড় 8, তাই top = 8।"))
P("stl", PQ, "pq-top-pop", "priority_queue.top() ও pop()", "top() সবচেয়ে অগ্রাধিকারের ডাটা দেখায়, pop() সেটা মুছে ফেলে।", "pq.top();\npq.pop();", "O(1) / O(log n)",
  E("বড় থেকে ছোট", "priority_queue<int> pq;\npq.push(5); pq.push(8); pq.push(7);\nwhile (!pq.empty()) {\n    cout << pq.top() << ' ';\n    pq.pop();\n}", "প্রতিবার সবচেয়ে বড়টা বের হয়, তাই 8 7 5।"),
  E("ছোট থেকে বড় (greater)", "priority_queue<int, vector<int>, greater<int>> pq;\npq.push(5); pq.push(8); pq.push(7);\nwhile (pq.size() > 0) {\n    cout << pq.top() << ' ';\n    pq.pop();\n}", "greater<int> দেওয়ায় সবচেয়ে ছোটটা আগে বের হয়। তাই 5 7 8।"))
P("stl", PQ, "pq-size-empty-swap", "priority_queue.size(), empty(), swap()", "সাইজ জানা, খালি চেক, ও দুইটা priority queue অদলবদল।", "pq.size();\npq.empty();\npq1.swap(pq2);", "O(1)",
  E("swap", "priority_queue<int> a, b;\na.push(1); a.push(9);\nb.push(4);\na.swap(b);\ncout << a.top() << \" \" << b.top() << endl << a.size() << \" \" << b.size();", "swap এর পর a তে b এর ডাটা (4) এবং b তে a এর ডাটা (1, 9) চলে গেছে।"))
P("stl", PQ, "pq-pair", "priority_queue এ pair", "pair রাখলে আগে first দিয়ে, সমান হলে second দিয়ে সাজায়। Dijkstra-তে প্রচুর লাগে।", "priority_queue<pair<int,int>> pq;", "O(log n)",
  E("pair দিয়ে সাজানো", "priority_queue<pair<int, int>> pq;\npq.push({3, 1});\npq.push({5, 2});\npq.push({5, 9});\nwhile (!pq.empty()) {\n    cout << pq.top().first << ' ' << pq.top().second << endl;\n    pq.pop();\n}", "first বড় হলে আগে। দুইটা 5 থাকলে second বড়টা (9) আগে আসে। তাই {5,9}, {5,2}, {3,1}।"))

ST = "set"
P("stl", ST, "set-declare-insert", "set.insert() ও emplace()", "Set-এ শুধু unique ডাটা থাকে এবং ডিফল্টে ছোট থেকে বড় সাজানো থাকে। একই ডাটা আবার দিলে ঢোকে না।", "set<int> s;\ns.insert(x);\nset<int, greater<int>> s;", "O(log n)",
  E("duplicate বাদ", "set<int> s;\ns.insert(2); s.insert(1); s.insert(4); s.insert(3); s.insert(2);\ns.emplace(5);\ncout << s.size() << endl;\nfor (auto u : s) cout << u << ' ';", "২ দুইবার দিয়েছি কিন্তু একবারই থাকে। তাই ৫টা ডাটা, আর সাজানো: 1 2 3 4 5।"),
  E("বড় থেকে ছোট set", "set<int, greater<int>> s = {3, 1, 4, 1, 5};\nfor (auto u : s) cout << u << ' ';", "greater<int> দেওয়ায় বড় থেকে ছোট সাজানো। duplicate 1 একটাই রইলো।"))
P("stl", ST, "set-erase", "set.erase()", "মান দিয়ে অথবা iterator দিয়ে ডাটা মুছে।", "s.erase(value);\ns.erase(iterator);", "O(log n)",
  E("মান ও iterator দিয়ে", "set<int> s = {1, 2, 3, 4, 5};\ns.erase(2);\ns.erase(s.begin());\nfor (auto u : s) cout << u << ' ';", "erase(2) এ 2 গেলো। erase(s.begin()) এ সবচেয়ে ছোট (1) গেলো। বাকি 3 4 5।"))
P("stl", ST, "set-find-count", "set.find() ও count()", "find() ডাটা খুঁজে iterator দেয় (না পেলে end())। count() ডাটা থাকলে 1, না থাকলে 0 দেয়।", "s.find(x);\ns.count(x);", "O(log n)",
  E("খোঁজা", "set<int> s = {1, 3, 5};\nauto it = s.find(3);\nif (it != s.end()) cout << \"Found \" << *it << endl;\nelse cout << \"Not Found\" << endl;\ncout << s.count(1) << \" \" << s.count(2);", "3 আছে তাই Found 3। count(1) = 1, কিন্তু 2 নেই তাই count(2) = 0।"))
P("stl", ST, "set-bounds", "set.lower_bound() ও upper_bound()", "lower_bound(x) = x বা তার চেয়ে বড় প্রথম ডাটা। upper_bound(x) = x এর চেয়ে বড় প্রথম ডাটা। না পেলে end()।", "s.lower_bound(x);\ns.upper_bound(x);", "O(log n)",
  E("lower ও upper", "set<int> s = {1, 2, 3, 4, 5, 6};\ncout << *s.lower_bound(2) << \" \" << *s.upper_bound(2) << endl;\nif (s.lower_bound(10) == s.end()) cout << \"10 er boro kichu nai\";", "lower_bound(2) = 2 (নিজেই আছে)। upper_bound(2) = 3 (2 এর পরের বড়)। 10 এর সমান বা বড় কিছু নেই তাই end()।"))
P("stl", ST, "set-size-empty-clear", "set.size(), empty(), clear()", "সাইজ, খালি কিনা, আর সব মুছে ফেলা।", "s.size();\ns.empty();\ns.clear();", "O(1) / clear O(n)",
  E("তিনটা একসাথে", "set<int> s = {7, 8, 9};\ncout << s.size() << endl;\ns.clear();\ncout << s.empty();", "আগে size 3। clear() এর পর empty() = 1।"))
P("stl", ST, "set-swap", "set.swap()", "দুইটা set অদলবদল করে।", "s1.swap(s2);", "O(1)",
  E("অদলবদল", "set<int> a = {1, 2}, b = {9};\na.swap(b);\nfor (auto u : a) cout << u << ' ';\ncout << \"| \";\nfor (auto u : b) cout << u << ' ';", "swap এর পর a তে 9 আর b তে 1 2।"))

MS = "multiset"
P("stl", MS, "multiset-insert", "multiset.insert()", "Multiset অনেকটা set-এর মতোই সাজানো থাকে, কিন্তু একই ডাটা একাধিকবার রাখা যায়।", "multiset<int> ms;\nms.insert(x);", "O(log n)",
  E("duplicate রাখা", "multiset<int> ms;\nms.insert(2); ms.insert(1); ms.insert(2); ms.insert(5);\nms.emplace(1);\ncout << ms.size() << endl;\nfor (auto u : ms) cout << u << ' ';", "set হলে ৩টা থাকতো, কিন্তু এখানে duplicate-সহ ৫টা ডাটা। সাজানো: 1 1 2 2 5।"))
P("stl", MS, "multiset-erase", "multiset.erase()", "erase(মান) ঐ মানের সবগুলো মুছে। একটাই মুছতে চাইলে erase(iterator) দিতে হয়।", "ms.erase(value);\nms.erase(iterator);", "O(log n + k)",
  E("সব বনাম একটা", "multiset<int> a = {1, 2, 2, 2, 3}, b = {1, 2, 2, 2, 3};\na.erase(2);\nb.erase(b.find(2));\nfor (auto u : a) cout << u << ' ';\ncout << endl;\nfor (auto u : b) cout << u << ' ';", "a তে erase(2) করায় তিনটা 2-ই গেছে। b তে শুধু find(2) এর একটা 2 গেছে, বাকি দুইটা রইলো।"))
P("stl", MS, "multiset-count-find", "multiset.count() ও find()", "count() ডাটা কতবার আছে তা জানায়। find() প্রথম ডাটাটার iterator দেয়।", "ms.count(x);\nms.find(x);", "O(log n + k)",
  E("কতবার আছে", "multiset<int> ms = {1, 2, 2, 5, 5, 5};\ncout << ms.count(5) << \" \" << ms.count(2) << \" \" << ms.count(9) << endl;\nif (ms.find(9) == ms.end()) cout << \"Not Found\";", "5 আছে তিনবার, 2 দুইবার, 9 একবারও না। 9 পাওয়া যায়নি তাই find() end() দিয়েছে।"))
P("stl", MS, "multiset-bounds", "multiset.lower_bound() ও upper_bound()", "set-এর মতোই। lower_bound = সমান বা বড় প্রথম ডাটা, upper_bound = শুধু বড় প্রথম ডাটা।", "ms.lower_bound(x);\nms.upper_bound(x);", "O(log n)",
  E("bounds", "multiset<int> ms = {1, 2, 2, 5, 6};\ncout << *ms.lower_bound(3) << \" \" << *ms.upper_bound(5) << \" \" << *ms.lower_bound(2);", "3 নেই, তাই lower_bound(3) = পরের বড় 5। upper_bound(5) = 6। lower_bound(2) নিজেই 2।"))
P("stl", MS, "multiset-size-clear", "multiset.size() ও clear()", "ডাটার সংখ্যা জানা ও সব মুছা।", "ms.size();\nms.clear();", "O(1) / O(n)",
  E("size ও clear", "multiset<int> ms = {4, 4, 4};\ncout << ms.size() << endl;\nms.clear();\ncout << ms.size();", "duplicate-সহ size 3। clear() এর পর 0।"))

L = "list"
P("stl", L, "list-push", "list.push_back() ও push_front()", "List হলো doubly linked list। push_back শেষে, push_front শুরুতে ডাটা বসায়।", "li.push_back(x);\nli.push_front(x);", "O(1)",
  E("দুই দিকে যোগ", "list<int> li;\nli.push_back(1); li.push_back(2); li.push_back(3);\nli.push_front(4); li.push_front(5);\nfor (auto u : li) cout << u << ' ';", "push_front এ 4 তারপর 5 সামনে এসেছে, তাই 5 4 1 2 3।"))
P("stl", L, "list-pop", "list.pop_back() ও pop_front()", "শেষের / শুরুর ডাটা মুছে।", "li.pop_back();\nli.pop_front();", "O(1)",
  E("দুই প্রান্ত থেকে মোছা", "list<int> li = {5, 4, 1, 2, 3};\nli.pop_front();\nli.pop_back();\nfor (auto u : li) cout << u << ' ';", "শুরুর 5 ও শেষের 3 গেছে। বাকি 4 1 2।"))
P("stl", L, "list-insert", "list.insert()", "iterator দিয়ে নির্দিষ্ট জায়গায় ডাটা ঢোকায়। list-এ it + 2 চলে না, তাই advance() ব্যবহার হয়।", "advance(it, n);\nli.insert(it, value);", "O(1) (iterator পাওয়ার পর)",
  E("advance + insert", "list<int> li = {5, 4, 1, 2, 3};\nauto it = li.begin();\nadvance(it, 2);\nli.insert(it, 3);\nfor (auto u : li) cout << u << ' ';", "begin() থেকে ২ ঘর এগিয়ে (1 এর জায়গায়) 3 ঢোকানো হলো। ফল 5 4 3 1 2 3।"))
P("stl", L, "list-front-back", "list.front() ও back()", "প্রথম ও শেষ ডাটা দেখায়।", "li.front();\nli.back();", "O(1)",
  E("প্রান্তের ডাটা", "list<int> li = {7, 8, 9};\ncout << li.front() << \" \" << li.back();", "প্রথম 7, শেষ 9।"))
P("stl", L, "list-remove", "list.remove()", "ঐ মানের সবগুলো ডাটা list থেকে মুছে।", "li.remove(value);", "O(n)",
  E("মান ধরে মোছা", "list<int> li = {1, 2, 2, 3, 3, 4};\nli.remove(2);\nfor (auto u : li) cout << u << ' ';", "দুইটা 2 ই গেছে। বাকি 1 3 3 4।"))
P("stl", L, "list-reverse-sort", "list.reverse() ও sort()", "reverse() ক্রম উল্টে দেয়, sort() ছোট থেকে বড় সাজায়। list-এ std::sort চলে না, তাই li.sort() লাগে।", "li.reverse();\nli.sort();", "O(n) / O(n log n)",
  E("উল্টানো ও সাজানো", "list<int> li = {3, 1, 4, 1, 5};\nli.reverse();\nfor (auto u : li) cout << u << ' ';\ncout << endl;\nli.sort();\nfor (auto u : li) cout << u << ' ';", "reverse এ 5 1 4 1 3। sort এ 1 1 3 4 5।"))
P("stl", L, "list-unique", "list.unique()", "পাশাপাশি থাকা duplicate মুছে। তাই আগে sort করে নিলে সব duplicate যায়।", "li.unique();", "O(n)",
  E("sort + unique", "list<int> li = {1, 2, 2, 3, 3, 4, 4, 5, 6, 1};\nli.unique();\nfor (auto u : li) cout << u << ' ';\ncout << endl;\nli.sort();\nli.unique();\nfor (auto u : li) cout << u << ' ';", "শুধু unique এ পাশাপাশির duplicate গেছে, কিন্তু শেষের 1 রয়ে গেছে। sort করে unique দিলে সব duplicate যায়।"))
P("stl", L, "list-merge-swap", "list.merge() ও swap()", "merge() দুইটা সাজানো list এক করে। swap() দুইটা list অদলবদল করে।", "a.merge(b);\na.swap(b);", "O(n)",
  E("merge", "list<int> a = {1, 3, 5}, b = {2, 4, 6};\na.merge(b);\nfor (auto u : a) cout << u << ' ';\ncout << endl << b.size();", "দুইটা সাজানো list মিলে সাজানো থাকলো: 1 2 3 4 5 6। b এর সব ডাটা a তে চলে গেছে, তাই b.size() = 0।"))
P("stl", L, "list-size-empty-clear", "list.size(), empty(), clear()", "সাইজ, খালি কিনা, আর সব মুছা।", "li.size();\nli.empty();\nli.clear();", "O(1)",
  E("তিনটা একসাথে", "list<int> li = {1, 2, 3};\ncout << li.size() << endl;\nli.clear();\nif (li.empty()) cout << \"Empty\";", "আগে size 3, clear() এর পর খালি।"))

M = "map"
P("stl", M, "map-declare", "map declare ও ডাটা বসানো", "Map-এ ডাটা থাকে key–value জোড়ায়। key গুলো unique এবং ছোট থেকে বড় সাজানো থাকে।", "map<key_type, value_type> m;\nm[key] = value;", "O(log n)",
  E("নামের সাথে id", "map<string, int> id;\nid[\"Sakib\"] = 101;\nid[\"Tamim\"] = 102;\nid[\"Miraz\"] = 105;\ncout << id[\"Miraz\"] << endl << id.size();", "key দিয়ে value ধরা হয়: Miraz এর id 105। ৩টা জোড়া তাই size 3।"))
P("stl", M, "map-iterate", "map loop (first ও second)", "foreach দিয়ে map ঘুরলে প্রতিটা জোড়ার key হলো first, value হলো second। key সাজানো ক্রমে আসে।", "for (auto u : m)\n  u.first, u.second", "O(n)",
  E("সাজানো key", "map<int, string> m;\nm[3] = \"c\"; m[1] = \"a\"; m[2] = \"b\";\nfor (auto u : m) cout << u.first << \" \" << u.second << endl;", "ঢোকানোর ক্রম 3, 1, 2 হলেও map key অনুযায়ী 1, 2, 3 সাজিয়ে রাখে।"))
P("stl", M, "map-frequency", "map দিয়ে frequency গোনা", "কোন ডাটা কতবার আছে — m[x]++ দিয়ে খুব সহজে গোনা যায়। CP-তে সবচেয়ে বেশি ব্যবহার।", "for (auto u : v) m[u]++;", "O(n log n)",
  E("frequency", "vector<int> v = {5, 5, 3, 9, 5, 3};\nmap<int, int> m;\nfor (auto u : v) m[u]++;\nfor (auto u : m) cout << u.first << \" -> \" << u.second << endl;", "5 আছে ৩ বার, 3 আছে ২ বার, 9 একবার। নতুন key এর value শুরুতে 0 ধরা হয় তাই ++ কাজ করে।"),
  E("string এর অক্ষর গোনা", "string s;\ncin >> s;\nmap<char, int> m;\nfor (char c : s) m[c]++;\nfor (auto u : m) cout << u.first << \" \" << u.second << endl;", "banana এ a আছে ৩টা, b ১টা, n ২টা। key (অক্ষর) সাজানো ক্রমে প্রিন্ট হয়েছে।", "banana"))
P("stl", M, "map-find-count", "map.find() ও count()", "key আছে কিনা চেক করতে ব্যবহার হয়। m[key] দিয়ে চেক করা ভালো না, কারণ ওটা key বানিয়ে ফেলে।", "m.find(key);\nm.count(key);", "O(log n)",
  E("key আছে কিনা", "map<string, int> m;\nm[\"a\"] = 1;\ncout << m.count(\"a\") << \" \" << m.count(\"z\") << endl;\nauto it = m.find(\"a\");\nif (it != m.end()) cout << it->first << \" = \" << it->second;", "\"a\" আছে তাই count = 1, \"z\" নেই তাই 0। find() পেলে it->first, it->second দিয়ে key ও value পাওয়া যায়।"))
P("stl", M, "map-erase", "map.erase() ও clear()", "erase(key) ঐ জোড়া মুছে। clear() পুরো map খালি করে।", "m.erase(key);\nm.clear();", "O(log n)",
  E("erase", "map<int, int> mp;\nmp[2] = 20; mp[6] = 60; mp[3] = 30; mp[1] = 10;\nmp.erase(3);\nfor (auto u : mp) cout << u.first << \" \" << u.second << endl;", "key 3 এর জোড়া মুছেছে। বাকি 1, 2, 6।"))
P("stl", M, "map-bounds", "map.lower_bound() ও upper_bound()", "key এর উপর binary search। lower_bound = সমান বা বড় প্রথম key, upper_bound = বড় প্রথম key।", "m.lower_bound(key);\nm.upper_bound(key);", "O(log n)",
  E("key দিয়ে bound", "map<int, string> m = {{10, \"a\"}, {20, \"b\"}, {30, \"c\"}};\nauto it = m.lower_bound(15);\ncout << it->first << \" \" << it->second << endl;\ncout << m.upper_bound(20)->first;", "15 নেই, তাই lower_bound = পরের key 20। upper_bound(20) = 20 এর চেয়ে বড় প্রথম key 30।"))
P("stl", M, "map-size-empty", "map.size() ও empty()", "জোড়ার সংখ্যা ও খালি কিনা জানা।", "m.size();\nm.empty();", "O(1)",
  E("unique গোনা", "vector<int> v = {1, 2, 2, 3, 3, 3};\nmap<int, int> m;\nfor (auto u : v) m[u]++;\ncout << m.size();", "map-এ প্রতি unique key একবার থাকে, তাই size = unique ডাটার সংখ্যা = 3।"))

PR = "pair"
P("stl", PR, "pair-basic", "pair", "দুইটা ডাটা একসাথে রাখতে pair ব্যবহার হয়। প্রথমটা first, দ্বিতীয়টা second।", "pair<int, string> p;\nmake_pair(a, b);\np.first; p.second;", "O(1)",
  E("pair বানানো", "pair<int, string> p = {1, \"Sakib\"};\npair<int, int> q = make_pair(3, 4);\ncout << p.first << \" \" << p.second << endl;\ncout << q.first + q.second;", "first = 1, second = \"Sakib\"। q এর দুই ডাটার যোগফল 7।"))
P("stl", PR, "pair-sort", "pair vector sort করা", "pair sort করলে আগে first দিয়ে, সমান হলে second দিয়ে সাজায়।", "sort(v.begin(), v.end());", "O(n log n)",
  E("pair sort", "vector<pair<int, int>> v = {{3, 1}, {1, 9}, {3, 0}, {2, 5}};\nsort(v.begin(), v.end());\nfor (auto u : v) cout << u.first << ' ' << u.second << endl;", "প্রথমে first ছোট থেকে বড়। দুইটা 3 আছে, তাই তাদের মধ্যে second ছোটটা (0) আগে।"))

STR = "string"
P("stl", STR, "string-basic", "string input ও length", "string হলো অক্ষরের সারি। cin >> s শুধু এক শব্দ পড়ে। length() বা size() দিয়ে দৈর্ঘ্য পাওয়া যায়।", "string s;\ns.length();\ns.size();", "O(1)",
  E("input ও length", "string s;\ncin >> s;\ncout << s.length() << \" \" << s[0];", "\"codeforces\" এ ১০টা অক্ষর, প্রথম অক্ষর c।", "codeforces"),
  E("getline দিয়ে পুরো লাইন", "string s;\ngetline(cin, s);\ncout << s << endl << s.size();", "getline স্পেসসহ পুরো লাইন পড়ে। \"I love CP\" এ স্পেসসহ ১০টা অক্ষর।", "I love CP"))
P("stl", STR, "string-reverse", "reverse() দিয়ে string উল্টানো", "reverse(s.begin(), s.end()) পুরো string উল্টে দেয়। palindrome চেকে কাজে লাগে।", "reverse(s.begin(), s.end());", "O(n)",
  E("উল্টানো", "string s = \"hello\";\nreverse(s.begin(), s.end());\ncout << s;", "hello উল্টে olleh।"),
  E("palindrome চেক", "string s, t;\ncin >> s;\nt = s;\nreverse(t.begin(), t.end());\nif (s == t) cout << \"Palindrome\";\nelse cout << \"Not Palindrome\";", "madam উল্টালেও madam থাকে, তাই Palindrome।", "madam"))
P("stl", STR, "string-sort", "sort() দিয়ে string সাজানো", "sort(s.begin(), s.end()) অক্ষরগুলো ASCII ক্রমে সাজায়।", "sort(s.begin(), s.end());", "O(n log n)",
  E("অক্ষর সাজানো", "string s = \"banana\";\nsort(s.begin(), s.end());\ncout << s;", "অক্ষর a a a b n n এভাবে সাজালো: aaabnn।"))
P("stl", STR, "string-case", "upper / lower case বানানো", "transform() দিয়ে পুরো string বড় বা ছোট হাতের করা যায়।", "transform(s.begin(), s.end(), s.begin(), ::toupper);", "O(n)",
  E("toupper / tolower", "string s = \"Hello World\";\ntransform(s.begin(), s.end(), s.begin(), ::toupper);\ncout << s << endl;\ntransform(s.begin(), s.end(), s.begin(), ::tolower);\ncout << s;", "প্রথমে সব বড় হাতের, তারপর সব ছোট হাতের।"))
P("stl", STR, "string-modify", "string.push_back(), pop_back(), back()", "string-এর শেষে অক্ষর যোগ, শেষের অক্ষর মোছা ও দেখা যায়।", "s.push_back(c);\ns.pop_back();\ns.back();", "O(1)",
  E("শেষ নিয়ে কাজ", "string s = \"abc\";\ns.push_back('d');\ncout << s << endl;\ns.pop_back();\ns.pop_back();\ncout << s << \" \" << s.back();", "d যোগ হয়ে abcd। দুইবার pop এ c ও d গেছে, বাকি ab এবং শেষ অক্ষর b।"))
P("stl", STR, "string-erase-substr", "string.erase() ও substr()", "erase(i) i নম্বর থেকে শেষ পর্যন্ত মুছে। erase(i, n) n টা অক্ষর মুছে। substr(i, n) অংশ কেটে আনে।", "s.erase(i, n);\ns.substr(i, n);", "O(n)",
  E("erase ও substr", "string s = \"abcdefg\";\ncout << s.substr(2, 3) << endl;\ns.erase(1, 2);\ncout << s;", "substr(2, 3) = index 2 থেকে ৩টা অক্ষর: cde। erase(1, 2) এ b ও c গেছে: adefg।"))
P("stl", STR, "string-find", "string.find()", "অক্ষর বা অংশ খুঁজে প্রথম index দেয়। না পেলে string::npos দেয়।", "s.find(\"text\");", "O(n)",
  E("খোঁজা", "string s = \"programming\";\nsize_t p = s.find(\"gram\");\nif (p != string::npos) cout << \"Found at \" << p << endl;\nif (s.find(\"xyz\") == string::npos) cout << \"xyz Not Found\";", "\"gram\" index 3 থেকে শুরু। \"xyz\" নেই তাই npos।"))
P("stl", STR, "string-next-permutation", "next_permutation() — string এর সব ক্রম", "পরের lexicographic ক্রমে সাজায়। আগে sort করে নিলে সব permutation বের হয়।", "next_permutation(s.begin(), s.end());", "O(n)",
  E("সব permutation", "string s = \"abc\";\ndo {\n    cout << s << endl;\n} while (next_permutation(s.begin(), s.end()));", "abc এর ৬টা ক্রম অভিধানের নিয়মে প্রিন্ট হলো।"))
