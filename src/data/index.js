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
