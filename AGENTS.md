# ESPtelepathy agent execution contract

This file applies to every implementation/research issue unless an issue explicitly overrides it.

## Authority and reading order

1. The current GitHub issue defines the immediate scope and acceptance criteria.
2. `rag/INDEX.md` identifies the normative project documents.
3. The RAG documents referenced by the issue define hardware facts, experimental contracts, architecture, and evidence rules.
4. Upstream vendor/manufacturer documentation in `rag/09-sources.md` is authoritative for external technical facts, subject to verification on the actual purchased boards.

Do not silently broaden an issue. If prerequisite repository state differs from the issue assumptions, reconcile it and document the discrepancy before continuing.

## Required workflow

For each issue:

- inspect the issue, referenced RAG documents, prerequisite merged work, and current repository state;
- implement the smallest coherent solution that satisfies the issue;
- add deterministic automated tests for software behavior where practical;
- preserve raw evidence and machine-readable metadata for experiments;
- run all applicable checks locally when possible;
- open a PR that links the issue and explains implementation, tests, evidence, limitations, and remaining uncertainty;
- wait for/inspect automated checks; fix failures rather than bypassing them;
- merge only after required automated checks pass;
- close the issue only when its acceptance criteria are actually satisfied.

If physical hardware action is required and the executing agent has no physical access, do **not** invent results or close the issue. Complete all software, fixture instructions, analysis, and operator tooling possible; leave a precise hardware-run blocker/evidence request.

## Evidence integrity

Experimental claims must distinguish:

- `measured`: captured from named physical boards with run metadata;
- `derived`: computed from measured data by a reproducible analysis step;
- `simulated`: generated without physical measurement;
- `hypothesis`: unverified expectation.

Never relabel simulated or synthetic data as measured. Never delete inconvenient runs merely because they weaken a hypothesis. Record negative controls, failed trials, board IDs, firmware commit, configuration, stimulus schedule, and environmental/fixture metadata required by `rag/03-measurement-contract.md`.

## Research quality rules

- Prefer paired/blocked experimental designs over one-off demonstrations.
- Use held-out sessions and, once multiple boards exist, held-out physical board identities/pairs to detect memorization.
- Avoid tuning thresholds on the final evaluation split.
- Include no-neighbour, wrong-code, radio-active/radio-quiet, LED-off, static-brightness, and shuffled-label controls when relevant.
- Report distributions and confidence intervals/effect sizes where useful, not only best-case screenshots.
- A falsified hypothesis is a successful research outcome if the evidence is reproducible.

## Hardware safety

Respect the vendor warning that excessive LED brightness can heat/damage the board. Characterization software must include conservative brightness/current limits, bounded test durations, and an emergency stop/abort path. Do not defeat protection merely to improve signal-to-noise ratio.
