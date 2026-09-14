---
rag_id: ESPT-RAG-ROADMAP
title: Implementation and research roadmap
status: normative
scope: project-wide
---

# Roadmap

The plan was reviewed to avoid two early mistakes: (1) building a pose classifier before proving an observable cross-board signal, and (2) assuming the reference schematic and post-frame LED-probe behavior are true on the purchased modules. The improved plan therefore front-loads hardware identity, telemetry integrity, controls, and falsifiable feasibility gates.

## GitHub issue map

Each roadmap item has a self-contained autonomous implementation/research prompt. The issue plus the normative RAG documents it references are the execution contract.

| ID | GitHub issue |
|---|---|
| ETP-001 | [#2](https://github.com/techrote/ESPtelepathy/issues/2) |
| ETP-002 | [#3](https://github.com/techrote/ESPtelepathy/issues/3) |
| ETP-003 | [#4](https://github.com/techrote/ESPtelepathy/issues/4) |
| ETP-004 | [#5](https://github.com/techrote/ESPtelepathy/issues/5) |
| ETP-005 | [#6](https://github.com/techrote/ESPtelepathy/issues/6) |
| ETP-006 | [#7](https://github.com/techrote/ESPtelepathy/issues/7) |
| ETP-007 | [#8](https://github.com/techrote/ESPtelepathy/issues/8) |
| ETP-008 | [#9](https://github.com/techrote/ESPtelepathy/issues/9) |
| ETP-009 | [#10](https://github.com/techrote/ESPtelepathy/issues/10) |
| ETP-010 | [#11](https://github.com/techrote/ESPtelepathy/issues/11) |
| ETP-011 | [#12](https://github.com/techrote/ESPtelepathy/issues/12) |
| ETP-012 | [#13](https://github.com/techrote/ESPtelepathy/issues/13) |
| ETP-013 | [#14](https://github.com/techrote/ESPtelepathy/issues/14) |
| ETP-014 | [#15](https://github.com/techrote/ESPtelepathy/issues/15) |
| ETP-015 | [#16](https://github.com/techrote/ESPtelepathy/issues/16) |
| ETP-016 | [#17](https://github.com/techrote/ESPtelepathy/issues/17) |
| ETP-017 | [#18](https://github.com/techrote/ESPtelepathy/issues/18) |
| ETP-018 | [#19](https://github.com/techrote/ESPtelepathy/issues/19) |

## Phase 0 — trustworthy substrate

| ID | Deliverable | Depends on |
|---|---|---|
| ETP-001 | Repository/build/test foundation for ESP-IDF + host tooling | — |
| ETP-002 | Hardware identity, schematic/pin-ownership verification, board capability report | ETP-001 |
| ETP-003 | Versioned telemetry schema, capture format, manifests, deterministic fixtures | ETP-001 |
| ETP-004 | Board bring-up: LED mapping, QMI8658C, IDs, USB/serial diagnostics | ETP-002, ETP-003 |

## Phase 1 — expose and control signals

| ID | Deliverable | Depends on |
|---|---|---|
| ETP-005 | Raw touch acquisition, denoise/filter/proximity modes, channel qualification | ETP-002–004 |
| ETP-006 | Deterministic LED stimulus engine and electrical-load feature logging | ETP-004 |
| ETP-007 | Bounded invisible/post-frame WS2812 serial-probe feasibility test | ETP-004, ETP-006 |
| ETP-008 | Direct GPIO coded near-field transmitter/control on exposed GP33–40 | ETP-002–004 |
| ETP-009 | ESP-NOW peer protocol, identity, schedules, radio-quiet windows, RSSI | ETP-003–004 |

## Phase 2 — characterize physics before estimating pose

| ID | Deliverable | Depends on |
|---|---|---|
| ETP-010 | Single-board touch-noise characterization vs LED/radio activity | ETP-005, ETP-006, ETP-009 |
| ETP-011 | Two-board passive-coupling campaign on stock hardware | ETP-005, ETP-010 |
| ETP-012 | Reproducible removable edge-electrode/fixture design and geometry sweep | ETP-011 |
| ETP-013 | Coded-probe correlation and effective coupling-rank study | ETP-007/008, ETP-009, ETP-012 as useful |

ETP-013 must support whichever active probe mechanisms survive their own feasibility gates; it must not assume ETP-007 succeeds.

## Phase 3 — calibrated inference

| ID | Deliverable | Depends on |
|---|---|---|
| ETP-014 | Calibration/response-volume dataset builder and board-pair split tooling | ETP-010–013 |
| ETP-015 | Transparent baseline adjacency/orientation/offset estimator with rejection | ETP-014 |
| ETP-016 | IMU + RSSI temporal fusion and ablation evaluation | ETP-009, ETP-015 |
| ETP-017 | Multi-neighbour slotting and local topology inference prototype | ETP-016 |

## Phase 4 — replication and decision

| ID | Deliverable | Depends on |
|---|---|---|
| ETP-018 | Cross-board replication, environmental stress tests, demo, and go/no-go report | ETP-015–017 as applicable |

The ETP-018 report must separate what works on stock boards, what requires removable electrodes, what requires active coded probes, and what would justify a custom PCB revision.
