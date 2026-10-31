import { useEffect, useRef, useState } from "react";

export const reduced = () => typeof window !== "undefined" && window.matchMedia?.("(prefers-reduced-motion: reduce)").matches;

// স্ক্রলে দেখা গেলে ভেসে ওঠে; once=false হলে বাইরে গেলে আবার false
export function useInView(once = true, margin = "-8% 0px") {
  const ref = useRef(null);
  const [v, setV] = useState(false);
  useEffect(() => {
    const el = ref.current;
    if (!el || reduced() || typeof IntersectionObserver === "undefined") { setV(true); return; }
    const io = new IntersectionObserver(([e]) => { if (e.isIntersecting) { setV(true); if (once) io.disconnect(); } else if (!once) setV(false); }, { rootMargin: margin });
    io.observe(el);
    return () => io.disconnect();
  }, [once, margin]);
  return [ref, v];
}

export default function Reveal({ children, delay = 0, className = "", as: Tag = "div" }) {
  const [ref, v] = useInView();
  return (
    <Tag ref={ref} style={{ transitionDelay: `${delay}ms` }}
      className={`transition-all duration-700 ease-out ${v ? "translate-y-0 opacity-100" : "translate-y-8 opacity-0"} ${className}`}>
      {children}
    </Tag>
  );
}
