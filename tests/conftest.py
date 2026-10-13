"""Shared pytest configuration for the weather data tests."""

from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def isolated_working_directory(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Run every test in an empty temporary working directory.

    The export has a default file name relative to the working directory. Without
    this fixture, a test that uses the default would write into the folder pytest
    was started from.
    """
    monkeypatch.chdir(tmp_path)
