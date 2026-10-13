"""Tests of the constants that the day-25 lectures fix."""

from weather import constants


def test_data_file_is_the_one_of_the_lecture() -> None:
    assert constants.DATA_FILE_NAME == "weather_data.csv"


def test_data_file_lies_next_to_the_modules_not_in_the_working_folder() -> None:
    assert constants.DATA_FILE.is_absolute()
    assert constants.DATA_FILE.parent == constants.PACKAGE_DIR
    assert constants.DATA_FILE.name == constants.DATA_FILE_NAME


def test_column_names_match_the_header_of_the_lecture() -> None:
    assert constants.COLUMN_DAY == "day"
    assert constants.COLUMN_TEMP == "temp"
    assert constants.COLUMN_CONDITION == "condition"


def test_temperature_is_the_second_value_of_a_row() -> None:
    assert constants.TEMP_COLUMN_INDEX == 1


def test_fahrenheit_factors_give_the_lecture_formula() -> None:
    celsius = 100
    fahrenheit = (
        celsius * constants.FAHRENHEIT_NUMERATOR / constants.FAHRENHEIT_DENOMINATOR
        + constants.FAHRENHEIT_OFFSET
    )
    assert fahrenheit == 212


def test_exported_file_has_the_name_of_the_lecture() -> None:
    assert constants.EXPORT_FILE_NAME == "new_data.csv"


def test_scores_table_has_the_columns_and_values_of_the_lecture() -> None:
    assert constants.COLUMN_STUDENTS == "students"
    assert constants.COLUMN_SCORES == "scores"
    assert constants.STUDENTS == ("Amy", "James", "Angela")
    assert constants.SCORES == (76, 56, 65)


def test_main_flow_uses_monday() -> None:
    assert constants.MONDAY == "Monday"


def test_missing_pandas_message_names_the_extra() -> None:
    assert 'pip install "weather[pandas]"' in constants.PANDAS_MISSING_MESSAGE
