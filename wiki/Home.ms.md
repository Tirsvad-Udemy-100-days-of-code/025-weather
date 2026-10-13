> Halaman ini dijana daripada README.md dan wiki/. Perubahan di sini akan ditimpa apabila wiki diterbitkan lagi.

> Halaman Bahasa Inggeris adalah yang rasmi; terjemahan ini mengikutinya.

[English](Home) | [Dansk](Home.da) | Bahasa Melayu

# Data Cuaca (hari 25)

Membaca data cuaca CSV dalam Python. Ia ialah tugasan hari ke-25 dalam *100 Days of Code: The Complete Python Pro Bootcamp* di Udemy. Pelajaran membaca cuaca satu minggu daripada `weather_data.csv` dengan pustaka `csv` terbina dalam Python dan mengumpul suhu sebagai nombor bulat, kemudian menunjukkan bagaimana pustaka `pandas` melakukan perkara yang sama dalam satu baris. Satu jadual ialah `DataFrame` dan satu lajur daripadanya ialah `Series`; kedua-duanya boleh ditukar kepada kamus dan senarai, suhu purata dan suhu maksimum boleh dikira, baris boleh dipilih mengikut syarat, dan `DataFrame` boleh dicipta daripada kamus serta dieksport ke fail CSV.

![Program berjalan dalam terminal: baris dan suhu yang dibaca dengan pustaka csv, kemudian data frame, kamus, senarai, purata 17.43, maksimum 24, baris hari Isnin, baris terpanas hari Ahad, Isnin dalam Fahrenheit 53.6 dan jadual skor](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-weather/raw/branch/main/docs/images/weather-run.png)

*`python -m weather` dalam terminal: bahagian csv dahulu, kemudian bahagian pandas.*

## Apa yang dipaparkan oleh program

| Bahagian | Hasil |
| --- | --- |
| Pustaka `csv` | Baris fail dan suhu `[12, 14, 15, 14, 21, 22, 24]` |
| `pandas` | `DataFrame`, kamus dan senarai suhu |
| Statistik | Purata 17.43 (secara manual dan dengan `mean`) dan maksimum 24 |
| Pemilihan baris | Baris hari Isnin, baris hari terpanas (Ahad), Isnin dalam Fahrenheit (53.6) |
| Cipta dan eksport | `DataFrame` pelajar dan skor yang dibuat daripada kamus; ditulis ke fail hanya dengan `--export` |

## Fungsi

| Fungsi | Modul | Pelajaran |
| --- | --- | --- |
| `read_rows`, `read_temperatures` | `weather.csv_reader` | Membaca dengan pustaka `csv` |
| `read_data` | `weather.analysis` | `pandas.read_csv` |
| `to_data_dict`, `to_temp_list` | `weather.analysis` | `to_dict`, `to_list` |
| `average_temp`, `average_temp_mean`, `max_temp` | `weather.analysis` | Jumlah dan panjang, `mean`, `max` |
| `row_for_day`, `hottest_row`, `day_in_fahrenheit` | `weather.analysis` | Memilih baris |
| `create_scores_frame`, `export_frame` | `weather.export` | `DataFrame` daripada kamus, `to_csv` |

## Jalankan

Python 3.13 atau lebih baharu diperlukan. Bahagian `csv` tiada kebergantungan semasa dijalankan; `pandas` ialah tambahan pilihan yang dipasang oleh tambahan `dev`.

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-weather.git
cd 025-weather
python -m venv .venv
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
python -m weather
```

Tambah `--export new_data.csv` untuk turut menulis jadual skor ke fail. README repositori mempunyai persediaan penuh untuk Windows, Linux dan macOS.
