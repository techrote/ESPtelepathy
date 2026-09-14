# Host tooling

The v0 host layer uses Python 3.12 and has **no runtime third-party dependencies**. Development lint/format checks use the single pinned dependency in `requirements-dev.txt`.

Current functionality is deliberately small: it parses the machine-readable firmware identity marker established by ETP-001. ETP-003 will own the full versioned telemetry and dataset schema.

Run tests from the repository root with:

```sh
python tools/dev.py host-test
```

Inspect the CLI with:

```sh
python -m host.esptelepathy_host --help
```
