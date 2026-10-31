import pages from "./pages.json";

export const tabs = [
  {
    id: "stl", label: "STL", color: "emerald", icon: "box",
    blurb: "Standard Template Library — প্রতিটা function আলাদা পেজে, উদাহরণ ও output সহ",
    about: "vector, set, map, string, algorithm … C++ এর তৈরি করা data structure ও function এর পুরো ভান্ডার। Contest এ সময় বাঁচাতে এগুলোই সবচেয়ে বেশি কাজে লাগে।",
    learn: ["vector, stack, queue, deque", "set, multiset, map, unordered", "string ও algorithm (sort, binary_search …)", "priority_queue, pair, bitset"],
  },
  {
    id: "bits", label: "বিটের মজা", color: "amber", icon: "bit",
    blurb: "Bit operation দিয়ে দ্রুত ও চালাক হিসাব",
    about: "কম্পিউটার সবকিছু 0 আর 1 দিয়ে বোঝে। বিটের খেলা শিখলে জোড়-বিজোড়, 2 এর ঘাত, subset — সবকিছু এক লাইনে করা যায়। প্রতিটা বিট ঘরে ঘরে ছবি দিয়ে দেখানো আছে।",
    learn: ["AND, OR, XOR, NOT — প্রতিটা ঘর ধরে ধরে", "Left/Right shift ও 2 এর ঘাত", "i-তম বিট check, set, clear, toggle", "popcount ও subset generation"],
  },
  {
    id: "nt", label: "নাম্বার থিওরি", color: "blue", icon: "sigma",
    blurb: "Prime, Divisor, Sieve, GCD/LCM, Modular Arithmetic ও Euler Phi",
    about: "Contest এর সবচেয়ে জনপ্রিয় বিষয়গুলোর একটা। Prime থেকে শুরু করে Modular Inverse ও Euler Phi পর্যন্ত — প্রতিটা ধাপের হিসাব টেবিলে ভেঙে দেখানো হয়েছে।",
    learn: ["Prime, Divisor ও Harmonic Series", "Sieve ও Prime Factorization", "GCD, LCM, NOD, SOD, SNOD", "Modular Arithmetic, Inverse, nCr, Euler Phi"],
  },
  {
    id: "rec", label: "রিকার্সন ও DP", color: "purple", icon: "loop",
    blurb: "Recursive function থেকে Memoization ও Basic Dynamic Programming",
    about: "function যখন নিজেকেই ডাকে, তখন সেটা recursion। কিন্তু একই কাজ বারবার করলে program ধীর হয়ে যায়। একবার করা কাজ মনে রাখার কৌশল (Memoization) শিখলেই Dynamic Programming এর প্রথম দরজা খুলে যায়। Fibonacci দিয়ে হাতে-কলমে দেখানো হয়েছে।",
    learn: ["Recursive function ও base case", "call tree ও কতবার function ডাকা হয়", "Memoization (Top-Down) ও Bottom-Up", "memset, int বনাম long long এর সীমা"],
  },
  {
    id: "graph", label: "গ্রাফ থিওরি", color: "rose", icon: "graph",
    blurb: "Adjacency Matrix/List, BFS (level, পথ), DFS (৩ রং, back edge), Dijkstra, DSU ও Minimum Spanning Tree",
    about: "রাস্তা, নেটওয়ার্ক, বন্ধুত্ব, maze — সবই graph। এখানে graph রাখার উপায় থেকে শুরু করে BFS, DFS, shortest path (Dijkstra), DSU আর MST (Kruskal, Prim) পর্যন্ত প্রতিটা ধাপ node আর edge এর ছবি এঁকে দেখানো হয়েছে।",
    learn: ["Adjacency Matrix ও List (weighted সহ)", "BFS এর level, queue ও পথ বের করা", "DFS এর ৩ রং, back edge ও cycle, grid এ হাঁটা", "Dijkstra, DSU, Kruskal ও Prim"],
    readingTitle: "আরও পড়ার জন্য: শাফায়েতের ব্লগের গ্রাফ থিওরি সিরিজ",
    readingNote: "এই সিরিজের সবগুলো লেখা PDF আকারে রিপোজিটরির CP/L2 ফোল্ডারে আছে। গ্রাফ শেখার ক্রম অনুযায়ী সাজানো:",
    reading: ["গ্রাফ থিওরিতে হাতেখড়ি - ১", "গ্রাফ থিওরিতে হাতেখড়ি - ২ (টিউটোরিয়াল)", "গ্রাফ থিওরিতে হাতেখড়ি - ৩ (ভ্যারিয়েবলে গ্রাফ স্টোর-২)", "গ্রাফ থিওরিতে হাতেখড়ি-৪ (ব্রেথড ফার্স্ট সার্চ-BFS)", "গ্রাফ থিওরিতে হাতেখড়ি ৫: মিনিমাম স্প্যানিং ট্রি (প্রিম অ্যালগরিদম)", "গ্রাফ থিওরিতে হাতেখড়ি ৬: মিনিমাম স্প্যানিং ট্রি (ক্রুসকাল অ্যালগরিদম)", "গ্রাফ থিওরিতে হাতেখড়ি ৭: টপোলজিকাল সর্ট", "গ্রাফ থিওরিতে হাতেখড়ি ৮: ডেপথ ফার্স্ট সার্চ এবং আবারো টপোলজিকাল সর্ট", "গ্রাফ থিওরিতে হাতেখড়ি-৯ (ডায়াক্সট্রা)", "গ্রাফ থিওরিতে হাতেখড়ি ১০: ফ্লয়েড ওয়ার্শল", "গ্রাফ থিওরিতে হাতেখড়ি ১১: বেলম্যান ফোর্ড", "গ্রাফ থিওরিতে হাতেখড়ি ১২ – ম্যাক্সিমাম ফ্লো (১) ও (২)", "গ্রাফ থিওরিতে হাতেখড়ি ১৩: আর্টিকুলেশন পয়েন্ট এবং ব্রিজ", "গ্রাফ থিওরিতে হাতেখড়ি ১৪ – স্ট্রংলি কানেক্টেড কম্পোনেন্ট", "অয়লার ট্যুর (ফ্লিরি এবং হেয়ারহজলার অ্যালগরিদম)", "লংগেস্ট পাথ প্রবলেম", "গ্রাফ থিওরি: স্টেবল ম্যারেজ প্রবলেম"],
    repo: "https://github.com/Hafiz-Sakib/CPP-for-CP/tree/main/CP/L2",
  },
];
export { pages };
export const colors = ["emerald", "amber", "blue", "purple"];
export const index = Object.fromEntries(pages.map((p, i) => [p.id, i]));
export const groupPages = (g) => pages.filter((p) => p.grp === g);
export const exampleCount = (g) => groupPages(g).reduce((n, p) => n + p.examples.length, 0);
export const bn = (n) => String(n).replace(/\d/g, (d) => "০১২৩৪৫৬৭৮৯"[d]);
export const categories = (g) => {
  const out = [];
  groupPages(g).forEach((p) => {
    let c = out.find((x) => x.cat === p.cat);
    if (!c) { c = { cat: p.cat, color: colors[out.length % 4], pages: [] }; out.push(c); }
    c.pages.push(p);
  });
  return out;
};
export const colorOf = (p) => categories(p.grp).find((c) => c.cat === p.cat)?.color || "slate";
