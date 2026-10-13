# MIL-004: Create and export a DataFrame

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-007 (Go) | [165e91a] |

---

## Purpose

This gate decides whether the end of the second lecture is delivered: a `DataFrame` is created from a dictionary and exported to a CSV file, and the whole lecture can be run with one command that prints each result. The work is delivered on the branch `mil-004-create-and-export` and one pull request.

## Deliverable

`src/weather/export.py` with `create_scores_frame` and `export_frame`, `src/weather/__main__.py` so that `python -m weather` prints the results of both lectures, and `tests/test_export.py` and `tests/test_main.py`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | A `DataFrame` is created from a dictionary | `create_scores_frame()` has the columns `students` and `scores` and the lecture's values | Another shape or values |
| 2 | The frame is exported to CSV | `export_frame(frame, path)` writes the file; reading it back gives an equal frame | The file is missing or the content differs |
| 3 | Export never writes where it is not told to | The default file name is `new_data.csv` from `constants.py`, written to the path given; tests use only `tmp_path` | A test writes in the working directory |
| 4 | `python -m weather` prints the lecture's results | Output lists the rows, the temperatures, the average, the maximum, the Monday row, the hottest row and Monday in Fahrenheit; exit code 0 | A result is missing or the exit code is not 0 |
| 5 | The program does not write a file by itself | Running `python -m weather` in an empty folder leaves it empty, unless the flag `--export` with a path is given | A file appears without the flag |
| 6 | Tests are green | `pytest` exit code 0 | A failing test |
| 7 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] accepted and merged | The program prints what the analysis module computes |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 7: create and export | [BC-001], criterion 6 in Success Criteria |
| Objective 10: tests with temporary files | [BC-001], criterion 7 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-21 — fourth of five gateways, inside the plan of [PP-001] that ends 2026-10-23.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create a DataFrame from a dictionary | Add `create_scores_frame()` in `src/weather/export.py`: a dictionary `data_dict` with `students` and `scores` is turned into a `DataFrame` with `pandas.DataFrame`, as the lecture does. The values are constants. Serves objective 7. | No | |
| 2 | Export a DataFrame to a CSV file | Add `export_frame(frame, path)` that calls `DataFrame.to_csv(path)`; the default name `new_data.csv` is a constant. Serves objective 7. | No | |
| 3 | Add the main flow | Add `src/weather/__main__.py`: print the results of both lectures in the order of the lectures; export only when `--export <path>` is given. Serves objectives 2 to 7. | No | |
| 4 | Add the tests for create, export and the main flow | Add `tests/test_export.py` (round trip through `tmp_path`) and `tests/test_main.py` (output of `main` captured with `capsys`, nothing written without the flag). | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-003]: ./mil-003-pandas-analysis.md
[165e91a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-weather/commit/165e91a0183c6351fbfdad53b050bb2918275e6d
