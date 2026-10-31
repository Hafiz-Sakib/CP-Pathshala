# কম্পিটিটিভ প্রোগ্রামিং পাঠশালা — PWA

    npm install
    npm run dev
    npm run build

## নতুন পেজ/উদাহরণ
1. `gen/p_*.py` (`p_rec.py` রিকার্সন ও DP, `p_graph.py` গ্রাফ সহ) ফাইলে `P(...)` ও `E(...)` লেখো
2. ধাপে ধাপে ব্যাখ্যা/ছবি/টেবিল দিতে `gen/e_bits.py`, `gen/e_nt1.py`, `gen/e_nt2.py`, `gen/e_rec.py`, `gen/e_graph1.py`, `gen/e_graph2.py` এ `EN(পেজ-id, intro, uses, tips, X(steps, viz, tables))` লেখো
   - `GV()` = গ্রাফের ছবি, `MV()` = ২D ঘর (matrix/grid/dp), `sims.py` = BFS/DFS/Dijkstra/MST simulation
   - `RB()/VB()` = বিটের ছবি, `VG()` = সংখ্যার গ্রিড (Sieve), `T()` = টেবিল
3. `cd gen && python3 build.py`  (g++ লাগবে; আসল output `src/data/pages.json` এ বসে)
4. `npm run build`

Deep link: `/?p=vector-push_back` , `/?tab=stl` , `/?tab=rec` , `/?tab=graph`

## ফন্ট
কোডে Fira Code (`src/fonts`, ligature সহ), বাকি সব জায়গায় Hind Siliguri।

## PWA আইকন
`public/` এ icon.svg, icon-192/512.png, icon-maskable-192/512.png, apple-touch-icon.png, favicon-32.png
