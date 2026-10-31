import { useMemo, useState } from "react";
import CodeBlock from "./CodeBlock";
import { SearchIcon } from "./Icons";

const C = {
  emerald: { badge: "bg-emerald-100 text-emerald-800", bar: "from-emerald-400 to-emerald-600", chip: "bg-emerald-50 text-emerald-700 ring-emerald-200" },
  amber: { badge: "bg-amber-100 text-amber-800", bar: "from-amber-400 to-amber-600", chip: "bg-amber-50 text-amber-700 ring-amber-200" },
  blue: { badge: "bg-blue-100 text-blue-800", bar: "from-blue-400 to-blue-600", chip: "bg-blue-50 text-blue-700 ring-blue-200" },
  purple: { badge: "bg-purple-100 text-purple-800", bar: "from-purple-400 to-purple-600", chip: "bg-purple-50 text-purple-700 ring-purple-200" },
};
const col = (c) => C[c] || { badge: "bg-slate-100 text-slate-800", bar: "from-slate-400 to-slate-600", chip: "bg-slate-50 text-slate-700 ring-slate-200" };

function FuncCard({ fn, topic, i, hit }) {
  const c = col(topic.color);
  return (
    <article style={{ animationDelay: `${Math.min(i, 12) * 50}ms` }}
      className={`card-lift animate-fade-up overflow-hidden rounded-2xl border bg-white shadow-sm ${hit ? "bg-yellow-100 ring-2 ring-yellow-300 border-yellow-300" : "border-slate-200"}`}>
      <div className={`h-1.5 bg-gradient-to-r ${c.bar}`} />
      <div className="p-4">
        <div className="flex items-start justify-between gap-2">
          <h3 className="break-words font-mono text-base font-bold text-brand-ink">{fn.name}</h3>
          <span className={`shrink-0 rounded-full px-2 py-0.5 text-xs font-semibold ${c.badge}`}>{topic.title}</span>
        </div>
        <p className="mt-2 text-sm text-slate-700">{fn.desc}</p>
        <div className="my-3 border-t border-dashed border-slate-300" />
        <pre className={`overflow-x-auto whitespace-pre-wrap break-words rounded-lg px-3 py-2 font-mono text-xs ring-1 ${c.chip}`}>{fn.ex}</pre>
      </div>
    </article>
  );
}

export default function TopicPage({ tab }) {
  const [active, setActive] = useState(0);
  const [q, setQ] = useState("");
  const topic = tab.data[active] || tab.data[0];
  const term = q.trim().toLowerCase();

  const results = useMemo(() => {
    if (!term) return [];
    return tab.data.flatMap((t) => t.funcs.filter((f) => (f.name + f.desc + f.ex).toLowerCase().includes(term)).map((fn) => ({ fn, topic: t })));
  }, [term, tab]);

  return (
    <>
      <section className="relative bg-brand-ink text-white">
        <div className="mx-auto max-w-6xl px-4 pb-8 pt-8 sm:px-8">
          <h1 className="animate-fade-in text-2xl font-bold sm:text-4xl">{tab.label}</h1>
          <p className="mt-1 text-white/80">{tab.blurb}</p>
          <div className="mt-4 flex flex-wrap gap-2">
            {tab.data.map((t, i) => (
              <button key={t.id} onClick={() => { setActive(i); setQ(""); }}
                className={`rounded-full px-3 py-1 text-sm ${i === active && !term ? "bg-white font-bold text-brand-ink" : "border border-white/30 text-white hover:bg-white/10"}`}>
                {t.title}
              </button>
            ))}
          </div>
        </div>
        <div className="road-dash" />
      </section>

      <div className="no-print sticky top-[67px] z-20 border-b border-slate-200 bg-white/90 px-4 py-2.5 backdrop-blur">
        <div className="relative mx-auto max-w-2xl">
          <SearchIcon className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" />
          <input value={q} onChange={(e) => setQ(e.target.value)} placeholder="function খোঁজো, যেমন push_back, find, sort…"
            aria-label="function খোঁজো"
            className="w-full rounded-xl border border-slate-300 bg-white py-2.5 pl-10 pr-3 text-sm outline-none focus:border-indigo-400 focus:ring-2 focus:ring-indigo-200" />
        </div>
      </div>

      <div className="mx-auto max-w-6xl px-4 py-8 sm:px-8">
        {term ? (
          <>
            <h2 className="text-lg font-bold">{results.length} টা ফলাফল</h2>
            {results.length === 0 && <p className="mt-2 text-slate-600">কিছু পাওয়া যায়নি। অন্য শব্দ দিয়ে চেষ্টা করো।</p>}
            <div className="mt-4 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {results.map((r, i) => <FuncCard key={r.topic.id + r.fn.name} fn={r.fn} topic={r.topic} i={i} hit />)}
            </div>
          </>
        ) : (
          <div key={topic.id} className="animate-fade-in">
            <h2 className="text-xl font-bold sm:text-2xl">{topic.title}</h2>
            <p className="mt-1 max-w-3xl text-slate-600">{topic.intro}</p>
            <div className="mt-6 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {topic.funcs.map((fn, i) => <FuncCard key={fn.name} fn={fn} topic={topic} i={i} />)}
            </div>
            <h3 className="mb-3 mt-10 text-lg font-bold">পুরো কোড</h3>
            <CodeBlock code={topic.code} title={`${topic.id}.cpp`} />
          </div>
        )}
      </div>
    </>
  );
}
