import { useEffect, useRef, useState } from "react";
import { BitRow, Weights } from "./BitViz";
import { useInView, reduced } from "./Reveal";

export default function BinaryCounter() {
  const [ref, inView] = useInView(false);
  const [n, setN] = useState(0);
  const prev = useRef(0);
  useEffect(() => {
    if (!inView || reduced()) return;
    const id = setInterval(() => setN((x) => { prev.current = x; return (x + 1) & 255; }), 800);
    return () => clearInterval(id);
  }, [inView]);
  const bits = n.toString(2).padStart(8, "0");
  const hl = [...bits].map((c, i) => (c !== prev.current.toString(2).padStart(8, "0")[i] ? i : -1)).filter((i) => i >= 0);
  const pop = [...bits].filter((c) => c === "1").length;
  return (
    <div ref={ref} className="rounded-3xl border border-emerald-200 bg-white p-4 shadow-md sm:p-6">
      <div className="overflow-x-auto pb-2 no-scrollbar"><div className="w-max">
        <Weights len={8} />
        <BitRow r={{ label: "n", bits, dec: n, tone: "r", hl, sep: false }} />
      </div></div>
      <div className="mt-4 grid gap-3 text-center sm:grid-cols-3">
        <div className="rounded-2xl bg-emerald-50 p-3 ring-1 ring-emerald-200"><p className="text-sm text-slate-600">n & 1</p><p className="font-mono text-lg font-bold text-brand-ink">{n & 1} → {n & 1 ? "বিজোড়" : "জোড়"}</p></div>
        <div className="rounded-2xl bg-amber-50 p-3 ring-1 ring-amber-200"><p className="text-sm text-slate-600">popcount (1 এর সংখ্যা)</p><p className="font-mono text-lg font-bold text-brand-ink">{pop}</p></div>
        <div className="rounded-2xl bg-sky-50 p-3 ring-1 ring-sky-200"><p className="text-sm text-slate-600">n & (n−1)</p><p className="font-mono text-lg font-bold text-brand-ink">{n & (n - 1)} {n && !(n & (n - 1)) ? "→ 2 এর ঘাত ✔" : ""}</p></div>
      </div>
    </div>
  );
}
