# Weather Data (Day 25)

Reading CSV weather data in Python, first with the built-in `csv` library and then
with `pandas`. It is the day-25 assignment of Udemy's *100 Days of Code: The
Complete Python Pro Bootcamp*. The lectures read the weather of one week from
`weather_data.csv`, collect the temperatures as whole numbers, and then show how
`pandas` does the same in one line: a table is a `DataFrame` and a column of it is
a `Series`. They convert both to a dictionary and a list, compute the average and
the maximum temperature, select rows by a condition (the row of Monday, the row of
the hottest day, Monday's temperature in Fahrenheit), create a `DataFrame` from a
dictionary, and export it to a CSV file.

The `csv` part has no runtime dependencies; `pandas` is an optional extra. The code
keeps the names of the lectures (`data`, `temperatures`, `temp_list`, `data_dict`,
`average_temp`, `monday`, `to_dict`, `to_list`, `mean`, `max`, `to_csv`) so that you
can compare it with your own solution.

> **Status:** in progress. The project foundation (configuration, constants,
> documentation settings and continuous integration) is in place; the readers and
> the analysis follow in the next milestones, see `docs/project-plan.md`.

## Requirements

- Python 3.13 or newer.
- `git`, to clone the repository.
- Optional: [Doxygen](https://www.doxygen.nl/) to build the source documentation.
- No runtime dependencies. `pandas` (the optional extra `pandas`) is needed for the
  second half of the lectures and is installed by the `dev` extra, together with
  the development tools (`pytest`, `ruff`, `mypy`).

## Set up

Clone the repository, then create a local virtual environment `.venv` in its
root, upgrade `pip` and install the project with its development tools. The
`.venv` folder is ignored by git.

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-weather.git
cd 025-weather
```

### Windows powershell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run the activation script, allow scripts for this
window only with `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`
and activate again.

### Linux debian

Debian 13 or newer ships Python 3.13. On older releases install Python 3.13
separately.

```bash
sudo apt install python3 python3-venv
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### MacOS

```bash
brew install python@3.13
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

To install only what the `csv` part needs, leave out the extras:
`python -m pip install -e .`. To add `pandas` without the development tools use
`python -m pip install -e ".[pandas]"`.

## Run

With the virtual environment active, the program that prints the results of the
lectures is added in a later milestone (`python -m weather`); until then the
package can be imported:

```bash
python -c "from weather import constants; print(constants.DATA_FILE)"
```

## Run the tests

The tests write only into temporary folders.

```bash
pytest
```

The same checks that continuous integration runs:

```bash
python -m pytest
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy
```

## Continuous integration

`.gitea/workflows/ci.yml` runs on Gitea Actions on every push and on every pull
request. It sets up Python 3.13, upgrades `pip`, installs `.[dev]`, then runs
`pytest`, `ruff` (lint and format check) and `mypy`. It does not build the source
documentation: run `doxygen Doxyfile` yourself, as the next section shows.

The workflow lives in `.gitea/workflows` and not in `.github/workflows`, so
GitHub does not run it and pushing to a GitHub mirror needs no workflow
permission.

## Build the source documentation

The source is documented with Doxygen comments and the `Doxyfile` in the root.
Install Doxygen (`winget install DimitriVanHeesch.Doxygen` on Windows,
`sudo apt install doxygen` on Debian, `brew install doxygen` on macOS), then:

```bash
doxygen Doxyfile
```

The HTML is written to `build/doxygen/index.html`. A warning fails the build.

## Project layout

```text
.
├── .gitea/workflows/ci.yml    continuous integration (Gitea Actions)
├── docs/                      business case, plan, milestones, reviews
├── src/weather/               the package
│   ├── __init__.py
│   └── constants.py           every constant of the lectures
├── tests/                     pytest tests (conftest.py runs every test in a
│                              temporary folder)
├── Doxyfile                   source documentation settings
├── LICENSE
├── pyproject.toml             project configuration
└── README.md
```

## License

GNU Affero General Public License v3.0 only. See [LICENSE](LICENSE).
