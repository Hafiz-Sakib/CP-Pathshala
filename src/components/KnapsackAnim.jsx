import { useEffect, useMemo, useState } from "react";
import { useInView, reduced } from "./Reveal";

// ───── নমুনা: সাজেক ট্রিপের ব্যাগ (ধারণক্ষমতা ৮ কেজি) ─────
const W = 8;
const ITEMS = [
  { e: "💧", n: "পানির বোতল", w: 2, v: 3 },
  { e: "📷", n: "ক্যামেরা", w: 3, v: 4 },
  { e: "🍱", n: "শুকনো খাবার", w: 4, v: 5 },
  { e: "🧥", n: "জ্যাকেট", w: 5, v: 8 },
];
const N = ITEMS.length;

// dp[i][j] = প্রথম i টা জিনিস থেকে j কেজির ব্যাগে সর্বোচ্চ কত মূল্য
const DP = Array.from({ length: N + 1 }, () => Array(W + 1).fill(0));
for (let i = 1; i <= N; i++) {
  for (let j = 0; j <= W; j++) {
    const { w, v } = ITEMS[i - 1];
    DP[i][j] = DP[i - 1][j];
    if (j >= w) DP[i][j] = Math.max(DP[i][j], DP[i - 1][j - w] + v);
  }
}

// প্রতিটা ধাপের ছবি আগে থেকেই বানিয়ে রাখি
function buildSteps() {
  const out = [{ kind: "init", upto: 0, msg: "শুরু: ০ টা জিনিস থাকলে যেকোনো ওজনে মূল্য ০ — তাই প্রথম সারি সব ০" }];
  for (let i = 1; i <= N; i++) {
    const { e, n, w, v } = ITEMS[i - 1];
    for (let j = 0; j <= W; j++) {
      const skip = DP[i - 1][j];
      let msg, a = [i - 1, j], b = null, took = false;
      if (j < w) {
        msg = `${e} ${n} (${w} কেজি) — ${j} কেজির ব্যাগে ধরে না, তাই উপরের ঘর থেকেই ${skip}`;
      } else {
        const take = DP[i - 1][j - w] + v;
        b = [i - 1, j - w];
        took = take > skip;
        msg = `${e} ${n}: না নিলে ${skip}, নিলে ${DP[i - 1][j - w]} + ${v} = ${take} → ${took ? `নিলেই ভালো, ${take}` : `না নেওয়াই ভালো, ${skip}`}`;
      }
      out.push({ kind: "fill", i, j, a, b, took, upto: (i - 1) * (W + 1) + j + 1, msg });
    }
  }
  // traceback: কোন কোন জিনিস নিলাম
  const path = [[N, W]], chosen = [];
  let j = W;
  out.push({ kind: "trace", upto: N * (W + 1), path: [...path], chosen: [], msg: `সব ঘর ভরা শেষ! সর্বোচ্চ মূল্য dp[${N}][${W}] = ${DP[N][W]}। এবার উল্টো দিকে হেঁটে দেখি কোন কোন জিনিস নিয়েছি` });
  for (let i = N; i >= 1; i--) {
    const { e, n, w } = ITEMS[i - 1];
    if (DP[i][j] !== DP[i - 1][j]) {
      chosen.push(i - 1);
      j -= w;
      path.push([i - 1, j]);
      out.push({ kind: "trace", upto: N * (W + 1), path: [...path], chosen: [...chosen], msg: `dp[${i}][${j + w}] ≠ উপরের ঘর → ${e} ${n} নিয়েছি! এখন ${w} কেজি কমিয়ে dp[${i - 1}][${j}] তে যাই` });
    } else {
      path.push([i - 1, j]);
      out.push({ kind: "trace", upto: N * (W + 1), path: [...path], chosen: [...chosen], msg: `dp[${i}][${j}] = উপরের ঘর → ${e} ${n} নিইনি, সোজা উপরে যাই` });
    }
  }
  const wt = chosen.reduce((s, k) => s + ITEMS[k].w, 0);
  out.push({ kind: "end", upto: N * (W + 1), path: [...path], chosen: [...chosen], msg: `শেষ! ব্যাগে ${[...chosen].reverse().map((k) => ITEMS[k].n).join(" + ")} — ওজন ${wt}/${W} কেজি, মোট মূল্য ${DP[N][W]} 🎒` });
  return out;
}

const STEPS = buildSteps();
const rowStarts = [0, ...Array.from({ length: N }, (_, r) => STEPS.findIndex((s) => s.kind === "fill" && s.i === r + 1))];
const traceStart = STEPS.findIndex((s) => s.kind === "trace");

export default function KnapsackAnim({ onOpen }) {
  const [ref, inView] = useInView(false);
  const [s, setS] = useState(0);
  const [play, setPlay] = useState(true);
  const total = STEPS.length;
  const st = STEPS[Math.min(s, total - 1)];
  const end = st.kind === "end";

  useEffect(() => {
    if (!inView || !play || reduced()) return;
    const delay = end ? 3200 : st.kind === "trace" ? 1500 : st.kind === "init" ? 1400 : 650;
    const id = setTimeout(() => setS((x) => (x >= total - 1 ? 0 : x + 1)), delay);
    return () => clearTimeout(id);
  }, [inView, play, s, end, st.kind, total]);

  const nextRow = () => {
    setPlay(false);
    setS((x) => {
      if (x >= traceStart) return total - 1;
      const nxt = rowStarts.find((r, idx) => idx > 0 && r > x);
      return nxt ?? traceStart;
    });
  };

  const view = useMemo(() => {
    const onPath = new Set((st.path || []).map(([i, j]) => `${i}-${j}`));
    const chosen = new Set(st.chosen || []);
    const cur = st.kind === "fill" ? `${st.i}-${st.j}` : null;
    const srcA = st.kind === "fill" ? `${st.a[0]}-${st.a[1]}` : null;
    const srcB = st.kind === "fill" && st.b ? `${st.b[0]}-${st.b[1]}` : null;
    return { onPath, chosen, cur, srcA, srcB };
  }, [st]);

  const filled = (i, j) => i === 0 || (i - 1) * (W + 1) + j < st.upto;
  const tracing = st.kind === "trace" || st.kind === "end";
  const curItem = st.kind === "fill" ? st.i - 1 : -1;
  const usedW = [...view.chosen].reduce((a, k) => a + ITEMS[k].w, 0);
  const usedV = [...view.chosen].reduce((a, k) => a + ITEMS[k].v, 0);

  const cellCls = (i, j) => {
    const key = `${i}-${j}`;
    if (!filled(i, j) && key !== view.cur) return "bg-white text-slate-300 ring-1 ring-slate-200";
    if (view.onPath.has(key)) return "bg-rose-500 text-white shadow ring-2 ring-rose-300";
    if (key === view.cur) return "bg-amber-400 text-slate-900 shadow ring-2 ring-amber-500 scale-110";
    if (key === view.srcB) return "bg-sky-500 text-white ring-1 ring-sky-600";
    if (key === view.srcA) return "bg-sky-200 text-sky-900 ring-1 ring-sky-400";
    if (i === 0) return "bg-slate-100 text-slate-400";
    return DP[i][j] !== DP[i - 1][j] ? "bg-emerald-100 text-emerald-900 ring-1 ring-emerald-300" : "bg-slate-100 text-slate-600 ring-1 ring-slate-200";
  };

  return (
    <div ref={ref} className="rounded-3xl border border-purple-200 bg-white p-4 shadow-md sm:p-6">
      {/* জিনিসের তালিকা */}
      <div className="grid grid-cols-2 gap-2 sm:grid-cols-4">
        {ITEMS.map((it, k) => {
          const picked = view.chosen.has(k);
          const active = k === curItem;
          return (
            <div key={it.n} className={`rounded-xl border px-3 py-2 text-center transition ${picked ? "border-emerald-400 bg-emerald-50 ring-2 ring-emerald-300" : active ? "border-amber-400 bg-amber-50 ring-2 ring-amber-300" : "border-slate-200 bg-slate-50"}`}>
              <p className="text-2xl leading-none">{it.e}</p>
              <p className="mt-1 text-sm font-bold text-slate-800">{it.n}</p>
              <p className="font-mono text-xs font-semibold text-slate-600">ওজন {it.w} · মূল্য {it.v}</p>
            </div>
          );
        })}
      </div>

      {/* DP table */}
      <p className="mb-1 mt-4 text-sm font-bold text-slate-600">dp[i][j] <span className="font-semibold text-slate-500">— প্রথম i টা জিনিস থেকে j কেজির ব্যাগে সর্বোচ্চ মূল্য</span></p>
      <div className="overflow-x-auto pb-2 no-scrollbar">
        <table className="mx-auto border-separate border-spacing-1">
          <thead>
            <tr>
              <th className="pr-1 text-right font-mono text-xs font-bold text-slate-500">j →</th>
              {Array.from({ length: W + 1 }, (_, j) => <th key={j} className="h-6 min-w-[2.1rem] text-center font-mono text-sm font-bold text-slate-500 sm:min-w-[2.4rem]">{j}</th>)}
            </tr>
          </thead>
          <tbody>
            {DP.map((row, i) => (
              <tr key={i}>
                <th className="whitespace-nowrap pr-1 text-right font-mono text-sm font-bold text-slate-500">{i === 0 ? "i=0" : `${ITEMS[i - 1].e} i=${i}`}</th>
                {row.map((val, j) => {
                  const show = filled(i, j) || `${i}-${j}` === view.cur;
                  return <td key={j} className={`h-9 min-w-[2.1rem] rounded-lg text-center font-mono text-base font-bold transition-all duration-300 sm:h-10 sm:min-w-[2.4rem] ${cellCls(i, j)}`}>{show ? val : "·"}</td>;
                })}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="flex flex-wrap justify-center gap-x-4 gap-y-1 text-xs text-slate-600 sm:text-sm">
        <span className="flex items-center gap-1.5"><i className="h-3 w-3 rounded bg-amber-400" />এখনকার ঘর</span>
        <span className="flex items-center gap-1.5"><i className="h-3 w-3 rounded bg-sky-200 ring-1 ring-sky-400" />না নিলে (উপরের ঘর)</span>
        <span className="flex items-center gap-1.5"><i className="h-3 w-3 rounded bg-sky-500" />নিলে (বাঁয়ে-উপরের ঘর)</span>
        <span className="flex items-center gap-1.5"><i className="h-3 w-3 rounded bg-emerald-100 ring-1 ring-emerald-300" />নিলে লাভ হয়েছে</span>
        <span className="flex items-center gap-1.5"><i className="h-3 w-3 rounded bg-rose-500" />ফেরার পথ</span>
      </div>

      {/* ব্যাগের মিটার */}
      <div className="mt-3 rounded-xl bg-slate-50 p-3 ring-1 ring-slate-200">
        <div className="flex items-center justify-between text-sm font-bold text-slate-600">
          <span>🎒 ব্যাগ <span className="font-semibold text-slate-500">— ধারণক্ষমতা {W} কেজি</span></span>
          <span className="font-mono">{tracing ? `${usedW}/${W} কেজি · মূল্য ${usedV}` : "ফাঁকা"}</span>
        </div>
        <div className="mt-2 flex h-6 overflow-hidden rounded-lg bg-slate-200">
          {[...view.chosen].reverse().map((k) => (
            <div key={k} style={{ width: `${(ITEMS[k].w / W) * 100}%` }} className="grid place-items-center border-r border-white bg-emerald-500 text-sm transition-all duration-500">{ITEMS[k].e}</div>
          ))}
        </div>
      </div>

      <div className="mt-4 flex flex-wrap items-center justify-between gap-3">
        <p className="min-h-[3.25rem] flex-1 text-base font-bold text-brand-ink sm:min-h-[1.75rem]" aria-live="polite">{st.msg}</p>
        <div className="flex flex-wrap gap-2">
          <button onClick={() => setPlay(!play)} className="rounded-lg bg-purple-600 px-4 py-1.5 text-sm font-bold text-white hover:bg-purple-700">{play ? "থামাও" : "চালাও"}</button>
          <button onClick={() => { setS(0); setPlay(true); }} className="rounded-lg border border-slate-300 px-4 py-1.5 text-sm font-bold text-slate-700 hover:bg-slate-100">আবার</button>
          <button onClick={() => { setPlay(false); setS((x) => Math.min(total - 1, x + 1)); }} className="rounded-lg border border-slate-300 px-4 py-1.5 text-sm font-bold text-slate-700 hover:bg-slate-100">পরের ধাপ</button>
          <button onClick={nextRow} className="rounded-lg border border-slate-300 px-4 py-1.5 text-sm font-bold text-slate-700 hover:bg-slate-100">পরের সারি ⏭</button>
        </div>
      </div>

      <div className="mt-3 flex flex-wrap gap-x-5 gap-y-1 border-t border-slate-100 pt-3">
        <button onClick={() => onOpen("rec-knapsack-01")} className="text-base font-bold text-purple-700 hover:underline">0/1 Knapsack এর ব্লগ ও কোড →</button>
        <button onClick={() => onOpen("rec-knapsack-fractional")} className="text-base font-bold text-amber-700 hover:underline">Fractional Knapsack এর ব্লগ →</button>
      </div>
    </div>
  );
}
