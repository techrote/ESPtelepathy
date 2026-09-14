# ESPtelepathy development quick start

## Toolchain contract

The v0 foundation deliberately pins a reproducible baseline instead of following floating `latest` tags:

- ESP-IDF: **v6.1**
- firmware image: **`espressif/idf:v6.1`** (official Espressif image)
- firmware target: **ESP32-S3**
- host Python: **3.12**
- Ruff: **0.16.7** (development-only; host runtime is standard-library-only)

The canonical machine-readable pins live in `toolchain/versions.env`. Changing the ESP-IDF minor/major baseline requires a normal PR with successful firmware CI and explicit migration notes.

Primary upstream references:

- https://github.com/espressif/esp-idf/releases/tag/v6.1
- https://docs.espressif.com/projects/esp-idf/en/v6.1/
- https://docs.espressif.com/projects/esp-idf/en/v6.1/esp32s3/api-guides/tools/idf-docker-image.html
- https://hub.docker.com/r/espressif/idf/tags

## Repository layout

```text
firmware/              ESP-IDF application; hardware behavior grows by roadmap issue
  main/                ETP-001 boot/build identity only
  components/README.md reserved component ownership boundaries
host/                  Python analysis/acquisition helpers and tests
toolchain/             pinned development/build versions
tools/dev.py           single developer command entry point
rag/                    normative research/architecture documents
.github/workflows/      automated validation/builds
```

## First setup

Python 3.12 and Docker are the only prerequisites for the default path.

```sh
python -m venv .venv
# Activate .venv using the normal command for your shell/OS.
python tools/dev.py bootstrap
python tools/dev.py check
python tools/dev.py firmware-build
```

`firmware-build` uses the official pinned Espressif image, so a separate local ESP-IDF installation is not required. If an exactly compatible native ESP-IDF v6.1 environment is already active, `python tools/dev.py firmware-build --native` is available for convenience.

## Developer commands

| Command | Purpose |
|---|---|
| `python tools/dev.py bootstrap` | install pinned development dependency/dependencies |
| `python tools/dev.py format` | format Python host/developer code with Ruff |
| `python tools/dev.py lint` | lint Python host/developer code |
| `python tools/dev.py host-test` | run deterministic standard-library unit tests |
| `python tools/dev.py rag` | validate RAG frontmatter/index/roadmap integrity |
| `python tools/dev.py check` | run RAG validation, lint, and host tests |
| `python tools/dev.py firmware-build` | build ESP32-S3 firmware in the pinned official Docker image |

## Build identity contract

`VERSION` is the source of the project version supplied to ESP-IDF as `PROJECT_VER`. The firmware boot line begins with `ESPTELEPATHY_IDENTITY ` and carries JSON with:

- project and project version;
- repository Git SHA (or explicit `unknown` fallback outside a Git checkout);
- compiled ESP-IDF version;
- target;
- provisional telemetry schema version `0-dev`;
- build-configuration ID;
- ELF SHA-256;
- compile date/time.

This is deliberately only the ETP-001 identity substrate. ETP-003 owns the full versioned telemetry and dataset contract.

## Evidence boundary

ETP-001 contains no physical-board measurements and makes no bring-up claim. Firmware compilation in CI is software evidence only. Hardware verification begins in the later roadmap issues and must follow `AGENTS.md` evidence labels.
