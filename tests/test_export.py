"""Tests of the creation and the export of the scores table."""

from pathlib import Path

import pytest

pandas = pytest.importorskip("pandas")

from weather import export  # noqa: E402


def test_create_scores_frame_has_the_columns_and_values_of_the_lecture() -> None:
    frame = export.create_scores_frame()

    assert isinstance(frame, pandas.DataFrame)
    assert list(frame.columns) == ["students", "scores"]
    assert frame["students"].to_list() == ["Amy", "James", "Angela"]
    assert frame["scores"].to_list() == [76, 56, 65]


def test_export_frame_round_trips_through_a_file(tmp_path: Path) -> None:
    frame = export.create_scores_frame()
    target = tmp_path / "scores.csv"

    export.export_frame(frame, target)

    assert target.is_file()
    read_back = pandas.read_csv(target, index_col=0)
    pandas.testing.assert_frame_equal(read_back, frame)


def test_export_frame_accepts_a_string_path(tmp_path: Path) -> None:
    target = tmp_path / "as_text.csv"

    export.export_frame(export.create_scores_frame(), str(target))

    assert target.is_file()


def test_export_frame_default_name_writes_only_new_data_csv_in_the_working_dir(
    tmp_path: Path,
) -> None:
    # The autouse fixture in conftest.py made tmp_path the working directory.
    export.export_frame(export.create_scores_frame())

    assert [item.name for item in tmp_path.iterdir()] == ["new_data.csv"]


def test_create_scores_frame_writes_nothing(tmp_path: Path) -> None:
    export.create_scores_frame()

    assert list(tmp_path.iterdir()) == []
