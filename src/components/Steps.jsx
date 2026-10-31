import Rich from "./Rich";

export default function Steps({ steps, dot = "bg-brand-green" }) {
  return (
    <ol className="space-y-3">
      {steps.map((s, i) => (
        <li key={i} className="relative flex gap-3">
          {i < steps.length - 1 && <span aria-hidden className="absolute left-[1.05rem] top-9 -bottom-3 w-0.5 bg-slate-300" />}
          <span className={`relative z-10 mt-1 grid h-9 w-9 shrink-0 place-items-center rounded-full text-base font-bold text-white shadow ${dot}`}>{i + 1}</span>
          <div className="min-w-0 flex-1 rounded-2xl border border-slate-200 bg-white px-4 py-3 text-base leading-relaxed text-slate-800 shadow-sm"><Rich text={s} /></div>
        </li>
      ))}
    </ol>
  );
}
