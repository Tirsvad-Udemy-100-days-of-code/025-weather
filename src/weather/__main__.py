## @file __main__.py
#  @brief Command line of the weather data project: `python -m weather`.
#
#  Prints the results of both lectures in the order of the lectures. The csv
#  part needs no third-party package; the pandas part needs the `pandas` extra.
#  A file is written only when `--export PATH` is given.

"""Prints the results of the weather lectures; run with `python -m weather`."""

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from weather.constants import MONDAY, PANDAS_MISSING_MESSAGE
from weather.csv_reader import read_rows, read_temperatures

## @brief Value that `main` returns when the run succeeded.
EXIT_OK = 0

## @brief Value that `main` returns when the optional pandas extra is missing.
EXIT_PANDAS_MISSING = 1


def _build_parser() -> argparse.ArgumentParser:
    """! @brief Build the command line parser with its one optional flag.

    @return The parser of `python -m weather`.
    """
    parser = argparse.ArgumentParser(
        prog="weather",
        description="Print the results of the weather data lectures.",
    )
    parser.add_argument(
        "--export",
        metavar="PATH",
        type=Path,
        default=None,
        help="also write the scores table to this CSV file",
    )
    return parser


def _print_csv_part() -> None:
    """! @brief Print the rows and temperatures read with the csv library."""
    print("Rows (csv library):")
    for row in read_rows():
        print(row)
    print(f"Temperatures (csv library): {read_temperatures()}")


def _print_pandas_part(export_path: Path | None) -> None:
    """! @brief Print the pandas results and export the scores when asked.

    @param export_path File to write the scores table to; `None` writes nothing.
    @throws ImportError When `pandas` is not installed.
    """
    # Imported here so that the csv part runs without the optional extra.
    from weather.analysis import (
        average_temp,
        average_temp_mean,
        day_in_fahrenheit,
        hottest_row,
        max_temp,
        read_data,
        row_for_day,
        to_data_dict,
        to_temp_list,
    )
    from weather.export import create_scores_frame, export_frame

    data = read_data()
    print(f"Data frame (pandas):\n{data}")
    print(f"Data dict: {to_data_dict(data)}")
    print(f"Temp list: {to_temp_list(data)}")
    print(f"Average temperature (sum / len): {average_temp(data)}")
    print(f"Average temperature (mean): {average_temp_mean(data)}")
    print(f"Maximum temperature: {max_temp(data)}")
    print(f"Row of {MONDAY}:\n{row_for_day(data, MONDAY)}")
    print(f"Hottest row:\n{hottest_row(data)}")
    print(f"{MONDAY} in Fahrenheit: {day_in_fahrenheit(data, MONDAY)}")
    scores = create_scores_frame()
    print(f"Scores frame (from a dictionary):\n{scores}")
    if export_path is not None:
        export_frame(scores, export_path)
        print(f"Scores frame exported to: {export_path}")


def main(argv: Sequence[str] | None = None) -> int:
    """! @brief Print the results of the lectures and optionally export a table.

    @param argv The command line arguments; `sys.argv[1:]` when `None`.
    @return `0` on success, `1` when the pandas extra is not installed.
    """
    args = _build_parser().parse_args(argv)
    _print_csv_part()
    try:
        _print_pandas_part(args.export)
    except ImportError as error:
        if error.name != "pandas":
            raise
        print(PANDAS_MISSING_MESSAGE, file=sys.stderr)
        return EXIT_PANDAS_MISSING
    return EXIT_OK


if __name__ == "__main__":
    raise SystemExit(main())
