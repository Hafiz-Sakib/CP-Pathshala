import { useEffect, useMemo, useState } from "react";
import { useInView, reduced } from "./Reveal";
import { GraphFig } from "./GraphViz";

// ───── নমুনা গ্রাফ (১ থেকে শুরু) ─────
const POS = { 1: [250, 32], 2: [80, 108], 3: [250, 108], 4: [415, 108], 5: [35, 184], 6: [125, 184], 7: [250, 184], 8: [355, 184], 9: [415, 184], 10: [475, 184], 11: [125, 250], 12: [415, 250] };
const EDGES = [[1, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [4, 9], [4, 10], [6, 11], [9, 12]];
const ADJ = {};
Object.keys(POS).forEach((k) => (ADJ[k] = []));
EDGES.forEach(([a, b]) => { ADJ[a].push(b); ADJ[b].push(a); });
Object.values(ADJ).forEach((l) => l.sort((x, y) => x - y));
const list = (a) => a.join(", ");

// প্রতিটা ধাপের ছবি আগে থেকেই বানিয়ে রাখি
function bfsSteps() {
  const out = [{ cur: null, done: [], wait: [1], tree: [], msg: "শুরু: root (১) কে queue তে রাখলাম" }];
  const seen = new Set([1]), q = [1], done = [], tree = [];
  while (q.length) {
    const u = q.shift();
    done.push(u);
    const fresh = ADJ[u].filter((v) => !seen.has(v));
    fresh.forEach((v) => { seen.add(v); q.push(v); tree.push([u, v]); });
    out.push({
      cur: u, done: [...done], wait: [...q], tree: [...tree],
      msg: `${u} কে queue এর সামনে থেকে নিলাম${fresh.length ? ` — নতুন প্রতিবেশী ${list(fresh)} queue এর পেছনে ঢুকলো` : " — নতুন কোনো প্রতিবেশী নেই"}`,
    });
  }
  out.push({ ...out[out.length - 1], cur: null, msg: `শেষ! BFS order: ${list(done)} — কাছের node আগে, দূরের node পরে 🌊` });
  return out;
}

function dfsSteps() {
  const out = [{ cur: null, done: [], wait: [], tree: [], msg: "শুরু: root (১) থেকে শুরু — যতটা পারি গভীরে যাবো" }];
  const seen = new Set(), path = [], done = [], tree = [];
  const snap = (cur, msg) => out.push({ cur, done: [...done], wait: [...path], tree: [...tree], msg });
  const go = (u, p) => {
    seen.add(u); path.push(u); done.push(u);
    if (p) tree.push([p, u]);
    const nxt = ADJ[u].filter((v) => !seen.has(v));
    snap(u, `${u} এ ঢুকলাম${nxt.length ? ` — না-দেখা প্রতিবেশী ${list(nxt)}, আগে ${nxt[0]} তে গভীরে যাই` : " — আর কোথাও যাওয়ার নেই, ফিরে যাবো"}`);
    ADJ[u].forEach((v) => {
      if (!seen.has(v)) go(v, u);
    });
    path.pop();
    if (path.length) snap(path[path.length - 1], `${u} এর কাজ শেষ — ফিরে এলাম ${path[path.length - 1]} এ (backtrack)`);
  };
  go(1, 0);
  out.push({ ...out[out.length - 1], cur: null, msg: `শেষ! DFS order: ${list(done)} — একদম গভীরে গিয়ে তারপর ফেরা 🧗` });
  return out;
}

const MODES = {
  bfs: { label: "BFS", sub: "Queue · ঢেউয়ের মতো", box: "Queue", hint: "সামনে থেকে বের, পেছনে ঢোকে (FIFO)", steps: bfsSteps(), page: "graph-bfs" },
  dfs: { label: "DFS", sub: "Stack · গভীরে গিয়ে ফেরা", box: "Stack (বর্তমান পথ)", hint: "যেভাবে ঢুকেছি, উল্টো পথে ফিরবো (LIFO)", steps: dfsSteps(), page: "graph-dfs" },
};

export default function BfsDfsAnim({ onOpen }) {
  const [ref, inView] = useInView(false);
  const [mode, setMode] = useState("bfs");
  const [s, setS] = useState(0);
  const [play, setPlay] = useState(true);
  const M = MODES[mode];
  const total = M.steps.length;
  const st = M.steps[Math.min(s, total - 1)];
  const done = s >= total - 1;

  useEffect(() => {
    if (!inView || !play || reduced()) return;
    const id = setTimeout(() => setS((x) => (x >= total - 1 ? 0 : x + 1)), done ? 2600 : 1300);
    return () => clearTimeout(id);
  }, [inView, play, s, done, total]);

  const pick = (m) => { setMode(m); setS(0); setPlay(true); };

  const fig = useMemo(() => {
    const order = Object.fromEntries(st.done.map((n, i) => [n, i + 1]));
    const waiting = new Set(st.wait);
    // level = root থেকে কত edge দূরে (tree edge ধরে)
    const depth = { 1: 0 };
    st.tree.forEach(([p, q]) => { depth[q] = (depth[p] ?? 0) + 1; });
    const nodes = Object.entries(POS).map(([id, [x, y]]) => {
      const n = +id;
      let c = "n";
      if (n === st.cur) c = "a";
      else if (waiting.has(n)) c = "q";
      else if (order[n]) c = "v";
      const seen = order[n] || waiting.has(n);
      const sub = !seen ? "" : mode === "bfs" ? `L${depth[n] ?? 0}` : `#${order[n]}`;
      return { id: n, x, y, s: c, sub };
    });
    const isTree = (a, b) => st.tree.some(([p, q]) => (p === a && q === b) || (p === b && q === a));
    const edges = EDGES.map(([a, b]) => ({ a, b, s: isTree(a, b) ? "t" : "n" }));
    return { w: 510, h: 280, r: 20, nodes, edges, caption: `${M.label} এর ধাপ` };
  }, [st, M.label, mode]);

  const tone = mode === "bfs" ? { on: "bg-rose-600 text-white", ring: "border-rose-200", btn: "bg-rose-600 hover:bg-rose-700", chip: "bg-sky-100 text-sky-900 ring-sky-300" } : { on: "bg-violet-600 text-white", ring: "border-violet-200", btn: "bg-violet-600 hover:bg-violet-700", chip: "bg-sky-100 text-sky-900 ring-sky-300" };

  return (
    <div ref={ref} className={`rounded-3xl border bg-white p-4 shadow-md sm:p-6 ${tone.ring}`}>
      <div className="mb-3 flex flex-wrap items-center gap-2" role="tablist" aria-label="BFS বা DFS বাছো">
        {Object.entries(MODES).map(([k, m]) => (
          <button key={k} role="tab" aria-selected={mode === k} onClick={() => pick(k)}
            className={`rounded-xl px-4 py-2 text-base font-bold transition ${mode === k ? (k === "bfs" ? "bg-rose-600 text-white shadow" : "bg-violet-600 text-white shadow") : "border border-slate-300 text-slate-700 hover:bg-slate-100"}`}>
            {m.label} <span className="hidden text-sm font-semibold opacity-90 sm:inline">· {m.sub}</span>
          </button>
        ))}
      </div>

      <GraphFig g={fig} />

      <div className="mt-3 grid gap-3 sm:grid-cols-2">
        <div className="rounded-xl bg-slate-50 p-3 ring-1 ring-slate-200">
          <p className="text-sm font-bold text-slate-600">{M.box} <span className="font-semibold text-slate-500">— {M.hint}</span></p>
          <div className="mt-2 flex min-h-[2.5rem] flex-wrap items-center gap-1.5">
            {st.wait.length === 0 && <span className="text-sm text-slate-400">ফাঁকা</span>}
            {st.wait.map((n, i) => (
              <span key={`${n}-${i}`} className={`grid h-9 min-w-[2.25rem] place-items-center rounded-lg px-2 font-mono text-base font-bold ring-1 ${tone.chip}`}>{n}</span>
            ))}
          </div>
        </div>
        <div className="rounded-xl bg-slate-50 p-3 ring-1 ring-slate-200">
          <p className="text-sm font-bold text-slate-600">Visit order <span className="font-semibold text-slate-500">— যে ক্রমে দেখা হলো</span></p>
          <div className="mt-2 flex min-h-[2.5rem] flex-wrap items-center gap-1.5">
            {st.done.length === 0 && <span className="text-sm text-slate-400">এখনো কেউ না</span>}
            {st.done.map((n) => (
              <span key={n} className="grid h-9 min-w-[2.25rem] place-items-center rounded-lg bg-emerald-600 px-2 font-mono text-base font-bold text-white">{n}</span>
            ))}
          </div>
        </div>
      </div>

      <div className="mt-4 flex flex-wrap items-center justify-between gap-3">
        <p className="min-h-[3.25rem] flex-1 text-base font-bold text-brand-ink sm:min-h-[1.75rem]" aria-live="polite">{st.msg}</p>
        <div className="flex gap-2">
          <button onClick={() => setPlay(!play)} className={`rounded-lg px-4 py-1.5 text-sm font-bold text-white ${tone.btn}`}>{play ? "থামাও" : "চালাও"}</button>
          <button onClick={() => setS(0)} className="rounded-lg border border-slate-300 px-4 py-1.5 text-sm font-bold text-slate-700 hover:bg-slate-100">আবার</button>
          <button onClick={() => { setPlay(false); setS((x) => Math.min(total - 1, x + 1)); }} className="rounded-lg border border-slate-300 px-4 py-1.5 text-sm font-bold text-slate-700 hover:bg-slate-100">পরের ধাপ</button>
        </div>
      </div>

      <div className="mt-3 flex flex-wrap gap-x-5 gap-y-1 border-t border-slate-100 pt-3">
        <button onClick={() => onOpen("graph-bfs")} className="text-base font-bold text-rose-700 hover:underline">BFS এর পুরো পেজ →</button>
        <button onClick={() => onOpen("graph-dfs")} className="text-base font-bold text-violet-700 hover:underline">DFS এর পুরো পেজ →</button>
      </div>
    </div>
  );
}
