# Meridian — the recurring worked-example client

Every deep-dive worked example runs on ONE stable fictional client so familiarity
compounds across the corpus. This file is the single source of truth. Deep dives may
add topic-local numbers but must never contradict what is written here. When a worked
example needs a new standing fact (a number reused by other topics), add it here first.

**Hard rule:** Meridian is a teaching device for a public repository. It is a *generic*
brownfield mid-size insurer. Never transplant real-client internals (names, repo lists,
headcounts, findings) into it.

## Profile

- **Meridian** — mid-size insurer, ~220 employees, ~40 engineers in 6 teams.
- Estate: **~25 repositories across ~5 systems**, grown over 12 years.
- Stack mix: **"PolicyCore"** policy-administration system (legacy Java 11 monolith,
  ~600k LOC), two .NET services (claims, documents), a React front end, one Python
  data/reporting service, a vendor CRM with in-house extensions.
- Delivery: trunk-ish git flow, Jenkins CI, quarterly-release habit on PolicyCore,
  weekly on the services.

## AI-tooling state (the brownfield default, not the exception)

- Developers already use **Cursor and Claude Code ad hoc, unguided** — no shared
  rules files, no memory discipline, no permission baseline. Assume artifacts
  (rules, memories, half-adopted configs) already exist and disagree.

## Verification state (standing numbers)

- PolicyCore billing module: **82% branch coverage**, no one has ever measured a
  mutation score anywhere.
- Test suite: ~14 min; **flake rate ~3%** (retry culture: "re-run until green").
- No characterization-test practice; golden files exist only in the reporting service.

## Cast

- **Dana Kovář — CTO.** Skeptical, numbers-driven; burned by a 2024 "AI pilot" that
  shipped demos and no process. Objects with metrics ("we already have 82% coverage").
- **Petr Lang — lead engineer, PolicyCore.** Pragmatic, protective of the monolith;
  adopts anything that demonstrably saves review time.
- **Mira Stone — PM, retail line.** Wants predictable delivery, asks what changes
  for requirements and acceptance.

## Usage rules

1. Worked examples name the module and the person they address (usually PolicyCore,
   Dana, or Petr) and walk ONE decision end to end with concrete numbers.
2. Show at least one judgment call under ambiguity (the reasoning, not just the verdict).
3. Numbers must be realistic and self-consistent with this file.
