# RC-012: Code review of MIL-004 (create and export a DataFrame, and the main flow)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: the source and tests that [MIL-004] delivers (create and export a DataFrame, and the main flow)
- Checklist used: [QC-PY-001]
- Scope: full review of the files changed on the branch of the milestone
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the assistant also wrote the code; the review of the files was done by the `python-developer` agent of the session)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | `export`, `create_scores_frame`, `export_frame`, `main`, `EXIT_OK`, `COLUMN_STUDENTS` follow PEP 8 casing; the private helpers start with `_`. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`_print_csv_part`, `_print_pandas_part`, `PANDAS_MISSING_MESSAGE`); `data_dict` and `scores` are the lecture's names. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` exit 0. The only suppressions are the two `# noqa: E402` after `pytest.importorskip("pandas")` in the test modules, explained by the guard. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | Every function is annotated: `create_scores_frame() -> DataFrame`, `export_frame(...) -> None`, `main(argv: Sequence[str] | None = None) -> int`, the helpers and the tests. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | `main` catches `ImportError` only when `error.name == "pandas"` and re-raises every other one; nothing is swallowed. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | The defaults are immutable (`EXPORT_FILE_NAME`, `None`); no builtin is shadowed. |
| 7 | Files, locks and connections are managed with context managers | N-A | The modules open no file themselves; `DataFrame.to_csv` opens and closes the file. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Module docstrings and Doxygen `@brief`, `@param`, `@return`, `@throws` on every function, private helpers included; `doxygen Doxyfile` exits 0 with no warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | The `print` calls of `__main__` are the program's output, the purpose of the command (as in the lectures); the missing-extra diagnostic goes to stderr; no secret or personal data is printed. There is no logging to replace. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No Design Class Diagram exists (a learning project of this size, recorded in the open issues of [PP-001]); the functions trace to the second lecture and to the tasks of [MIL-004]. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `tests/test_export.py` and `tests/test_main.py` cover the Go/No-Go criteria of [MIL-004]: the frame's columns and values, the round trip through `tmp_path`, the default name only in the temporary working folder, the printed results, no file without `--export`, the missing-pandas path; `pytest` reports 39 passed; none depends on order or the network. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | `python -m mypy` runs with `strict = true`: no issues in 12 source files; no new `Any`. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No dependency added; `pandas` stays in the extras and is imported only in `analysis` and `export`; `__main__` imports them inside a function so the csv part runs without it. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The lecture's dictionary values, column names, the day and the message are constants in `constants.py`; the export name is defined once. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `__main__` (delivery) imports `csv_reader`, `analysis`, `export` and `constants`; none of them imports `__main__`; no cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | `create_scores_frame`, `export_frame` and `main` each have one reason to change; the printing is split into small helpers; no class hierarchy. |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable. Assessed on 2026-10-13 by the assistant that wrote the code, as stand-in for S01 in autonomous mode. Mode: autonomous, not independent. The pull request is the second look.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Challenge this `Go` in the run summary or on the pull request if the stand-in decision is not wanted | S01 | 2026-10-23 |

---

[MIL-004]: ../../milestones/mil-004-create-and-export.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[PP-001]: ../../project-plan.md
