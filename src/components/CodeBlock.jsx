import { useState } from "react";
import { Highlight, themes } from "prism-react-renderer";
import { CopyIcon, CheckIcon } from "./Icons";

export default function CodeBlock({ code, title = "main.cpp" }) {
  const [done, setDone] = useState(false);
  const copy = async () => {
    try { await navigator.clipboard.writeText(code); setDone(true); setTimeout(() => setDone(false), 1500); } catch { /* ignore */ }
  };
  return (
    <div className="overflow-hidden rounded-2xl border border-slate-700 bg-[#1e1e1e] shadow-sm">
      <div className="flex items-center justify-between bg-slate-800 px-4 py-2 text-xs text-slate-300">
        <span className="font-mono">{title}</span>
        <button onClick={copy} className="no-print flex items-center gap-1.5 rounded-md px-2 py-1 hover:bg-white/10" aria-label="কোড কপি করো">
          {done ? <CheckIcon /> : <CopyIcon />} {done ? "কপি হয়েছে" : "কপি"}
        </button>
      </div>
      <Highlight theme={themes.vsDark} code={code.trim()} language="cpp">
        {({ tokens, getLineProps, getTokenProps }) => (
          <pre className="max-h-[32rem] overflow-auto p-4 text-[13px] leading-relaxed font-mono">
            {tokens.map((line, i) => (
              <div key={i} {...getLineProps({ line })} className="flex">
                <span className="mr-4 w-6 shrink-0 select-none text-right text-slate-500">{i + 1}</span>
                <span className="whitespace-pre">{line.map((t, k) => <span key={k} {...getTokenProps({ token: t })} />)}</span>
              </div>
            ))}
          </pre>
        )}
      </Highlight>
    </div>
  );
}
