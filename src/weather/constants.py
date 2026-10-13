## @file constants.py
#  @brief Constants of the weather data project.
#
#  Every value that the day-25 lectures fix lives here, so that no other module
#  contains a magic string or number: the name of the data file, the names of
#  its columns, the factors of the Fahrenheit conversion, the name of the
#  exported file, the table that is created from a dictionary and the message
#  for a missing optional dependency.

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

## @brief Name of the column that holds the student names of the lecture's table.
COLUMN_STUDENTS: Final[str] = "students"

## @brief Name of the column that holds the scores of the lecture's table.
COLUMN_SCORES: Final[str] = "scores"

## @brief Student names of the table that the lecture creates from a dictionary.
STUDENTS: Final[tuple[str, ...]] = ("Amy", "James", "Angela")

## @brief Scores of the students, in the order of `STUDENTS`.
SCORES: Final[tuple[int, ...]] = (76, 56, 65)

## @brief Name of the day that the main flow selects and converts.
MONDAY: Final[str] = "Monday"

## @brief Message printed when `pandas`, an optional extra, is not installed.
PANDAS_MISSING_MESSAGE: Final[str] = (
    "pandas is not installed; the pandas part needs the extra: "
    'pip install "weather[pandas]"'
)
