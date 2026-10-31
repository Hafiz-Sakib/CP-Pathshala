<div align="center">

<img src="https://ibb.co.com/bRdS3sGC" alt="CP Pathshala logo" width="120" />

# কম্পিটিটিভ প্রোগ্রামিং পাঠশালা

### Competitive Programming Pathshala — learn CP in Bangla, the easy way

An offline-capable **Progressive Web App** that teaches C++ competitive programming in simple Bangla — from **STL** and **bit manipulation** to **number theory**, **recursion / DP** and **graph theory** — with real, compiler-verified code, step-by-step walkthroughs and colourful visualisations.

![React](https://img.shields.io/badge/React-18.3-61DAFB?logo=react&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-5.4-646CFF?logo=vite&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4-06B6D4?logo=tailwindcss&logoColor=white)
![PWA](https://img.shields.io/badge/PWA-installable%20%26%20offline-5A0FC8?logo=pwa&logoColor=white)
![Python](https://img.shields.io/badge/Content%20pipeline-Python%203-3776AB?logo=python&logoColor=white)
![Language](https://img.shields.io/badge/Content-বাংলা-00694d)
![Version](https://img.shields.io/badge/version-1.2.0-c8283a)

**144 lessons · 200 runnable C++ examples · 5 learning tracks · 100 % Bangla explanations**

</div>

---

## Table of Contents

- [কম্পিটিটিভ প্রোগ্রামিং পাঠশালা](#কম্পিটিটিভ-প্রোগ্রামিং-পাঠশালা)
  - [Competitive Programming Pathshala — learn CP in Bangla, the easy way](#competitive-programming-pathshala--learn-cp-in-bangla-the-easy-way)
  - [Table of Contents](#table-of-contents)
  - [1. Overview](#1-overview)
  - [2. Features](#2-features)
  - [3. Curriculum](#3-curriculum)
  - [4. Tech Stack](#4-tech-stack)
  - [5. Project Structure](#5-project-structure)
  - [6. Getting Started](#6-getting-started)
    - [Prerequisites](#prerequisites)
    - [Install and run](#install-and-run)
    - [Production build](#production-build)
  - [7. Available Scripts](#7-available-scripts)
  - [8. How the Content Pipeline Works](#8-how-the-content-pipeline-works)
  - [9. Adding or Editing Lessons](#9-adding-or-editing-lessons)
    - [9.1 Add a new lesson page](#91-add-a-new-lesson-page)
    - [9.2 Add the step-by-step enrichment](#92-add-the-step-by-step-enrichment)
    - [9.3 Helper cheat-sheet (`enrich_lib.py`)](#93-helper-cheat-sheet-enrich_libpy)
    - [9.4 Rebuild and ship](#94-rebuild-and-ship)
    - [9.5 Add a brand-new track](#95-add-a-brand-new-track)
  - [10. Data Model (`pages.json`)](#10-data-model-pagesjson)
  - [11. Application Architecture](#11-application-architecture)
  - [12. Components Reference](#12-components-reference)
  - [13. Routing and Deep Links](#13-routing-and-deep-links)
  - [14. PWA, Offline Support and Icons](#14-pwa-offline-support-and-icons)
  - [15. Design System](#15-design-system)
  - [16. Accessibility and Print](#16-accessibility-and-print)
  - [17. Build and Deployment](#17-build-and-deployment)
  - [18. Troubleshooting](#18-troubleshooting)
  - [19. Contributing](#19-contributing)
  - [20. Author and Credits](#20-author-and-credits)

---

## 1. Overview

Most competitive programming (CP) resources are written in English and assume the reader already knows the jargon. **CP Pathshala** ("পাঠশালা" = a little school) is built for Bangla-speaking beginners who want to start CP in C++ without that barrier.

Every lesson page follows the same predictable shape:

| Section                                | What the learner gets                                                    |
| -------------------------------------- | ------------------------------------------------------------------------ |
| **Short description**                  | One-line summary of the function / concept                               |
| **সহজ কথায় ধারণা** (Plain-words idea) | A friendly explanation plus "where is this used?" chips                  |
| **Syntax + Time complexity**           | The exact way to write it and what it costs                              |
| **Examples**                           | Syntax-highlighted, copyable C++ with real **input** and real **output** |
| **ধাপে ধাপে ব্যাখ্যা** (Step by step)  | Line-by-line trace of what the program does                              |
| **ছবিতে দেখো** (See it)                | Bit rows, sieve grids, graph drawings, DP tables                         |
| **সাবধান ও টিপস** (Pitfalls and tips)  | The mistakes everyone makes — overflow, operator priority, off-by-one    |

> **Nothing is guessed.** Each example's output shown on the site is produced by compiling and running the code with `g++ -std=c++17` during the build of the content, so what the learner reads is exactly what the program prints.

---

## 2. Features

- **Real, verified output** — every one of the 200 examples is compiled and executed by the content pipeline; compile failures and empty outputs are reported.
- **Step-by-step explanations** — bits, number theory, recursion and graph lessons break each program into numbered steps with a "সারকথা" (summary) box.
- **Rich visualisations** (all rendered as React components, no images):
  - Bit rows with highlighted columns and place-value weights
  - Sieve of Eratosthenes grid
  - Node/edge graph drawings with state colours (current, visited, queued, skipped, chosen edge)
  - 2-D matrix / grid / DP table views
  - Trace tables for loops, recursion and algorithm state
- **Interactive widgets** — a **Bit Playground** (`& | ^ << >> ~` on live numbers, click-to-toggle bits), an animated **Sieve**, an animated **BFS / DFS** and a **binary counter**.
- **One-click copy** on every code block with C++ syntax highlighting (`prism-react-renderer`, VS Dark theme).
- **Fira Code** with ligatures for code and **Hind Siliguri** for Bangla text, both bundled locally.
- **Installable & offline** — a full PWA with a service worker, manifest, maskable icons and home-screen shortcuts.
- **Deep links** — every lesson and every track has a shareable URL.
- **Responsive** — sticky sidebar table of contents on desktop, collapsible one on mobile, hamburger navigation below `xl`.
- **Print-friendly** — A4 landscape print stylesheet that hides navigation chrome.
- **Reduced-motion aware** — animations switch off for users who ask for it.

---

## 3. Curriculum

| Track                                | ID      | Lessons | Examples | Topics                                                                                                                                                                                                 |
| ------------------------------------ | ------- | ------: | -------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **STL**                              | `stl`   |      83 |      101 | `vector`, `stack`, `queue`, `deque`, `priority_queue`, `set`, `multiset`, `list`, `map`, `pair`, `string`, `algorithm`, `bitset`, `unordered_map/set` — one page per function                          |
| **বিটের মজা** (Bit tricks)           | `bits`  |      11 |       14 | AND / OR / XOR / NOT, shifts, odd-even, power-of-two check, check/set/clear/toggle a bit, `__builtin_popcount`, subset generation                                                                      |
| **নাম্বার থিওরি** (Number theory)    | `nt`    |      27 |       36 | Primes, divisors and the harmonic series, Sieve (plain, bitset, query), prime factorisation, GCD / LCM, NOD, SOD, SNOD, modular arithmetic, fast exponentiation, modular inverse, nCr, Euler's totient |
| **রিকার্সন ও DP** (Recursion and DP) | `rec`   |       3 |        9 | Recursion and base cases, call tree, memoisation (top-down), bottom-up DP, `memset`, `int` vs `long long` limits                                                                                       |
| **গ্রাফ থিওরি** (Graph theory)       | `graph` |      20 |       40 | Adjacency matrix / list (weighted), BFS (levels, paths, grid), DFS (3 colours, back edge, grid), connected components, cycle detection, bipartite check, Dijkstra, DSU, Kruskal, Prim                  |
| **Total**                            |         | **144** |  **200** |                                                                                                                                                                                                        |

The graph track also links to a curated reading list (Shafayet's graph-theory blog series) hosted in the original [`CPP-for-CP`](https://github.com/Hafiz-Sakib/CPP-for-CP/tree/main/CP/L2) repository.

---

## 4. Tech Stack

| Layer               | Technology                                                                       | Version   |
| ------------------- | -------------------------------------------------------------------------------- | --------- |
| UI library          | [React](https://react.dev)                                                       | `^18.3.1` |
| Build tool          | [Vite](https://vitejs.dev) with `@vitejs/plugin-react`                           | `^5.4.0`  |
| Styling             | [Tailwind CSS](https://tailwindcss.com) + PostCSS + Autoprefixer                 | `^3.4.4`  |
| PWA                 | [`vite-plugin-pwa`](https://vite-pwa-org.netlify.app) (Workbox `generateSW`)     | `^0.20.5` |
| Syntax highlighting | [`prism-react-renderer`](https://github.com/FormidableLabs/prism-react-renderer) | `^2.3.1`  |
| Bangla font         | [`@fontsource/hind-siliguri`](https://fontsource.org/fonts/hind-siliguri)        | `^5.0.0`  |
| Code font           | Fira Code (self-hosted `.woff2`, weights 300–700)                                | —         |
| Content pipeline    | Python 3 + `g++` (C++17)                                                         | —         |

There is **no backend, no router library and no state-management library**. The whole site is a static bundle; all lesson data ships as one JSON file.

---

## 5. Project Structure

```bash
cp-pathshala-bangla/
├── README.md                      # ← you are here
└── site/                          # the entire application lives here
    ├── index.html                 # HTML shell (lang="bn", PWA/iOS meta tags, theme colour)
    ├── package.json               # scripts + dependencies (v1.2.0)
    ├── package-lock.json
    ├── vite.config.js             # Vite + React + VitePWA (manifest, workbox, shortcuts)
    ├── tailwind.config.js         # fonts, brand colours, custom keyframes/animations
    ├── postcss.config.js          # tailwindcss + autoprefixer
    ├── README.md                  # short Bangla quick-start for the content workflow
    │
    ├── public/                    # copied as-is to the site root (PWA icons)
    │   ├── icon.svg               # master vector logo (also the favicon)
    │   ├── icon-192.png
    │   ├── icon-512.png
    │   ├── icon-maskable-192.png  # Android adaptive icon (safe-zone padded)
    │   ├── icon-maskable-512.png
    │   ├── apple-touch-icon.png   # iOS home-screen icon
    │   └── favicon-32.png
    │
    ├── src/                       # React front-end
    │   ├── main.jsx               # entry: fonts, CSS, service-worker registration, <App/>
    │   ├── App.jsx                # tiny URL-driven router (home / track index / lesson)
    │   ├── index.css              # @font-face, Tailwind layers, print + reduced-motion rules
    │   │
    │   ├── data/
    │   │   ├── index.js           # track metadata + helpers (groupPages, categories, bn …)
    │   │   └── pages.json         # ⚙ GENERATED — all 144 lessons (~470 KB). Do not edit by hand
    │   │
    │   ├── fonts/                 # Fira Code (Light/Regular/Medium/SemiBold/Bold .woff2)
    │   │
    │   └── components/
    │       ├── Navbar.jsx         # sticky top bar, desktop pill menu + mobile dropdown
    │       ├── Footer.jsx         # credits and repository links
    │       ├── Home.jsx           # landing page: hero, features, roadmap, popular lessons
    │       ├── GroupIndex.jsx     # per-track index grouped by category
    │       ├── LessonPage.jsx     # the lesson template (TOC, examples, steps, tips, prev/next)
    │       │
    │       ├── CodeBlock.jsx      # highlighted C++ with copy button
    │       ├── Steps.jsx          # numbered vertical step list
    │       ├── Rich.jsx           # tiny inline markup: `code` and **bold**
    │       ├── TraceTable.jsx     # truth tables / loop & recursion trace tables
    │       ├── BitViz.jsx         # visual dispatcher: bits | graph | mat | grid
    │       ├── GraphViz.jsx       # <GraphFig> (SVG graph) and <MatFig> (2-D grid)
    │       ├── Icons.jsx          # inline SVG icon set
    │       ├── Colors.js          # colour-theme map used by tracks/categories
    │       │
    │       ├── BitPlayground.jsx  # interactive bit-operator sandbox (home page)
    │       ├── HeroBitDemo.jsx    # animated bit demo in the hero
    │       ├── BinaryCounter.jsx  # animated binary counter
    │       ├── SieveAnim.jsx      # animated Sieve of Eratosthenes
    │       ├── BfsDfsAnim.jsx     # animated BFS vs DFS traversal
    │       ├── TipTerminal.jsx    # typing "contest tip" terminal in the hero
    │       ├── Reveal.jsx         # scroll-reveal wrapper + reduced-motion helper
    │       └── CountUp.jsx        # animated number counter
    │
    └── gen/                       # Python content pipeline (source of truth for lessons)
        ├── build.py               # ★ entry point: compile → enrich → validate → write JSON
        ├── lib.py                 # P() / E() builders and the g++ runner (run_all)
        ├── enrich_lib.py          # EN() / X() / VB() / T() / GV() / MV() … enrichment helpers
        ├── sims.py                # BFS / DFS / Dijkstra / Kruskal / Prim step simulators
        │
        ├── p_stl1.py              # ┐
        ├── p_stl2.py              # ├ STL lessons (code + short explanation)
        ├── p_stl3.py              # ┘
        ├── p_bits.py              # bit-manipulation lessons
        ├── p_nt.py                # number-theory lessons
        ├── p_rec.py               # recursion and DP lessons
        ├── p_graph.py             # graph-theory lessons
        │
        ├── e_bits.py              # ┐
        ├── e_nt1.py               # │
        ├── e_nt2.py               # ├ enrichment: intro, steps, visuals, tables, tips
        ├── e_rec.py               # │
        ├── e_graph1.py            # │
        └── e_graph2.py            # ┘
```

> **Naming convention in `gen/`:** `p_*.py` = **P**age definitions (code + syntax + complexity), `e_*.py` = **E**nrichment for those pages (intro, step-by-step, visuals, tables, tips). STL pages have no `e_*.py` file; when an example's explanation has three or more sentences, `LessonPage.jsx` automatically splits it into numbered steps.

Generated at install/build time and **not** part of the source tree: `site/node_modules/`, `site/dist/`, `site/gen/__pycache__/`.

---

## 6. Getting Started

### Prerequisites

| Tool                                 | Needed for                  | Notes                    |
| ------------------------------------ | --------------------------- | ------------------------ |
| **Node.js ≥ 18** (22 tested) and npm | Running / building the site | Required                 |
| **Python 3** and **`g++`** (C++17)   | Regenerating `pages.json`   | Only if you edit lessons |

### Install and run

```bash
# 1. Go to the application folder
cd cp-pathshala-bangla/site

# 2. Install dependencies
npm install

# 3. Start the dev server (hot reload)
npm run dev
```

Vite prints a local URL (usually `http://localhost:5173`). Open it and you have the full site — the lesson data is already pre-generated in `src/data/pages.json`, so **Python is not needed just to run the site**.

### Production build

```bash
npm run build      # outputs to site/dist/
npm run preview    # serve the production build locally to test the PWA
```

A successful build ends with the PWA plugin reporting `generateSW` and the number of precached files (36 entries, ≈ 1.4 MB at the time of writing). Vite will print a _"chunks larger than 500 kB"_ warning — this is expected: all lesson data and the app live in one chunk so the site works fully offline after the first visit.

---

## 7. Available Scripts

Run these inside `site/`.

| Command                      | What it does                                                                |
| ---------------------------- | --------------------------------------------------------------------------- |
| `npm run dev`                | Start the Vite development server with hot module replacement               |
| `npm run build`              | Create an optimised production bundle + service worker in `dist/`           |
| `npm run preview`            | Serve `dist/` locally (use this to test install / offline behaviour)        |
| `cd gen && python3 build.py` | Regenerate `src/data/pages.json` from the Python lesson sources (see below) |

---

## 8. How the Content Pipeline Works

Lessons are **not** hand-written in JSON. They are authored in small Python files and compiled into `pages.json` by `gen/build.py`.

```text
 p_*.py  ──►  lib.pages  ──►  run_all()  ──►  merge()  ──►  validate  ──►  src/data/pages.json
 (P / E)     (code, syntax)   g++ compile      e_*.py        column /        consumed by the
                              + run each       (EN / X)      enrichment      React app
                              example                        checks
```

1. **Define pages** — importing each `p_*.py` calls `P(...)` which appends a page (with its `E(...)` examples) to `lib.pages`.
2. **Compile and run** — `lib.run_all()` writes each example to a temp `.cpp`, compiles it with `g++ -std=c++17 -O1`, runs it with the example's `input` (10-second timeout) and stores the **real stdout** as `output`.
3. **Merge enrichment** — importing each `e_*.py` registers `EN(...)` entries in a dictionary; `enrich_lib.merge()` attaches `intro`, `uses`, `tips`, `truth`, and per-example `steps / viz / tables` to the matching page by `id`.
4. **Validate** — `build.py` aborts (non-zero exit) if:
   - a `bits`, `nt`, `rec` or `graph` page has **no enrichment**;
   - an enrichment has a **different number of examples** than its page;
   - an enrichment references an **unknown page id**;
   - a table row has a **different column count** from its header;
   - bit rows in one visual have **different widths**.
5. **Write** — the result is dumped (UTF-8, `ensure_ascii=False`) to `../src/data/pages.json`.

The script also prints the total page count and any `EMPTY/ERR` examples (empty output or compile error) so you can fix them.

> ⚠️ Run `build.py` **from inside `gen/`** — the output path `../src/data/pages.json` is relative.

---

## 9. Adding or Editing Lessons

### 9.1 Add a new lesson page

Open the right `gen/p_*.py` file and add a `P(...)` call:

```python
from lib import *

P("bits",                      # track id: stl | bits | nt | rec | graph
  "বিটের মজা",                  # category (groups pages in the sidebar)
  "bit-flip-all",              # unique page id (also used in the URL ?p=…)
  "সব বিট উল্টানো",              # page title
  "XOR দিয়ে সব বিট একসাথে উল্টানো যায়।",   # short description (supports `code` and **bold**)
  "x ^ mask",                  # syntax block
  "O(1)",                      # time complexity
  E("৮ বিটের সব ঘর উল্টাও",       # example title
    "int x = 5, mask = 255;\ncout << (x ^ mask);",   # code *inside* main()
    "5 = 00000101, mask = 11111111, XOR করলে 11111010 = 250।",  # explanation
    ""))                       # stdin (optional)
```

`E()` automatically wraps your snippet with `#include <bits/stdc++.h>`, `using namespace std;`, `int main() { … return 0; }`. Pass `pre="…"` to inject global code (helper functions, arrays, structs) before `main`.

### 9.2 Add the step-by-step enrichment

For `bits`, `nt`, `rec` and `graph` pages an enrichment is **mandatory**. In the matching `gen/e_*.py`:

```python
from enrich_lib import *

EN("bit-flip-all",
   "XOR হলো ‘আলাদা কিনা?’ গেট … **bold** আর `code` ব্যবহার করা যায়।",   # intro
   "সব বিট উল্টানো • mask এর সাথে কাজ",                                  # uses, separated by •
   ["টিপস ১", "টিপস ২"],                                                   # tips / pitfalls
   X(["ধাপ ১ …", "ধাপ ২ …", "ধাপ ৩ …"],                                    # one X(...) per example
     viz=[VB("প্রতিটা ঘর উল্টে গেলো",
             RB("x", 5, tone="a"),
             RB("mask", 255, tone="b"),
             RB("x ^ mask", 250, tone="r", sep=True))]),
   truth=T(["a", "b", "a ^ b"], [[0,0,0],[0,1,1],[1,0,1],[1,1,0]], "XOR truth table"))
```

### 9.3 Helper cheat-sheet (`enrich_lib.py`)

| Helper                                      | Purpose                                                                                                            |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `EN(id, intro, uses, tips, *X, truth=None)` | Register enrichment for a page; one `X(...)` **per example**, in order                                             |
| `X(steps, viz=None, tables=None)`           | Steps (list of strings) + optional visuals + optional trace tables for one example                                 |
| `RB(label, n, w=8, tone, hl, dec, sep)`     | A bit row from an integer (two's complement for negatives). `tone`: `a` blue, `b` violet, `r` green, `n` slate     |
| `R(label, bits, …)`                         | A bit row from an explicit string such as `"00001100"`                                                             |
| `hlv(w, *values)`                           | Convert place-values (e.g. `8, 4`) into column indexes to highlight                                                |
| `VB(caption, *rows)`                        | A bit-row visual group                                                                                             |
| `VG(caption, cells)`                        | A grid of `(text, state)` cells — states `p` prime/ok, `x` crossed, `n` normal, `h` highlight (used for the Sieve) |
| `T(cols, rows, caption, hl)`                | A table (truth table, trace table, DP table)                                                                       |
| `GV(caption, nodes, edges, …)`              | A graph drawing — nodes `(id, x, y, state, label, sub)`, edges `(a, b, state, weight, directed)`                   |
| `MV(caption, rows, cols, rowLabels)`        | A 2-D matrix / grid / DP-table drawing                                                                             |
| `g1(caption, st, sub, es, …)`               | Pre-built sample graph **G1** (6 nodes, 7 edges) reused across graph lessons                                       |

**Graph node states:** `n` normal · `a` current · `v` visited · `q` queued · `x` removed · `r` second colour
**Graph edge states:** `n` normal · `t` taken · `x` skipped · `a` current

`gen/sims.py` provides ready-made simulators — `bfs_trace`, `dfs_trace`, `dijkstra`, `kruskal`, `prim` — so the trace tables in lessons are **computed**, then cross-checked against the real program output, instead of typed by hand.

### 9.4 Rebuild and ship

```bash
cd site/gen
python3 build.py          # regenerates ../src/data/pages.json

cd ..
npm run dev               # preview your lesson
npm run build             # production bundle
```

### 9.5 Add a brand-new track

1. Add a new `{ id, label, color, icon, blurb, about, learn: [...] }` object to `tabs` in `src/data/index.js`.
2. Add a matching `{ id, label, Icon }` item in `Navbar.jsx` and (if you want a new icon) in `Icons.jsx` + the `TabIcon` map in `Home.jsx`.
3. Add a `shortcuts` entry in `vite.config.js` if you want a home-screen shortcut.
4. Create `gen/p_<track>.py` / `gen/e_<track>.py`, import them in `build.py`, and — if the track should be enriched — add its id to the `("bits", "nt", "rec", "graph")` check in `build.py`.

---

## 10. Data Model (`pages.json`)

`src/data/pages.json` is a flat array of page objects, ordered the way the learner should read them (the lesson footer's **← previous / next →** buttons simply follow this order).

```jsonc
{
  "grp": "stl",                    // track id
  "cat": "vector",                 // category inside the track
  "id": "vector-push_back",        // unique id → URL: /?p=vector-push_back
  "title": "vector.push_back()",
  "desc": "…",                     // short summary (inline markup allowed)
  "syntax": "v.push_back(value);",
  "time": "O(1) (গড়ে)",
  "examples": [
    {
      "title": "একটা একটা করে ঢোকানো",
      "code": "#include <bits/stdc++.h>\n…",
      "input": "",                 // stdin given to the program
      "output": "1 2 3",           // REAL stdout captured from g++
      "explain": "…",              // summary (or auto-split into steps for STL)

      // ── only on enriched pages ───────────────────────────
      "steps":  ["…", "…"],        // numbered walkthrough
      "viz":    [ { "kind": "bits | grid | graph | mat", … } ],
      "tables": [ { "caption": "…", "cols": […], "rows": [[…]], "hl": […] } ]
    }
  ],

  // ── only on enriched pages ─────────────────────────────
  "intro": "…",                    // "সহজ কথায় ধারণা"
  "uses":  "a • b • c",            // chips, split on •
  "tips":  ["…"],                  // "সাবধান ও টিপস"
  "truth": { "caption": "…", "cols": […], "rows": […] }   // optional truth table
}
```

**Inline markup** (`Rich.jsx`) is deliberately tiny: `` `code` `` → monospace chip, `**bold**` → emphasised text. Nothing else is parsed, so content cannot inject HTML.

---

## 11. Application Architecture

```text
index.html
   └─ main.jsx ── registers service worker, loads fonts + index.css
        └─ <App/>  ── reads ?p= / ?tab= from the URL, owns { tab, pid } state
             ├─ <Navbar/>        tab switching
             ├─ <main>
             │    ├─ pid set      → <LessonPage/>   one lesson
             │    ├─ tab is track → <GroupIndex/>   list of lessons in the track
             │    └─ otherwise    → <Home/>         landing page
             └─ <Footer/>
```

- **State** is a single `{ tab, pid }` object in `App.jsx`. There is no router dependency.
- **Navigation** calls `history.pushState`, and a `popstate` listener keeps the back/forward buttons working. The scroll position resets on every change.
- **Data helpers** in `src/data/index.js`:

| Export            | Meaning                                                                                       |
| ----------------- | --------------------------------------------------------------------------------------------- |
| `tabs`            | Track metadata (id, label, colour, icon, blurb, “what you will learn”, optional reading list) |
| `pages`           | The array from `pages.json`                                                                   |
| `index`           | `{ pageId → array index }` for O(1) lookup and prev/next                                      |
| `groupPages(g)`   | All pages of a track                                                                          |
| `categories(g)`   | Pages of a track grouped by category, each with an assigned colour                            |
| `exampleCount(g)` | Number of examples in a track                                                                 |
| `colorOf(page)`   | Colour theme of a page's category                                                             |
| `bn(n)`           | Converts digits to Bangla numerals (`12` → `১২`)                                              |

- **Visual dispatch:** `BitViz.jsx`'s `BitGroup` looks at `viz.kind` and renders either bit rows, a Sieve grid, an SVG graph (`GraphFig`) or a 2-D matrix (`MatFig`). New visual kinds are added in that one place.

---

## 12. Components Reference

| Component                                                    | Role                                                                                                                                |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
| `LessonPage`                                                 | Page template — hero header, sidebar/mobile TOC, description, concept box, truth table, syntax, per-example blocks, tips, prev/next |
| `GroupIndex`                                                 | Track landing page listing lessons by category                                                                                      |
| `Home`                                                       | Landing page with hero, feature grid, learning roadmap, interactive demos and “popular lessons”                                     |
| `CodeBlock`                                                  | VS-Dark highlighted C++ with line numbers and a copy-to-clipboard button                                                            |
| `Steps`                                                      | Vertical numbered timeline of explanation steps                                                                                     |
| `TraceTable`                                                 | Highlightable table for truth tables and execution traces                                                                           |
| `BitViz` (`BitRow`, `Weights`, `BitGroup`)                   | Bit rows with place-value weights and highlighted columns; also the dispatcher for other visual kinds                               |
| `GraphViz` (`GraphFig`, `MatFig`)                            | SVG graph drawing and 2-D cell grids                                                                                                |
| `BitPlayground`                                              | Pick two numbers and an operator; click bits to toggle; see the result and an explanation                                           |
| `SieveAnim` / `BfsDfsAnim` / `BinaryCounter` / `HeroBitDemo` | Small self-running animations on the home page                                                                                      |
| `TipTerminal`                                                | Terminal-style typing animation cycling through contest tips                                                                        |
| `Reveal` / `CountUp`                                         | Scroll-triggered reveal and number count-up; both respect `prefers-reduced-motion`                                                  |
| `Rich`                                                       | Safe inline `code` / `**bold**` renderer                                                                                            |
| `Navbar` / `Footer`                                          | Global chrome (Esc and outside-click close the mobile menu)                                                                         |

---

## 13. Routing and Deep Links

The site uses **query-string routing**, so it works on any static host without server-side rewrite rules.

| URL             | Opens                                                                                  |
| --------------- | -------------------------------------------------------------------------------------- |
| `/`             | Home                                                                                   |
| `/?tab=stl`     | STL track index                                                                        |
| `/?tab=bits`    | Bit tricks track index                                                                 |
| `/?tab=nt`      | Number theory track index                                                              |
| `/?tab=rec`     | Recursion and DP track index                                                           |
| `/?tab=graph`   | Graph theory track index                                                               |
| `/?p=<page-id>` | A specific lesson, e.g. `/?p=vector-push_back`, `/?p=graph-bfs`, `/?p=nt-sieve-bitset` |

An unknown `tab` falls back to Home; an unknown `p` is ignored.

---

## 14. PWA, Offline Support and Icons

Configured in `site/vite.config.js` through `vite-plugin-pwa`:

- **`registerType: "autoUpdate"`** — a new deployment is picked up automatically; `main.jsx` calls `registerSW({ immediate: true })`.
- **Workbox precache** — `**/*.{js,css,html,svg,png,woff2,json}`, with the per-file cap raised to 5 MB to fit the lesson bundle.
- **Manifest** — Bangla name (`কম্পিটিটিভ প্রোগ্রামিং পাঠশালা`), short name (`সিপি পাঠশালা`), `lang: "bn"`, `display: "standalone"`, theme/background colour `#0a3631`, categories `education` and `books`.
- **Shortcuts** (long-press the installed app icon): STL · বিটের মজা · নাম্বার থিওরি · রিকার্সন ও DP · গ্রাফ থিওরি.
- **Icons** in `public/`:

| File                                             | Use                                      |
| ------------------------------------------------ | ---------------------------------------- |
| `icon.svg`                                       | Master logo, favicon, “any” purpose icon |
| `icon-192.png`, `icon-512.png`                   | Standard install icons                   |
| `icon-maskable-192.png`, `icon-maskable-512.png` | Android adaptive (maskable) icons        |
| `apple-touch-icon.png`                           | iOS home-screen icon                     |
| `favicon-32.png`                                 | Classic browser tab icon                 |

> The manifest uses `scope: "/"` and `start_url: "/"`, so the app must be served from the **root of a domain** (or sub-domain). To host under a sub-path, set Vite's `base` and update `scope` / `start_url` / `id` in the manifest.

To test installation and offline mode, use `npm run build && npm run preview`, open the preview URL, then toggle "Offline" in the browser dev-tools. The service worker does not run in `npm run dev`.

---

## 15. Design System

| Token         | Value                                  | Usage                                                                  |
| ------------- | -------------------------------------- | ---------------------------------------------------------------------- |
| `brand.ink`   | `#0a3631`                              | Deep green — headers, hero, headings, PWA theme colour                 |
| `brand.green` | `#00694d`                              | Primary actions, active states, focus ring                             |
| `brand.red`   | `#c8283a`                              | Accent borders, "summary" and warning highlights                       |
| Track colours | emerald · amber · blue · purple · rose | One colour per track; categories cycle emerald → amber → blue → purple |

- **Typography** — body in _Hind Siliguri_ (400–700), code in _Fira Code_ with contextual ligatures; generous base size (100 % → 103 % on `sm+`) and `line-height: 1.75` for comfortable Bangla reading.
- **Motion** — `fade-up`, `fade-in`, `slide-down`, `pop-in` keyframes in `tailwind.config.js`, plus marquee/float helpers in `index.css`.
- **Motifs** — dotted hero background and a dashed "road" divider, a nod to the _road to contests_.
- **Bit-row tones** — blue (`a`), violet (`b`), green (`r` = result), slate (neutral); an amber ring marks the highlighted column.

---

## 16. Accessibility and Print

- Semantic landmarks: `<header>`, `<nav aria-label>`, `<main>`, `<article>`, `<footer>`.
- `aria-current="page"` on active navigation / TOC items, `aria-expanded` and `aria-controls` on menu toggles, `aria-label`s on icon-only buttons (copy, bit toggles).
- Visible `:focus-visible` outline (`#00694d`).
- `prefers-reduced-motion: reduce` disables all animations and smooth scrolling.
- `lang="bn"` on the document root.
- Print stylesheet: **A4 landscape**, 10 mm margins, navigation and buttons hidden (`.no-print`), colours preserved — a lesson can be saved as a clean PDF straight from the browser.

---

## 17. Build and Deployment

The output of `npm run build` is a fully **static** site in `site/dist/`, so it can be hosted anywhere:

| Host                                    | Setup                                                                                                                    |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Netlify / Vercel / Cloudflare Pages** | Base directory `site`, build command `npm run build`, publish directory `dist`                                           |
| **GitHub Pages**                        | Build locally or in CI, publish `site/dist`; use a custom domain or a root `user.github.io` site (manifest scope is `/`) |
| **Any static server / Nginx**           | Copy the contents of `dist/` to the web root                                                                             |

Checklist before releasing:

- [ ] `cd site/gen && python3 build.py` finishes without `COMPILE FAIL`, `EMPTY/ERR` or validation errors (only if lessons changed)
- [ ] `npm run build` succeeds
- [ ] `npm run preview` — lessons load, deep links work, app installs, offline mode works
- [ ] Bump `version` in `package.json`

---

## 18. Troubleshooting

| Problem                                      | Likely cause and fix                                                                                                    |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `python3 build.py` → `COMPILE FAIL <id> <n>` | The C++ in that example does not compile. Fix the snippet in the `p_*.py` file; the error excerpt is printed            |
| `SystemExit: [('NOT ENRICHED', '<id>')]`     | A `bits` / `nt` / `rec` / `graph` page has no `EN(...)`. Add one in the matching `e_*.py`                               |
| `EXAMPLE COUNT MISMATCH`                     | The number of `X(...)` blocks in `EN(...)` differs from the number of `E(...)` examples on the page                     |
| `UNKNOWN IDS`                                | An `EN("…")` uses an id that no `P(...)` defines (typo?)                                                                |
| `COL MISMATCH`                               | A row in `T(...)` has more/fewer cells than there are columns                                                           |
| `g++: command not found`                     | Install a C++ compiler (`sudo apt install g++`, `xcode-select --install`, or MinGW/WSL on Windows)                      |
| `FileNotFoundError: ../src/data/pages.json`  | You ran `build.py` from the wrong folder — `cd site/gen` first                                                          |
| Blank page after deploy under a sub-path     | App assumes domain root; set Vite `base` and the manifest `scope`/`start_url`                                           |
| Old content after redeploy                   | The service worker is serving a cached copy; reload twice, or _Application → Service Workers → Unregister_ in dev-tools |
| Offline mode does not work in `npm run dev`  | Expected — the service worker is only built for production; use `npm run preview`                                       |

---

## 19. Contributing

Contributions that make CP easier for Bangla readers are very welcome.

1. Fork the repository and create a branch: `git checkout -b feat/new-lesson`.
2. Edit lessons in `site/gen/` (**not** `pages.json` directly) and run `python3 build.py`.
3. Verify with `npm run build` and look through the lesson in `npm run dev`.
4. Open a pull request describing the lesson or fix.

**Content style guide**

- Explain in simple, conversational Bangla; keep technical terms (`vector`, `queue`, `overflow`) in English.
- Every example should be small, runnable, and printed output should demonstrate the idea.
- Prefer _what happens at each step_ over theory; add a visual or table wherever values change over time.
- Put real contest pitfalls (overflow, off-by-one, operator priority, TLE) in **সাবধান ও টিপস**.

Suggested `.gitignore` for the repository (none ships in the archive):

```gitignore
node_modules/
dist/
__pycache__/
*.pyc
.DS_Store
```

---

## 20. Author and Credits

**Mohammad Hafizur Rahman Sakib** — [@Hafiz-Sakib](https://github.com/Hafiz-Sakib)

- All code samples and notes originate from the [**CPP-for-CP**](https://github.com/Hafiz-Sakib/CPP-for-CP) repository.
- The graph-theory reading list references Shafayet's Bangla blog series (PDFs kept in [`CP/L2`](https://github.com/Hafiz-Sakib/CPP-for-CP/tree/main/CP/L2) of that repository).
- Built with [React](https://react.dev), [Vite](https://vitejs.dev), [Tailwind CSS](https://tailwindcss.com), [vite-plugin-pwa](https://vite-pwa-org.netlify.app), [prism-react-renderer](https://github.com/FormidableLabs/prism-react-renderer), [Hind Siliguri](https://fontsource.org/fonts/hind-siliguri) and [Fira Code](https://github.com/tonsky/FiraCode).

<div align="center">

**Made with ❤️ for every Bangla-speaking beginner who wants to start competitive programming.**

_Happy coding — আর ভুল করেই শেখো!_

</div>
