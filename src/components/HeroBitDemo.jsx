import { useEffect, useState } from "react";
import { reduced } from "./Reveal";
import { ArrowIcon } from "./Icons";

const A = 12, B = 10, LEN = 8;
const bits = (n) => n.toString(2).padStart(LEN, "0").split("").map(Number);
const OPS = {
  and: { sym: "&", name: "AND", f: (x, y) => x & y, page: "bit-and", rule: "দুইটা বিট-ই 1 হলে ফল 1, নাহলে 0।" },
  or: { sym: "|", name: "OR", f: (x, y) => x | y, page: "bit-or", rule: "যেকোনো একটা বিট 1 হলেই ফল 1।" },
  xor: { sym: "^", name: "XOR", f: (x, y) => x ^ y, page: "bit-xor", rule: "দুইটা বিট আলাদা হলে ফল 1, একই হলে 0।" },
};
const ORDER = ["and", "or", "xor"];
const a = bits(A), b = bits(B);
const weight = (i) => 2 ** (LEN - 1 - i);

const cell = (on, tone, active) =>
  `grid h-8 w-6 shrink-0 place-items-center rounded-md font-mono text-sm font-bold transition-all duration-300 min-[420px]:h-9 min-[420px]:w-7 min-[420px]:text-base sm:h-10 sm:w-9 ${
    on ? tone : "bg-slate-100 text-slate-400"} ${active ? "scale-110 ring-2 ring-amber-400 ring-offset-1" : ""}`;

export default function HeroBitDemo({ onOpen }) {
  const [op, setOp] = useState("and");
  const [locked, setLocked] = useState(false);
  const [step, setStep] = useState(reduced() ? LEN : 0); // কতগুলো ঘর হিসাব হয়ে গেছে
  const O = OPS[op];
  const res = a.map((x, i) => O.f(x, b[i]));
  const finished = step >= LEN;

  useEffect(() => {
    if (reduced()) return;
    const id = setTimeout(() => {
      if (!finished) return setStep((s) => s + 1);
      if (locked) return setStep(0);
      setOp((p) => ORDER[(ORDER.indexOf(p) + 1) % ORDER.length]);
      setStep(0);
    }, finished ? 2200 : step === 0 ? 700 : 520);
    return () => clearTimeout(id);
  }, [step, finished, locked, op]);

  const pick = (k) => { setOp(k); setLocked(true); setStep(0); };
  const cur = step > 0 && step <= LEN ? step - 1 : -1; // এইমাত্র হিসাব হওয়া ঘর
  const resVal = res.reduce((s, v, i) => s + v * weight(i), 0);
  const msg = finished
    ? `ফল: ${A} ${O.sym} ${B} = ${resVal}`
    : cur >= 0
      ? `${weight(cur)} এর ঘর: ${a[cur]} ${O.sym} ${b[cur]} = ${res[cur]}`
      : "ঘরে ঘরে হিসাব শুরু হচ্ছে…";

  return (
    <div className="animate-pop-in rounded-3xl bg-white p-4 text-slate-800 sm:p-5 shadow-2xl">
      <div className="flex flex-wrap items-center justify-between gap-2">
        <p className="inline-flex items-center gap-2 text-sm font-bold text-brand-red">
          <span className="relative flex h-2.5 w-2.5"><span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-rose-400 opacity-75" /><span className="relative inline-flex h-2.5 w-2.5 rounded-full bg-brand-red" /></span>
          লাইভ ডেমো · বিট অপারেশন
        </p>
        <div className="flex gap-1" role="tablist" aria-label="অপারেটর বাছো">
          {ORDER.map((k) => (
            <button key={k} role="tab" aria-selected={op === k} onClick={() => pick(k)}
              className={`rounded-lg px-2.5 py-1 font-mono text-sm font-bold transition ${op === k ? "bg-brand-ink text-white" : "bg-slate-100 text-slate-600 hover:bg-slate-200"}`}>{OPS[k].name}</button>
          ))}
        </div>
      </div>

      <h2 className="mt-2 text-xl">{O.name} ( {O.sym} ) অপারেটর</h2>
      <p className="mt-1 text-base text-slate-600">{O.rule} প্রতিটা ঘর আলাদা করে হিসাব হচ্ছে — নিচে দেখো:</p>

      <div className="mt-3 overflow-x-auto rounded-2xl border border-slate-200 bg-white p-3 no-scrollbar">
        <div className="w-max">
          <div className="flex items-end gap-2 sm:gap-3">
            <span className="w-14 shrink-0 text-right text-[10px] font-semibold text-slate-500 min-[420px]:w-16 min-[420px]:text-xs sm:w-20">ঘরের মান →</span>
            <div className="flex gap-0.5 min-[420px]:gap-1">
              {Array.from({ length: LEN }, (_, i) => (
                <span key={i} className={`w-6 shrink-0 text-center font-mono text-[9px] font-semibold transition min-[420px]:w-7 min-[420px]:text-[11px] sm:w-9 ${i === cur ? "text-amber-600" : "text-slate-500"}`}>{weight(i)}</span>
              ))}
            </div>
          </div>
          {[["a = 12", a, "bg-sky-600 text-white", A], ["b = 10", b, "bg-violet-600 text-white", B]].map(([lb, arr, tone, dec]) => (
            <div key={lb} className="mt-1.5 flex items-center gap-2 sm:gap-3">
              <span className="w-14 shrink-0 text-right text-xs font-semibold text-slate-700 min-[420px]:w-16 min-[420px]:text-sm sm:w-20 sm:text-base">{lb}</span>
              <div className="flex gap-0.5 min-[420px]:gap-1">{arr.map((v, i) => <span key={i} className={cell(v === 1, tone, i === cur)}>{v}</span>)}</div>
              <span className="shrink-0 font-mono text-sm font-bold text-slate-700">= {dec}</span>
            </div>
          ))}
          <div className="mt-2 flex items-center gap-2 sm:gap-3 border-t-[3px] border-slate-400 pt-2">
            <span className="w-14 shrink-0 text-right text-xs font-semibold text-slate-700 min-[420px]:w-16 min-[420px]:text-sm sm:w-20 sm:text-base">a {O.sym} b</span>
            <div className="flex gap-0.5 min-[420px]:gap-1">
              {res.map((v, i) => i < step
                ? <span key={i} className={cell(v === 1, "bg-emerald-600 text-white", i === cur)}>{v}</span>
                : <span key={i} className={cell(false, "", false) + " !bg-slate-50 !text-slate-300"}>?</span>)}
            </div>
            <span className={`shrink-0 font-mono text-sm font-bold transition-opacity ${finished ? "text-emerald-700 opacity-100" : "opacity-0"}`}>= {resVal}</span>
          </div>
        </div>
      </div>

      <p className="mt-3 min-h-[1.75rem] font-mono text-base font-bold text-brand-ink" aria-live="polite">{msg}</p>
      <button onClick={() => onOpen(O.page)} className="mt-2 flex items-center gap-1.5 text-base font-bold text-brand-green hover:underline">{O.name} এর পুরো পেজ দেখো <ArrowIcon /></button>
    </div>
  );
}
