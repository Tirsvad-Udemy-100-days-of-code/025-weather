# MIL-005: Screenshot, wiki and finish

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-005 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-008 (Go) | pending |

---

## Purpose

This gate decides whether the repository is finished for S02 and S03: a real screenshot of the program running, shown in the README and on a wiki in English, Danish and Bahasa Melayu, and the README checked against the finished program. The work is delivered on the branch `mil-005-screenshot-wiki-and-finish` and one pull request.

## Deliverable

`docs/images/weather-run.png`, the README Run section with the screenshot, and the wiki pages `wiki/Home.md`, `wiki/Home.da.md`, `wiki/Home.ms.md` and `wiki/_Sidebar.md`, in the form of the wiki of `TirSystem/github-action`.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | The screenshot is real | `docs/images/weather-run.png` is a capture of a terminal window in which `python -m weather` has run, and shows the average and the maximum temperature | A drawn or edited picture, or one that does not show the output |
| 2 | The README shows it | The Run section contains the image with alternative text | The image is missing or its path is broken |
| 3 | The wiki exists in three languages | `Home.md` (English), `Home.da.md` (Danish) and `Home.ms.md` (Bahasa Melayu) exist, each with description, functions, how to run it and the screenshot, and `_Sidebar.md` links all three | A page or a language is missing |
| 4 | The wiki refers to the screenshot on `main` | The address of the image on `main` answers HTTP 200 with an image content type | Any other status |
| 5 | The README steps work from a fresh clone | The commands of Set up, Run and Run the tests for Windows PowerShell end with a green `pytest` and the printed results | A command fails |
| 6 | Doxygen still builds | `doxygen Doxyfile` ends with 0 warnings | Any warning |
| 7 | The repository page is still complete | Non-empty description and at least 5 topics on the git host | Description empty or fewer than 5 topics |
| 8 | Every milestone is merged and its issues are closed | MIL-001 to MIL-004 pull requests merged; every issue of them closed | An open issue of an earlier milestone |
| 9 | The code and documents are reviewed | `RC-*` records have the verdict `Go` | Verdict `No-Go` or `Go-with-conditions` |
| 10 | No secret is in the change | `.env` is not tracked and no token appears in any changed file | A token is found in the diff |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-004] accepted and merged | The screenshot shows the finished program |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 11: README with set-up instructions | [BC-001], criterion 8 in Success Criteria |
| Objective 13: repository page and wiki | [BC-001], criterion 12 in Success Criteria |
| Objective 14: screenshot | [BC-001], criterion 13 in Success Criteria |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-23 — last of five gateways, the end of the plan of [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Take the screenshot of the program running | Run `python -m weather` in a terminal window and capture that window once, with a one-off script outside the repository, into `docs/images/weather-run.png`. Say in the pull request how it was taken. Serves objective 14. | No | |
| 2 | Show the screenshot in the README | Add the image to the Run section of `README.md` and finish the Run section against the finished program (all commands, with the `--export` flag). Serves S02 and S03. | No | |
| 3 | Write the wiki in English, Danish and Bahasa Melayu | Write `wiki/Home.md`, `wiki/Home.da.md`, `wiki/Home.ms.md` and `wiki/_Sidebar.md` in the form of the wiki of `TirSystem/github-action`, each page with the description, the functions of the lectures, how to run it and the screenshot by its address on `main`. Serves objective 13. | No | |
| 4 | Verify the finished repository end to end | In a fresh clone follow the README on Windows PowerShell: set-up, run, tests, Doxygen. Check the repository description and topics and that every earlier pull request is merged. Record the result in the pull request. Serves S01. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-004]: ./mil-004-create-and-export.md
