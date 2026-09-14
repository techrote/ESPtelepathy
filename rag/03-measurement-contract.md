---
rag_id: ESPT-RAG-MEASURE
title: Measurement, telemetry, and dataset contract
status: normative
scope: firmware-and-analysis
---

# Measurement contract

## Core rule

Raw evidence must survive model changes. Firmware must emit machine-readable records that allow host analysis to be rerun without reflashing or reverse-engineering console prose.

## Required identities

Every run records at minimum:

- schema version;
- firmware git SHA and build configuration fingerprint;
- board logical ID and MAC-derived hardware ID;
- operator-assigned physical board ID;
- reference-board/revision declaration (`verified`, `suspected-clone`, etc.);
- experiment/run UUID;
- boot/session UUID;
- local monotonic timestamp;
- stimulus sequence ID and deterministic seed;
- role (`receiver`, `emitter`, `coordinator`, `standalone`).

## Sample record families

Use versioned records rather than one unstable giant struct. At minimum define:

- `touch_sample`: raw, smooth, benchmark and proximity values where enabled; channel/GPIO; denoise state; scan configuration;
- `led_state`: 64 RGB values or content-addressed frame ID, global brightness policy, predicted load summaries;
- `led_tx`: start/end timestamp, byte/bit count, RMT/config mode, payload hash, reset/latch interval, probe ID;
- `gpio_probe`: pin mask, code family, code index/seed, symbol timing;
- `espnow_rx` / `espnow_tx`: peer ID, sequence, timestamps, RSSI/rx metadata where available;
- `imu_sample`: accel, gyro, temperature/status as available, configuration/ODR;
- `pose_truth`: fixture-defined relative edge, rotation, offset, gap, height/tilt if controlled;
- `event`: movement, operator action, abort, thermal/voltage warning, dropped sample, sync loss.

## File format

Start with newline-delimited JSON for debuggability and add a compact binary transport only if profiling proves it necessary. Host tooling may normalize NDJSON to Parquet/Arrow later, but raw captures remain immutable.

Large LED frames may be deduplicated by SHA-256/content ID after the first full definition in a session.

## Time model

Do not treat ESP-NOW receive time as a precision phase reference. Peers exchange schedules/epochs; precise stimulus/capture timing executes from local hardware timers. Record enough timing events to reconstruct uncertainty and dropped/late slots.

## Dataset provenance

A dataset directory must contain:

- immutable raw capture(s);
- `manifest.json` with board IDs, fixture state, firmware/config SHA, experiment protocol version, environmental notes, operator, and exclusions;
- analysis command/config;
- generated summary artifacts in a separate derived path.

Never edit raw captures in place.

## Truth and split labels

Pose truth comes from a documented fixture/operator protocol, not from the model prediction. Dataset splitting must be explicit. Later model evaluation must support:

- held-out time/session;
- held-out physical board;
- held-out board pair;
- held-out environmental condition.

This is essential to avoid a classifier learning manufacturing quirks of a particular pair instead of relative pose.
