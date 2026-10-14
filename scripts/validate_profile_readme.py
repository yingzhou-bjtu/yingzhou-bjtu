#!/usr/bin/env python3
"""Validate the GitHub profile README project index."""

from __future__ import annotations

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


def main() -> None:
    readme_text = README.read_text(encoding="utf-8")
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

    print("PROFILE_README_CHECK_PASS")
    print(f"selected_repository_count={len(repositories)}")
    print("selected_repositories=" + ",".join(repositories))


if __name__ == "__main__":
    main()
