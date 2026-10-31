from lib import *
V = "vector"
P("stl", V, "vector-declare", "vector declare করা", "Vector হলো dynamic array — সাইজ বাড়ে-কমে। declare করার সময় <> এর ভেতর ডাটার type লিখতে হয়।", "vector<int> v;\nvector<int> v = {1, 2, 3};\nvector<int> v(n, x);", "O(1) / O(n) ভ্যালু বসালে",
  E("খালি ও ভ্যালুসহ declare", "vector<int> a;\nvector<int> b = {1, 2, 3, 4, 5};\nvector<int> c(4, 7);\ncout << a.size() << \" \" << b.size() << \" \" << c.size() << endl;\nfor (auto u : c) cout << u << ' ';", "a খালি তাই size 0। b তে ৫টা ডাটা। c(4, 7) মানে ৪টা ঘর, প্রতিটায় 7।"),
  E("input নিয়ে vector ভরা", "int n;\ncin >> n;\nvector<int> v(n);\nfor (int i = 0; i < n; i++) cin >> v[i];\nfor (auto u : v) cout << u << ' ';", "প্রথমে n=4 নিলাম, তারপর ৪টা সংখ্যা। v(n) দিয়ে আগেই ৪টা ঘর বানানো হয়েছে, তাই v[i] তে সরাসরি input যায়।", "4\n10 20 30 40"))
P("stl", V, "vector-push_back", "vector.push_back()", "Vector-এর একদম শেষে নতুন ডাটা যোগ করে। এটাই সবচেয়ে বেশি ব্যবহৃত function।", "v.push_back(value);", "O(1) (গড়ে)",
  E("একটা একটা করে ঢোকানো", "vector<int> v;\nv.push_back(1);\nv.push_back(2);\nv.push_back(3);\ncout << v[0] << \" \" << v[1] << \" \" << v[2];", "প্রতিবার শেষে ডাটা বসে। তাই index 0 তে 1, index 1 এ 2, index 2 এ 3।"),
  E("input নিয়ে push_back", "int n, x;\ncin >> n;\nvector<int> v;\nwhile (n--) {\n    cin >> x;\n    v.push_back(x);\n}\ncout << v.size();", "n = 3, তাই লুপ ৩ বার চলে। প্রতিবার x পড়ে vector-এর শেষে বসানো হলো, শেষে size = 3।", "3\n5 8 9"))
P("stl", V, "vector-pop_back", "vector.pop_back()", "Vector-এর শেষের ডাটাটা মুছে ফেলে। খালি vector-এ চালালে সমস্যা হয়, তাই আগে empty() চেক করা ভালো।", "v.pop_back();", "O(1)",
  E("শেষের ডাটা মোছা", "vector<int> v = {1, 2, 3, 4, 5};\nv.pop_back();\nfor (auto u : v) cout << u << ' ';\ncout << endl << v.size();", "শেষের 5 মুছে গেছে। এখন বাকি 1 2 3 4, size 4।"),
  E("পরপর দুইবার pop", "vector<int> v = {10, 20, 30};\nv.pop_back();\nv.pop_back();\ncout << v.back();", "দুইবারে 30 ও 20 গেছে। এখন শেষ ডাটা 10।"))
P("stl", V, "vector-index", "vector[i] ও at()", "i নম্বর index-এর ডাটা পড়া/বদলানো যায়। v[i] দ্রুত, কিন্তু index ভুল হলে garbage দেয়। at() ভুল index-এ error দেয়।", "v[i]\nv.at(i)", "O(1)",
  E("পড়া ও বদলানো", "vector<int> v = {5, 6, 7};\ncout << v[0] << \" \" << v.at(1) << endl;\nv[2] = 100;\ncout << v[2];", "v[0]=5, v.at(1)=6। পরে v[2] তে 100 বসালাম, তাই 7 এর জায়গায় 100।"),
  E("at() এ ভুল index", "vector<int> v = {1, 2, 3};\ntry {\n    cout << v.at(10);\n} catch (...) {\n    cout << \"Index nai!\";\n}", "index 10 নেই, তাই at() exception ছুড়ে। catch ধরে message প্রিন্ট করেছে। v[10] হলে crash বা garbage আসতো।"))
P("stl", V, "vector-size", "vector.size()", "Vector-এ কয়টা ডাটা আছে তা জানায়। লুপ চালাতে খুব কাজে লাগে।", "v.size();", "O(1)",
  E("size দিয়ে লুপ", "vector<int> v = {4, 8, 15, 16, 23, 42};\nfor (int i = 0; i < v.size(); i++) cout << v[i] << ' ';\ncout << endl << \"Size: \" << v.size();", "size = 6, তাই লুপ i = 0 থেকে 5 পর্যন্ত চলে।"),
  E("push_back এর সাথে size", "vector<int> v;\ncout << v.size() << endl;\nv.push_back(9);\nv.push_back(9);\ncout << v.size();", "শুরুতে 0। দুইবার push_back করায় 2।"))
P("stl", V, "vector-front-back", "vector.front() ও back()", "front() প্রথম ডাটা, back() শেষ ডাটা দেয়। এদের দিয়ে মানও বদলানো যায়।", "v.front();\nv.back();", "O(1)",
  E("প্রথম ও শেষ", "vector<int> v = {3, 6, 9};\ncout << v.front() << \" \" << v.back();", "প্রথম ডাটা 3, শেষ ডাটা 9।"),
  E("front/back বদলানো", "vector<int> v = {1, 2, 3};\nv.front() = 5;\nv.back() = 10;\nfor (auto u : v) cout << u << ' ';", "front() = 5 দিয়ে প্রথমটা 5 হলো, back() = 10 দিয়ে শেষটা 10 হলো। মাঝের 2 অপরিবর্তিত।"))
P("stl", V, "vector-erase", "vector.erase()", "iterator দিয়ে নির্দিষ্ট ডাটা বা একটা রেঞ্জ মুছে ফেলে। মুছলে পরের ডাটাগুলো এগিয়ে আসে।", "v.erase(v.begin() + i);\nv.erase(v.begin() + l, v.begin() + r);", "O(n)",
  E("একটা index মোছা", "vector<int> v = {1, 2, 3, 4, 5};\nv.erase(v.begin() + 2);\nfor (auto u : v) cout << u << ' ';", "index 2 এর ডাটা (3) মুছে গেছে। বাকি 1 2 4 5।"),
  E("রেঞ্জ মোছা", "vector<int> v = {1, 2, 3, 4, 5};\nv.erase(v.begin() + 2, v.end());\nfor (auto u : v) cout << u << ' ';", "index 2 থেকে শেষ পর্যন্ত সব মুছেছে। বাকি 1 2।"))
P("stl", V, "vector-clear-empty", "vector.clear() ও empty()", "clear() সব ডাটা মুছে size 0 করে দেয়। empty() খালি কিনা চেক করে (খালি হলে true)।", "v.clear();\nv.empty();", "O(n) / O(1)",
  E("clear করে চেক", "vector<int> v = {1, 2, 3};\nv.clear();\ncout << v.size() << endl;\nif (v.empty()) cout << \"Empty\";\nelse cout << \"Not Empty\";", "clear() এর পর size 0, তাই empty() true হলো ও Empty প্রিন্ট হলো।"),
  E("empty দিয়ে নিরাপদ pop", "vector<int> v = {7};\nwhile (!v.empty()) {\n    cout << v.back() << endl;\n    v.pop_back();\n}\ncout << \"Done\";", "v খালি না হওয়া পর্যন্ত শেষ ডাটা প্রিন্ট করে মুছছে। এতে খালি vector-এ pop হওয়ার ভুল হয় না।"))
P("stl", V, "vector-insert", "vector.insert()", "নির্দিষ্ট জায়গায় নতুন ডাটা ঢোকায়, পরের ডাটারা ডানে সরে যায়।", "v.insert(v.begin() + i, value);", "O(n)",
  E("মাঝে ঢোকানো", "vector<int> v = {1, 2, 4, 5};\nv.insert(v.begin() + 2, 3);\nfor (auto u : v) cout << u << ' ';", "index 2 এ 3 ঢুকেছে, 4 ও 5 ডানে সরেছে। ফল 1 2 3 4 5।"))
P("stl", V, "vector-iterate", "vector loop করা (foreach)", "vector-এর সব ডাটা একে একে দেখার সহজ নিয়ম। auto u : v মানে v-এর প্রতিটা ডাটা u তে আসবে।", "for (auto u : v)\nfor (auto &u : v)", "O(n)",
  E("প্রিন্ট ও বদলানো", "vector<int> v = {1, 2, 3};\nfor (auto u : v) cout << u << ' ';\ncout << endl;\nfor (auto &u : v) u *= 2;\nfor (auto u : v) cout << u << ' ';", "প্রথম লুপ শুধু পড়ে। &u (reference) দিলে আসল ডাটা বদলায়, তাই দ্বিতীয়বারে সব দ্বিগুণ।"))
P("stl", V, "vector-2d", "2D vector", "vector-এর ভেতর vector রাখলে table/matrix বানানো যায়।", "vector<vector<int>> g(n, vector<int>(m));", "O(n·m)",
  E("৩×৩ matrix", "vector<vector<int>> g(3, vector<int>(3, 0));\nfor (int i = 0; i < 3; i++) g[i][i] = 1;\nfor (auto &row : g) {\n    for (auto u : row) cout << u << ' ';\n    cout << endl;\n}", "৩ সারি ও ৩ কলামের সবঘরে 0 ছিল। কর্ণের ঘরে (i, i) 1 বসিয়ে identity matrix হলো।"))

S = "stack"
P("stl", S, "stack-push", "stack.push()", "Stack চলে LIFO নিয়মে (Last In First Out)। push() দিয়ে সবার মাথায় ডাটা বসে।", "st.push(value);", "O(1)",
  E("ডাটা বসানো", "stack<int> st;\nst.push(2);\nst.push(4);\nst.push(6);\ncout << st.size();", "৩টা ডাটা বসেছে তাই size 3।"))
P("stl", S, "stack-top", "stack.top()", "সবার উপরের ডাটা দেখায়, কিন্তু মুছে না। খালি stack-এ চালানো যাবে না।", "st.top();", "O(1)",
  E("top দেখা", "stack<int> st;\nst.push(1);\nst.push(5);\nst.push(9);\ncout << st.top() << endl << st.size();", "শেষে 9 বসেছে তাই top = 9। top() মুছে না, তাই size এখনো 3।"))
P("stl", S, "stack-pop", "stack.pop()", "সবার উপরের ডাটাটা মুছে ফেলে। এটা কোনো মান return করে না।", "st.pop();", "O(1)",
  E("pop করে প্রিন্ট", "stack<int> st;\nst.push(2);\nst.push(4);\nst.push(6);\nst.push(5);\nwhile (!st.empty()) {\n    cout << st.top() << ' ';\n    st.pop();\n}\ncout << endl << st.size();", "সবার শেষে 5 ঢুকেছিল, তাই সবার আগে বের হয়। উল্টো ক্রমে 5 6 4 2 প্রিন্ট হলো, শেষে size 0।"))
P("stl", S, "stack-size-empty", "stack.size() ও empty()", "size() ডাটার সংখ্যা জানায়, empty() খালি কিনা চেক করে।", "st.size();\nst.empty();", "O(1)",
  E("খালি চেক", "stack<int> st;\ncout << st.empty() << endl;\nst.push(3);\ncout << st.empty() << \" \" << st.size();", "শুরুতে খালি তাই empty() = 1 (true)। push করার পর 0 (false) এবং size 1।"),
  E("বন্ধনী balance", "string s = \"(()())\";\nstack<char> st;\nbool ok = true;\nfor (char c : s) {\n    if (c == '(') st.push(c);\n    else {\n        if (st.empty()) { ok = false; break; }\n        st.pop();\n    }\n}\nif (!st.empty()) ok = false;\ncout << (ok ? \"Balanced\" : \"Not Balanced\");", "'(' এলে push, ')' এলে pop। শেষে stack খালি থাকলে বন্ধনী ঠিকঠাক মিলেছে।"))

Q = "queue"
P("stl", Q, "queue-push", "queue.push() ও emplace()", "Queue চলে FIFO নিয়মে (First In First Out)। push() ও emplace() দুটোই পেছনে ডাটা যোগ করে।", "q.push(value);\nq.emplace(value);", "O(1)",
  E("পেছনে যোগ", "queue<int> q;\nq.push(5);\nq.push(10);\nq.push(15);\nq.emplace(20);\ncout << q.size();", "push ও emplace মিলিয়ে ৪টা ডাটা, তাই size 4।"))
P("stl", Q, "queue-front-back", "queue.front() ও back()", "front() সামনের (সবচেয়ে পুরনো) ডাটা, back() পেছনের (সবচেয়ে নতুন) ডাটা দেখায়।", "q.front();\nq.back();", "O(1)",
  E("সামনে ও পেছনে", "queue<int> q;\nq.push(5);\nq.push(10);\nq.push(15);\ncout << q.front() << \" ... \" << q.back();", "5 সবার আগে ঢুকেছে, 15 সবার শেষে। তাই front = 5, back = 15।"))
P("stl", Q, "queue-pop", "queue.pop()", "সামনের ডাটাটা মুছে ফেলে। এভাবে লাইনের প্রথম জন বের হয়ে যায়।", "q.pop();", "O(1)",
  E("পুরো queue প্রিন্ট", "queue<int> q;\nq.push(5);\nq.push(10);\nq.push(15);\nwhile (q.size() > 0) {\n    cout << q.front() << ' ';\n    q.pop();\n}", "যে আগে ঢুকেছে সে আগে বের হয়, তাই 5 10 15 ঢোকানোর ক্রমেই প্রিন্ট হলো।"))
P("stl", Q, "queue-size-empty", "queue.size() ও empty()", "size() কয়টা ডাটা আছে জানায়, empty() খালি কিনা চেক করে।", "q.size();\nq.empty();", "O(1)",
  E("চেক করা", "queue<int> q;\nif (q.empty()) cout << \"Empty\" << endl;\nq.push(1);\nq.push(2);\nif (!q.empty()) cout << \"Not Empty, size = \" << q.size();", "শুরুতে খালি। দুইটা ডাটা বসানোর পর size 2।"))
P("stl", Q, "queue-swap", "queue.swap()", "দুইটা queue-এর সব ডাটা পরস্পর অদলবদল করে।", "q1.swap(q2);", "O(1)",
  E("দুই queue অদলবদল", "queue<int> a, b;\na.push(1); a.push(2);\nb.push(9);\na.swap(b);\ncout << a.size() << \" \" << b.size() << endl << a.front() << \" \" << b.front();", "আগে a তে 2টা, b তে 1টা ছিল। swap এর পর a তে 1টা (9), b তে 2টা (1, 2)।"))

D = "deque"
P("stl", D, "deque-push_back", "deque.push_back() ও pop_back()", "Deque-এ দুই দিক থেকেই ডাটা ঢোকানো-মোছা যায়। push_back পেছনে ঢোকায়, pop_back পেছন থেকে মুছে।", "dq.push_back(x);\ndq.pop_back();", "O(1)",
  E("পেছনে ঢোকা ও মোছা", "deque<int> dq;\ndq.push_back(5);\ndq.push_back(10);\ndq.push_back(15);\ndq.pop_back();\nfor (auto u : dq) cout << u << ' ';", "3টা ঢোকার পর শেষের 15 মুছে গেছে। বাকি 5 10।"))
P("stl", D, "deque-push_front", "deque.push_front() ও pop_front()", "push_front সামনে ডাটা ঢোকায়, pop_front সামনের ডাটা মুছে।", "dq.push_front(x);\ndq.pop_front();", "O(1)",
  E("সামনে ঢোকা ও মোছা", "deque<int> dq;\ndq.push_back(5);\ndq.push_back(10);\ndq.push_front(1);\nfor (auto u : dq) cout << u << ' ';\ncout << endl;\ndq.pop_front();\nfor (auto u : dq) cout << u << ' ';", "push_front(1) এ 1 সবার সামনে এলো। pop_front() এ সেই 1 মুছে আবার 5 10 রইলো।"))
P("stl", D, "deque-front-back", "deque.front() ও back()", "সামনের ও পেছনের ডাটা দেখায়।", "dq.front();\ndq.back();", "O(1)",
  E("দুই প্রান্ত", "deque<int> dq = {1, 5, 10, 15};\ncout << dq.front() << endl << dq.back();", "প্রথম ডাটা 1, শেষ ডাটা 15।"))
P("stl", D, "deque-index", "deque[i] ও at()", "vector-এর মতোই index দিয়ে ডাটা ধরা যায়।", "dq[i]\ndq.at(i)", "O(1)",
  E("index দিয়ে প্রিন্ট", "deque<int> dq = {1, 5, 10, 15};\nfor (int i = 0; i < dq.size(); i++) cout << dq[i] << ' ';", "size = 4, তাই 0 থেকে 3 পর্যন্ত index ধরে সব প্রিন্ট হলো।"))
P("stl", D, "deque-insert-erase", "deque.insert() ও erase()", "iterator দিয়ে নির্দিষ্ট জায়গায় ডাটা ঢোকায় ও মুছে।", "dq.insert(it, count, value);\ndq.erase(it1, it2);", "O(n)",
  E("insert ও erase", "deque<int> dq = {1, 5, 10, 15};\nauto it = dq.begin() + 2;\ndq.insert(it, 3, 0);\nfor (auto u : dq) cout << u << ' ';\ncout << endl;\ndq.erase(dq.begin() + 2, dq.begin() + 5);\nfor (auto u : dq) cout << u << ' ';", "index 2 এ তিনটা 0 ঢুকলো। এরপর index 2 থেকে 4 পর্যন্ত (তিনটা 0) মুছে আগের অবস্থায় ফিরলো।"))
P("stl", D, "deque-size-clear-empty", "deque.size(), clear(), empty()", "size() ডাটার সংখ্যা, clear() সব মুছা, empty() খালি কিনা চেক।", "dq.size();\ndq.clear();\ndq.empty();", "O(1) / clear O(n)",
  E("তিনটাই একসাথে", "deque<int> dq = {1, 2, 3};\ncout << dq.size() << endl;\ndq.clear();\nif (dq.empty()) cout << \"Empty\";\nelse cout << \"Not Empty\";", "আগে size 3। clear() এর পর খালি, তাই Empty প্রিন্ট।"),
  E("deque দিয়ে array উল্টানো", "deque<int> dq;\nint a[] = {1, 2, 3, 4};\nfor (int x : a) dq.push_front(x);\nfor (auto u : dq) cout << u << ' ';", "প্রতিটা ডাটা সামনে ঢোকালে শেষে ক্রম উল্টে যায়। তাই 4 3 2 1।"))
