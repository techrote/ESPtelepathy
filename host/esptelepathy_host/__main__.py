"""Small command-line surface for the host foundation."""

from __future__ import annotations

import argparse
import json
import sys

from . import __version__
from .identity import parse_identity_line


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="esptelepathy-host")
    parser.add_argument("--version", action="version", version=__version__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    parse_parser = subparsers.add_parser(
        "parse-identity", help="parse a firmware ESPTELEPATHY_IDENTITY line"
    )
    parse_parser.add_argument(
        "line",
        nargs="?",
        help="identity line; when omitted, one line is read from stdin",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "parse-identity":
        line = args.line if args.line is not None else sys.stdin.readline()
        identity = parse_identity_line(line)
        print(json.dumps(identity.as_dict(), sort_keys=True, separators=(",", ":")))
        return 0
    raise AssertionError(f"unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())
