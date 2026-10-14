#!/usr/bin/env python3
"""Tests for the profile README validator."""

from __future__ import annotations

import tempfile
from pathlib import Path

from validate_profile_readme import (
    EXPECTED_REPOSITORIES,
    ProfileReadmeError,
    ProfileReadmeSpec,
    main,
    validate_profile_readme,
)


def write_profile_fixture(
    root: Path,
    repositories: tuple[str, ...] = tuple(EXPECTED_REPOSITORIES),
) -> Path:
    docs = root / "docs"
    docs.mkdir()
    (docs / "PROJECT_IDENTITY.md").write_text("# Identity\n", encoding="utf-8")
    (docs / "OPEN_SOURCE_STANDARD.md").write_text("# Standard\n", encoding="utf-8")

    rows = "\n".join(
        f"| [{repo}](https://github.com/yingzhou-bjtu/{repo}) | Scope for {repo} |"
        for repo in repositories
    )
    readme = root / "README.md"
    readme.write_text(
        "\n".join(
            [
                "# Profile",
                "",
                "## Selected Public Repositories",
                "",
                "| Repository | Scope |",
                "| --- | --- |",
                rows,
                "",
                "---",
                "",
                "See docs/PROJECT_IDENTITY.md.",
                "See docs/OPEN_SOURCE_STANDARD.md.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    return readme


def test_validate_profile_readme_accepts_custom_paths() -> None:
    with tempfile.TemporaryDirectory(prefix="profile-readme-test-") as temporary:
        root = Path(temporary)
        readme = write_profile_fixture(root)
        report = validate_profile_readme(
            ProfileReadmeSpec(readme_path=readme, repo_root=root)
        )

        assert report["selected_repository_count"] == len(EXPECTED_REPOSITORIES)
        assert report["selected_repositories"] == list(EXPECTED_REPOSITORIES)


def test_validate_profile_readme_reports_wrong_order() -> None:
    with tempfile.TemporaryDirectory(prefix="profile-readme-order-test-") as temporary:
        root = Path(temporary)
        repositories = tuple(reversed(EXPECTED_REPOSITORIES))
        readme = write_profile_fixture(root, repositories)

        try:
            validate_profile_readme(
                ProfileReadmeSpec(readme_path=readme, repo_root=root)
            )
        except ProfileReadmeError as exc:
            assert "unexpected selected repository order" in str(exc)
        else:
            raise AssertionError("wrong repository order was accepted")


def test_main_writes_json_report_for_custom_paths() -> None:
    with tempfile.TemporaryDirectory(prefix="profile-readme-cli-test-") as temporary:
        root = Path(temporary)
        readme = write_profile_fixture(root)
        report = root / "report.json"

        assert main(
            [
                "--readme",
                str(readme),
                "--repo-root",
                str(root),
                "--json-out",
                str(report),
            ]
        ) == 0
        assert report.is_file()
        assert '"selected_repository_count": 5' in report.read_text(encoding="utf-8")


if __name__ == "__main__":
    test_validate_profile_readme_accepts_custom_paths()
    test_validate_profile_readme_reports_wrong_order()
    test_main_writes_json_report_for_custom_paths()
