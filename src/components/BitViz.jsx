import Rich from "./Rich";
import { GraphFig, MatFig } from "./GraphViz";

const ON = { a: "bg-sky-600 text-white", b: "bg-violet-600 text-white", r: "bg-emerald-600 text-white", n: "bg-slate-700 text-white" };
const isOn = (ch) => ch !== "0" && ch !== "·";

function Cell({ ch, tone, hl, onClick, label }) {
  const cls = `grid h-8 w-6 shrink-0 place-items-center rounded-md font-mono text-sm font-bold transition min-[420px]:h-9 min-[420px]:w-7 min-[420px]:text-base sm:h-10 sm:w-9 ${
    isOn(ch) ? ON[tone] || ON.n : "bg-slate-100 text-slate-400"} ${hl ? "scale-110 ring-2 ring-amber-400 ring-offset-1" : ""}`;
  return onClick
    ? <button type="button" onClick={onClick} aria-label={label} className={`${cls} cursor-pointer hover:brightness-110 active:scale-95`}>{ch}</button>
    : <span className={cls}>{ch}</span>;
}

export function BitRow({ r, onToggle }) {
  return (
    <div className={`flex items-center gap-2 sm:gap-3 ${r.sep ? "mt-2 border-t-[3px] border-slate-400 pt-2" : "mt-1.5"}`}>
      <span className="w-16 shrink-0 text-right text-xs font-semibold text-slate-700 min-[420px]:w-24 min-[420px]:text-sm sm:w-32 sm:text-base">{r.label}</span>
      <div className="flex gap-0.5 min-[420px]:gap-1">
        {r.bits.split("").map((ch, i) => (
          <Cell key={i} ch={ch} tone={r.tone} hl={r.hl?.includes(i)} onClick={onToggle ? () => onToggle(i) : undefined} label={`বিট ${i} টগল করো`} />
        ))}
      </div>
      {r.dec !== null && r.dec !== undefined && <span className="shrink-0 font-mono text-sm font-bold text-slate-700 sm:text-base">= {r.dec}</span>}
    </div>
  );
}

export function Weights({ len, offset = true }) {
  return (
    <div className="flex items-end gap-2 sm:gap-3">
      <span className="w-16 shrink-0 text-right text-[10px] font-semibold text-slate-500 min-[420px]:w-24 min-[420px]:text-xs sm:w-32">জায়গার মান →</span>
      <div className="flex gap-0.5 min-[420px]:gap-1">
        {Array.from({ length: len }, (_, i) => (
          <span key={i} className="w-6 shrink-0 text-center font-mono text-[9px] font-semibold text-slate-500 min-[420px]:w-7 min-[420px]:text-[11px] sm:w-9">{2 ** (len - 1 - i)}</span>
        ))}
      </div>
    </div>
  );
}

const GS = {
  p: "bg-emerald-600 text-white shadow-sm",
  x: "bg-slate-200 text-slate-400 line-through decoration-2",
  n: "bg-white text-slate-800 ring-1 ring-slate-300",
  h: "bg-amber-400 text-slate-900",
};

function Grid({ g }) {
  const has = (s) => g.cells.some((c) => c.s === s);
  return (
    <>
      <div className="flex flex-wrap gap-1.5">
        {g.cells.map((c, i) => (
          <span key={i} className={`grid h-10 min-w-[2.5rem] place-items-center rounded-lg px-1 font-mono text-base font-bold ${GS[c.s] || GS.n}`}>{c.t}</span>
        ))}
      </div>
      <div className="mt-3 flex flex-wrap gap-x-4 gap-y-1 text-sm text-slate-600">
        {has("p") && <span className="flex items-center gap-1.5"><i className="h-3 w-3 rounded bg-emerald-600" />ঠিক / prime</span>}
        {has("n") && <span className="flex items-center gap-1.5"><i className="h-3 w-3 rounded bg-white ring-1 ring-slate-400" />এখনো বাকি</span>}
        {has("x") && <span className="flex items-center gap-1.5"><i className="h-3 w-3 rounded bg-slate-300" />কাটা / বাদ</span>}
      </div>
    </>
  );
}

export function BitGroup({ g }) {
  const numeric = g.kind === "bits" && g.rows.every((r) => /^[01]+$/.test(r.bits));
  return (
    <figure className="mt-4 rounded-2xl border border-slate-200 bg-white p-4 shadow-sm">
      {g.caption && <figcaption className="mb-3 text-base font-bold text-brand-ink"><Rich text={g.caption} /></figcaption>}
      {g.kind === "graph" ? <GraphFig g={g} /> : g.kind === "mat" ? <MatFig g={g} /> : g.kind === "grid" ? <Grid g={g} /> : (
        <div className="overflow-x-auto pb-2 no-scrollbar">
          <div className="w-max">
            {numeric && <Weights len={g.rows[0].bits.length} />}
            {g.rows.map((r, i) => <BitRow key={i} r={r} />)}
          </div>
        </div>
      )}
    </figure>
  );
}
