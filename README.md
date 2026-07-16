# Agentic Development — Study Programme & Consulting Materials

An interactive study workbook and a growing set of deep-dive companions for introducing
**agentic software development** (an agentic engineering harness) at a client with an
existing (brownfield) codebase of unknown stack.

Prepared by Roman (senior software architect, Sudolabs) as the learning + reference base
for a potential client engagement. Working language of the *content* is English (established
English technical terms preserved); working notes and commit messages may be in Slovak.

**Live version:** [selmeci.github.io/agentic-sdlc-learning](https://selmeci.github.io/agentic-sdlc-learning/workbook/agentic-development-study.html)

---

## The core thesis we are developing

> **Agents assist; humans retain judgment.** An agent is a *model wrapped in a harness*
> (`Agent = Model + Harness`). The model is a commodity you rent; the **harness** — the
> scaffolding that gives it state, tools, a feedback loop and *enforceable* constraints —
> is the durable thing we design, own, and are paid to build.

Three ideas run through everything:

1. **Advisory vs deterministic.** Text the model *interprets* (prompts, `CLAUDE.md`) is
   advisory; rules the harness *enforces* (hooks, permissions, sandbox, egress allowlist)
   are deterministic. Only the deterministic layer holds under pressure or prompt injection.
2. **Verification sets the ceiling.** The strength and speed of the verification loop —
   not the model — decides how much autonomy is safe. No trustworthy tests ⇒ no safe delegation.
3. **Autonomy is a staffing decision, not a capability score.** Expressed as three original
   autonomy scales: **L1–L5** (engineering), **P1–P5** (product), **D1–D5** (design).
   Higher is not better; the safe level is set by the weakest enabling component, and is
   always capped by *"never scale agents beyond review capacity."*

The framing is deliberately **conceptual/methodological over tool-specific**, because the
client stack is unknown and tools churn weekly. Where specific tools appear (Spec Kit, Kiro,
BMAD, Superpowers, Compound Engineering, Claude Code config, Stryker/PIT/mutmut, DORA, METR),
they are reference points to *borrow mechanics from*, never dependencies to adopt wholesale.

---

## What's in this archive

```
.
├── README.md                     ← you are here
├── workbook/
│   └── agentic-development-study.html   ← THE primary deliverable (interactive, ~v1.7)
├── deep-dives/                   ← standalone companion documents (one topic each)
│   ├── SDLC-foundations-deepdive.html
│   ├── E1-agent-model-harness-deepdive.html
│   ├── E2-context-engineering-deepdive.html
│   ├── E3-harness-in-practice-deepdive.html
│   ├── E4-verification-first-deepdive.html
│   ├── E5-governance-deepdive.html
│   ├── E6-autonomy-levels-deepdive.html
│   ├── E7-metrics-anti-patterns-deepdive.html
│   ├── E8-spec-driven-development-deepdive.html
│   └── P1-ai-assisted-discovery-deepdive.html
├── archive/
│   └── agenticky-vyvoj-studium.html     ← original Slovak v0.1 (superseded, kept for history)
├── docs/                         ← project documentation (read these to continue the work)
│   ├── CONTENT-MAP.md            ← every module, topic, report, diagram, deep dive
│   ├── ARCHITECTURE.md           ← how the HTML/CSS/JS/storage is built; the overlay pattern
│   ├── AUTHORING-GUIDE.md        ← step-by-step recipe to add the next deep dive
│   ├── CHANGELOG.md              ← version history (v0.1 → current)
│   └── ROADMAP.md                ← what's done, what's next (P2–P5, D-series, M3–M7 …)
├── scripts/
│   └── validate.py               ← HTML/JS/SVG + wiring validator (run after every edit)
└── CLAUDE.md                     ← instructions for Claude Code when continuing this project
```

---

## The primary deliverable

**`workbook/agentic-development-study.html`** is a single, self-contained interactive study
workbook. No build step, no dependencies to install — open it in a browser. It contains:

- **An intro + two inline "map" sections**: an **SDLC Foundations** section and a **Domain
  map** (5 notational views), each with tabbed SVG diagrams.
- **8 modules** — M1 Engineering harness (E1–E8), M2 Product harness (P1–P5),
  M3 Handoff contract, M4 Information architecture, M5 Brownfield bootstrap,
  M6 Design harness (D1–D5), M7 Security (cross-cutting), M8 Study trajectory (backlog).
  **52 study topics** total, each with know / concepts / open questions / self-check / notes.
- **6 embedded research reports** (the source research), rendered from Markdown.
- **10 embedded deep-dive companions** (SDLC, E1–E8, P1) that open in-page as overlays.
- **Progress + notes tracking**, persisted in the browser (see ARCHITECTURE.md for the
  storage caveat when moving to Git).

The `deep-dives/*.html` files are the **same deep-dive content as standalone documents** —
useful for sharing, printing, or reading one topic in isolation. The workbook embeds a copy
of each; the standalone files are duplicates kept in sync by the authoring recipe.

---

## How to work with the artifacts

**To study / present:** open `workbook/agentic-development-study.html` in a browser.
Start with the **SDLC Foundations** section, then work module by module. Inside a topic,
the **"Go deeper"** links open the embedded deep dive for that topic.

**To read one topic standalone:** open the matching file in `deep-dives/`.

**To continue development (the point of this archive):** read **`CLAUDE.md`** first, then
`docs/ARCHITECTURE.md` and `docs/AUTHORING-GUIDE.md`. The next unit of work is almost always
"add the next deep-dive companion" — the recipe is mechanical and validated by
`scripts/validate.py`. `docs/ROADMAP.md` lists what remains.

---

## Status at time of packaging

- Workbook at **v1.7** (see `docs/CHANGELOG.md`).
- Deep-dive companions complete for: **SDLC** + **E1–E8** (all of module M1) + **P1**.
- Next: **P2–P5** (finish M2), then the **D1–D5** design scale (M6), then M3/M4/M5/M7 topics,
  and the trajectory research (T-series) — pilot design (DORA + METR) and engagement economics.

> **Note on sources.** Content is grounded in six research reports plus named practitioners,
> papers (arXiv IDs), incidents and CVEs. Fast-moving tool details (versions, marketplace
> status, star counts) are point-in-time (mid-2026) — re-verify before a client meeting.
> The **D1–D5** design scale is an *original synthesis*, not an industry standard, and is
> flagged as such wherever it appears.
