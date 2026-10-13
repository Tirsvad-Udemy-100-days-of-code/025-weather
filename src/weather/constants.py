## @file constants.py
#  @brief Constants of the weather data project.
#
#  Every value that the day-25 lectures fix lives here, so that no other module
#  contains a magic string or number: the name of the data file, the names of
#  its columns, the factors of the Fahrenheit conversion and the name of the
#  exported file.

"""Constants of the weather data project, as fixed by the day-25 lectures."""

from pathlib import Path
from typing import Final

## @brief Folder of this package; the data file lies next to the modules.
PACKAGE_DIR: Final[Path] = Path(__file__).resolve().parent

## @brief Name of the weather data file of the lecture.
DATA_FILE_NAME: Final[str] = "weather_data.csv"

## @brief Full path of the weather data file, independent of the working folder.
DATA_FILE: Final[Path] = PACKAGE_DIR / DATA_FILE_NAME

## @brief Name of the file that the exported table is written to by default.
EXPORT_FILE_NAME: Final[str] = "new_data.csv"

## @brief Encoding of the CSV files that are read and written.
FILE_ENCODING: Final[str] = "utf-8"

## @brief Name of the column that holds the day of the week.
COLUMN_DAY: Final[str] = "day"

## @brief Name of the column that holds the temperature in degrees Celsius.
COLUMN_TEMP: Final[str] = "temp"

## @brief Name of the column that holds the weather condition, such as `Sunny`.
COLUMN_CONDITION: Final[str] = "condition"

## @brief Position of the temperature in a row that `csv.reader` returns.
TEMP_COLUMN_INDEX: Final[int] = 1

## @brief Numerator of the Celsius to Fahrenheit factor: `temp * 9 / 5 + 32`.
FAHRENHEIT_NUMERATOR: Final[int] = 9

## @brief Denominator of the Celsius to Fahrenheit factor: `temp * 9 / 5 + 32`.
FAHRENHEIT_DENOMINATOR: Final[int] = 5

## @brief Offset of the Celsius to Fahrenheit conversion: `temp * 9 / 5 + 32`.
FAHRENHEIT_OFFSET: Final[int] = 32
