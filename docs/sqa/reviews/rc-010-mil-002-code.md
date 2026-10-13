# RC-010: Code review of MIL-002 (the csv reader: read_rows and read_temperatures)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the source and tests that [MIL-002] delivers (the csv reader: read_rows and read_temperatures)
- Checklist used: [QC-PY-001]
- Scope: full review of the files changed on the branch of the milestone
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the assistant also wrote the code; the review of the files was done by the `python-developer` agent of the session)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `csv_reader`, `read_rows`, `read_temperatures`, `small_csv` are `snake_case`; no new constant. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names say what they return (`read_rows`, `read_temperatures`, `data_rows`); `row` and `file` are tiny-scope names from the lecture. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `python -m ruff check src tests` and `python -m ruff format --check src tests` exit 0; no `noqa`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | `read_rows(path: Path | str = DATA_FILE) -> list[list[str]]` and `read_temperatures(...) -> list[int]`; the tests are annotated `-> None`. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | N-A | The module raises and catches nothing; a missing file raises `FileNotFoundError` and a non-number raises `ValueError` to the caller, which is the lecture's behaviour. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | The only default is an immutable `DATA_FILE`; no builtin is shadowed (`file` is not a builtin in Python 3). |
| 7 | Files, locks and connections are managed with context managers | Pass | The file is opened with `with open(...)` in `read_rows`; no other file is opened. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module docstring and Doxygen `@brief`, `@param`, `@return` on both functions; `doxygen Doxyfile` exits 0 with no warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | The module neither logs nor prints. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists (a learning project of this size, recorded in the open issues of [PP-001]); the two functions trace to the first lecture and to the tasks of [MIL-002]. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_csv_reader.py` has 8 tests named for behaviour (header included, temperatures as `int`, header skipped, small file in `tmp_path`, default path from another folder, `path` override, no `pandas` import in a fresh interpreter); none depends on order or the network; `pytest` reports 14 passed. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `python -m mypy` runs with `strict = true`: no issues in 6 source files; no `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | The module imports only the standard library; `dependencies = []` is unchanged. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The file name, the encoding and the temperature position are read from `constants.py`; the temperatures are read through `read_rows`, so the reading is written once. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `csv_reader` imports `csv`, `pathlib` and `weather.constants`; no import cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Two small functions, each with one reason to change; no class hierarchy. |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable. Assessed on 2026-10-13 by the assistant that wrote the code, as stand-in for S01 in autonomous mode. Mode: autonomous, not independent. The pull request is the second look.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this `Go` in the run summary or on the pull request if the stand-in decision is not wanted | S01 | 2026-10-23 |

---

[MIL-002]: ../../milestones/mil-002-read-with-csv.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[PP-001]: ../../project-plan.md
