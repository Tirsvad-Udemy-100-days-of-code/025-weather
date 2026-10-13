"""Tests of the csv reader against the real data file and small files."""

import subprocess
import sys
from pathlib import Path

import pytest

from weather import csv_reader
from weather.constants import DATA_FILE

LECTURE_TEMPERATURES = [12, 14, 15, 14, 21, 22, 24]


@pytest.fixture
def small_csv(tmp_path: Path) -> Path:
    file = tmp_path / "small.csv"
    file.write_text("day,temp,condition\nMonday,3,Rain\nTuesday,-4,Snow\n")
    return file


def test_read_rows_gives_header_first_and_eight_rows_for_the_real_file() -> None:
    rows = csv_reader.read_rows()

    assert rows[0] == ["day", "temp", "condition"]
    assert len(rows) == 8
    assert all(isinstance(value, str) for row in rows for value in row)


def test_read_temperatures_gives_the_lecture_values_for_the_real_file() -> None:
    temperatures = csv_reader.read_temperatures()

    assert temperatures == LECTURE_TEMPERATURES
    assert all(isinstance(value, int) for value in temperatures)


def test_read_temperatures_skips_the_header() -> None:
    assert len(csv_reader.read_temperatures()) == len(csv_reader.read_rows()) - 1


def test_read_temperatures_gives_the_values_of_a_small_file(small_csv: Path) -> None:
    assert csv_reader.read_temperatures(small_csv) == [3, -4]


def test_read_rows_gives_the_rows_of_a_small_file(small_csv: Path) -> None:
    assert csv_reader.read_rows(small_csv) == [
        ["day", "temp", "condition"],
        ["Monday", "3", "Rain"],
        ["Tuesday", "-4", "Snow"],
    ]


def test_default_path_works_from_another_working_directory(tmp_path: Path) -> None:
    assert Path.cwd() == tmp_path
    assert DATA_FILE.parent != Path.cwd()

    assert csv_reader.read_temperatures() == LECTURE_TEMPERATURES


def test_path_argument_overrides_the_default_as_str_and_as_path(
    small_csv: Path,
) -> None:
    assert csv_reader.read_temperatures(small_csv) == [3, -4]
    assert csv_reader.read_temperatures(str(small_csv)) == [3, -4]


def test_importing_csv_reader_does_not_import_pandas() -> None:
    code = "import sys, weather.csv_reader; sys.exit('pandas' in sys.modules)"

    result = subprocess.run(
        [sys.executable, "-I", "-c", code],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
