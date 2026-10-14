#!/usr/bin/env python3
"""Validate the GitHub profile README project index."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
README = REPO_ROOT / "README.md"
OWNER = "yingzhou-bjtu"

EXPECTED_REPOSITORIES = [
    "flowfish-streaming-clustering",
    "PIFCA",
    "containerized-routing-simulator",
    "multipath-delay-measurements",
    "paper-agent",
]
REQUIRED_DOCUMENT_REFERENCES = [
    ("docs/PROJECT_IDENTITY.md", REPO_ROOT / "docs" / "PROJECT_IDENTITY.md"),
    ("docs/OPEN_SOURCE_STANDARD.md", REPO_ROOT / "docs" / "OPEN_SOURCE_STANDARD.md"),
]

REPOSITORY_LINK_PATTERN = re.compile(
    r"\| \[[^\]]+\]\(https://github\.com/(?P<owner>[^/)]+)/(?P<repo>[^/)]+)\) \| (?P<scope>[^|]+) \|"
)


def fail(message: str) -> None:
    print(f"PROFILE_README_CHECK_FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def extract_selected_repositories(readme_text: str) -> list[tuple[str, str, str]]:
    marker = "## Selected Public Repositories"
    if marker not in readme_text:
        fail("missing selected public repositories section")

    section = readme_text.split(marker, 1)[1].split("\n---", 1)[0]
    rows = []
    for line in section.splitlines():
        match = REPOSITORY_LINK_PATTERN.fullmatch(line.strip())
        if match:
            rows.append((match.group("owner"), match.group("repo"), match.group("scope").strip()))
    return rows


def validate_profile_readme(readme_path: Path = README) -> dict[str, object]:
    readme_text = readme_path.read_text(encoding="utf-8")
    rows = extract_selected_repositories(readme_text)
    if not rows:
        fail("selected public repositories table has no repository rows")

    owners = {owner for owner, _, _ in rows}
    if owners != {OWNER}:
        fail(f"unexpected repository owner set: {sorted(owners)}")

    repositories = [repo for _, repo, _ in rows]
    if repositories != EXPECTED_REPOSITORIES:
        fail(f"unexpected selected repository order: {repositories}")

    empty_scopes = [repo for _, repo, scope in rows if not scope]
    if empty_scopes:
        fail(f"repository rows with empty scope: {empty_scopes}")

    duplicate_repositories = sorted({repo for repo in repositories if repositories.count(repo) > 1})
    if duplicate_repositories:
        fail(f"duplicate selected repositories: {duplicate_repositories}")

    missing_documents = [name for name, path in REQUIRED_DOCUMENT_REFERENCES if not path.is_file()]
    if missing_documents:
        fail(f"missing required documentation files: {missing_documents}")

    missing_references = [name for name, _ in REQUIRED_DOCUMENT_REFERENCES if name not in readme_text]
    if missing_references:
        fail(f"README does not reference required documentation files: {missing_references}")

    return {
        "selected_repository_count": len(repositories),
        "selected_repositories": repositories,
        "document_references": [name for name, _ in REQUIRED_DOCUMENT_REFERENCES],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json-out", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    report = validate_profile_readme()
    if args.json_out is not None:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(
            json.dumps(report, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    print("PROFILE_README_CHECK_PASS")
    print(f"selected_repository_count={report['selected_repository_count']}")
    print("selected_repositories=" + ",".join(report["selected_repositories"]))
    print("document_references=" + ",".join(report["document_references"]))


if __name__ == "__main__":
    main()
