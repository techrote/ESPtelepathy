# ESPtelepathy

ESPtelepathy is an experimental research project for estimating the relative edge-to-edge pose of compact ESP32-S3 RGB matrix boards using hardware that is already present on the target module: ESP32-S3 capacitive touch sensing, the 8×8 WS2812B-0807 LED matrix and its serial chain, ESP-NOW, RSSI, and the onboard QMI8658C IMU.

The initial hardware target is the 25 mm × 25 mm ESP32-S3 Matrix board sold under/compatible with the Waveshare ESP32-S3-Matrix design and the user-selected AliExpress module. The exact purchased hardware is authoritative: clone/substitution differences must be verified during bring-up rather than assumed from the reference schematic.

This repository is intentionally evidence-first. A negative result is a valid result; fabricated, simulated-as-measured, or cherry-picked hardware evidence is not.

Start with [`rag/INDEX.md`](rag/INDEX.md) and [`AGENTS.md`](AGENTS.md).

## Research objective

Determine whether two boards placed edge-to-edge can robustly estimate some or all of:

- neighbour presence and identity;
- facing edge / relative quarter-turn orientation;
- lateral seam offset;
- approximate gap / coupling quality;
- motion-consistent temporal pose;
- eventually, local multi-tile topology.

The project explicitly investigates whether known or deliberately manipulated LED electrical activity can act as a sparse, coded near-field reference pattern rather than merely as interference.
