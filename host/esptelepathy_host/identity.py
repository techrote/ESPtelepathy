"""Parsing for the minimal ETP-001 firmware identity record."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass

IDENTITY_MARKER = "ESPTELEPATHY_IDENTITY "
_REQUIRED_FIELDS = (
    "record",
    "project",
    "project_version",
    "git_sha",
    "idf_version",
    "telemetry_schema",
    "target",
    "build_config",
    "elf_sha256",
)


@dataclass(frozen=True, slots=True)
class FirmwareIdentity:
    """Stable subset of the boot identity emitted by the firmware foundation."""

    record: str
    project: str
    project_version: str
    git_sha: str
    idf_version: str
    telemetry_schema: str
    target: str
    build_config: str
    elf_sha256: str

    def as_dict(self) -> dict[str, str]:
        """Return a deterministic JSON-serializable mapping."""

        return asdict(self)


def parse_identity_line(line: str) -> FirmwareIdentity:
    """Parse an ESPtelepathy identity marker from an exact or log-prefixed line."""

    marker_offset = line.find(IDENTITY_MARKER)
    if marker_offset < 0:
        raise ValueError("identity marker not found")

    raw_payload = line[marker_offset + len(IDENTITY_MARKER) :].strip()
    try:
        payload = json.loads(raw_payload)
    except json.JSONDecodeError as exc:
        raise ValueError("invalid identity JSON") from exc

    if not isinstance(payload, dict):
        raise ValueError("identity payload must be a JSON object")

    missing = [field for field in _REQUIRED_FIELDS if field not in payload]
    if missing:
        raise ValueError(f"identity payload missing fields: {', '.join(missing)}")

    for field in _REQUIRED_FIELDS:
        if not isinstance(payload[field], str) or not payload[field]:
            raise ValueError(f"identity field {field!r} must be a non-empty string")

    if payload["record"] != "identity":
        raise ValueError("identity record has unexpected record type")
    if payload["project"] != "ESPtelepathy":
        raise ValueError("identity record belongs to a different project")

    return FirmwareIdentity(**{field: payload[field] for field in _REQUIRED_FIELDS})
