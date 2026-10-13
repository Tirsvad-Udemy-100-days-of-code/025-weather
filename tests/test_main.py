"""Tests of the command line: the printed results and what is written."""

import sys
from pathlib import Path

import pytest

from weather.__main__ import main


def test_main_without_arguments_prints_the_results_of_the_lectures(
    capsys: pytest.CaptureFixture[str],
) -> None:
    pytest.importorskip("pandas")

    assert main([]) == 0

    output = capsys.readouterr().out
    assert "17.428" in output
    assert "24" in output
    assert "Sunny" in output
    assert "53.6" in output
    assert "Sunday" in output
    assert "Angela" in output


def test_main_without_the_flag_writes_no_file(tmp_path: Path) -> None:
    pytest.importorskip("pandas")

    assert main([]) == 0

    assert list(tmp_path.iterdir()) == []


def test_main_with_the_export_flag_writes_the_scores_frame(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    pandas = pytest.importorskip("pandas")
    from weather.export import create_scores_frame

    target = tmp_path / "out.csv"

    assert main(["--export", str(target)]) == 0

    assert [item.name for item in tmp_path.iterdir()] == ["out.csv"]
    read_back = pandas.read_csv(target, index_col=0)
    pandas.testing.assert_frame_equal(read_back, create_scores_frame())
    assert str(target) in capsys.readouterr().out


def test_main_reports_the_missing_pandas_extra_and_writes_nothing(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    # None in sys.modules makes "import pandas" raise ImportError; the modules
    # that import it are removed so that they are imported again.
    monkeypatch.setitem(sys.modules, "pandas", None)
    monkeypatch.delitem(sys.modules, "weather.analysis", raising=False)
    monkeypatch.delitem(sys.modules, "weather.export", raising=False)

    assert main(["--export", str(tmp_path / "out.csv")]) == 1

    captured = capsys.readouterr()
    assert 'pip install "weather[pandas]"' in captured.err
    assert "Sunny" in captured.out
    assert "17.428" not in captured.out
    assert list(tmp_path.iterdir()) == []
