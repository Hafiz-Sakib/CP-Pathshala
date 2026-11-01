import { useState } from "react";
import { pages, categories, colorOf, tabs, bn } from "../data";
import { col } from "./Colors";
import CodeBlock from "./CodeBlock";
import Rich from "./Rich";
import Steps from "./Steps";
import TraceTable from "./TraceTable";
import { BitGroup } from "./BitViz";
import { BulbIcon, WarnIcon, ListIcon, EyeIcon, TargetIcon, ClockIcon, ArrowIcon, BookIcon } from "./Icons";

function Toc({ page, onOpen, onDone }) {
  return (
    <nav aria-label="সূচিপত্র" className="space-y-4">
      {categories(page.grp).map((c) => {
        const k = col(c.color);
        return (
          <div key={c.cat}>
            <p className="mb-1 flex items-center gap-2 text-sm font-bold text-slate-600"><span className={`h-2.5 w-2.5 rounded-full ${k.dot}`} />{c.cat}</p>
            {c.pages.map((p) => (
              <button key={p.id} onClick={() => { onOpen(p.id); onDone?.(); }} aria-current={p.id === page.id ? "page" : undefined}
                className={`block w-full rounded-lg px-3 py-1.5 text-left text-base ${p.id === page.id ? "bg-brand-green font-bold text-white" : "text-slate-700 hover:bg-brand-green/10"}`}>
                {p.title}
              </button>
            ))}
          </div>
        );
      })}
    </nav>
  );
}

function NavButtons({ i, onOpen }) {
  const prev = pages[i - 1], next = pages[i + 1];
  return (
    <div className="no-print mt-12 grid grid-cols-2 gap-3">
      {prev ? (
        <button onClick={() => onOpen(prev.id)} className="rounded-xl border border-slate-300 bg-white p-4 text-left hover:border-brand-green hover:bg-emerald-50">
          <span className="text-sm text-slate-500">← আগের পেজ</span>
          <span className="mt-0.5 block truncate font-mono text-base font-bold text-brand-ink">{prev.title}</span>
        </button>) : <span />}
      {next ? (
        <button onClick={() => onOpen(next.id)} className="rounded-xl bg-brand-green p-4 text-right text-white hover:bg-brand-ink">
          <span className="text-sm text-white/80">পরের পেজ →</span>
          <span className="mt-0.5 block truncate font-mono text-base font-bold">{next.title}</span>
        </button>) : <span />}
    </div>
  );
}

const SectionTitle = ({ Icon, children, tone = "text-brand-green" }) => (
  <h3 className="mb-3 mt-6 flex items-center gap-2 text-lg sm:text-xl"><Icon width={22} height={22} className={tone} />{children}</h3>
);

export default function LessonPage({ page, i, onOpen, onIndex }) {
  const [toc, setToc] = useState(false);
  const k = col(colorOf(page));
  const tabLabel = tabs.find((t) => t.id === page.grp)?.label;
  const uses = page.uses ? page.uses.split("•").map((s) => s.trim()).filter(Boolean) : [];
  return (
    <>
      <section className="on-dark dots-bg relative bg-brand-ink text-white">
        <div className="mx-auto max-w-6xl px-4 pb-10 pt-8 sm:px-8">
          <p className="text-base text-emerald-200">
            <button onClick={onIndex} className="font-semibold underline-offset-2 hover:underline">{tabLabel}</button> › {page.cat}
          </p>
          <h1 className="mt-2 break-words font-mono text-xl sm:text-4xl animate-fade-in">{page.title}</h1>
          <div className="mt-4 flex flex-wrap gap-2 text-base">
            <span className="rounded-full bg-white px-3.5 py-1 font-bold text-brand-ink">পেজ {bn(i + 1)} / {bn(pages.length)}</span>
            <span className="flex items-center gap-1.5 rounded-full border border-white/40 px-3.5 py-1"><ClockIcon width={16} height={16} />Time: {page.time}</span>
            <span className="rounded-full border border-white/40 px-3.5 py-1">{bn(page.examples.length)} টা উদাহরণ</span>
            {page.intro && <span className="rounded-full bg-amber-400 px-3.5 py-1 font-bold text-slate-900">ধাপে ধাপে ব্যাখ্যা ✓</span>}
          </div>
        </div>
        <div className="road-dash" />
      </section>

      <div className="mx-auto grid max-w-6xl gap-8 px-4 py-8 sm:px-8 lg:grid-cols-[17rem_1fr]">
        <aside className="no-print hidden lg:block">
          <div className="sticky top-24 max-h-[calc(100vh-7rem)] overflow-y-auto pr-2"><Toc page={page} onOpen={onOpen} /></div>
        </aside>

        <article key={page.id} className="min-w-0 animate-fade-in">
          <button onClick={() => setToc(!toc)} aria-expanded={toc} className="no-print mb-4 rounded-lg border border-brand-green/40 bg-white px-4 py-2 text-base font-bold text-brand-green lg:hidden">
            {toc ? "সূচিপত্র বন্ধ করো" : "সূচিপত্র দেখো"}
          </button>
          {toc && <div className="no-print mb-6 max-h-80 animate-slide-down overflow-y-auto rounded-2xl border border-slate-200 bg-white p-3 shadow lg:hidden"><Toc page={page} onOpen={onOpen} onDone={() => setToc(false)} /></div>}

          <div className="rounded-r-2xl border-l-[6px] border-brand-red bg-white p-5 shadow-sm">
            <p className="text-base font-medium text-slate-800"><Rich text={page.desc} /></p>
          </div>

          {page.intro && (
            <div className={`mt-6 rounded-2xl border p-5 ${k.soft} ${k.border}`}>
              <h2 className="flex items-center gap-2 text-xl"><BulbIcon width={24} height={24} className={k.text} />সহজ কথায় ধারণা</h2>
              <p className="mt-2 text-base leading-relaxed text-slate-800"><Rich text={page.intro} /></p>
              {uses.length > 0 && (
                <div className="mt-4">
                  <p className="mb-2 flex items-center gap-2 text-base font-bold text-slate-700"><TargetIcon width={18} height={18} />কোথায় কাজে লাগে?</p>
                  <div className="flex flex-wrap gap-2">{uses.map((u) => <span key={u} className="rounded-full bg-white px-3 py-1 text-base ring-1 ring-slate-300"><Rich text={u} /></span>)}</div>
                </div>
              )}
            </div>
          )}

          {page.blog?.length > 0 && (
            <section className={`mt-8 rounded-3xl border bg-white p-5 shadow-sm sm:p-7 ${k.border}`}>
              <h2 className="flex items-center gap-2 text-xl sm:text-2xl"><BookIcon width={26} height={26} className={k.text} />ব্লগ — গল্পে গল্পে বুঝি</h2>
              <div className="mt-5 space-y-7">
                {page.blog.map((s, si) => (
                  <div key={si}>
                    <h3 className="flex items-start gap-3 text-lg sm:text-xl">
                      <span className={`mt-0.5 grid h-8 w-8 shrink-0 place-items-center rounded-full text-base text-white ${k.dot}`}>{bn(si + 1)}</span>
                      <span>{s.h}</span>
                    </h3>
                    <div className="mt-3 space-y-3 pl-0 sm:pl-11">
                      {s.p.map((para, pi) => <p key={pi} className="text-base leading-relaxed text-slate-800"><Rich text={para} /></p>)}
                      {s.ul.length > 0 && (
                        <ul className="space-y-2">
                          {s.ul.map((li, li2) => (
                            <li key={li2} className="flex gap-2.5 text-base leading-relaxed text-slate-800">
                              <ArrowIcon width={18} height={18} className={`mt-2 shrink-0 ${k.text}`} /><span><Rich text={li} /></span>
                            </li>
                          ))}
                        </ul>
                      )}
                      {s.table && <TraceTable t={s.table} />}
                    </div>
                  </div>
                ))}
              </div>
            </section>
          )}

          {page.truth && <TraceTable t={page.truth} />}

          <h2 className="mb-3 mt-8 text-lg sm:text-xl">লেখার নিয়ম (Syntax)</h2>
          <pre className={`overflow-x-auto whitespace-pre-wrap break-words rounded-2xl px-5 py-4 font-mono text-base font-semibold ring-1 ${k.chip}`}>{page.syntax}</pre>

          {page.examples.map((e, n) => {
            const sentences = e.steps ? null : e.explain.split("।").map((s) => s.trim()).filter(Boolean).map((s) => s + "।");
            return (
              <section key={n} className="mt-12">
                <h2 className="mb-4 flex items-start gap-3 text-lg sm:text-xl">
                  <span className={`mt-0.5 grid h-10 w-10 shrink-0 place-items-center rounded-full text-lg text-white ${k.dot}`}>{bn(n + 1)}</span>
                  <span>উদাহরণ {bn(n + 1)}: {e.title}</span>
                </h2>
                <CodeBlock code={e.code} title={`example${n + 1}.cpp`} />
                <div className="mt-4 grid gap-4 sm:grid-cols-2">
                  <div className="rounded-2xl border border-slate-200 bg-white p-4">
                    <p className="mb-1 text-sm font-bold uppercase tracking-wide text-slate-500">Input</p>
                    <pre className="whitespace-pre-wrap break-words font-mono text-base text-slate-800">{e.input || "(কোনো input নেই)"}</pre>
                  </div>
                  <div className="rounded-2xl border border-emerald-300 bg-emerald-50 p-4">
                    <p className="mb-1 text-sm font-bold uppercase tracking-wide text-emerald-700">Output</p>
                    <pre className="whitespace-pre-wrap break-words font-mono text-base text-emerald-900">{e.output}</pre>
                  </div>
                </div>

                {e.viz?.length > 0 && (<><SectionTitle Icon={EyeIcon} tone="text-sky-600">ছবিতে দেখো</SectionTitle>{e.viz.map((g, gi) => <BitGroup key={gi} g={g} />)}</>)}

                {e.steps ? (
                  <>
                    <SectionTitle Icon={ListIcon}>ধাপে ধাপে কী ঘটছে</SectionTitle>
                    <Steps steps={e.steps} dot={k.dot} />
                    {e.tables?.map((t, ti) => <TraceTable key={ti} t={t} />)}
                    <div className="mt-5 rounded-r-2xl border-l-[6px] border-brand-red bg-white p-4 shadow-sm">
                      <p className="mb-1 text-base font-bold text-brand-red">সারকথা</p>
                      <p className="text-base text-slate-800"><Rich text={e.explain} /></p>
                    </div>
                  </>
                ) : sentences.length >= 3 ? (
                  <>
                    <SectionTitle Icon={ListIcon}>ব্যাখ্যা — ধাপে ধাপে</SectionTitle>
                    <Steps steps={sentences} dot={k.dot} />
                  </>
                ) : (
                  <div className="mt-5 rounded-r-2xl border-l-[6px] border-brand-red bg-white p-5 shadow-sm">
                    <p className="mb-1 text-lg font-bold text-brand-red">ব্যাখ্যা</p>
                    <p className="text-base text-slate-800"><Rich text={e.explain} /></p>
                  </div>
                )}
              </section>
            );
          })}

          {page.tips?.length > 0 && (
            <section className="mt-12 rounded-2xl border border-rose-200 bg-rose-50 p-5">
              <h2 className="flex items-center gap-2 text-xl"><WarnIcon width={24} height={24} className="text-brand-red" />সাবধান ও টিপস</h2>
              <ul className="mt-3 space-y-2.5">
                {page.tips.map((t, ti) => (
                  <li key={ti} className="flex gap-3 text-base leading-relaxed text-slate-800">
                    <ArrowIcon width={18} height={18} className="mt-2 shrink-0 text-brand-red" /><span><Rich text={t} /></span>
                  </li>
                ))}
              </ul>
            </section>
          )}
          <NavButtons i={i} onOpen={onOpen} />
        </article>
      </div>
    </>
  );
}
