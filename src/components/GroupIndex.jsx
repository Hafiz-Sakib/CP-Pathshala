import { useMemo, useState } from "react";
import { categories, groupPages, exampleCount, bn } from "../data";
import { col } from "./Colors";
import { SearchIcon, ClockIcon, BookIcon, ArrowIcon } from "./Icons";

export default function GroupIndex({ tab, onOpen }) {
  const [q, setQ] = useState("");
  const term = q.trim().toLowerCase();
  const cats = useMemo(() => categories(tab.id).map((c) => ({
    ...c, pages: c.pages.filter((p) => !term || (p.title + p.desc + p.syntax + p.cat).toLowerCase().includes(term)),
  })).filter((c) => c.pages.length), [tab, term]);
  const total = cats.reduce((n, c) => n + c.pages.length, 0);

  return (
    <>
      <section className="on-dark dots-bg relative bg-brand-ink text-white">
        <div className="mx-auto max-w-6xl px-4 pb-10 pt-10 sm:px-8">
          <h1 className="animate-fade-in text-3xl sm:text-4xl">{tab.label}</h1>
          <p className="mt-2 max-w-3xl text-base text-white/90">{tab.about}</p>
          <p className="mt-2 text-base font-semibold text-amber-300">{bn(groupPages(tab.id).length)} টা পেজ · {bn(exampleCount(tab.id))} টা উদাহরণ</p>
          <div className="mt-4 flex flex-wrap gap-2">
            {categories(tab.id).map((c, i) => (
              <a key={c.cat} href={`#cat-${i}`} className={`rounded-full px-3.5 py-1 text-base ${i === 0 ? "bg-white font-bold text-brand-ink" : "border border-white/40 hover:bg-white/10"}`}>{c.cat}</a>
            ))}
          </div>
        </div>
        <div className="road-dash" />
      </section>
      <div className="no-print sticky top-16 z-20 border-b border-slate-200 bg-white/95 px-4 py-3 backdrop-blur">
        <div className="relative mx-auto max-w-2xl">
          <SearchIcon className="absolute left-3 top-1/2 -translate-y-1/2 text-slate-400" width={20} height={20} />
          <input value={q} onChange={(e) => setQ(e.target.value)} aria-label="পেজ খোঁজো" placeholder="খোঁজো: push_back, sort, sieve, gcd …"
            className="w-full rounded-xl border border-slate-300 bg-white py-2.5 pl-11 pr-3 text-base outline-none focus:border-brand-green focus:ring-2 focus:ring-emerald-200" />
        </div>
      </div>
      <div className="mx-auto max-w-6xl px-4 py-8 sm:px-8">
        {total === 0 && <p className="text-base text-slate-600">কিছু পাওয়া যায়নি। অন্য শব্দ দিয়ে চেষ্টা করো।</p>}
        {cats.map((c, ci) => {
          const k = col(c.color);
          return (
            <section key={c.cat} id={`cat-${ci}`} className="mb-12 scroll-mt-36">
              <h2 className="mb-4 flex items-center gap-3 text-lg sm:text-xl"><span className={`h-4 w-4 rounded-full ${k.dot}`} />{c.cat}<span className="text-lg font-normal text-slate-500">({bn(c.pages.length)})</span></h2>
              <div className="grid items-stretch gap-5 sm:grid-cols-2 lg:grid-cols-3">
                {c.pages.map((p, i) => (
                  <article key={p.id} style={{ animationDelay: `${Math.min(i, 12) * 50}ms` }}
                    className={`card-lift animate-fade-up relative flex h-full flex-col overflow-hidden rounded-2xl border bg-white shadow-sm ${term ? "ring-2 ring-yellow-300 border-yellow-300" : "border-slate-200"}`}>
                    <div className={`h-2 bg-gradient-to-r ${k.bar}`} />
                    <div className="flex flex-1 flex-col p-5">
                      <h3 className="font-mono text-lg"><button onClick={() => onOpen(p.id)} className="stretch-link text-left">{p.title}</button></h3>
                      <p className="mt-2 line-clamp-3 min-h-[5.2rem] text-base text-slate-600">{p.desc}</p>
                      <div className="mt-auto flex flex-wrap items-center gap-2 pt-4">
                        <span className={`rounded-full px-2.5 py-0.5 text-sm font-bold ${k.badge}`}>{bn(p.examples.length)} টা উদাহরণ</span>
                        <span className="flex items-center gap-1 rounded-full bg-slate-100 px-2.5 py-0.5 text-sm font-semibold text-slate-700"><ClockIcon width={14} height={14} />{p.time}</span>
                        {p.intro && <span className="rounded-full bg-amber-100 px-2.5 py-0.5 text-sm font-bold text-amber-800">ধাপে ধাপে ✓</span>}
                      </div>
                    </div>
                  </article>
                ))}
              </div>
            </section>
          );
        })}
        {tab.reading && !term && (
          <section className="mb-4 rounded-3xl border border-rose-200 bg-rose-50/70 p-5 sm:p-7">
            <h2 className="flex items-center gap-3 text-lg sm:text-xl"><BookIcon width={24} height={24} className="text-rose-600" />{tab.readingTitle}</h2>
            <p className="mt-2 text-base text-slate-700">{tab.readingNote}</p>
            <ol className="mt-4 grid gap-2 sm:grid-cols-2">
              {tab.reading.map((t, i) => (
                <li key={t} className="flex items-start gap-3 rounded-xl bg-white px-3.5 py-2.5 text-base shadow-sm ring-1 ring-rose-100">
                  <span className="mt-0.5 grid h-7 w-7 shrink-0 place-items-center rounded-full bg-rose-500 text-sm font-bold text-white">{bn(i + 1)}</span>
                  <span>{t}</span>
                </li>
              ))}
            </ol>
            {tab.repo && <a href={tab.repo} target="_blank" rel="noreferrer" className="mt-4 inline-flex items-center gap-2 text-base font-bold text-rose-700 hover:underline">PDF গুলো GitHub এ দেখো <ArrowIcon /></a>}
          </section>
        )}
      </div>
    </>
  );
}
