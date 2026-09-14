---
rag_id: ESPT-RAG-EXPERIMENT
title: Experimental method and anti-confounding controls
status: normative
scope: experiments
---

# Experimental method

## Experimental ladder

Use increasingly difficult experiments. Do not jump directly to a pose classifier.

### A. Single-board noise floor

Measure touch channels with no neighbour under controlled LED and radio conditions. Sweep representative LED states: off, low uniform, high-but-safe uniform, mid duty, checkerboards, sparse pixels, random seeded frames, and animation. Separately characterize LED serial-write windows and ESP-NOW/Wi-Fi activity.

### B. Positive coupling control

Use an intentionally strong, known nearby conductive/driven target to verify that the acquisition chain can detect capacitance changes and coded coupling at all.

### C. Two-board passive coupling

Introduce a second powered/unpowered board at controlled edge, rotation, gap, and offset. Compare against sham/no-neighbour placements.

### D. Active coded coupling

Test direct GPIO edge transmitters, LED-state basis patterns, and serial-chain probes. Correlate only against predeclared codes/seeds.

### E. Pose inference

Only after observability is demonstrated should a pose estimator be trained/calibrated.

## Required controls

Use relevant controls in every campaign:

- no neighbour;
- unpowered neighbour;
- neighbour present but wrong/random probe code;
- emitter enabled vs disabled;
- LED data transmission excluded vs deliberately included;
- radio quiet vs ESP-NOW/Wi-Fi active;
- shuffled code labels during analysis;
- repeated fixture placement after complete removal/reseating;
- changed USB cable/power source and table material when testing robustness.

## Avoiding circular inference

The measurement used to prove an effect cannot also define its ground truth. For example, an LED pattern ID sent over ESP-NOW may identify the stimulus, but the true physical orientation must come from fixture/operator metadata.

## Replication

Early feasibility may use two boards, but project-level claims require multiple physical units and board-pair holdouts. Do not publish a robust-orientation claim based only on repeated runs of one pair.

## Research issue completion

A research issue can close with a negative result if:

- the protocol and software are reproducible;
- required controls were run;
- raw data and manifests are committed/released or otherwise linked in a durable way appropriate to their size;
- analysis is deterministic;
- the conclusion states what was falsified and what remains possible.

## Safety and thermal policy

Use bounded brightness and bounded run duration. Add pauses where sustained LED load causes heating. Log supply/thermal observations available to the system/operator. A test is invalid if the board browns out, resets, thermally misbehaves, or silently drops samples without that condition being recorded.
