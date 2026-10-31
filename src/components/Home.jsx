import { tabs, pages, index, groupPages, categories, exampleCount, bn } from "../data";
import { col } from "./Colors";
import { BitGroup } from "./BitViz";
import BitPlayground from "./BitPlayground";
import Reveal from "./Reveal";
import CountUp from "./CountUp";
import SieveAnim from "./SieveAnim";
import BinaryCounter from "./BinaryCounter";
import { BoxIcon, BitIcon, SigmaIcon, CheckIcon, ArrowIcon, CodeIcon, EyeIcon, ListIcon, TableIcon, WarnIcon, BookIcon, PlayIcon } from "./Icons";

const TabIcon = { box: BoxIcon, bit: BitIcon, sigma: SigmaIcon };

const demo = {
  kind: "bits", caption: "12 & 10 — প্রতিটা ঘর আলাদা করে AND (হলুদ ঘরে দুইজনেই 1)",
  rows: [
    { label: "a = 12", bits: "00001100", dec: 12, tone: "a", hl: [4], sep: false },
    { label: "b = 10", bits: "00001010", dec: 10, tone: "b", hl: [4], sep: false },
    { label: "a & b", bits: "00001000", dec: 8, tone: "r", hl: [4], sep: true },
  ],
};

const features = [
  { Icon: CodeIcon, t: "কপি করা যায় এমন কোড", d: "রঙিন syntax সহ পুরো কোড। এক ক্লিকে কপি করে নিজের মতো চালাও।" },
  { Icon: BookIcon, t: "Syntax ও Time Complexity", d: "লেখার নিয়ম আর কত সময় লাগে — প্রতিটা পেজের শুরুতেই পাবে।" },
  { Icon: PlayIcon, t: "আসল Input ও Output", d: "প্রতিটা উদাহরণ আসল g++ দিয়ে চালিয়ে output নেওয়া — কোনো আন্দাজ নেই।" },
  { Icon: ListIcon, t: "ধাপে ধাপে ব্যাখ্যা", d: "বিট ও নাম্বার থিওরিতে প্রতিটা লাইনে কী ঘটছে, একদম ভেঙে ভেঙে বাংলায়।" },
  { Icon: EyeIcon, t: "ছবি দিয়ে বোঝা", d: "বিটের প্রতিটা ঘর, Sieve এর কাটাকাটি — সব রঙিন ছবিতে।" },
  { Icon: TableIcon, t: "হিসাবের টেবিল", d: "লুপ বা recursion এর প্রতিটা ধাপে মান কেমন বদলাচ্ছে তা টেবিলে দেখো।" },
  { Icon: WarnIcon, t: "সাবধান ও টিপস", d: "যেসব ভুল সবাই করে — overflow, priority, off-by-one — আগেই জেনে নাও।" },
  { Icon: BitIcon, t: "নিজে করে দেখো", d: "নিচের Bit Playground এ সংখ্যা বদলাও, ফল সাথে সাথে দেখো।" },
];

const road = [
  { t: "STL দিয়ে হাত পাকাও", d: "vector, string, set, map … ধীরে ধীরে একটা একটা function শেখো। প্রতিটার আলাদা পেজ।", to: () => groupPages("stl")[0].id, b: "STL শুরু করো" },
  { t: "বিটের মজা বোঝো", d: "AND, OR, XOR থেকে শুরু। প্রতিটা বিটের ঘর দেখে দেখে বুঝবে, মুখস্থ লাগবে না।", to: () => "bit-and", b: "বিট শুরু করো" },
  { t: "নাম্বার থিওরি ধরো", d: "Prime → Divisor → Sieve → GCD → Modular। ক্রম মেনে এগোলে সহজ।", to: () => "nt-prime-check", b: "নাম্বার থিওরি শুরু করো" },
  { t: "নিজে হাতে চালাও", d: "উদাহরণের input বদলাও, কোড ভাঙো, আবার জোড়া লাগাও। ভুল করেই শেখা হয়।", to: null, b: "কীভাবে চালাবে ↓" },
];

const popular = ["vector-push_back", "algo-sort", "map-frequency", "bit-xor", "bit-check-set", "is_powerOF2", "nt-sieve-bitset", "nt-gcd", "nt-binary-exponentiation", "nt-euler-phi"].filter((id) => index[id] !== undefined);

export default function Home({ onSelect, onOpen }) {
  const totalPages = pages.length;
  const totalEx = tabs.reduce((n, t) => n + exampleCount(t.id), 0);

  return (
    <>
      {/* ───── Hero ───── */}
      <section className="on-dark dots-bg relative bg-brand-ink text-white">
        <div aria-hidden className="pointer-events-none absolute inset-0 overflow-hidden font-mono font-bold text-white/10">
          {[["1", "6%", "12%", "4rem", "-8deg", "0s"], ["0", "88%", "20%", "5rem", "10deg", "1.2s"], ["&", "46%", "78%", "4.5rem", "6deg", "2s"], ["^", "70%", "62%", "3.5rem", "-12deg", "0.6s"], ["01", "14%", "70%", "3.5rem", "8deg", "1.8s"]].map(([t, l, tp, fs, r, d]) => (
            <span key={t + l} className="floaty absolute" style={{ left: l, top: tp, fontSize: fs, "--r": r, animationDelay: d }}>{t}</span>
          ))}
        </div>
        <div className="relative mx-auto grid max-w-6xl gap-10 px-4 py-12 sm:px-8 sm:py-16 lg:grid-cols-[1.15fr_1fr] lg:items-center">
          <div className="animate-fade-up">
            <p className="inline-block rounded-full border border-white/25 bg-white/10 px-4 py-1 text-base font-semibold text-emerald-200">বাংলায় C++ টিউটোরিয়াল • Competitive Programming</p>
            <h1 className="mt-4 text-xl sm:text-2xl lg:text-5xl">STL, বিটের মজা ও নাম্বার থিওরি শিখি বাংলায়</h1>
            <p className="mt-4 text-base text-white/90 sm:text-lg">প্রতিটা function-এর জন্য আলাদা পেজ — কোড, input, output আর <strong className="text-amber-300">ধাপে ধাপে ব্যাখ্যা</strong>। বিটের ছবি আর হিসাবের টেবিল দেখে দেখে শেখো, কঠিন জিনিসও জলের মতো সোজা।</p>
            <div className="mt-6 flex flex-wrap gap-3">
              <button onClick={() => onOpen(groupPages("stl")[0].id)} className="flex items-center gap-2 rounded-xl bg-white px-5 py-3 text-base font-bold text-brand-ink shadow hover:bg-emerald-50">STL শুরু করো <ArrowIcon /></button>
              <button onClick={() => onSelect("bits")} className="rounded-xl border border-white/50 px-5 py-3 text-base font-bold text-white hover:bg-white/10">বিটের মজা</button>
              <button onClick={() => onSelect("nt")} className="rounded-xl border border-white/50 px-5 py-3 text-base font-bold text-white hover:bg-white/10">নাম্বার থিওরি</button>
            </div>
            <dl className="mt-8 grid max-w-lg grid-cols-3 gap-3 text-center">
              {[[tabs.length, "টা বিষয়"], [totalPages, "টা পেজ"], [totalEx, "টা উদাহরণ"]].map(([n, l]) => (
                <div key={l} className="rounded-2xl bg-white/10 px-2 py-3 ring-1 ring-white/20">
                  <dt className="text-2xl font-bold text-amber-300"><CountUp to={n} /></dt>
                  <dd className="text-base text-white/85">{l}</dd>
                </div>
              ))}
            </dl>
          </div>

          <div className="animate-pop-in rounded-3xl bg-white p-5 text-slate-800 shadow-2xl">
            <p className="mb-1 text-base font-bold text-brand-red">পেজ দেখতে এমন — একটা ঝলক</p>
            <h2 className="text-xl">AND ( &amp; ) অপারেটর</h2>
            <p className="mt-1 text-base text-slate-600">দুইটা বিট-ই <strong>1</strong> হলে ফল 1, নাহলে 0। নিচে ঘরে ঘরে দেখো:</p>
            <BitGroup g={demo} />
            <button onClick={() => onOpen("bit-and")} className="mt-3 flex items-center gap-1.5 text-base font-bold text-brand-green hover:underline">পুরো পেজ দেখো <ArrowIcon /></button>
          </div>
        </div>
        <div className="road-dash" />
      </section>

      {/* ───── চলন্ত ticker ───── */}
      <div className="overflow-hidden border-b border-slate-200 bg-white py-3" aria-hidden>
        <div className="marquee">
          {[0, 1].map((k) => (
            <div key={k} className="flex shrink-0 gap-3 pr-3">
              {["vector", "set", "map", "sort()", "priority_queue", "XOR ^", "popcount", "1 << i", "Sieve", "GCD", "LCM", "modpow", "nCr", "φ(n)", "string", "bitset", "binary_search"].map((w) => (
                <span key={w + k} className="rounded-full bg-emerald-50 px-4 py-1 font-mono text-sm font-bold text-emerald-800 ring-1 ring-emerald-200">{w}</span>
              ))}
            </div>
          ))}
        </div>
      </div>

      {/* ───── বিষয়ের কার্ড (সবগুলো সমান মাপের) ───── */}
      <Reveal as="section" className="mx-auto max-w-6xl px-4 py-12 sm:px-8 sm:py-16">
        <h2 className="text-xl sm:text-2xl">কী কী শিখবে?</h2>
        <p className="mt-2 max-w-3xl text-base text-slate-600">তিনটা বিষয় — যেকোনো একটা বেছে নাও। প্রতিটা পেজে আছে একাধিক উদাহরণ, input দিলে কী output আসে, আর তার ব্যাখ্যা।</p>
        <div className="mt-8 grid items-stretch gap-6 md:grid-cols-3">
          {tabs.map((t, i) => {
            const k = col(t.color);
            const Icon = TabIcon[t.icon];
            const cats = categories(t.id);
            const shown = cats.slice(0, 5);
            return (
              <article key={t.id} style={{ animationDelay: `${i * 80}ms` }}
                className="card-lift animate-fade-up relative flex h-full flex-col overflow-hidden rounded-3xl border border-slate-200 bg-white shadow-sm">
                <div className={`h-2 bg-gradient-to-r ${k.bar}`} />
                <div className="flex flex-1 flex-col p-6">
                  <div className="flex items-center gap-3">
                    <span className={`grid h-14 w-14 shrink-0 place-items-center rounded-2xl ${k.icon}`}><Icon width={28} height={28} /></span>
                    <div>
                      <h3 className="text-xl">{t.label}</h3>
                      <p className="text-base text-slate-500">{bn(groupPages(t.id).length)} টা পেজ · {bn(exampleCount(t.id))} টা উদাহরণ</p>
                    </div>
                  </div>
                  <p className="mt-4 min-h-[5.5rem] text-base text-slate-700">{t.about}</p>
                  <ul className="mt-3 space-y-1.5 text-base">
                    {t.learn.map((l) => (
                      <li key={l} className="flex items-start gap-2"><CheckIcon width={18} height={18} className={`mt-1.5 shrink-0 ${k.text}`} /><span>{l}</span></li>
                    ))}
                  </ul>
                  <div className="mt-4 flex min-h-[6.5rem] flex-wrap content-start gap-1.5">
                    {shown.map((d) => <span key={d.cat} className={`rounded-full px-2.5 py-0.5 text-sm font-semibold ${k.badge}`}>{d.cat.replace(/^[০-৯]+\s/, "")}</span>)}
                    {cats.length > shown.length && <span className="rounded-full border border-slate-200 px-2.5 py-0.5 text-sm text-slate-500">+{bn(cats.length - shown.length)} আরও</span>}
                  </div>
                  <div className="mt-auto pt-5">
                    <button onClick={() => onSelect(t.id)} className={`stretch-link flex w-full items-center justify-center gap-2 rounded-xl py-3 text-base font-bold text-white ${k.btn}`}>
                      {t.label} দেখো <ArrowIcon />
                    </button>
                  </div>
                </div>
              </article>
            );
          })}
        </div>
      </Reveal>

      {/* ───── রোডম্যাপ ───── */}
      <Reveal as="section" className="border-y border-slate-200 bg-white/70">
        <div className="mx-auto max-w-6xl px-4 py-12 sm:px-8 sm:py-16">
          <h2 className="text-xl sm:text-2xl">শেখার রোডম্যাপ</h2>
          <p className="mt-2 max-w-3xl text-base text-slate-600">কোথা থেকে শুরু করবে বুঝতে পারছো না? এই চার ধাপ মেনে এগোও।</p>
          <div className="mt-8 grid items-stretch gap-5 sm:grid-cols-2 lg:grid-cols-4">
            {road.map((r, i) => (
              <div key={r.t} className="card-lift relative flex h-full flex-col rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
                <span className={`grid h-12 w-12 place-items-center rounded-full text-xl font-bold text-white ${["bg-emerald-500", "bg-amber-500", "bg-blue-500", "bg-purple-500"][i]}`}>{bn(i + 1)}</span>
                <h3 className="mt-3 text-lg">{r.t}</h3>
                <p className="mt-1 flex-1 text-base text-slate-600">{r.d}</p>
                <button onClick={() => (r.to ? onOpen(r.to()) : document.getElementById("run")?.scrollIntoView({ behavior: "smooth" }))}
                  className="stretch-link mt-4 flex items-center gap-1.5 text-base font-bold text-brand-green hover:underline">{r.b} {r.to && <ArrowIcon />}</button>
              </div>
            ))}
          </div>
        </div>
      </Reveal>

      {/* ───── প্রতিটা পেজে কী পাবে ───── */}
      <Reveal as="section" className="mx-auto max-w-6xl px-4 py-12 sm:px-8 sm:py-16">
        <h2 className="text-xl sm:text-2xl">প্রতিটা পেজে কী কী পাবে?</h2>
        <p className="mt-2 max-w-3xl text-base text-slate-600">শুধু কোড না — বোঝার জন্য যা যা লাগে সব এক জায়গায়।</p>
        <div className="mt-8 grid items-stretch gap-5 sm:grid-cols-2 lg:grid-cols-4">
          {features.map(({ Icon, t, d }) => (
            <div key={t} className="flex h-full flex-col rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
              <span className="grid h-12 w-12 place-items-center rounded-xl bg-emerald-100 text-emerald-700"><Icon width={24} height={24} /></span>
              <h3 className="mt-3 text-lg">{t}</h3>
              <p className="mt-1 text-base text-slate-600">{d}</p>
            </div>
          ))}
        </div>
      </Reveal>

      <Reveal as="section" className="mx-auto max-w-5xl px-4 py-12 sm:px-8 sm:py-16">
        <div className="grid items-start gap-8 lg:grid-cols-2">
          <div>
            <p className="text-sm font-bold text-blue-700">লাইভ অ্যানিমেশন · নাম্বার থিওরি</p>
            <h2 className="mt-1 text-xl sm:text-2xl">Sieve নিজের চোখে দেখো</h2>
            <p className="mt-2 text-base text-slate-600">২ থেকে ৫০ পর্যন্ত সংখ্যা। প্রতিটা prime এর গুণিতক একটা একটা করে কাটা পড়ছে (লাল)। শেষে যারা বেঁচে থাকে, তারাই prime (সবুজ)।</p>
            <button onClick={() => onOpen("nt-sieve-bitset")} className="mt-4 flex items-center gap-2 text-base font-bold text-blue-700 hover:underline">Sieve এর পুরো পেজ <ArrowIcon /></button>
          </div>
          <SieveAnim />
        </div>
      </Reveal>

      <Reveal as="section" className="border-y border-emerald-200 bg-emerald-50/60">
        <div className="mx-auto grid max-w-5xl items-start gap-8 px-4 py-12 sm:px-8 sm:py-16 lg:grid-cols-2">
          <BinaryCounter />
          <div>
            <p className="text-sm font-bold text-emerald-700">লাইভ অ্যানিমেশন · বিটের মজা</p>
            <h2 className="mt-1 text-xl sm:text-2xl">গুনতে গুনতে বিট বদলায়</h2>
            <p className="mt-2 text-base text-slate-600">প্রতি সেকেন্ডে সংখ্যা ১ বাড়ছে। কোন বিট উল্টে যাচ্ছে (হলুদ) খেয়াল করো। পাশে দেখো জোড়-বিজোড়, 1 এর সংখ্যা আর 2 এর ঘাত কখন ধরা পড়ছে।</p>
            <button onClick={() => onOpen("bit-popcount")} className="mt-4 flex items-center gap-2 text-base font-bold text-emerald-700 hover:underline">popcount পেজ দেখো <ArrowIcon /></button>
          </div>
        </div>
      </Reveal>

      {/* ───── Bit Playground ───── */}
      <Reveal as="section" className="border-y border-amber-200 bg-amber-50/70">
        <div className="mx-auto max-w-4xl px-4 py-12 sm:px-8 sm:py-16">
          <h2 className="text-xl sm:text-2xl">নিজে করে দেখো — Bit Playground</h2>
          <p className="mt-2 text-base text-slate-700">operator বাছো, সংখ্যা বদলাও, অথবা বিটের ঘরে ক্লিক করো। ফল সাথে সাথে বদলে যাবে।</p>
          <div className="mt-6"><BitPlayground /></div>
          <button onClick={() => onSelect("bits")} className="mt-5 flex items-center gap-2 text-lg font-bold text-amber-700 hover:underline">আরও শিখতে বিটের মজা দেখো <ArrowIcon /></button>
        </div>
      </Reveal>

      {/* ───── জনপ্রিয় পেজ ───── */}
      <Reveal as="section" className="mx-auto max-w-6xl px-4 py-12 sm:px-8 sm:py-16">
        <h2 className="text-xl sm:text-2xl">জনপ্রিয় পেজ</h2>
        <p className="mt-2 text-base text-slate-600">সরাসরি এখান থেকেই শুরু করতে পারো।</p>
        <div className="mt-6 flex flex-wrap gap-3">
          {popular.map((id) => {
            const p = pages[index[id]];
            const t = tabs.find((x) => x.id === p.grp);
            const k = col(t.color);
            return (
              <button key={id} onClick={() => onOpen(id)} className={`card-lift flex items-center gap-2 rounded-xl border bg-white px-4 py-2.5 text-left shadow-sm ${k.border}`}>
                <span className={`rounded-md px-2 py-0.5 text-sm font-bold ${k.badge}`}>{t.label}</span>
                <span className="font-mono text-base font-bold text-brand-ink">{p.title}</span>
              </button>
            );
          })}
        </div>
      </Reveal>

      {/* ───── কীভাবে চালাবে ───── */}
      <Reveal as="section" className="scroll-mt-20 border-t border-slate-200 bg-white/70">
        <div className="mx-auto max-w-6xl px-4 py-12 sm:px-8 sm:py-16">
          <h2 className="text-xl sm:text-2xl">কোড কীভাবে চালাবে?</h2>
          <p className="mt-2 max-w-3xl text-base text-slate-600">পেজ থেকে কোড কপি করে নিজের কম্পিউটারে চালাতে এই তিনটা ধাপই যথেষ্ট (g++ ইনস্টল থাকতে হবে)।</p>
          <div className="mt-8 grid items-stretch gap-5 md:grid-cols-3">
            {[
              ["কোড সেভ করো", "পেজ থেকে ‘কপি’ চেপে কোডটা `main.cpp` নামে সেভ করো।", null],
              ["Compile করো", "টার্মিনালে এই কমান্ড দাও:", "g++ -std=c++17 main.cpp -o main"],
              ["চালাও", "Linux/Mac এ `./main`, Windows এ `main.exe`। input লাগলে নিচের মতো দাও:", "echo 29 | ./main"],
            ].map(([t, d, cmd], i) => (
              <div key={t} className="flex h-full flex-col rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">
                <div className="flex items-center gap-3">
                  <span className="grid h-11 w-11 place-items-center rounded-full bg-brand-green text-lg font-bold text-white">{bn(i + 1)}</span>
                  <h3 className="text-lg">{t}</h3>
                </div>
                <p className="mt-2 flex-1 text-base text-slate-700">{d.split("`").map((s, j) => (j % 2 ? <code key={j} className="rounded bg-slate-100 px-1.5 py-0.5 text-[0.9em] font-semibold ring-1 ring-slate-200">{s}</code> : s))}</p>
                {cmd && <pre className="mt-3 overflow-x-auto rounded-xl bg-[#1e1e1e] px-4 py-3 font-mono text-sm text-emerald-300"><span className="select-none text-slate-500">$ </span>{cmd}</pre>}
              </div>
            ))}
          </div>
          <p className="mt-5 text-base text-slate-600">অনলাইনে চালাতে চাইলে OnlineGDB, Programiz বা Codeforces এর custom test ব্যবহার করতে পারো — কোড সেখানে পেস্ট করলেই হলো।</p>
        </div>
      </Reveal>

      {/* ───── শেষ CTA ───── */}
      <section className="on-dark dots-bg relative bg-brand-ink text-white">
        <div className="mx-auto max-w-4xl px-4 py-12 text-center sm:px-8 sm:py-16">
          <h2 className="text-xl sm:text-2xl">আর দেরি কেন? আজই শুরু করো</h2>
          <p className="mt-3 text-base text-white/85">একটা একটা করে পেজ পড়ো, কোড চালাও, নিজে বদলে দেখো — দেখবে Competitive Programming আর ভয়ের কিছু না।</p>
          <div className="mt-6 flex flex-wrap justify-center gap-3">
            {tabs.map((t) => (
              <button key={t.id} onClick={() => onSelect(t.id)} className="rounded-xl bg-white px-5 py-3 text-base font-bold text-brand-ink hover:bg-emerald-50">{t.label}</button>
            ))}
          </div>
        </div>
        <div className="road-dash" />
      </section>
    </>
  );
}
