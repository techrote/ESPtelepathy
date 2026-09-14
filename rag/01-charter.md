---
rag_id: ESPT-RAG-CHARTER
title: Project charter and success hierarchy
status: normative
scope: project-wide
---

# Project charter

## Primary question

Can two target ESP32-S3 8×8 RGB matrix boards placed edge-to-edge infer useful relative pose from existing/onboard electrical phenomena plus minimal passive electrode augmentation, while continuing to function as LED/Wi-Fi/IMU devices?

The central novelty is to treat known LED PWM/load patterns, WS2812 serial activity, and deliberately coded electrical excitation as potentially useful references rather than only as touch-sensor interference.

## Ordered success hierarchy

The project should progress only as evidence supports additional complexity:

1. **Observability:** repeatable cross-board electrical/capacitive coupling exists above controls.
2. **Adjacency:** distinguish neighbour vs no-neighbour robustly.
3. **Discrete orientation:** distinguish relative 0/90/180/270-degree edge orientation where geometry supports it.
4. **Offset/gap:** estimate lateral seam offset and/or coarse gap.
5. **Identity-aware sensing:** associate the measured coupling with an ESP-NOW peer.
6. **Temporal fusion:** use IMU/RSSI/history to stabilize pose and reject implausible transitions.
7. **Multi-tile topology:** infer a local graph when several boards are nearby.

Failure at a later level does not invalidate earlier useful levels.

## Non-goals for v0 research

- Do not claim calibrated vector E/H-field imaging.
- Do not assume every LED is an independently observable electromagnetic emitter.
- Do not assume the AliExpress unit is electrically identical to the Waveshare reference until verified.
- Do not require machine learning where a transparent baseline is adequate.
- Do not redesign a custom PCB before the stock-board observability limits are measured.
- Do not optimize for regulatory production readiness; Espressif explicitly warns that S3 touch sensing has limited interference immunity.

## Technology choice

Use **ESP-IDF** as the primary firmware environment. Low-level touch configuration, raw/proximity data, ESP-NOW receive metadata/RSSI, RMT/timing control, and reproducible build configuration are core research requirements and should not be hidden behind an Arduino-only abstraction.

Host tooling should default to Python with a small dependency surface and deterministic command-line workflows.

## Research principle

Optimize for information gain. Every experiment should distinguish competing explanations. A measurement campaign that proves a proposed signal is unusable is preferable to a visually impressive but confounded demo.
