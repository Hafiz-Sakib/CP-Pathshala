import { useEffect, useState } from "react";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Home from "./components/Home";
import GroupIndex from "./components/GroupIndex";
import LessonPage from "./components/LessonPage";
import { tabs, pages, index } from "./data";

const valid = ["home", ...tabs.map((t) => t.id)];
const read = () => {
  const q = new URLSearchParams(window.location.search);
  const p = q.get("p");
  if (p && index[p] !== undefined) return { tab: pages[index[p]].grp, pid: p };
  const t = q.get("tab");
  return { tab: valid.includes(t) ? t : "home", pid: null };
};

export default function App() {
  const [s, setS] = useState(read);
  useEffect(() => {
    const pop = () => setS(read());
    window.addEventListener("popstate", pop);
    return () => window.removeEventListener("popstate", pop);
  }, []);
  useEffect(() => { window.scrollTo({ top: 0 }); }, [s.tab, s.pid]);

  const go = (tab, pid = null) => {
    setS({ tab, pid });
    window.history.pushState(null, "", pid ? `/?p=${pid}` : tab === "home" ? "/" : `/?tab=${tab}`);
  };
  const openPage = (pid) => go(pages[index[pid]].grp, pid);
  const current = tabs.find((t) => t.id === s.tab);

  return (
    <div className="flex min-h-screen flex-col">
      <Navbar tab={s.tab} onSelect={(id) => go(id)} />
      <main key={s.tab + (s.pid || "")} className="animate-fade-in flex-1">
        {s.pid ? <LessonPage page={pages[index[s.pid]]} i={index[s.pid]} onOpen={openPage} onIndex={() => go(s.tab)} />
          : current ? <GroupIndex tab={current} onOpen={openPage} />
          : <Home onSelect={(id) => go(id)} onOpen={openPage} />}
      </main>
      <Footer />
    </div>
  );
}
