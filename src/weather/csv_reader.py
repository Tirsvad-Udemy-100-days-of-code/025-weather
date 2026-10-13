## @file csv_reader.py
#  @brief Reads the weather data file with Python's built-in `csv` library.
#
#  This is the first half of the first lecture: the rows are read with
#  `csv.reader` and the temperatures are converted to whole numbers. The module
#  needs no third-party dependency.

"""Reads the weather data file with the built-in csv library."""

import csv
from pathlib import Path

from weather.constants import DATA_FILE, FILE_ENCODING, TEMP_COLUMN_INDEX


def read_rows(path: Path | str = DATA_FILE) -> list[list[str]]:
    """! @brief Read every row of a CSV file, the header row included.

    @param path Path of the CSV file; the weather data file by default.
    @return The rows, each a list of strings, in file order.
    """
    with open(path, newline="", encoding=FILE_ENCODING) as file:
        return [row for row in csv.reader(file) if row]


def read_temperatures(path: Path | str = DATA_FILE) -> list[int]:
    """! @brief Read the temperatures of a weather CSV file as whole numbers.

    The first row is the header and is skipped.

    @param path Path of the CSV file; the weather data file by default.
    @return The temperature of each data row, in file order.
    """
    data_rows = read_rows(path)[1:]
    return [int(row[TEMP_COLUMN_INDEX]) for row in data_rows]
