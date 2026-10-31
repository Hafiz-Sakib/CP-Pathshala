import Rich from "./Rich";

export default function TraceTable({ t }) {
  return (
    <figure className="mt-5">
      {t.caption && <figcaption className="mb-2 text-base font-bold text-slate-700"><Rich text={t.caption} /></figcaption>}
      <div className="overflow-x-auto rounded-2xl border border-slate-200 bg-white shadow-sm">
        <table className="w-full min-w-max border-collapse text-left text-sm">
          <thead>
            <tr className="bg-brand-ink text-white">
              {t.cols.map((c, i) => <th key={i} className="whitespace-nowrap px-3.5 py-2.5 text-sm font-bold first:rounded-tl-2xl last:rounded-tr-2xl">{c}</th>)}
            </tr>
          </thead>
          <tbody>
            {t.rows.map((r, ri) => (
              <tr key={ri} className={`border-t border-slate-100 ${t.hl?.includes(ri) ? "bg-amber-50 font-bold" : ri % 2 ? "bg-slate-50/70" : ""}`}>
                {r.map((c, ci) => <td key={ci} className={`px-3.5 py-2 ${ci === 0 ? "font-mono font-bold text-brand-ink" : ""}`}><Rich text={c} /></td>)}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </figure>
  );
}
