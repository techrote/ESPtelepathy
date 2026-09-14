---
rag_id: ESPT-RAG-HYP
title: Hypothesis and falsification register
status: normative
scope: research
---

# Hypothesis register

Each hypothesis must be tested against explicit controls. Results should update this file or a linked evidence record.

| ID | Hypothesis | Strong evidence for | Evidence against / falsification direction |
|---|---|---|---|
| H1 | Stock GPIO1-7 touch channels show repeatable response to an adjacent board | neighbour/no-neighbour distributions separate across reseating sessions | separation vanishes under reseating, power-source, or shuffled-label controls |
| H2 | Receiver LED self-interference is structured enough to model/subtract | held-out residual variance falls materially vs raw without erasing injected/peer signals | model helps only training runs or removes true positive-control coupling |
| H3 | Visible LED spatial/load patterns create pose-dependent peer fingerprints | receiver response tracks known basis patterns and changes reproducibly with pose | only global total brightness/current is observable; spatial permutations are indistinguishable |
| H4 | Extra serial traffic after the 64 visible words can traverse the LED chain invisibly | DOUT/code activity observed while displayed frame remains invariant across bounded tests | any probe length/pattern causes pixel corruption, reset ambiguity, instability, or unsafe behavior |
| H5 | Direct coded GP33-40 excitation is recoverable by a neighbouring touch/electrode receiver | correct code correlation exceeds wrong-code controls across reseats | correlation disappears with independent timing/shuffled code or is dominated by common ground artifacts |
| H6 | A low-dimensional coupling matrix changes predictably with pose | stable singular modes/templates generalize to held-out sessions/board pairs | effective modes are unstable or dominated by board identity/environment |
| H7 | Relative quarter-turn orientation is classifiable with useful rejection | held-out board-pair confusion matrix materially exceeds chance with calibrated unknown state | performance collapses on new board pair/environment or relies on leakage from labels/protocol |
| H8 | IMU/RSSI improve temporal reliability | ablation shows lower transition error / better rejection on held-out sequences | no measurable gain or added sensitivity to RF/environment |

No hypothesis is promoted to a project claim from a single visually convincing run.
