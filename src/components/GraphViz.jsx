import Rich from "./Rich";

// ───── গ্রাফের ছবি (SVG): node, edge, রঙ দিয়ে অবস্থা ─────
const NODE = {
  n: { f: "#ffffff", s: "#475569", t: "#0f172a" },   // সাধারণ
  a: { f: "#fbbf24", s: "#b45309", t: "#0f172a" },   // এখন যেটা নিয়ে কাজ হচ্ছে
  v: { f: "#059669", s: "#064e3b", t: "#ffffff" },   // শেষ / visited
  q: { f: "#38bdf8", s: "#0369a1", t: "#0f172a" },   // queue / stack এ অপেক্ষায়
  x: { f: "#e2e8f0", s: "#94a3b8", t: "#64748b" },   // বাদ / পুরনো
  r: { f: "#fb7185", s: "#be123c", t: "#ffffff" },   // দ্বিতীয় রঙ (bipartite)
};
const EDGE = {
  n: { c: "#94a3b8", w: 2.5, d: "" },
  t: { c: "#059669", w: 5, d: "" },       // নেওয়া হয়েছে (tree / MST)
  x: { c: "#fb7185", w: 2.5, d: "7 6" },  // বাদ (cycle হতো)
  a: { c: "#f59e0b", w: 5, d: "" },       // এখনকার edge
};
const LEG = {
  n: ["#ffffff", "সাধারণ"], a: ["#fbbf24", "এখন যেটা দেখছি"], v: ["#059669", "শেষ / visited"],
  q: ["#38bdf8", "queue / stack এ অপেক্ষায়"], x: ["#e2e8f0", "বাদ / memo থেকে নেওয়া"], r: ["#fb7185", "২ নম্বর রঙ"],
};

export function GraphFig({ g }) {
  const W = g.w || 460, H = g.h || 210, R = g.r || 20;
  const byId = Object.fromEntries(g.nodes.map((n) => [n.id, n]));
  return (
    <>
      <svg viewBox={`0 0 ${W} ${H}`} role="img" aria-label={g.caption || "গ্রাফের ছবি"} className="mx-auto block w-full" style={{ maxWidth: Math.min(W * 1.5, 720) }}>
        <defs>
          <marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#64748b" /></marker>
        </defs>
        {g.edges.map((e, i) => {
          const a = byId[e.a], b = byId[e.b], st = EDGE[e.s || "n"];
          if (!a || !b) return null;
          const dx = b.x - a.x, dy = b.y - a.y, L = Math.hypot(dx, dy) || 1;
          const sx = a.x + (dx / L) * (e.d ? R + 1 : 0), sy = a.y + (dy / L) * (e.d ? R + 1 : 0);
          const ex = b.x - (dx / L) * (e.d ? R + 5 : 0), ey = b.y - (dy / L) * (e.d ? R + 5 : 0);
          const mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2;
          return (
            <g key={i}>
              <line x1={sx} y1={sy} x2={ex} y2={ey} stroke={st.c} strokeWidth={st.w} strokeDasharray={st.d} strokeLinecap="round" markerEnd={e.d ? "url(#arr)" : undefined} />
              {e.w !== undefined && e.w !== null && (
                <g><rect x={mx - 12} y={my - 10} width="24" height="20" rx="6" fill="#fff" stroke={st.c} strokeWidth="1.5" />
                  <text x={mx} y={my + 4.5} textAnchor="middle" fontSize="13" fontWeight="700" fill="#0a3631" fontFamily="Fira Code, monospace">{e.w}</text></g>
              )}
            </g>
          );
        })}
        {g.nodes.map((n) => {
          const st = NODE[n.s || "n"];
          return (
            <g key={n.id}>
              <circle cx={n.x} cy={n.y} r={R} fill={st.f} stroke={st.s} strokeWidth="3" />
              <text x={n.x} y={n.y + 5.5} textAnchor="middle" fontSize={String(n.t ?? n.id).length > 3 ? 12 : 16} fontWeight="700" fill={st.t} fontFamily="Fira Code, monospace">{n.t ?? n.id}</text>
              {n.sub !== undefined && n.sub !== null && n.sub !== "" && (
                <text x={n.x} y={n.y + R + 15} textAnchor="middle" fontSize="12.5" fontWeight="700" fill="#b91c1c" fontFamily="Fira Code, monospace">{n.sub}</text>
              )}
            </g>
          );
        })}
      </svg>
      <div className="mt-2 flex flex-wrap justify-center gap-x-4 gap-y-1 text-sm text-slate-600">
        {[...new Set(g.nodes.map((n) => n.s || "n"))].filter((s) => s !== "n").map((s) => (
          <span key={s} className="flex items-center gap-1.5"><i className="h-3 w-3 rounded-full ring-1 ring-slate-500" style={{ background: LEG[s]?.[0] }} />{LEG[s]?.[1]}</span>
        ))}
        {g.edges.some((e) => e.s === "t") && <span className="flex items-center gap-1.5"><i className="h-1.5 w-4 rounded bg-emerald-600" />নেওয়া edge</span>}
        {g.edges.some((e) => e.s === "x") && <span className="flex items-center gap-1.5"><i className="h-0 w-4 border-t-2 border-dashed border-rose-400" />বাদ edge</span>}
      </div>
      {g.note && <p className="mt-2 text-center text-base text-slate-600"><Rich text={g.note} /></p>}
    </>
  );
}

// ───── 2D ঘরের ছবি (adjacency matrix, grid, dp ইত্যাদি) ─────
const CELL = {
  n: "bg-white text-slate-800 ring-1 ring-slate-300",
  z: "bg-slate-100 text-slate-400",
  o: "bg-emerald-600 text-white shadow-sm",
  w: "bg-slate-800 text-slate-500",
  a: "bg-amber-400 text-slate-900",
  s: "bg-sky-500 text-white",
  v: "bg-emerald-100 text-emerald-900 ring-1 ring-emerald-300",
  p: "bg-rose-400 text-white",
};
const MLEG = { o: ["bg-emerald-600", "edge আছে / ঠিক"], z: ["bg-slate-200", "ফাঁকা (0)"], w: ["bg-slate-800", "দেয়াল (#)"], a: ["bg-amber-400", "খেয়াল করো"], s: ["bg-sky-500", "শুরুর ঘর"], v: ["bg-emerald-100 ring-1 ring-emerald-300", "ঘুরে আসা ঘর"], p: ["bg-rose-400", "রাস্তা"] };

export function MatFig({ g }) {
  const used = [...new Set(g.rows.flat().map((c) => c.s || "n"))].filter((s) => MLEG[s]);
  return (
    <>
      <div className="overflow-x-auto pb-2 no-scrollbar">
        <table className="mx-auto border-separate border-spacing-1">
          {g.cols && (
            <thead><tr>
              {g.rowLabels && <th />}
              {g.cols.map((c, i) => <th key={i} className="h-7 min-w-[2.4rem] text-center font-mono text-sm font-bold text-slate-500">{c}</th>)}
            </tr></thead>
          )}
          <tbody>
            {g.rows.map((r, ri) => (
              <tr key={ri}>
                {g.rowLabels && <th className="pr-1 text-right font-mono text-sm font-bold text-slate-500">{g.rowLabels[ri]}</th>}
                {r.map((c, ci) => (
                  <td key={ci} className={`h-10 min-w-[2.4rem] rounded-lg px-1 text-center font-mono text-base font-bold ${CELL[c.s || "n"] || CELL.n}`}>{c.t}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="mt-2 flex flex-wrap justify-center gap-x-4 gap-y-1 text-sm text-slate-600">
        {g.legend
          ? g.legend.map(([s, txt]) => <span key={s} className="flex items-center gap-1.5"><i className={`h-3 w-3 rounded ${CELL[s] || CELL.n}`} />{txt}</span>)
          : used.map((s) => <span key={s} className="flex items-center gap-1.5"><i className={`h-3 w-3 rounded ${MLEG[s][0]}`} />{MLEG[s][1]}</span>)}
      </div>
      {g.note && <p className="mt-2 text-center text-base text-slate-600"><Rich text={g.note} /></p>}
    </>
  );
}
