#!/usr/bin/env python3
"""Tests for the profile README validator."""

from __future__ import annotations

import contextlib
import io
import tempfile
from pathlib import Path

from validate_profile_readme import (
    EXPECTED_REPOSITORIES,
    EXPECTED_REPOSITORY_LINKS,
    REQUIRED_SUPPORT_FILES,
    ProfileReadmeError,
    ProfileReadmeSpec,
    main,
    resolve_report_path,
    validate_profile_readme,
    write_report_json,
)


def write_profile_fixture(
    root: Path,
    repositories: tuple[str, ...] = tuple(EXPECTED_REPOSITORIES),
    repository_links: tuple[tuple[str, str], ...] | None = None,
) -> Path:
    for name in REQUIRED_SUPPORT_FILES:
        (root / name).write_text(f"{name}\n", encoding="utf-8")

    docs = root / "docs"
    docs.mkdir()
    (docs / "PROJECT_IDENTITY.md").write_text("# Identity\n", encoding="utf-8")
    (docs / "OPEN_SOURCE_STANDARD.md").write_text("# Standard\n", encoding="utf-8")

    if repository_links is None:
        labels_by_repo = {repo: label for label, repo in EXPECTED_REPOSITORY_LINKS}
        repository_links = tuple((labels_by_repo[repo], repo) for repo in repositories)
    rows = "\n".join(
        f"| [{label}](https://github.com/yingzhou-bjtu/{repo}) | Scope for {repo} |"
        for label, repo in repository_links
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
        assert report["selected_repository_labels"] == [
            label for label, _ in EXPECTED_REPOSITORY_LINKS
        ]
        assert report["support_files"] == list(REQUIRED_SUPPORT_FILES)


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


def test_validate_profile_readme_reports_wrong_label() -> None:
    with tempfile.TemporaryDirectory(prefix="profile-readme-label-test-") as temporary:
        root = Path(temporary)
        repository_links = tuple(EXPECTED_REPOSITORY_LINKS)
        repository_links = (("FlowFish", repository_links[0][1]),) + repository_links[1:]
        readme = write_profile_fixture(root, repository_links=repository_links)

        try:
            validate_profile_readme(
                ProfileReadmeSpec(readme_path=readme, repo_root=root)
            )
        except ProfileReadmeError as exc:
            assert "unexpected selected repository labels" in str(exc)
        else:
            raise AssertionError("wrong repository label was accepted")


def test_main_writes_json_report_for_custom_paths() -> None:
    with tempfile.TemporaryDirectory(prefix="profile-readme-cli-test-") as temporary:
        root = Path(temporary)
        readme = write_profile_fixture(root)
        report = root / "logs" / "report.json"

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
        assert '"support_files"' in report.read_text(encoding="utf-8")


def test_validate_profile_readme_reports_missing_support_file() -> None:
    with tempfile.TemporaryDirectory(prefix="profile-readme-support-test-") as temporary:
        root = Path(temporary)
        readme = write_profile_fixture(root)
        (root / "SECURITY.md").unlink()

        try:
            validate_profile_readme(
                ProfileReadmeSpec(readme_path=readme, repo_root=root)
            )
        except ProfileReadmeError as exc:
            assert "missing required support files" in str(exc)
            assert "SECURITY.md" in str(exc)
        else:
            raise AssertionError("missing support file was accepted")


def test_resolve_report_path_rejects_root_report_file() -> None:
    with tempfile.TemporaryDirectory(prefix="profile-readme-report-test-") as temporary:
        root = Path(temporary)
        readme = write_profile_fixture(root)
        spec = ProfileReadmeSpec(readme_path=readme, repo_root=root)
        try:
            resolve_report_path(root / "report.json", spec)
        except ValueError as exc:
            assert "logs/ or reports/" in str(exc)
        else:
            raise AssertionError("json_out accepted a repository-root report")


def test_resolve_report_path_rejects_non_json_suffix() -> None:
    with tempfile.TemporaryDirectory(prefix="profile-readme-report-suffix-") as temporary:
        root = Path(temporary)
        readme = write_profile_fixture(root)
        spec = ProfileReadmeSpec(readme_path=readme, repo_root=root)
        try:
            resolve_report_path(root / "logs" / "report.txt", spec)
        except ValueError as exc:
            assert "must end with .json" in str(exc)
        else:
            raise AssertionError("json_out accepted a non-json suffix")


def test_resolve_report_path_rejects_readme_overwrite() -> None:
    with tempfile.TemporaryDirectory(prefix="profile-readme-report-overwrite-") as temporary:
        root = Path(temporary)
        readme = root / "README.json"
        docs = root / "docs"
        docs.mkdir()
        (docs / "PROJECT_IDENTITY.md").write_text("# Identity\n", encoding="utf-8")
        (docs / "OPEN_SOURCE_STANDARD.md").write_text("# Standard\n", encoding="utf-8")
        readme.write_text("# Profile\n", encoding="utf-8")
        spec = ProfileReadmeSpec(readme_path=readme, repo_root=root)
        try:
            resolve_report_path(readme, spec)
        except ValueError as exc:
            assert "must not overwrite" in str(exc)
        else:
            raise AssertionError("json_out accepted a README overwrite path")


def test_resolve_report_path_accepts_tmp_json() -> None:
    with tempfile.TemporaryDirectory(prefix="profile-readme-report-tmp-") as temporary:
        root = Path(temporary) / "profile"
        root.mkdir()
        readme = write_profile_fixture(root)
        spec = ProfileReadmeSpec(readme_path=readme, repo_root=root)
        report = resolve_report_path(Path(temporary) / "profile_report.json", spec)
        assert report.name == "profile_report.json"


def test_write_report_json_replaces_report_without_temp_files() -> None:
    with tempfile.TemporaryDirectory(prefix="profile-readme-write-report-") as temporary:
        report = Path(temporary) / "logs" / "report.json"
        report.parent.mkdir()
        report.write_text('{"old": true}\n', encoding="utf-8")

        write_report_json(report, {"selected_repository_count": 5})

        report_text = report.read_text(encoding="utf-8")
        assert '"selected_repository_count": 5' in report_text
        assert not list(report.parent.glob(".report.json.*.tmp"))


def test_missing_readme_uses_validator_failure_contract() -> None:
    with tempfile.TemporaryDirectory(prefix="profile-readme-missing-test-") as temporary:
        root = Path(temporary)
        missing = root / "README.md"

        try:
            validate_profile_readme(
                ProfileReadmeSpec(readme_path=missing, repo_root=root)
            )
        except ProfileReadmeError as exc:
            assert "cannot read profile README" in str(exc)
        else:
            raise AssertionError("missing README was accepted")

        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            exit_code = main(
                [
                    "--readme",
                    str(missing),
                    "--repo-root",
                    str(root),
                ]
            )
        assert exit_code == 1
        assert "PROFILE_README_CHECK_FAIL" in stderr.getvalue()


if __name__ == "__main__":
    for name, test_func in sorted(globals().items()):
        if name.startswith("test_") and callable(test_func):
            test_func()
