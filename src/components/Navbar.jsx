import { useEffect, useRef, useState } from "react";
import { HomeIcon, BoxIcon, BitIcon, SigmaIcon, MenuIcon, CloseIcon } from "./Icons";

const items = [
  { id: "home", label: "হোম", Icon: HomeIcon },
  { id: "stl", label: "STL", Icon: BoxIcon },
  { id: "bits", label: "বিটের মজা", Icon: BitIcon },
  { id: "nt", label: "নাম্বার থিওরি", Icon: SigmaIcon },
];

export default function Navbar({ tab, onSelect }) {
  const [open, setOpen] = useState(false);
  const ref = useRef(null);

  useEffect(() => {
    const esc = (e) => e.key === "Escape" && setOpen(false);
    const out = (e) => ref.current && !ref.current.contains(e.target) && setOpen(false);
    document.addEventListener("keydown", esc);
    document.addEventListener("mousedown", out);
    return () => { document.removeEventListener("keydown", esc); document.removeEventListener("mousedown", out); };
  }, []);

  const btn = (it, mobile) => {
    const active = tab === it.id;
    return (
      <button key={it.id} aria-current={active ? "page" : undefined}
        onClick={() => { onSelect(it.id); setOpen(false); }}
        className={`flex items-center gap-2 rounded-full border text-base font-bold transition ${mobile ? "w-full rounded-xl px-4 py-3" : "px-3.5 py-2"} ${
          active ? "bg-brand-green text-white border-brand-ink shadow-sm" : "border-transparent text-slate-700 hover:bg-brand-green/10"}`}>
        <it.Icon /> {it.label}
      </button>
    );
  };

  return (
    <header className="no-print sticky top-0 z-40 h-16 bg-white/95 backdrop-blur border-b-[3px] border-brand-red shadow-sm">
      <div ref={ref} className="relative mx-auto flex h-full max-w-[90rem] items-center justify-between px-3 sm:px-6">
        <button onClick={() => onSelect("home")} className="flex items-center gap-2 text-left" aria-label="হোম পেজে যাও">
          <img src="/icon.svg" alt="সি++ লোগো" className="h-9 w-auto sm:h-10 xl:h-12 rounded-lg" />
          <span className="h-8 w-px bg-slate-300" />
          <span className="font-bold text-brand-ink leading-tight text-base sm:text-lg">সি++ শিখি<br className="sm:hidden" /> বাংলায়</span>
        </button>

        <nav className="hidden lg:flex h-12 items-center gap-1 rounded-full bg-emerald-50/70 border border-brand-green/40 ring-1 ring-brand-green/10 px-1.5" aria-label="প্রধান মেনু">
          {items.map((it) => btn(it, false))}
        </nav>

        <span className="hidden xl:block text-right text-sm text-slate-500">Hafiz Sakib-এর<br />নোট থেকে তৈরি</span>

        <button className="lg:hidden grid h-11 w-11 place-items-center rounded-full bg-white border border-brand-green/40"
          aria-expanded={open} aria-controls="mobile-menu" aria-label="মেনু" onClick={() => setOpen(!open)}>
          {open ? <CloseIcon width={20} height={20} /> : <MenuIcon width={20} height={20} />}
        </button>

        {open && (
          <div id="mobile-menu" className="lg:hidden animate-slide-down absolute right-3 top-full mt-2 w-[min(18rem,calc(100vw-1.5rem))] rounded-2xl bg-white border border-brand-green/40 shadow-xl p-2 space-y-1">
            {items.map((it) => btn(it, true))}
          </div>
        )}
      </div>
    </header>
  );
}
