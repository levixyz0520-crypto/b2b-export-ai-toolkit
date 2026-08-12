"""Command-line interface for the deterministic toolkit."""

import argparse
import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

from .buyer_qualification import qualify_buyer
from .customer_research import research_customer
from .followup import create_followup
from .outreach import create_email
from .quotation import analyze_quotation
from .sanitizer import sanitize

Command = Callable[[dict[str, Any]], Any]
COMMANDS: dict[str, Command] = {
    "research": research_customer,
    "qualify": qualify_buyer,
    "email": create_email,
    "followup": create_followup,
    "quote": analyze_quotation,
    "sanitize": sanitize,
}


def load_input(raw: str) -> dict[str, Any]:
    """Load a JSON object from a file path, inline JSON, or plain text."""
    path = Path(raw)
    text = path.read_text(encoding="utf-8") if path.is_file() else raw
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        return {"input": text}
    if not isinstance(value, dict):
        raise ValueError("Input JSON must be an object.")
    return value


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    parser = argparse.ArgumentParser(prog="export-ai", description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for name in COMMANDS:
        command = subparsers.add_parser(name)
        command.add_argument("input", help="JSON file, inline JSON object, or text")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Run a command and print stable JSON output."""
    args = build_parser().parse_args(argv)
    try:
        result = COMMANDS[args.command](load_input(args.input))
    except (OSError, ValueError, TypeError) as exc:
        build_parser().error(str(exc))
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
