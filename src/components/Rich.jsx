import { Fragment } from "react";

// `code` ও **bold** — ছোট্ট inline markup
export default function Rich({ text, className = "" }) {
  const parts = String(text ?? "").split(/(`[^`]+`|\*\*[^*]+\*\*)/g).filter(Boolean);
  return (
    <span className={className}>
      {parts.map((p, i) => {
        if (p.startsWith("`") && p.endsWith("`") && p.length > 2)
          return <code key={i} className="rounded-md bg-slate-100 px-1.5 py-0.5 text-[0.88em] font-semibold text-brand-ink ring-1 ring-slate-200">{p.slice(1, -1)}</code>;
        if (p.startsWith("**") && p.endsWith("**") && p.length > 4)
          return <strong key={i} className="font-bold text-brand-ink">{p.slice(2, -2)}</strong>;
        return <Fragment key={i}>{p}</Fragment>;
      })}
    </span>
  );
}
