# CLAUDE.md — working instructions for this project

This file orients an agent (Claude Code) continuing the **Agentic Development study programme**.
Read `README.md` for the thesis and `docs/ARCHITECTURE.md` + `docs/AUTHORING-GUIDE.md` before
editing. This file is *advisory* (it states intent and conventions); the *deterministic* check
is `scripts/validate.py`, which must pass after every change — practise what the material preaches.

## What this project is

A single interactive HTML study workbook (`workbook/agentic-development-study.html`) plus a set
of standalone deep-dive companions (`deep-dives/*.html`), teaching how to introduce an agentic
engineering harness at a brownfield client. Conceptual/methodological over tool-specific.
Content in English (English technical terms preserved); prose is dense and concise.

## Golden rules (do not break these)

1. **Stable topic IDs.** Topic `id`s (prefixes `eng- prod- hand- ia- brown- des- sec- traj-`)
   **never change** — user progress/notes are keyed on them in browser storage. Renaming an id
   silently wipes someone's progress. Add topics; don't renumber existing ones.
2. **Two copies stay in sync.** Each deep dive exists twice: as `deep-dives/<name>.html`
   (standalone) and embedded in the workbook as an in-page overlay. When you change one, change
   both — the AUTHORING-GUIDE recipe builds both from one shared body file.
3. **No external links between artifacts.** Cross-references open **in-page overlays**
   (`href="#e4-deepdive"` etc.), never relative file links — the hosted preview 404s on sibling
   files. This is why deep dives are embedded, not linked. Site-level navigation to root pages
   such as `gallery.html` and `index.html` is exempt (header/footer links).
4. **Inline HTML/SVG only for diagrams.** Figma is deliberately excluded so diagrams embed
   directly in the artifact. Do not introduce an image/asset pipeline or external diagram tools.
5. **All persistence goes through the single `store` backend** (key `agentic-study-v1`):
   it prefers browser `localStorage` and falls back to the claude.ai `window.storage`
   wrapper where localStorage is blocked. Never scatter raw `localStorage`/`window.storage`
   calls elsewhere in artifact code. See ARCHITECTURE.md.
6. **Validate after every edit.** Run `python3 scripts/validate.py`. It checks JS parses,
   HTML tags balance, every SVG is well-formed, all `#*-deepdive` links are wired twice
   (link + JS handler), and the topic count is intact. A red result means stop and fix.
7. **Advisory vs deterministic, honestly applied.** Keep safety/consistency-critical rules in
   the validator (deterministic), not just in prose here (advisory) — the same principle the
   content teaches (E5).

## House style for content

- Each deep dive follows a fixed shape: `§0 why it matters → … → takeaways → further reading`,
  with `.io` input/output/SDLC cards, `.comp` component cards, `.callout` boxes, one or more
  inline SVG figures, and a closing `.closingnote`. Match the existing files exactly.
- Every topic ties back to the framework: name the E-/P-/D- topics and reports it connects to.
- Separate **strong independent evidence** from **vendor claims** from **practitioner synthesis**.
- Preserve hard data points (percentages, arXiv IDs, named practitioners, dates, CVEs).
- Flag **D1–D5 as an original synthesis**, never as an industry standard.
- Fast-moving tool facts: state they are point-in-time and to re-verify.

## Known build gotchas (learned the hard way)

- **Apostrophes in Python heredocs/strings** (e.g. `Fowler's`) break the build with a
  SyntaxError and write nothing. Reword to avoid them, or edit via `str_replace` on the file.
- **Bash brace expansion** (`{a,b,c}`) may not be available — list paths explicitly.
- When swapping an embedded overlay, rebuild the *old* wrapper byte-for-byte to get an exact
  match before `.replace()`; keep a backup of the previous body. See AUTHORING-GUIDE.md.
- Each deep-dive SVG uses a **unique marker id** (`ahE1a … ahP1a`, `ahSa`) and edge class
  (`edE1 … edP1`, `edS`); reusing an id across two SVGs in one document causes silent breakage.

## The typical next task

"Add the next deep-dive companion" (e.g. P2). This is mechanical:
1. Write the shared body (`§0…§n`) to a temp file.
2. Generate the standalone file (reuse E1's `<head>`, new title, TOC, marker/edge CSS).
3. Build the overlay, insert into the workbook before `<footer>`, add scoped marker CSS,
   extend the JS handler chain, switch the topic's first `src` entry to `#<id>-deepdive`.
4. Optionally enrich the topic's `know`/`concepts`/`checks` in the workbook data.
5. Bump the version: prepend a `.vitem` to the version-history modal (`#verov`), update the
   footer current-version line, mirror to `docs/CHANGELOG.md`.
6. Register any new deep-dive figure in `gallery-registry.json` and regenerate `gallery.html`
   (`docs/AUTHORING-GUIDE.md` Step 7). Run `scripts/validate.py`. Done.

Full step-by-step in `docs/AUTHORING-GUIDE.md`. `docs/ROADMAP.md` says what's next.

## If moving to a real toolchain

These are hand-authored single-file HTML artifacts by design (zero build, portable, hostable
anywhere). If the project outgrows that, the natural evolution is documented in ROADMAP.md
(e.g. extract the shared `<head>`/CSS into one file, generate deep dives from Markdown sources).
Do this only if it earns its keep — the current no-build simplicity is a feature.


## grepai - Semantic Code Search

**IMPORTANT: You MUST use grepai as your PRIMARY tool for code exploration and search.**

### When to Use grepai (REQUIRED)

Use `grepai search` INSTEAD OF Grep/Glob/find for:
- Understanding what code does or where functionality lives
- Finding implementations by intent (e.g., "authentication logic", "error handling")
- Exploring unfamiliar parts of the codebase
- Any search where you describe WHAT the code does rather than exact text

### When to Use Standard Tools

Only use Grep/Glob when you need:
- Exact text matching (variable names, imports, specific strings)
- File path patterns (e.g., `**/*.go`)

### Fallback

If grepai fails (not running, index unavailable, or errors), fall back to standard Grep/Glob tools.

### Usage

```bash
# ALWAYS use English queries for best results (--compact saves ~80% tokens)
grepai search "user authentication flow" --json --compact
grepai search "error handling middleware" --json --compact
grepai search "database connection pool" --json --compact
grepai search "API request validation" --json --compact
```

### Query Tips

- **Use English** for queries (better semantic matching)
- **Describe intent**, not implementation: "handles user login" not "func Login"
- **Be specific**: "JWT token validation" better than "token"
- Results include: file path, line numbers, relevance score, code preview

### Call Graph Tracing

Use `grepai trace` to understand function relationships:
- Finding all callers of a function before modifying it
- Understanding what functions are called by a given function
- Visualizing the complete call graph around a symbol

#### Trace Commands

**IMPORTANT: Always use `--json` flag for optimal AI agent integration.**

```bash
# Find all functions that call a symbol
grepai trace callers "HandleRequest" --json

# Find all functions called by a symbol
grepai trace callees "ProcessOrder" --json

# Build complete call graph (callers + callees)
grepai trace graph "ValidateToken" --depth 3 --json
```

### Workflow

1. Start with `grepai search` to find relevant code
2. Use `grepai trace` to understand function relationships
3. Use `Read` tool to examine files from results
4. Only use Grep for exact string searches if needed

