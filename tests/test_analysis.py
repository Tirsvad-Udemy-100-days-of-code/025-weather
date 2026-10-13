"""Tests of the pandas analysis against the real data file and small files."""

from pathlib import Path

import pytest

pandas = pytest.importorskip("pandas")

from weather import analysis, csv_reader  # noqa: E402

LECTURE_TEMPERATURES = [12, 14, 15, 14, 21, 22, 24]
COLUMNS = ["day", "temp", "condition"]


@pytest.fixture
def small_csv(tmp_path: Path) -> Path:
    file = tmp_path / "small.csv"
    file.write_text("day,temp,condition\nMonday,3,Rain\nTuesday,-4,Snow\n")
    return file


def test_read_data_gives_a_dataframe_with_seven_rows_and_three_columns() -> None:
    data = analysis.read_data()

    assert isinstance(data, pandas.DataFrame)
    assert len(data) == 7
    assert list(data.columns) == COLUMNS


def test_a_column_of_the_data_is_a_series() -> None:
    data = analysis.read_data()

    assert isinstance(data["temp"], pandas.Series)


def test_to_data_dict_has_a_key_for_each_column() -> None:
    data_dict = analysis.to_data_dict(analysis.read_data())

    assert list(data_dict) == COLUMNS


def test_to_temp_list_gives_the_lecture_temperatures() -> None:
    assert analysis.to_temp_list(analysis.read_data()) == LECTURE_TEMPERATURES


def test_both_averages_agree_and_equal_the_sum_over_the_count() -> None:
    data = analysis.read_data()
    expected = 122 / 7

    assert analysis.average_temp(data) == pytest.approx(expected)
    assert analysis.average_temp_mean(data) == pytest.approx(expected)
    mean_way = analysis.average_temp_mean(data)
    assert analysis.average_temp(data) == pytest.approx(mean_way)


def test_max_temp_gives_the_highest_temperature() -> None:
    assert analysis.max_temp(analysis.read_data()) == 24


def test_row_for_day_gives_the_single_row_of_monday() -> None:
    rows = analysis.row_for_day(analysis.read_data(), "Monday")

    assert len(rows) == 1
    assert rows["condition"].iloc[0] == "Sunny"
    assert rows["temp"].iloc[0] == 12


def test_row_for_day_gives_an_empty_result_for_an_unknown_day() -> None:
    assert analysis.row_for_day(analysis.read_data(), "Funday").empty


def test_hottest_row_is_the_row_of_sunday() -> None:
    rows = analysis.hottest_row(analysis.read_data())

    assert len(rows) == 1
    assert rows["day"].iloc[0] == "Sunday"
    assert rows["temp"].iloc[0] == 24


def test_day_in_fahrenheit_converts_monday() -> None:
    assert analysis.day_in_fahrenheit(analysis.read_data(), "Monday") == pytest.approx(
        53.6
    )


def test_day_in_fahrenheit_raises_value_error_for_an_unknown_day() -> None:
    with pytest.raises(ValueError, match="Funday"):
        analysis.day_in_fahrenheit(analysis.read_data(), "Funday")


def test_csv_and_pandas_readers_agree_on_the_temperatures() -> None:
    pandas_temps = analysis.to_temp_list(analysis.read_data())

    assert pandas_temps == csv_reader.read_temperatures()


def test_read_data_reads_a_small_file_through_the_path_argument(
    small_csv: Path,
) -> None:
    for path in (small_csv, str(small_csv)):
        data = analysis.read_data(path)

        assert len(data) == 2
        assert analysis.to_temp_list(data) == [3, -4]
        assert analysis.max_temp(data) == 3
        assert analysis.day_in_fahrenheit(data, "Tuesday") == pytest.approx(24.8)
