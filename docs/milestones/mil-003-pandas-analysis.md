# MIL-003: Read and analyse with pandas

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-006 (Go) | pending |

---

## Purpose

This gate decides whether the pandas half of both lectures is delivered: the data file is read in one line, the `DataFrame` and `Series` are used, converted to a dictionary and a list, and the average and maximum temperature and the row selections are computed. The work is delivered on the branch `mil-003-pandas-analysis` and one pull request.

## Deliverable

`src/weather/analysis.py` with `read_data`, `to_data_dict`, `to_temp_list`, `average_temp`, `average_temp_mean`, `max_temp`, `row_for_day`, `hottest_row` and `day_in_fahrenheit`, the `pandas` extra in `pyproject.toml` used as designed, and `tests/test_analysis.py`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `read_data` returns a `DataFrame` | `isinstance(data, pandas.DataFrame)`, 7 rows, columns `day`, `temp`, `condition`; the body is one `pandas.read_csv` call | Another type, or a different row or column count |
| 2 | A column is a `Series` | `isinstance(data["temp"], pandas.Series)` | Another type |
| 3 | The conversions work | `to_data_dict(data)` has the keys `day`, `temp`, `condition`; `to_temp_list(data)` is `[12, 14, 15, 14, 21, 22, 24]` | A wrong key or value |
| 4 | The average is right two ways | `average_temp` (sum and length) and `average_temp_mean` (`Series.mean()`) both give 17.428571... | The two ways differ, or a wrong value |
| 5 | The maximum is right | `max_temp(data)` is 24 | A different value |
| 6 | Row selection is right | `row_for_day(data, "Monday")` is one row with `condition` `Sunny` and `temp` 12; `hottest_row(data)` is the row of Sunday | A wrong row or an empty result |
| 7 | Fahrenheit is right | `day_in_fahrenheit(data, "Monday")` is 53.6 | A different value |
| 8 | The `csv` part still needs no dependency | `dependencies = []` and `import weather.csv_reader` works without `pandas` | A dependency added, or `csv_reader` imports `pandas` |
| 9 | The `csv` and `pandas` readers agree | `to_temp_list(read_data())` equals `read_temperatures()` | The lists differ |
| 10 | Tests are green | `pytest` exit code 0 | A failing test |
| 11 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] accepted and merged | The data file and the `csv` reader are the reference for the agreement test |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3: reading with `pandas` | [BC-001], criterion 3 in Success Criteria |
| Objective 4: conversions | [BC-001], criterion 3 in Success Criteria |
| Objective 5: average and maximum | [BC-001], criterion 4 in Success Criteria |
| Objective 6: row selection and Fahrenheit | [BC-001], criterion 5 in Success Criteria |
| Objective 9: `pandas` is an extra | [BC-001], criterion 10 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-19 — third of five gateways, inside the plan of [PP-001] that ends 2026-10-23.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Read the weather data with pandas | Add `read_data(path)` in `src/weather/analysis.py`: one `pandas.read_csv` call returning the `DataFrame` `data`; the default path is the data file. `pandas` is imported only in this module. Serves objective 3. | No | |
| 2 | Convert the data to a dictionary and a list | Add `to_data_dict(data)` (`DataFrame.to_dict()`) and `to_temp_list(data)` (`data["temp"].to_list()`), as the lecture does. Serves objective 4. | No | |
| 3 | Compute the average and maximum temperature | Add `average_temp(data)` that returns the sum of `temp_list` divided by its length, and `average_temp_mean(data)` that uses `Series.mean()`, so the two ways of the lecture can be compared; add `max_temp(data)` with `Series.max()`. Serves objective 5. | No | |
| 4 | Select rows by a condition | Add `row_for_day(data, day)` (`data[data.day == day]`), `hottest_row(data)` (`data[data.temp == data.temp.max()]`) and `day_in_fahrenheit(data, day)` (`temp * 9 / 5 + 32`, factors from `constants.py`). Serves objective 6. | No | |
| 5 | Add the tests for the pandas analysis | Add `tests/test_analysis.py` for the criteria of this gateway, including that the two readers agree. The test module is skipped with `pytest.importorskip` when `pandas` is missing. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-002]: ./mil-002-read-with-csv.md
