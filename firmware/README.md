# Firmware foundation

The firmware is a conventional ESP-IDF application targeting ESP32-S3. ETP-001 only emits deterministic build identity; hardware peripherals are intentionally deferred to their roadmap issues.

The canonical ESP-IDF pin is stored in `../toolchain/versions.env`. The supported local build path is:

```sh
python tools/dev.py firmware-build
```

This uses Espressif's official pinned Docker image. If a matching native ESP-IDF environment is already active, use:

```sh
python tools/dev.py firmware-build --native
```

At boot the application emits one line beginning with `ESPTELEPATHY_IDENTITY ` followed by JSON containing project version, Git SHA, ESP-IDF version, target, the provisional telemetry schema `0-dev`, build configuration ID, ELF SHA-256, and compile date/time. ETP-003 may extend the record but must preserve explicit schema/version provenance.
