> Denne side er genereret fra README.md og wiki/. Ændringer her bliver overskrevet, næste gang wikien udgives.

> Den engelske side er den gældende; denne oversættelse følger den.

[English](Home) | Dansk | [Bahasa Melayu](Home.ms)

# Vejrdata (dag 25)

At læse CSV-vejrdata i Python. Det er opgaven fra dag 25 i Udemys *100 Days of Code: The Complete Python Pro Bootcamp*. Lektionerne læser en uges vejr fra `weather_data.csv` med Pythons indbyggede `csv`-bibliotek og samler temperaturerne som hele tal, og viser derefter, hvordan biblioteket `pandas` gør det samme på én linje. En tabel er en `DataFrame`, og en kolonne i den er en `Series`; begge kan omdannes til en ordbog og en liste, gennemsnits- og maksimumtemperaturen kan beregnes, rækker kan udvælges ud fra en betingelse, og en `DataFrame` kan oprettes ud fra en ordbog og eksporteres til en CSV-fil.

![Programmet kører i en terminal: rækkerne og temperaturerne læst med csv-biblioteket, derefter datarammen, ordbogen, listen, gennemsnittet 17,43, maksimum 24, mandagens række, den varmeste række søndag, mandag i Fahrenheit 53,6 og tabellen med point](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-weather/raw/branch/main/docs/images/weather-run.png)

*`python -m weather` i en terminal: først csv-delen, derefter pandas-delen.*

## Hvad programmet skriver

| Del | Resultat |
| --- | --- |
| `csv`-biblioteket | Filens rækker og temperaturerne `[12, 14, 15, 14, 21, 22, 24]` |
| `pandas` | `DataFrame`, ordbogen og listen med temperaturer |
| Statistik | Gennemsnit 17,43 (i hånden og med `mean`) og maksimum 24 |
| Rækkeudvælgelse | Mandagens række, den varmeste dags række (søndag), mandag i Fahrenheit (53,6) |
| Opret og eksportér | En `DataFrame` med elever og point lavet ud fra en ordbog; skrives kun til en fil med `--export` |

## Funktioner

| Funktion | Modul | Lektion |
| --- | --- | --- |
| `read_rows`, `read_temperatures` | `weather.csv_reader` | Læsning med `csv`-biblioteket |
| `read_data` | `weather.analysis` | `pandas.read_csv` |
| `to_data_dict`, `to_temp_list` | `weather.analysis` | `to_dict`, `to_list` |
| `average_temp`, `average_temp_mean`, `max_temp` | `weather.analysis` | Sum og længde, `mean`, `max` |
| `row_for_day`, `hottest_row`, `day_in_fahrenheit` | `weather.analysis` | Udvælgelse af rækker |
| `create_scores_frame`, `export_frame` | `weather.export` | `DataFrame` ud fra en ordbog, `to_csv` |

## Kør programmet

Der skal bruges Python 3.13 eller nyere. `csv`-delen har ingen afhængigheder ved kørsel; `pandas` er et valgfrit tilvalg, som `dev`-tilvalget installerer.

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-weather.git
cd 025-weather
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m weather
```

Tilføj `--export new_data.csv` for også at skrive tabellen med point til en fil. Repositoriets README har den fulde opsætning til Windows, Linux og macOS.
