# Domain Dictionary: Weather Data (Day 25)

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version, reviewed in RC-003 (Go) | [165e91a] |

---

## Purpose and Scope

Maps each Product Owner (PO) term to its professional information technology (IT) term. PO language: `en` (domain `it`), from the registry's `Languages` section. The PO terms are the words of the day-25 lectures as the planning documents use them; the IT terms are the names in the code. The dictionary exists so that the planning documents use one word for one thing and so that S02 can find the lectures' names in the code.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| CSV file | en | `weather_data.csv` | The text file with one line per day and the values `day`, `temp` and `condition` separated by commas. | BC, SA, PP, MIL | PY |
| header row | en | first row of the file | The first line of the CSV file, which names the columns and is not data. | BC, PP, MIL | PY |
| row | en | `row` | The values of one day. | BC, SA, PP, MIL | PY |
| column | en | `Series` | The values of one name, for example `temp`, from every row. | BC, SA, PP, MIL | PY |
| table | en | `DataFrame` | The whole data of the file, as rows and columns, like a sheet in a spreadsheet. | BC, SA, PP, MIL | PY |
| temperature | en | `temp` | The temperature of a day in degrees Celsius, a whole number. | BC, SA, PP, MIL | PY |
| condition | en | `condition` | The weather of a day as a word, for example `Sunny`. | BC, SA, PP, MIL | PY |
| read with csv | en | `csv.reader` | Getting the rows of the CSV file into the program with Python's built-in `csv` library. | BC, SA, PP, MIL | PY |
| read with pandas | en | `pandas.read_csv` | Getting the table of the CSV file into the program with one call of the `pandas` library. | BC, SA, PP, MIL | PY |
| dictionary | en | `DataFrame.to_dict()` | Names mapped to values; the table is turned into one, and a table can also be made from one. | BC, PP, MIL | PY |
| list | en | `Series.to_list()` | The values of a column in order. | BC, PP, MIL | PY |
| average | en | `average_temp` | The sum of the temperatures divided by their number. | BC, SA, PP, MIL | PY |
| mean | en | `Series.mean()` | The average that `pandas` computes for a column, used to check the average that is computed by hand. | BC, PP, MIL | PY |
| maximum | en | `Series.max()` | The largest temperature of the column. | BC, PP, MIL | PY |
| select | en | `data[data.day == "Monday"]` | Getting the rows for which a condition holds. | BC, PP, MIL | PY |
| Fahrenheit | en | `temp * 9 / 5 + 32` | The temperature converted from Celsius to the Fahrenheit scale. | BC, PP, MIL | PY |
| export | en | `DataFrame.to_csv` | Writing a table to a CSV file. | BC, SA, PP, MIL | PY |
| screenshot | en | `docs/images/weather-run.png` | The picture of the program running in a terminal that the README and the wiki show. | BC, SA, PP, MIL | none |

## Rules

- The Business Case, Stakeholder Analysis, Project Plan and milestones use the PO term; the source code and its tests use the IT term.
- One IT term per PO term and one PO term per IT term; no synonyms.
- The planning documents use British spelling; identifiers follow the lectures and the libraries.
- A code identifier written in backticks in a planning document is an IT term and is allowed there.
- "Step" is not a PO term of the program. In the planning documents it means a step of the project (a task, a milestone).

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[165e91a]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-weather/commit/165e91a0183c6351fbfdad53b050bb2918275e6d
