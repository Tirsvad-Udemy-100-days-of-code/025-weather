# MIL-002: Read with the csv library

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-005 (Go) | [165e91a] |

---

## Purpose

This gate decides whether the first half of the first lecture is delivered: the weather data file is in the repository and its rows and temperatures are read with Python's built-in `csv` library, without any dependency. The work is delivered on the branch `mil-002-read-with-csv` and one pull request.

## Deliverable

`src/weather/weather_data.csv` (the lecture's file, adopted unchanged), `src/weather/csv_reader.py` with `read_rows` and `read_temperatures`, and `tests/test_csv_reader.py`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The data file is the lecture's | Header `day,temp,condition` and 7 data rows, Monday to Sunday, identical to the file S01 downloaded | A different header, row count or content |
| 2 | `read_rows` returns the rows as lists of strings | The first element is `["day", "temp", "condition"]`; 8 rows in all | Rows are not lists of strings or the header is lost |
| 3 | `read_temperatures` returns whole numbers without the header | `[12, 14, 15, 14, 21, 22, 24]`, every element an `int` | A string in the list, the header word, or a wrong value |
| 4 | The default path does not depend on the working directory | Running from another folder finds the file; a `path` argument overrides the default | The call fails when started elsewhere |
| 5 | The file is closed and opened with `with` | Review of `src/` finds no `open` outside `with` | A file left open |
| 6 | The module needs no dependency | `import weather.csv_reader` works with `pandas` not installed | An import of `pandas` in the module |
| 7 | Tests are green and use no file outside `tmp_path` | `pytest` exit code 0 | A failing test, or a write outside a temporary folder |
| 8 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] accepted and merged | The package, `constants.py` and the test set-up come from it |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 1: the data file | [BC-001], criterion 1 in Success Criteria |
| Objective 2: reading with `csv` | [BC-001], criteria 2 and 10 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-17 — second of five gateways, inside the plan of [PP-001] that ends 2026-10-23.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add the weather data file | Copy `weather_data.csv` from S01's download folder to `src/weather/weather_data.csv` unchanged (header `day,temp,condition`, 7 rows). Add its name to `constants.py`. Serves objective 1. | No | |
| 2 | Read the weather rows with the csv library | Add `read_rows(path)` in `src/weather/csv_reader.py`: open the file with `with`, read it with `csv.reader` and return the rows as a list of lists of strings, header included, as the lecture does. The default path is the data file next to the module. Serves objective 2. | No | |
| 3 | Extract the temperatures as integers | Add `read_temperatures(path)`: skip the header row, take the second value of each row and convert it with `int`, as the lecture does, returning the list `temperatures`. Serves objective 2. | No | |
| 4 | Add the tests for the csv reader | Add `tests/test_csv_reader.py`: the real file gives `[12, 14, 15, 14, 21, 22, 24]`, a small file in `tmp_path` gives its own values, the header is skipped, and importing the module needs no `pandas`. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-001]: ./mil-001-project-foundation.md
[165e91a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-weather/commit/165e91a0183c6351fbfdad53b050bb2918275e6d
