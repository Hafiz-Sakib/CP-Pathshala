import { useEffect, useState } from "react";
import { bn } from "../data";
import { useInView, reduced } from "./Reveal";

export default function CountUp({ to, ms = 1400 }) {
  const [ref, v] = useInView();
  const [n, setN] = useState(0);
  useEffect(() => {
    if (!v) return;
    if (reduced()) { setN(to); return; }
    let raf, t0;
    const tick = (t) => { t0 ??= t; const p = Math.min(1, (t - t0) / ms); setN(Math.round(to * (1 - (1 - p) ** 3))); if (p < 1) raf = requestAnimationFrame(tick); };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [v, to, ms]);
  return <span ref={ref}>{bn(n)}</span>;
}
