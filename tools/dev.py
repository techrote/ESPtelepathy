#!/usr/bin/env python3
"""Single deterministic developer entry point for ESPtelepathy."""

from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSIONS_FILE = ROOT / "toolchain" / "versions.env"


def run(command: list[str], *, cwd: Path = ROOT) -> None:
    """Run a command while making the exact invocation visible."""

    print("+", shlex.join(command), flush=True)
    subprocess.run(command, cwd=cwd, check=True)


def load_versions() -> dict[str, str]:
    """Load the deliberately simple KEY=VALUE toolchain pin file."""

    versions: dict[str, str] = {}
    for raw_line in VERSIONS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            raise ValueError(f"invalid toolchain line: {raw_line!r}")
        key, value = line.split("=", 1)
        if not key or not value:
            raise ValueError(f"invalid toolchain line: {raw_line!r}")
        versions[key] = value
    return versions


def bootstrap() -> None:
    run([sys.executable, "-m", "pip", "install", "-r", "host/requirements-dev.txt"])


def format_sources() -> None:
    run([sys.executable, "-m", "ruff", "format", "host", "tools"])


def lint() -> None:
    run([sys.executable, "-m", "ruff", "check", "host", "tools"])


def host_test() -> None:
    run([sys.executable, "-m", "unittest", "discover", "-s", "host/tests", "-t", ".", "-v"])


def rag_check() -> None:
    run([sys.executable, "tools/validate_rag.py"])


def check() -> None:
    rag_check()
    lint()
    host_test()


def firmware_build(*, native: bool) -> None:
    if native:
        run(["idf.py", "set-target", "esp32s3"], cwd=ROOT / "firmware")
        run(["idf.py", "build"], cwd=ROOT / "firmware")
        return

    image = load_versions()["ESP_IDF_IMAGE"]
    command = [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{ROOT}:/project",
        "-w",
        "/project/firmware",
        "-e",
        "HOME=/tmp",
        "-e",
        "IDF_GIT_SAFE_DIR=/project",
    ]
    if os.name != "nt" and hasattr(os, "getuid"):
        command.extend(["--user", f"{os.getuid()}:{os.getgid()}"])
    command.extend(
        [image, "bash", "-lc", "idf.py set-target esp32s3 && idf.py build"]
    )
    run(command)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("bootstrap", help="install pinned host development dependencies")
    subparsers.add_parser("format", help="format Python host/developer sources")
    subparsers.add_parser("lint", help="lint Python host/developer sources")
    subparsers.add_parser("host-test", help="run deterministic host unit tests")
    subparsers.add_parser("rag", help="validate retrieval/RAG documents")
    subparsers.add_parser("check", help="run RAG, lint, and host tests")
    firmware_parser = subparsers.add_parser(
        "firmware-build", help="build the ESP32-S3 firmware using the pinned toolchain"
    )
    firmware_parser.add_argument(
        "--native",
        action="store_true",
        help="use an already-active local ESP-IDF instead of the pinned Docker image",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    commands = {
        "bootstrap": bootstrap,
        "format": format_sources,
        "lint": lint,
        "host-test": host_test,
        "rag": rag_check,
        "check": check,
    }
    if args.command == "firmware-build":
        firmware_build(native=args.native)
    else:
        commands[args.command]()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
