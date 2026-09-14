# ESPtelepathy

ESPtelepathy is an experimental research project for estimating the relative edge-to-edge pose of compact ESP32-S3 RGB matrix boards using hardware that is already present on the target module: ESP32-S3 capacitive touch sensing, the 8×8 WS2812B-0807 LED matrix and its serial chain, ESP-NOW, RSSI, and the onboard QMI8658C IMU.

The initial hardware target is the 25 mm × 25 mm ESP32-S3 Matrix board sold under/compatible with the Waveshare ESP32-S3-Matrix design and the user-selected AliExpress module. The exact purchased hardware is authoritative: clone/substitution differences must be verified during bring-up rather than assumed from the reference schematic.

This repository is intentionally evidence-first. A negative result is a valid result; fabricated, simulated-as-measured, or cherry-picked hardware evidence is not.

Start with [`rag/INDEX.md`](rag/INDEX.md) and [`AGENTS.md`](AGENTS.md). For a clean development checkout, see [`DEVELOPMENT.md`](DEVELOPMENT.md).

## Development foundation

The v0 toolchain is pinned in `toolchain/versions.env`: ESP-IDF v6.1 for ESP32-S3, Python 3.12, and a single development-only Ruff pin. Host runtime tooling otherwise uses only the standard library.

```sh
python -m venv .venv
# activate the virtual environment
python tools/dev.py bootstrap
python tools/dev.py check
python tools/dev.py firmware-build
```

The firmware build uses Espressif's official pinned Docker image by default. No physical-hardware success is implied by a successful CI build.

## Research objective

Determine whether two boards placed edge-to-edge can robustly estimate some or all of:

- neighbour presence and identity;
- facing edge / relative quarter-turn orientation;
- lateral seam offset;
- approximate gap / coupling quality;
- motion-consistent temporal pose;
- eventually, local multi-tile topology.

The project explicitly investigates whether known or deliberately manipulated LED electrical activity can act as a sparse, coded near-field reference pattern rather than merely as interference.
