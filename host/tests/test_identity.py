from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path

from host.esptelepathy_host import __version__, parse_identity_line

ROOT = Path(__file__).resolve().parents[2]


def sample_payload() -> dict[str, str]:
    return {
        "record": "identity",
        "project": "ESPtelepathy",
        "project_version": "0.1.0",
        "git_sha": "0123456789ab",
        "idf_version": "v6.1",
        "telemetry_schema": "0-dev",
        "target": "esp32s3",
        "build_config": "foundation-v1",
        "elf_sha256": "a" * 64,
    }


class IdentityParserTests(unittest.TestCase):
    def test_parses_exact_marker_line(self) -> None:
        payload = sample_payload()
        line = "ESPTELEPATHY_IDENTITY " + json.dumps(payload)
        self.assertEqual(parse_identity_line(line).as_dict(), payload)

    def test_parses_log_prefixed_line_and_ignores_future_fields(self) -> None:
        payload = sample_payload()
        payload["future_field"] = "ignored-by-v0-parser"
        line = "I (123) app: ESPTELEPATHY_IDENTITY " + json.dumps(payload)
        parsed = parse_identity_line(line)
        self.assertEqual(parsed.git_sha, "0123456789ab")
        self.assertEqual(parsed.telemetry_schema, "0-dev")

    def test_rejects_missing_marker(self) -> None:
        with self.assertRaisesRegex(ValueError, "marker"):
            parse_identity_line(json.dumps(sample_payload()))

    def test_rejects_missing_required_field(self) -> None:
        payload = sample_payload()
        del payload["git_sha"]
        with self.assertRaisesRegex(ValueError, "missing fields: git_sha"):
            parse_identity_line("ESPTELEPATHY_IDENTITY " + json.dumps(payload))

    def test_rejects_wrong_project(self) -> None:
        payload = sample_payload()
        payload["project"] = "other"
        with self.assertRaisesRegex(ValueError, "different project"):
            parse_identity_line("ESPTELEPATHY_IDENTITY " + json.dumps(payload))

    def test_version_matches_repository_version(self) -> None:
        repository_version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
        self.assertEqual(__version__, repository_version)

    def test_module_cli_reports_version(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "host.esptelepathy_host", "--version"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.stdout.strip(), __version__)


if __name__ == "__main__":
    unittest.main()
