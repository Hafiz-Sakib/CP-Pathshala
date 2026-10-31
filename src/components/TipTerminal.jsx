import { useEffect, useState } from "react";
import { reduced } from "./Reveal";

// হিরোর স্ট্যাটের জায়গায়: টার্মিনালে টাইপ হওয়া contest-টিপস (প্রতিবার নতুন একটা)
const TIPS = [
  ["n & (n - 1)", "সবচেয়ে ডানের 1 বিটটা মুছে দেয়"],
  ["i * i <= n", "√n পর্যন্ত গেলেই prime check শেষ"],
  ["vis[child] = 1", "queue তে ঢোকানোর সময়ই, pop এ নয়"],
  ["dp[n] != -1", "আগে করা কাজ আবার নয়, খাতা থেকে নাও"],
  ["long long", "int এ fibo(47) থেকেই overflow"],
  ["find(u) == find(v)", "সত্য হলে edge নিলে cycle হবে"],
  ["cin.tie(NULL)", "বড় input এ সময় বাঁচায়"],
];

export default function TipTerminal() {
  const [i, setI] = useState(0);
  const [n, setN] = useState(reduced() ? 999 : 0);
  const [code, hint] = TIPS[i];
  const full = code.length + 3;

  useEffect(() => {
    if (reduced()) return;
    const t = setTimeout(() => {
      if (n < full + 26) setN(n + 1);
      else { setI((i + 1) % TIPS.length); setN(0); }
    }, n < full ? 70 : 60);
    return () => clearTimeout(t);
  }, [n, full]);

  const typed = ("$ " + code).slice(0, Math.min(n, code.length + 2));
  return (
    <div className="mt-8 max-w-lg overflow-hidden rounded-2xl bg-black/35 ring-1 ring-white/20" aria-label="contest টিপস">
      <div className="flex items-center gap-1.5 border-b border-white/10 bg-white/5 px-3 py-2">
        <i className="h-2.5 w-2.5 rounded-full bg-rose-400" /><i className="h-2.5 w-2.5 rounded-full bg-amber-300" /><i className="h-2.5 w-2.5 rounded-full bg-emerald-400" />
        <span className="ml-2 font-mono text-xs text-white/60">contest-tip.cpp</span>
      </div>
      <div className="min-h-[5.2rem] px-4 py-3 font-mono text-[15px] leading-relaxed">
        <p className="text-emerald-300">{typed}<span className="ml-0.5 inline-block h-4 w-2 translate-y-0.5 animate-pulse bg-amber-300" /></p>
        <p className={`mt-1 text-white/80 transition-opacity duration-500 ${n >= code.length + 3 ? "opacity-100" : "opacity-0"}`}>// {hint}</p>
      </div>
    </div>
  );
}
