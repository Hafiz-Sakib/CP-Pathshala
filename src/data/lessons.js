import vectorCode from "../code/vector.cpp?raw";
import stackCode from "../code/STL_Stack.cpp?raw";
import queueCode from "../code/STL_Queue.cpp?raw";
import dequeCode from "../code/STL_Deque.cpp?raw";
import pqCode from "../code/STL_Priority_Queue.cpp?raw";
import setCode from "../code/STL_Set.cpp?raw";
import msetCode from "../code/STL_MultiSet.cpp?raw";
import listCode from "../code/STL_List.cpp?raw";
import mapDecl from "../code/2__map_declaration.cpp?raw";
import mapFreq from "../code/3_count__frequency__with__map.cpp?raw";
import mapErase from "../code/map__erase.cpp?raw";
import shiftCode from "../code/divide_by_powOF2.cpp?raw";
import pow2Code from "../code/is_powerOF2.cpp?raw";
import oddEvenCode from "../code/odd_even.cpp?raw";
import primeCode from "../code/prime__check__TrialDivision.cpp?raw";
import divisorsCode from "../code/divisors.cpp?raw";
import sumCntCode from "../code/sum__and___cnt__of__divisors.cpp?raw";
import sieveCode from "../code/Basic_Sieve_of_Eratosthenes.cpp?raw";
import bitsetSieveCode from "../code/Bitset_Sieve.cpp?raw";
import snodCode from "../code/SNOD_efficient.cpp?raw";

const f = (name, desc, ex) => ({ name, desc, ex });

/* ---------- STL ---------- */
export const stl = [
  { id: "vector", title: "Vector", color: "emerald",
    intro: "Vector হলো একটা dynamic array — মানে ইচ্ছামতো বড়-ছোট হতে পারে। শুরুতেই সাইজ বলে দিতে হয় না।",
    funcs: [
      f("vector<int> v;", "খালি vector declare করে। <int> মানে এতে int ডাটা থাকবে।", "vector<int> v;"),
      f("v = {1,2,3,4,5}", "declare করার সময়ই সরাসরি ডাটা বসিয়ে দেয়।", "vector<int> vv = {1, 2, 3, 4, 5};"),
      f("push_back()", "Vector-এর একদম শেষে নতুন ডাটা যোগ করে।", "v.push_back(1); // v[0] = 1"),
      f("pop_back()", "Vector-এর শেষের ডাটাটা মুছে ফেলে।", "vv.pop_back();"),
      f("v[i]", "i নম্বর index-এর ডাটা দেখায়। index না থাকলে garbage value দেয়।", "cout << v[0];"),
      f("at()", "v[i]-এর মতোই, কিন্তু index না থাকলে error message দেয় (নিরাপদ)।", "cout << v.at(0);"),
      f("size()", "Vector-এ কয়টা ডাটা আছে তা জানায়।", "cout << v.size();"),
      f("front()", "প্রথম ডাটা দেখায়, আবার নতুন মানও বসানো যায়।", "v.front() = 5;"),
      f("back()", "শেষ ডাটা দেখায়, আবার নতুন মানও বসানো যায়।", "v.back() = 10;"),
      f("erase()", "iterator দিয়ে নির্দিষ্ট index-এর ডাটা মুছে। দুইটা দিলে রেঞ্জ মুছে।", "vv.erase(vv.begin() + 2); // index 2 delete\nvvv.erase(vvv.begin() + 2, vvv.end()); // index 2 থেকে শেষ পর্যন্ত"),
      f("clear()", "Vector-এর সব ডাটা মুছে ফেলে, size হয়ে যায় 0।", "v.clear();"),
      f("empty()", "Vector খালি কিনা চেক করে (খালি হলে true)।", "if (v.empty()) cout << \"Empty\";"),
    ], code: vectorCode },
  { id: "stack", title: "Stack", color: "amber",
    intro: "Stack চলে LIFO নিয়মে — Last In First Out। যে ডাটা সবার শেষে ঢুকেছে সেটাই আগে বের হয়, যেমন থালার স্তূপ।",
    funcs: [
      f("stack<int> st;", "খালি stack declare করে।", "stack<int> st;"),
      f("push()", "Stack-এর মাথায় নতুন ডাটা বসায়।", "st.push(2);"),
      f("top()", "সবার উপরের ডাটা দেখায় (মুছে না)।", "cout << st.top();"),
      f("pop()", "সবার উপরের ডাটাটা মুছে ফেলে।", "st.pop();"),
      f("size()", "Stack-এ কয়টা ডাটা আছে তা জানায়।", "cout << st.size();"),
      f("empty()", "Stack খালি কিনা চেক করে। while লুপে প্রিন্টের সময় লাগে।", "while (!st.empty()) { cout << st.top(); st.pop(); }"),
    ], code: stackCode },
  { id: "queue", title: "Queue", color: "blue",
    intro: "Queue চলে FIFO নিয়মে — First In First Out। লাইনে যে আগে দাঁড়ায় সে আগে বের হয়।",
    funcs: [
      f("queue<int> q;", "খালি queue declare করে।", "queue<int> q;"),
      f("push()", "Queue-এর পেছনে ডাটা যোগ করে।", "q.push(5);"),
      f("emplace()", "push()-এর মতোই পেছনে ডাটা যোগ করে।", "q.emplace(20);"),
      f("front()", "সামনের (প্রথম) ডাটা দেখায়।", "cout << q.front();"),
      f("back()", "পেছনের (শেষ) ডাটা দেখায়।", "cout << q.back();"),
      f("pop()", "সামনের ডাটাটা মুছে ফেলে।", "q.pop();"),
      f("size()", "Queue-এ কয়টা ডাটা আছে।", "cout << q.size();"),
      f("empty()", "Queue খালি কিনা চেক করে।", "if (q.empty()) cout << \"Empty\";"),
      f("swap()", "দুইটা queue-এর ডাটা অদলবদল করে।", "q.swap(q2);"),
    ], code: queueCode },
  { id: "deque", title: "Deque", color: "purple",
    intro: "Deque (Double Ended Queue)-তে সামনে ও পেছন — দুই দিক থেকেই ডাটা ঢোকানো ও মোছা যায়।",
    funcs: [
      f("deque<int> dq;", "খালি deque declare করে।", "deque<int> dq;"),
      f("push_back()", "পেছনে ডাটা যোগ করে।", "dq.push_back(5);"),
      f("push_front()", "সামনে ডাটা যোগ করে।", "dq.push_front(1);"),
      f("pop_back()", "পেছনের ডাটা মুছে।", "dq.pop_back();"),
      f("pop_front()", "সামনের ডাটা মুছে।", "dq.pop_front();"),
      f("insert()", "iterator দিয়ে নির্দিষ্ট জায়গায় ডাটা ঢোকায়।", "dq.insert(dq.begin() + 2, 3, 0); // index 2-এ ৩টা 0"),
      f("erase()", "iterator দিয়ে নির্দিষ্ট জায়গার ডাটা মুছে।", "dq.erase(it, it2);"),
      f("front() / back()", "প্রথম ও শেষ ডাটা দেখায়।", "cout << dq.front() << dq.back();"),
      f("size()", "কয়টা ডাটা আছে।", "int s = dq.size();"),
      f("clear()", "সব ডাটা মুছে।", "dq.clear();"),
      f("empty()", "খালি কিনা চেক করে।", "if (dq.empty()) cout << \"Empty\";"),
    ], code: dequeCode },
  { id: "pq", title: "Priority Queue", color: "emerald",
    intro: "Priority Queue-তে ডাটা নিজে নিজেই সাজানো থাকে। ডিফল্টে সবচেয়ে বড় ডাটা সবার আগে বের হয়।",
    funcs: [
      f("priority_queue<int>", "বড় থেকে ছোট ক্রমে ডাটা দেয় (Max Heap)।", "priority_queue<int> pq1;"),
      f("greater<int>", "ছোট থেকে বড় ক্রমে ডাটা দিতে এভাবে declare করতে হয় (Min Heap)।", "priority_queue<int, vector<int>, greater<int>> pq2;"),
      f("push()", "ডাটা ঢোকায়, নিজে থেকেই সঠিক জায়গায় বসে যায়।", "pq1.push(5);"),
      f("emplace()", "push()-এর মতোই কাজ করে।", "pq2.emplace(7);"),
      f("top()", "সবচেয়ে অগ্রাধিকারের ডাটা দেখায়।", "cout << pq1.top();"),
      f("pop()", "top-এর ডাটাটা মুছে ফেলে।", "pq1.pop();"),
      f("size() / empty()", "সাইজ জানায় / খালি কিনা চেক করে।", "while (!pq1.empty()) { ... }"),
      f("swap()", "দুইটা priority queue অদলবদল করে।", "pq1.swap(pq3);"),
    ], code: pqCode },
  { id: "set", title: "Set", color: "amber",
    intro: "Set-এ শুধু unique ডাটা থাকে, আর ডিফল্টে ছোট থেকে বড় ক্রমে সাজানো থাকে। একই ডাটা দুইবার দিলে একবারই থাকে।",
    funcs: [
      f("set<int> s;", "খালি set declare করে। বড় থেকে ছোট চাইলে set<int, greater<int>> s;", "set<int> s;"),
      f("insert()", "ডাটা ঢোকায়। আগে থেকে থাকলে আর ঢোকে না।", "s.insert(2);"),
      f("emplace()", "insert()-এর মতোই।", "s.emplace(5);"),
      f("size() / max_size()", "বর্তমান ডাটার সংখ্যা / সর্বোচ্চ কতটা ধরতে পারবে।", "cout << s.size() << s.max_size();"),
      f("erase()", "মান দিয়ে বা iterator দিয়ে ডাটা মুছে।", "s.erase(2);"),
      f("find()", "ডাটা খোঁজে। পেলে iterator, না পেলে s.end() দেয়।", "auto it3 = s.find(1);"),
      f("count()", "ডাটা আছে কিনা বলে (set-এ 1 বা 0)।", "if (s.count(1)) cout << \"Found\";"),
      f("lower_bound()", "দেওয়া মান বা তার চেয়ে বড় প্রথম ডাটার iterator দেয়।", "s1.lower_bound(2);"),
      f("upper_bound()", "দেওয়া মানের চেয়ে বড় প্রথম ডাটার iterator দেয়।", "s1.upper_bound(2);"),
      f("empty()", "খালি কিনা চেক করে।", "if (s.empty()) ..."),
      f("clear()", "সব ডাটা মুছে।", "s.clear();"),
      f("swap()", "দুইটা set অদলবদল করে।", "s.swap(s1);"),
    ], code: setCode },
  { id: "multiset", title: "Multiset", color: "blue",
    intro: "Multiset অনেকটা set-এর মতোই সাজানো থাকে, কিন্তু এখানে একই ডাটা একাধিকবার রাখা যায়।",
    funcs: [
      f("multiset<int> ms;", "খালি multiset declare করে। descending-এর জন্য multiset<int, greater<int>>", "multiset<int> ms;"),
      f("insert() / emplace()", "ডাটা ঢোকায়, duplicate ঢোকানোও যায়।", "ms.insert(2); ms.insert(2);"),
      f("erase(value)", "ঐ মানের সবগুলো ডাটা একসাথে মুছে ফেলে।", "ms.erase(2);"),
      f("erase(iterator)", "শুধু ঐ একটা জায়গার ডাটা মুছে।", "ms.erase(ms.begin());"),
      f("find()", "ডাটা খোঁজে, না পেলে end() দেয়।", "auto it2 = ms.find(1);"),
      f("count()", "ঐ ডাটা কতবার আছে তা বলে।", "cout << ms.count(7);"),
      f("lower_bound()", "মান বা তার চেয়ে বড় প্রথম ডাটা দেয়। না থাকলে end()।", "ms.lower_bound(3);"),
      f("upper_bound()", "দেওয়া মানের পরের বড় ডাটা দেয়। না থাকলে end()।", "ms.upper_bound(5);"),
      f("size() / clear()", "সাইজ জানায় / সব মুছে।", "ms2.clear();"),
      f("swap() / assign", "অদলবদল করে / একটাকে আরেকটায় কপি করে।", "ms1 = ms;"),
    ], code: msetCode },
  { id: "list", title: "List", color: "purple",
    intro: "List হলো doubly linked list। মাঝখানে insert/delete করা সহজ, কিন্তু v[i]-এর মতো সরাসরি index ধরা যায় না।",
    funcs: [
      f("list<int> li;", "খালি list declare করে।", "list<int> li;"),
      f("push_back()", "শেষে ডাটা যোগ করে।", "li.push_back(1);"),
      f("push_front()", "শুরুতে ডাটা যোগ করে।", "li.push_front(4);"),
      f("pop_back() / pop_front()", "শেষের / শুরুর ডাটা মুছে।", "li.pop_front();"),
      f("insert()", "iterator দিয়ে নির্দিষ্ট জায়গায় ডাটা ঢোকায়। advance() দিয়ে iterator এগোনো যায়।", "advance(ite, 2); li.insert(ite, 3);"),
      f("front() / back()", "প্রথম ও শেষ ডাটা দেখায়।", "cout << li.front();"),
      f("remove()", "ঐ মানের সবগুলো ডাটা মুছে।", "li2.remove(2);"),
      f("reverse()", "list উল্টে দেয়।", "li2.reverse();"),
      f("sort()", "ছোট থেকে বড় ক্রমে সাজায়।", "li2.sort();"),
      f("unique()", "পাশাপাশি থাকা duplicate মুছে (আগে sort করা ভালো)।", "li2.unique();"),
      f("merge()", "দুইটা list এক করে।", "li2.merge(li3);"),
      f("swap()", "দুইটা list অদলবদল করে।", "li2.swap(li3);"),
      f("size() / empty() / clear()", "সাইজ / খালি কিনা / সব মুছা।", "li.clear();"),
    ], code: listCode },
  { id: "map", title: "Map", color: "emerald",
    intro: "Map-এ ডাটা থাকে key–value জোড়ায়। key দিয়ে value খোঁজা যায়, আর key গুলো সবসময় ছোট থেকে বড় ক্রমে সাজানো থাকে।",
    funcs: [
      f("map<key, value> m;", "map declare করার নিয়ম: map<key_dataType, value_dataType> mapName;", "map<string, int> id;"),
      f("m[key] = value", "key-তে value বসায়।", "id[\"Sakib\"] = 101;"),
      f("m[key]", "key দিয়ে value দেখায়।", "cout << id[\"Miraz\"];"),
      f("m[key]++", "frequency (কোনটা কতবার আছে) গুনতে কাজে লাগে।", "for (auto u : v) m[u]++;"),
      f("u.first / u.second", "foreach লুপে key হলো first, value হলো second।", "for (auto u : m) cout << u.first << \" \" << u.second;"),
      f("erase()", "key দিয়ে জোড়া মুছে। clear() দিলে সব মুছে।", "mp.erase(3);"),
    ], code: mapDecl + "\n// ---------- frequency গোনা ----------\n" + mapFreq + "\n// ---------- erase ----------\n" + mapErase },
];

/* ---------- বিটের মজা ---------- */
export const bits = [
  { id: "shift", title: "Right Shift দিয়ে ভাগ", color: "emerald",
    intro: "a >> n মানে a কে 2 এর n ঘাত দিয়ে ভাগ করা। ভাগের চেয়ে অনেক দ্রুত কাজ করে।",
    funcs: [
      f("a >> 1", "a / 2^1 এর সমান।", "int x = a >> 1; // 1024/2 = 512"),
      f("a >> 4", "a / 2^4 এর সমান।", "int y = a >> 4; // 1024/16 = 64"),
      f("a >> 6", "a / 2^6 এর সমান।", "int z = a >> 6; // 1024/64 = 16"),
      f("a >> 8", "a / 2^8 এর সমান।", "int n = a >> 8; // 1024/256 = 4"),
    ], code: shiftCode },
  { id: "pow2", title: "2 এর ঘাত কিনা", color: "amber",
    intro: "একটা সংখ্যা 2 এর ঘাত (1, 2, 4, 8, 16 ...) কিনা এক লাইনে O(1) এ বের করা যায়।",
    funcs: [
      f("x & (x - 1)", "2 এর ঘাতে মাত্র একটা বিট 1 থাকে, তাই x ও x-1 এর AND সবসময় 0 হয়।", "x & (x - 1)"),
      f("x && ...", "x = 0 হলে ভুল উত্তর আসে, তাই আগে x != 0 চেক করা হয়।", "return (x && (!(x & (x - 1))));"),
      f("Time Complexity", "লুপ ছাড়াই কাজ হয়, তাই O(1)।", "isPowerOFTwo(512) // YES"),
    ], code: pow2Code },
  { id: "oddeven", title: "জোড়-বিজোড় চেক", color: "blue",
    intro: "একটা সংখ্যার শেষ বিট 1 হলে সেটা বিজোড় (odd), 0 হলে জোড় (even)।",
    funcs: [
      f("a & 1", "শেষ বিট বের করে। 1 পেলে odd, 0 পেলে even।", "if (a & 1) cout << \"Odd Number\";"),
      f("a % 2 এর বদলে", "% এর চেয়ে বিট অপারেশন দ্রুত।", "else cout << \"Even Number\";"),
    ], code: oddEvenCode },
];

/* ---------- Number Theory ---------- */
export const nt = [
  { id: "prime", title: "Prime Check", color: "emerald",
    intro: "Trial Division: 3 থেকে √n পর্যন্ত ভাগ করে দেখা হয়। কোনোটাতে ভাগ গেলে সংখ্যাটা prime না।",
    funcs: [
      f("i * i <= n", "√n পর্যন্ত গেলেই যথেষ্ট। এতে সময় O(√n) লাগে।", "for (ll i = 3; i * i <= n; i++)"),
      f("n % i == 0", "ভাগ গেলে n composite, তখনই return।", "if (n % i == 0) { cout << \"Not a Prime\"; return; }"),
    ], code: primeCode },
  { id: "divisors", title: "Divisors বের করা", color: "amber",
    intro: "i দিয়ে n ভাগ গেলে i এবং n/i দুইটাই divisor। তাই √n পর্যন্ত গেলেই সব divisor পাওয়া যায়।",
    funcs: [
      f("set<ll> s", "divisor গুলো সাজানো ও unique রাখতে set ব্যবহার করা হয়েছে।", "s.insert({i, n / i});"),
      f("n / i", "জোড়ার অপর divisor।", "if (n % i == 0) ..."),
    ], code: divisorsCode },
  { id: "sumcnt", title: "Divisor সংখ্যা ও যোগফল", color: "blue",
    intro: "এক লুপেই divisor-এর সংখ্যা (cnt) আর যোগফল (sum) দুটোই বের করা যায়।",
    funcs: [
      f("cnt", "প্রতিটা divisor পেলে 1 করে বাড়ে।", "cnt += 1;"),
      f("sum", "প্রতিটা divisor যোগ হয়।", "sum += i;"),
      f("i != n / i", "perfect square হলে একই divisor দুইবার গুনা এড়াতে এই চেক।", "if (i != (n / i)) { sum += n / i; cnt++; }"),
    ], code: sumCntCode },
  { id: "sieve", title: "Sieve of Eratosthenes", color: "purple",
    intro: "একসাথে 1 থেকে n পর্যন্ত সব prime বের করার পদ্ধতি। প্রথমে সবাইকে prime ধরে নিয়ে গুণিতকগুলো কেটে দেওয়া হয়।",
    funcs: [
      f("is_prime(mx, 1)", "শুরুতে সবাইকে prime (1) ধরা হয়।", "vector<bool> is_prime(mx, 1);"),
      f("j += i", "i এর সব গুণিতককে 0 (prime না) করা হয়।", "for (int j = i + i; j <= n; j += i) is_prime[j] = 0;"),
      f("prime vector", "যেগুলো 1 থেকে গেছে সেগুলো prime vector-এ ঢোকানো হয়।", "prime.push_back(i);"),
      f("Time Complexity", "এই basic ভার্সনে O(n log n)।", "Sieve(20);"),
    ], code: sieveCode },
  { id: "bitsetsieve", title: "Bitset Sieve", color: "emerald",
    intro: "বড় রেঞ্জের (যেমন 1e8) জন্য bitset দিয়ে sieve। মেমোরি অনেক কম লাগে, শুধু বিজোড় সংখ্যা চেক হয়।",
    funcs: [
      f("bitset<mx>", "প্রতিটা সংখ্যার জন্য মাত্র ১ বিট মেমোরি।", "bitset<mx> is_prime;"),
      f("i += 2", "শুধু বিজোড় সংখ্যা নিয়ে কাজ, 2 আলাদা ভাবে prime ধরা হয়।", "for (int i = 3; i <= n; i += 2)"),
      f("j = i * i", "i*i থেকে শুরু করে (i + i) ধাপে গুণিতক কাটা হয়।", "for (int j = i * i; j <= n; j += (i + i))"),
      f("Time Complexity", "O(n log(log n))।", "sieve(1e8);"),
    ], code: bitsetSieveCode },
  { id: "snod", title: "SNOD (O(√n))", color: "amber",
    intro: "SNOD = 1 থেকে n পর্যন্ত সব সংখ্যার divisor সংখ্যার যোগফল। এটা O(√n) এ বের করা যায়।",
    funcs: [
      f("n / i", "i কতগুলো সংখ্যার divisor হয় তা এটা দিয়ে বোঝা যায়।", "ans += (n / i) - i;"),
      f("ans *= 2", "জোড়ায় জোড়ায় গোনা হয় বলে দ্বিগুণ করা হয়।", "ans *= 2;"),
      f("ans += u", "u = √n, শেষে এটা যোগ করে নিতে হয়।", "ans += u;"),
    ], code: snodCode },
];

export const tabs = [
  { id: "stl", label: "STL", data: stl, blurb: "Standard Template Library-র container ও তাদের function" },
  { id: "bits", label: "বিটের মজা", data: bits, blurb: "Bit operation দিয়ে দ্রুত হিসাব" },
  { id: "nt", label: "নাম্বার থিওরি", data: nt, blurb: "Prime, Divisor, Sieve ও SNOD" },
];
