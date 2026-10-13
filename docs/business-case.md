# Business Case: Weather Data (Day 25)

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [DICT-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-001 (Go) | [165e91a] |

---

## Executive Summary

Weather Data (Day 25) is the day-25 assignment of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*: reading comma-separated values (CSV) data in Python with the weather data of one week as the example. The first lecture reads `weather_data.csv` with Python's built-in `csv` library, collects the temperatures as whole numbers, and then shows how the `pandas` library does the same in one line. The second lecture introduces the two data structures of pandas, `DataFrame` (a table) and `Series` (a column), converts them to a dictionary and a list, computes the average and the maximum temperature, selects rows by a condition (the row of Monday, the row of the hottest day, Monday's temperature in Fahrenheit), creates a `DataFrame` from a dictionary, and exports it to a CSV file.

This repository turns both lectures into one small, tested and documented Python package with a command-line entry point, and gives it the identity of a repository: name, README, description, topics, a wiki in English, Danish and Bahasa Melayu, and a screenshot. The work is planned in five milestones, each delivered by one branch and one pull request.

## Methodological and Standards Foundation

- **Process:** the Software Quality Assurance (SQA) and Quality Criteria (QC) framework mounted at `framework/`: Business Case, Stakeholder Analysis, Project Plan, milestones, tasks synced as issues, then code, each step reviewed before the next.
- **Quality model:** ISO/IEC 25010:2023; every QC criterion is tagged with a characteristic of it.
- **Code:** Python Enhancement Proposals (PEP) 8, 257 and 484, reviewed against `QC-PY-001`; comments in Doxygen style; tests with pytest.
- **Domain terms:** the lectures' own terms and names, recorded in the Domain Dictionary [DICT-001]: CSV, row, column, `DataFrame`, `Series`, `read_csv`, `to_dict`, `to_list`, `mean`, `max`, `to_csv`.

## Problem Statement

- The lectures work in one script with scratch variables; a participant who wants to compare solutions or re-run a step has to edit the script.
- Reading a CSV file with the `csv` library is easy to get subtly wrong: the header row is data to the reader, every value is a string, and the file path depends on the current working directory.
- The `pandas` library is a large dependency; a repository that needs it to run any code at all is heavy for a visitor who only wants to see the `csv` part.
- A repository without a description, topics, README, wiki or a picture of the result is hard to find and to judge for the people who browse for ideas.

## Business Opportunity

A finished, reproducible repository shows the path from the day-25 lectures to documented, tested code and lets the `csv` way and the `pandas` way be compared side by side on the same file. It can be shared with, and compared against, the solutions of other participants.

## Objectives

| # | Objective |
| --- | --- |
| 1 | Provide the weather data of the lecture: `weather_data.csv` with the columns `day`, `temp` and `condition` for Monday to Sunday, kept in the repository |
| 2 | Deliver the `csv` part of the lecture: read the file with the built-in `csv` library into a list of rows and extract the temperatures as whole numbers, leaving out the header row |
| 3 | Deliver the `pandas` reading of the lecture: read the file with `pandas.read_csv`, and show that the result is a `DataFrame` and that a column of it is a `Series` |
| 4 | Deliver the conversions of the lecture: `DataFrame.to_dict()` and `Series.to_list()` |
| 5 | Deliver the computations of the lecture: the average temperature by sum and length and by `Series.mean()`, and the maximum temperature by `Series.max()` |
| 6 | Deliver the row selection of the lecture: the row of a given day (Monday), the row of the hottest day, and the temperature of a day converted to Fahrenheit (`temp * 9 / 5 + 32`) |
| 7 | Deliver the creation and export of the lecture: build a `DataFrame` from a dictionary (`students` and `scores`) and write it to a CSV file with `DataFrame.to_csv` |
| 8 | Keep the code simple to read and the names of the lectures (`data`, `temperatures`, `temp_list`, `data_dict`, `average_temp`, `monday`, `to_dict`, `to_list`, `mean`, `max`, `to_csv`), constants in `constants.py` |
| 9 | Provide a reproducible environment: Python 3.13 or newer, a local `.venv`, a `pyproject.toml`; the `csv` part runs with zero runtime dependencies and `pandas` is an optional extra |
| 10 | Prove the behaviour with pytest tests that use temporary files and never overwrite a file of the user |
| 11 | Document the project: Doxygen comments in the source with a `Doxyfile`, and a README with set-up instructions for Windows PowerShell, Linux Debian and macOS |
| 12 | Keep every step traceable: one branch and one pull request per milestone, each pull request closing the issues it completes |
| 13 | Publish the repository with a description and topics, and a wiki in English, Danish and Bahasa Melayu |
| 14 | Show the result in a real screenshot of the program running in a terminal, kept in the repository and shown in the README and on the wiki |

## Scope

### In Scope

- The two day-25 lectures on reading CSV data and on `DataFrame` and `Series`, as listed in the objectives.
- The data file `weather_data.csv` that S01 downloaded for the lecture, adopted unchanged.
- Constants in `constants.py`; source in `src/`, tests in `tests/`, documents in `docs/`.
- `pyproject.toml`, Python `.gitignore`, `Doxyfile`, `README.md` following the Product Owner's template, a continuous integration (CI) workflow.
- Repository description and topics on the git host.
- A wiki in English, Danish and Bahasa Melayu, in the form of the wiki of `TirSystem/github-action`.
- A screenshot of the program running in a terminal, kept in `docs/images/` and shown in the README and on the three wiki pages.

### Out of Scope

- The later pandas lessons the lecturer announces (NumPy, Matplotlib, plots, aggregation beyond the lectures).
- Reading from the internet, a database or a spreadsheet; creating the Google Sheets document of the lecture.
- A graphical user interface.
- Packaging for or publishing to the Python Package Index (PyPI).
- A tool in the repository that takes the screenshot: the screenshot is taken once with a one-off script outside the repository.
- Using or testing the tokens in `.env`; the file is for personal use only and is never imported by the project.

## Expected Benefits

### Tangible Benefits

- A finished day-25 solution that runs with one command after the README steps, and whose `csv` part needs nothing to install.
- A test suite that runs in continuous integration and never touches a file of the user.
- Generated source documentation.
- A repository page with description, topics, README, a three-language wiki and a screenshot.

### Intangible Benefits

- Practice with the `csv` library and the basic `pandas` structures, which is the aim of the lectures.
- A pattern for the following days of the course.
- Confidence from a step-by-step, reviewed delivery.

## Strategic Alignment

The project supports the participant's goal of finishing the bootcamp with repositories that other people can read, run and learn from, and it exercises the framework's rule that planning, review and code stay in step.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The data file is the lecture's | `weather_data.csv` has the header `day,temp,condition` and 7 data rows, Monday to Sunday | Test of the file; review |
| 2 | The `csv` reader is correct | Temperatures read as `[12, 14, 15, 14, 21, 22, 24]`, all `int`, header skipped | Matching tests |
| 3 | The `pandas` reader is correct | `read_csv` returns a `DataFrame` with 7 rows; its `temp` column is a `Series`; `to_list` gives the same temperatures as the `csv` reader | Matching tests |
| 4 | The computations are correct | Average is 17.428... (the manual and the `mean` way agree), maximum is 24 | Matching tests |
| 5 | The row selection is correct | The Monday row has `Sunny` and 12; the hottest day is Sunday; Monday in Fahrenheit is 53.6 | Matching tests |
| 6 | Create and export work | A `DataFrame` made from the `students`/`scores` dictionary is written to a CSV file and reads back equal | Matching tests with `tmp_path` |
| 7 | Tests are green | 100% of tests pass; 0 tests write outside a temporary directory | `pytest` exit code 0 locally and in CI |
| 8 | The set-up steps work | A fresh clone reaches a green `pytest` by following the README alone, on Windows PowerShell (by S01) and on Linux (by CI) | One run per operating system, recorded in the pull request |
| 9 | Source documentation builds | `doxygen Doxyfile` ends with 0 warnings | Doxygen output |
| 10 | The `csv` part needs no dependency | `[project].dependencies` is empty and the `csv` reader imports without `pandas` installed | `pyproject.toml`; a test of the import |
| 11 | Steps are traceable | 5 of 5 milestones merged by pull request, each description with one `Closes #N` line per completed issue | Pull request list and issue states |
| 12 | The repository page is complete | Non-empty description, at least 5 topics, and the wiki pages `Home`, `Home.da` and `Home.ms` | Git host |
| 13 | The result is shown in a real screenshot | `docs/images/weather-run.png` is a capture of a terminal that runs the program; the README and the three wiki pages show it, and its address on `main` answers HTTP 200 with an image | The file, the README and the wiki, checked against the Go/No-Go list of [MIL-005] |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| `pandas` is a heavy dependency and has to support Python 3.13 | Installation fails or is slow | `pandas` is an optional extra, the `csv` part runs without it; the pin is a lower bound only and is checked in CI |
| Debian 12 ships Python 3.11, below the required 3.13 | Linux set-up fails | README states Debian 13 or newer, or a separately installed Python 3.13 |
| The data file path depends on the working directory | The program finds no file when started elsewhere | The default path is resolved against the package folder, not the working directory; the path is a parameter |
| A test overwrites a file of the user | The user loses data | The export takes a path; tests pass a temporary path (pytest `tmp_path`) |
| Author and reviewer are the same person (S01) | A defect can pass review unnoticed | Review against the QC checklists, record each review as an `RC-*`, and let the pull request be the second look |
| The lectures are available only as the summaries in the request | The code differs from the video | S01 compares the finished program with the video at the [MIL-003] and [MIL-004] Go/No-Go |
| Tokens in `.env` leak into the repository | Credentials exposed | `.env` is in `.gitignore`, is never imported, and is not part of any task |
| The wiki publish workflow needs a secret of the organization that may be missing | The wiki stays empty | The pages are files in `wiki/` of the pull request; a missing secret is reported, not worked around |
| The screenshot is a capture of a real terminal window, which needs a display | It cannot be repeated in CI | It is taken once on S01's machine with a one-off script outside the repository and committed as a file |

## Assumptions

- Python 3.13 or newer is available on the machines that run the program.
- S01 is the only person who reviews and accepts artifacts.
- The git host is the Tirsvad Gitea instance, and its issues and milestones are used for tracking.
- The two lecture summaries in the request are the specification of day 25; the video is the tie-breaker when a detail is missing.
- `weather_data.csv` from S01's download folder holds the data of the lecture and is adopted unchanged.
- The wiki of the repository is enabled and has no page yet.

## Constraints

- Python 3.13 or newer, in a virtual environment (`venv`).
- pytest for tests; `constants.py` for constants; `pyproject.toml` for project configuration; a Python `.gitignore`; Doxygen comments in the source and a `Doxyfile`.
- Folder structure `src/`, `tests/`, `docs/`.
- No runtime dependencies unless needed; `pandas` is needed only for the second half of the lectures and is therefore an extra.
- Plan window from 2026-10-14 to 2026-10-23 (proposed, see [PP-001]).
- S01 switched on autonomous mode in chat on 2026-10-13: S01's acceptance of the plan is the request to commit, push, open and merge the pull requests; the assistant's reviews are then not independent (see `AGENTS.md`, Modes).
- The plan gate holds: no file under `src/` or `tests/` before an accepted, reviewed milestone that lists the task.

## Cost–Benefit Assessment

The assessment is qualitative on purpose: this is an unpaid learning project with one participant, so money does not measure either side.

| Costs | Benefits |
| --- | --- |
| About eight days of S01's spare time, most of it review of the planning documents | A finished and shareable repository (objectives 1 to 14) |
| `pandas`, Doxygen and pytest as tools | A comparison of the `csv` and the `pandas` way, source documentation and automatic checks |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Wants a correct, tested and documented solution of the assignment: objectives 1 to 14 |
| S02 | Needs readable, runnable code with the lectures' names and README instructions (objectives 2 to 9 and 11) |
| S03 | Needs a clear repository page and as little as possible to install (objectives 9, 11, 13 and 14) |

## Recommendation

Proceed — the work is small (two lectures, a handful of functions, tests, documentation and publishing), the cost is about eight days of the Product Owner's spare time, and the result is a reusable, documented repository.

---

[SA-001]: ./stakeholder-analysis.md
[DICT-001]: ./dictionary.md
[PP-001]: ./project-plan.md
[MIL-003]: ./milestones/mil-003-pandas-analysis.md
[MIL-004]: ./milestones/mil-004-create-and-export.md
[MIL-005]: ./milestones/mil-005-screenshot-wiki-and-finish.md
[165e91a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-weather/commit/165e91a0183c6351fbfdad53b050bb2918275e6d
