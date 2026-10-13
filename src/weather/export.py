## @file export.py
#  @brief Creates a `DataFrame` from a dictionary and exports it to a CSV file.
#
#  This is the end of the second lecture: the table of students and scores is
#  built from a dictionary and written with `DataFrame.to_csv`. Nothing is
#  written unless `export_frame` is called with a path or its default name.

"""Creates a DataFrame from a dictionary and exports it to a CSV file."""

from pathlib import Path

import pandas

from weather.constants import (
    COLUMN_SCORES,
    COLUMN_STUDENTS,
    EXPORT_FILE_NAME,
    SCORES,
    STUDENTS,
)


def create_scores_frame() -> pandas.DataFrame:
    """! @brief Create the table of students and scores from a dictionary.

    @return A table with the columns `students` and `scores`, one row per student.
    """
    data_dict = {COLUMN_STUDENTS: list(STUDENTS), COLUMN_SCORES: list(SCORES)}
    return pandas.DataFrame(data_dict)


def export_frame(frame: pandas.DataFrame, path: Path | str = EXPORT_FILE_NAME) -> None:
    """! @brief Write a table to a CSV file, the row index included.

    @param frame The table to write.
    @param path Path of the file to write; `new_data.csv` in the working folder
           by default.
    """
    frame.to_csv(path)
