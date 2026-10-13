# MIL-001: Project foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-004 (Go) | [165e91a] |

---

## Purpose

This gate decides whether the repository has the files that carry no program logic yet: configuration, ignore rules, constants, README, source documentation settings, the continuous integration workflow, and the repository description and topics. The work is delivered on the branch `mil-001-project-foundation` and one pull request.

## Deliverable

`pyproject.toml`, the Python `.gitignore`, the package `src/weather/` with `__init__.py` and `constants.py`, `tests/test_constants.py`, `README.md` following the Product Owner's template, `Doxyfile`, and `.gitea/workflows/ci.yml`. The repository description and topics on the git host are set.

Proposed repository description and topics, for S01 to confirm by accepting the plan:

- Description: "Reading CSV weather data in Python with the csv library and pandas, day 25 of Udemy's 100 Days of Code bootcamp: DataFrame and Series, average, maximum, row selection, create and export. pytest tests, Doxygen docs, no runtime dependencies for the csv part."
- Topics: `100-days-of-code`, `csv`, `data-analysis`, `doxygen`, `education`, `pandas`, `pytest`, `python`, `python-bootcamp`, `udemy`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | In a fresh clone, `python -m venv .venv`, `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"` succeed in Windows PowerShell | All three commands exit 0 | Any command fails |
| 2 | `pytest` runs | Exit code 0, at least one test of `constants.py` | Failing test, or no test of `constants.py` |
| 3 | `pyproject.toml` states the Python version and the dependencies | `requires-python = ">=3.13"`, `dependencies = []`, an extra `pandas`, a `dev` extra with pytest, ruff, mypy and pandas, and a repository URL that names this repository | Any of the four is missing or different |
| 4 | The `.gitignore` protects local files | `git check-ignore .venv .env __pycache__ build` lists all four | One of them is not ignored |
| 5 | `constants.py` holds the file names and the Fahrenheit factors with Doxygen comments | Every value is an `UPPER_SNAKE` constant with a Doxygen comment | A value is missing or has no Doxygen comment |
| 6 | `doxygen Doxyfile` builds the source documentation | Ends with 0 warnings and writes HTML for `src/` | Any warning, or no output |
| 7 | The README follows the Product Owner's template | Every section title of the template in the given order (Requirements, Set up with Windows powershell, Linux debian and MacOS, Run, Run the tests, Continuous integration, Build the source documentation, Project layout, License), with commands for the three systems | A heading is missing or out of order, or a section has no commands |
| 8 | The CI workflow exists | `.gitea/workflows/ci.yml` installs `.[dev]` and runs `pytest`, `ruff` and `mypy` on Python 3.13, and nothing under `.github/workflows` exists | No workflow, or it does not run the tests, or a file exists under `.github/workflows` |
| 9 | The repository page is complete | Description is non-empty and there are at least 5 topics on the git host | Description empty or fewer than 5 topics |
| 10 | The code is reviewed | `RC-*` against `QC-PY-001` has the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |
| 11 | No secret is in the change | `.env` is not tracked and no token appears in any changed file | A token is found in the diff |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [PP-001] accepted | The plan schedules this gateway; the plan-first gate needs it before any code |
| This milestone accepted with a `Go` review | The plan-first gate allows no file under `src/` or `tests/` before that |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 9: reproducible environment, `csv` part without dependencies | [BC-001], criteria 8 and 10 in Success Criteria |
| Objective 10: tests with temporary files | [BC-001], criterion 7 in Success Criteria |
| Objective 11: Doxygen and README | [BC-001], criteria 8 and 9 in Success Criteria |
| Objective 13: repository page | [BC-001], criterion 12 in Success Criteria |
| Objective 12: traceable steps | [BC-001], criterion 11 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-15 — first of five gateways, inside the plan of [PP-001] that ends 2026-10-23.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml for the Day 25 weather repository | Create `pyproject.toml` for the project `weather`: `requires-python = ">=3.13"`, an empty `dependencies` list, an optional extra `pandas`, a `dev` extra with pytest, ruff, mypy and pandas, the `src` layout for the package `weather`, the pytest settings, and a description and repository URL that name this repository and day 25. Serves objective 9. | No | |
| 2 | Add the Python .gitignore for the Day 25 weather repository | Add the Python `.gitignore`: bytecode, `.venv/`, build and packaging output, pytest, ruff, mypy and Doxygen caches. It also ignores `.env`, so the personal tokens can never be committed. | No | |
| 3 | Add constants.py and its test | Create `src/weather/__init__.py`, `src/weather/constants.py` and `tests/test_constants.py`. Every value (the data file name, the column names, the Fahrenheit factors, the export file name) is an `UPPER_SNAKE` constant with a Doxygen comment. Serves objective 8. | No | |
| 4 | Add the README for the Day 25 weather repository | Write `README.md` in the Product Owner's template. Document creating a local `.venv`, `python -m pip install --upgrade pip` and `python -m pip install -e ".[dev]"`, with Windows PowerShell, Linux Debian (Debian 13 or newer) and macOS. The Run section is finished in MIL-005. Serves S02 and S03. | No | |
| 5 | Add the Doxyfile for the Day 25 weather repository | Add a `Doxyfile` that reads `src/`, writes to `build/doxygen`, extracts documentation for Python and treats warnings as failures; the project brief names day 25. | No | |
| 6 | Add the continuous integration workflow | Add `.gitea/workflows/ci.yml`: check out, set up Python 3.13, upgrade `pip`, install `.[dev]`, run `pytest`, `ruff` and `mypy`. The file stays in `.gitea/workflows`, not `.github/workflows`. | No | |
| 7 | Set the repository description and topics | Set the description and at least 5 topics of this repository on the git host with the Gitea application programming interface (API), using `GITEA_TOKEN` from the personal `.env` file; the file is only read by the command, never imported, tested or tracked. Use the proposed text of the Deliverable section. Serves S03 and objective 13. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[165e91a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-weather/commit/165e91a0183c6351fbfdad53b050bb2918275e6d
