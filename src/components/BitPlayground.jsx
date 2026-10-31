import { useState } from "react";
import { BitRow, Weights } from "./BitViz";

const OPS = ["&", "|", "^", "<<", ">>", "~"];
const bits8 = (n) => (n & 255).toString(2).padStart(8, "0");
const NOTE = {
  "&": "যে ঘরে দুটোই 1, শুধু সেখানেই 1 — ‘দুইজনেই রাজি’।",
  "|": "যেকোনো একটাতে 1 হলেই 1 — ‘একজন রাজি হলেই চলবে’।",
  "^": "ঘর আলাদা হলে 1, একই হলে 0 — ‘আলাদা কিনা?’",
  "<<": "সব বিট n ঘর বামে সরলো, ডানে 0 ঢুকলো → a × 2ⁿ।",
  ">>": "সব বিট n ঘর ডানে সরলো, ডানের বিট ঝরে গেলো → a / 2ⁿ (পূর্ণসংখ্যা)।",
  "~": "প্রতিটা বিট উল্টে গেলো। int এ ~a = −a − 1 (নিচে ৮ ঘরের নিচের অংশ দেখানো হচ্ছে)।",
};

export default function BitPlayground() {
  const [a, setA] = useState(12);
  const [b, setB] = useState(10);
  const [op, setOp] = useState("&");
  const shift = op === "<<" || op === ">>";
  const unary = op === "~";
  const clamp = (v, m) => Math.max(0, Math.min(m, Number.isFinite(v) ? Math.floor(v) : 0));
  let res;
  if (op === "&") res = a & b;
  else if (op === "|") res = a | b;
  else if (op === "^") res = a ^ b;
  else if (op === "<<") res = a << b;
  else if (op === ">>") res = a >> b;
  else res = ~a;

  const A = bits8(a), B = bits8(b), Rb = bits8(res);
  const hl = !shift && !unary ? Rb.split("").map((c, i) => (c === "1" ? i : -1)).filter((i) => i >= 0) : [];
  const toggle = (setter, val) => (i) => setter(val ^ (1 << (7 - i)));
  const expr = unary ? `~${a}` : `${a} ${op} ${b}`;

  return (
    <div className="rounded-3xl border border-amber-200 bg-white p-4 shadow-md sm:p-6">
      <div className="flex flex-wrap items-center gap-2" role="group" aria-label="operator বাছাই">
        {OPS.map((o) => (
          <button key={o} type="button" onClick={() => setOp(o)} aria-pressed={op === o}
            className={`rounded-full px-4 py-1.5 font-mono text-lg font-bold transition ${op === o ? "bg-amber-500 text-white shadow" : "bg-slate-100 text-slate-700 hover:bg-amber-100"}`}>{o}</button>
        ))}
      </div>

      <div className="mt-4 flex flex-wrap items-center gap-4">
        <label className="flex items-center gap-2 text-base font-bold text-slate-700">a =
          <input type="number" min={0} max={255} value={a} onChange={(e) => setA(clamp(e.target.valueAsNumber, 255))}
            className="w-24 rounded-xl border border-slate-300 px-3 py-1.5 font-mono text-lg outline-none focus:border-amber-500 focus:ring-2 focus:ring-amber-200" />
        </label>
        {!unary && (
          <label className="flex items-center gap-2 text-base font-bold text-slate-700">{shift ? "n (কত ঘর) =" : "b ="}
            <input type="number" min={0} max={shift ? 7 : 255} value={b} onChange={(e) => setB(clamp(e.target.valueAsNumber, shift ? 7 : 255))}
              className="w-24 rounded-xl border border-slate-300 px-3 py-1.5 font-mono text-lg outline-none focus:border-amber-500 focus:ring-2 focus:ring-amber-200" />
          </label>
        )}
        <span className="text-sm text-slate-500">(বিটের ঘরে ক্লিক করেও বদলাতে পারো 👆)</span>
      </div>

      <div className="mt-5 overflow-x-auto pb-2 no-scrollbar">
        <div className="w-max">
          <Weights len={8} />
          <BitRow r={{ label: "a", bits: A, dec: a, tone: "a", hl: [], sep: false }} onToggle={toggle(setA, a)} />
          {!unary && !shift && <BitRow r={{ label: "b", bits: B, dec: b, tone: "b", hl: [], sep: false }} onToggle={toggle(setB, b)} />}
          <BitRow r={{ label: unary ? "~a (৮ ঘর)" : "ফল", bits: Rb, dec: res, tone: "r", hl, sep: true }} />
        </div>
      </div>

      <div className="mt-4 rounded-2xl bg-amber-50 p-4 text-base ring-1 ring-amber-200">
        <p className="font-mono text-lg font-bold text-brand-ink">{expr} = {res}</p>
        <p className="mt-1 text-slate-700">{NOTE[op]}</p>
        {shift && op === "<<" && res > 255 && <p className="mt-1 text-sm font-semibold text-brand-red">ফল ৮ ঘরের বাইরে গেছে — int এ আসল মান {res}, তাই ছবিতে শুধু নিচের ৮ বিট।</p>}
      </div>
    </div>
  );
}
