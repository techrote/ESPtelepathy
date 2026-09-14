#!/usr/bin/env python3
"""Minimal dependency-free structural validation for ESPtelepathy RAG docs."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
RAG = ROOT / "rag"
REQUIRED = {"rag_id", "title", "status", "scope"}

def frontmatter(path: Path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML-style frontmatter")
    try:
        block = text.split("---\n", 2)[1]
    except IndexError as exc:
        raise ValueError("unterminated frontmatter") from exc
    data = {}
    for line in block.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip()
    return text, data

def main() -> int:
    errors = []
    ids = {}
    files = sorted(RAG.glob("*.md"))
    if not files:
        errors.append("rag/: no markdown documents found")
    for path in files:
        try:
            text, meta = frontmatter(path)
        except ValueError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        missing = REQUIRED - meta.keys()
        if missing:
            errors.append(f"{path.relative_to(ROOT)}: missing {sorted(missing)}")
        rid = meta.get("rag_id")
        if rid:
            if rid in ids:
                errors.append(f"duplicate rag_id {rid}: {ids[rid]} and {path}")
            ids[rid] = path
        if "TODO_SOURCE" in text or "TBD_SOURCE" in text:
            errors.append(f"{path.relative_to(ROOT)}: unresolved source placeholder")
    index = (RAG / "INDEX.md").read_text(encoding="utf-8") if (RAG / "INDEX.md").exists() else ""
    for rid, path in ids.items():
        if path.name != "INDEX.md" and rid not in index:
            errors.append(f"{path.relative_to(ROOT)}: rag_id {rid} absent from INDEX.md")
    roadmap = (RAG / "07-roadmap.md").read_text(encoding="utf-8") if (RAG / "07-roadmap.md").exists() else ""
    expected = [f"ETP-{i:03d}" for i in range(1, 19)]
    for issue_id in expected:
        if issue_id not in roadmap:
            errors.append(f"roadmap missing {issue_id}")
    if errors:
        print("RAG validation failed:")
        print("\n".join(f"- {e}" for e in errors))
        return 1
    print(f"RAG validation passed: {len(files)} docs, {len(ids)} unique IDs, {len(expected)} roadmap items")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
