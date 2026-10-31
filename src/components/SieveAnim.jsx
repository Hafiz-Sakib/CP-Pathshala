import { useEffect, useMemo, useState } from "react";
import { useInView, reduced } from "./Reveal";

const N = 50;
function buildEvents() {
  const ev = [], crossed = new Set();
  for (let p = 2; p * p <= N; p++) {
    if (crossed.has(p)) continue;
    ev.push({ p });
    for (let j = p * p; j <= N; j += p) { if (!crossed.has(j)) { crossed.add(j); ev.push({ p, x: j }); } }
  }
  return ev;
}

export default function SieveAnim() {
  const ev = useMemo(buildEvents, []);
  const [ref, inView] = useInView(false);
  const [s, setS] = useState(0);
  const [play, setPlay] = useState(true);
  const done = s >= ev.length;

  useEffect(() => {
    if (!inView || !play || reduced()) return;
    const id = setTimeout(() => setS((x) => (x >= ev.length + 6 ? 0 : x + 1)), done ? 400 : 260);
    return () => clearTimeout(id);
  }, [inView, play, s, done, ev.length]);

  const crossed = new Set();
  let cur = null;
  ev.slice(0, s).forEach((e) => { if (e.x) crossed.add(e.x); else cur = e.p; });
  const last = s > 0 && s <= ev.length ? ev[s - 1] : null;
  const msg = done ? "শেষ! যারা কাটা পড়েনি সবাই prime 🎉" : last?.x ? `${last.p} এর গুণিতক ${last.x} কেটে দেওয়া হলো` : last ? `${last.p} prime — এবার ওর গুণিতক কাটবো` : "শুরু: সবাই সম্ভাব্য prime";

  return (
    <div ref={ref} className="rounded-3xl border border-blue-200 bg-white p-4 shadow-md sm:p-6">
      <div className="grid grid-cols-5 gap-1.5 sm:grid-cols-10">
        {Array.from({ length: N }, (_, i) => i + 1).map((k) => {
          const x = k === 1 || crossed.has(k);
          const isCur = last && !last.x && last.p === k;
          const hit = last?.x === k;
          const prime = done && !x;
          return (
            <span key={k} className={`grid h-10 place-items-center rounded-lg font-mono text-sm font-bold transition-all duration-300 sm:h-11 ${
              hit ? "scale-110 bg-rose-500 text-white" : isCur ? "scale-110 bg-amber-400 text-slate-900 shadow" : prime ? "bg-emerald-600 text-white" : x ? "bg-slate-200 text-slate-400 line-through" : cur === k ? "bg-amber-200 text-slate-900" : "bg-white text-slate-800 ring-1 ring-slate-300"}`}>{k}</span>
          );
        })}
      </div>
      <div className="mt-4 flex flex-wrap items-center justify-between gap-3">
        <p className="min-h-[1.75rem] text-base font-bold text-brand-ink" aria-live="polite">{msg}</p>
        <div className="flex gap-2">
          <button onClick={() => setPlay(!play)} className="rounded-lg bg-blue-600 px-4 py-1.5 text-sm font-bold text-white hover:bg-blue-700">{play ? "থামাও" : "চালাও"}</button>
          <button onClick={() => { setS(0); }} className="rounded-lg border border-slate-300 px-4 py-1.5 text-sm font-bold text-slate-700 hover:bg-slate-100">আবার</button>
          <button onClick={() => { setPlay(false); setS((x) => Math.min(ev.length, x + 1)); }} className="rounded-lg border border-slate-300 px-4 py-1.5 text-sm font-bold text-slate-700 hover:bg-slate-100">পরের ধাপ</button>
        </div>
      </div>
    </div>
  );
}
