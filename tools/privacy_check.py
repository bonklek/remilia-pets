#!/usr/bin/env python3
"""Fail when public repository text appears to contain identity or secret data."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEXT_NAMES = {".gitattributes", ".gitignore"}
TEXT_SUFFIXES = {".css", ".htm", ".html", ".js", ".json", ".md", ".py", ".svg", ".txt", ".yaml", ".yml"}


def patterns() -> list[tuple[str, re.Pattern[str]]]:
    users = "Users"
    home = "home"
    return [
        # Separators may be JSON-escaped as double backslashes.
        ("Windows user path", re.compile(rf"[A-Za-z]:\\{{1,2}}{users}\\{{1,2}}[^\\\s]+", re.I)),
        ("macOS user path", re.compile(rf"/{users}/[^/\s]+")),
        ("Linux home path", re.compile(rf"/{home}/[^/\s]+")),
        ("email address", re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)),
        ("OpenAI-style key", re.compile(r"\bsk-[A-Za-z0-9_-]{16,}\b")),
        ("GitHub token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
        ("private key", re.compile(r"-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-----")),
    ]


def text_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.name in TEXT_NAMES or path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return sorted(files)


def main() -> int:
    findings: list[str] = []
    checks = patterns()
    files = text_files()
    for path in files:
        relative = path.relative_to(ROOT)
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            findings.append(f"{relative}: not valid UTF-8, cannot be checked")
            continue
        for line_number, line in enumerate(text.splitlines(), start=1):
            for label, pattern in checks:
                if pattern.search(line):
                    findings.append(f"{relative}:{line_number}: {label}")

    if findings:
        print("Privacy check failed:")
        print("\n".join(findings))
        return 1

    print(f"Privacy check passed across {len(files)} text files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
