# সি++ শিখি বাংলায় (PWA)

    npm install
    npm run dev
    npm run build

## নতুন পেজ/উদাহরণ
1. `gen/p_*.py` ফাইলে `P(...)` ও `E(...)` লেখো
2. ধাপে ধাপে ব্যাখ্যা/ছবি/টেবিল দিতে `gen/e_bits.py`, `gen/e_nt1.py`, `gen/e_nt2.py` এ `EN(পেজ-id, intro, uses, tips, X(steps, viz, tables))` লেখো
   - `RB()/VB()` = বিটের ছবি, `VG()` = সংখ্যার গ্রিড (Sieve), `T()` = টেবিল
3. `cd gen && python3 build.py`  (g++ লাগবে; আসল output `src/data/pages.json` এ বসে)
4. `npm run build`

Deep link: `/?p=vector-push_back` , `/?tab=stl`
