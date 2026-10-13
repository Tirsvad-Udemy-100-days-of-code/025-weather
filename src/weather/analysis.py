## @file analysis.py
#  @brief Reads and analyses the weather data file with `pandas`.
#
#  This is the second half of the lectures: the file is read in one line into a
#  `DataFrame`, converted to a dictionary and a list, and the average and
#  maximum temperature and the row selections are computed. This is the only
#  module of the package that imports `pandas`, which is an optional extra.

"""Reads and analyses the weather data file with pandas."""

from collections.abc import Hashable
from pathlib import Path
from typing import Any

import pandas

from weather.constants import (
    COLUMN_DAY,
    COLUMN_TEMP,
    DATA_FILE,
    FAHRENHEIT_DENOMINATOR,
    FAHRENHEIT_NUMERATOR,
    FAHRENHEIT_OFFSET,
)


def read_data(path: Path | str = DATA_FILE) -> pandas.DataFrame:
    """! @brief Read a weather CSV file into a `DataFrame`.

    @param path Path of the CSV file; the weather data file by default.
    @return The table, one row per day, with the columns of the file.
    """
    return pandas.read_csv(path)


def to_data_dict(data: pandas.DataFrame) -> dict[Hashable, Any]:  # Any: cell values
    """! @brief Convert the table to a dictionary of columns.

    @param data The weather table.
    @return A dictionary that maps each column name to its values by row index.
    """
    return data.to_dict()


def to_temp_list(data: pandas.DataFrame) -> list[int]:
    """! @brief Convert the temperature column to a list.

    @param data The weather table.
    @return The temperatures in row order.
    """
    return data[COLUMN_TEMP].to_list()


def average_temp(data: pandas.DataFrame) -> float:
    """! @brief Compute the average temperature from the sum and the length.

    @param data The weather table.
    @return The average temperature.
    """
    temp_list = to_temp_list(data)
    return sum(temp_list) / len(temp_list)


def average_temp_mean(data: pandas.DataFrame) -> float:
    """! @brief Compute the average temperature with `Series.mean()`.

    @param data The weather table.
    @return The average temperature.
    """
    return float(data[COLUMN_TEMP].mean())


def max_temp(data: pandas.DataFrame) -> int:
    """! @brief Find the highest temperature.

    @param data The weather table.
    @return The maximum of the temperature column.
    """
    return int(data[COLUMN_TEMP].max())


def row_for_day(data: pandas.DataFrame, day: str) -> pandas.DataFrame:
    """! @brief Select the rows of one day.

    @param data The weather table.
    @param day Name of the day, such as `Monday`.
    @return The matching rows; empty when the day is not in the table.
    """
    return data.loc[data[COLUMN_DAY] == day]


def hottest_row(data: pandas.DataFrame) -> pandas.DataFrame:
    """! @brief Select the row or rows with the highest temperature.

    @param data The weather table.
    @return The rows whose temperature equals the maximum.
    """
    return data.loc[data[COLUMN_TEMP] == max_temp(data)]


def day_in_fahrenheit(data: pandas.DataFrame, day: str) -> float:
    """! @brief Convert the temperature of one day from Celsius to Fahrenheit.

    @param data The weather table.
    @param day Name of the day, such as `Monday`.
    @return The temperature in degrees Fahrenheit.
    @throws ValueError When the day is not in the table exactly once.
    """
    rows = row_for_day(data, day)
    if len(rows) != 1:
        raise ValueError(f"Expected exactly one row for day {day!r}, got {len(rows)}")
    celsius = int(rows[COLUMN_TEMP].iloc[0])
    return celsius * FAHRENHEIT_NUMERATOR / FAHRENHEIT_DENOMINATOR + FAHRENHEIT_OFFSET
