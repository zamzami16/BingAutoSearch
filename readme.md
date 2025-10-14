# What this

Automate Microsoft Bing auto search to earn point from Microsoft Reward. for more information about microsoft reward go to [this](https://rewards.bing.com/).

# Requirements

you can directly using executable files on release. you just need using this directly.

- Python installed on your machine.
- Basic knowledge using `terminal`

# Get Started

## Clone repository

```bash
    git clone https://github.com/zamzami16/BingAutoSearch.git
```

or download this as zip.

## Create Virtual Environment (optional)

I recomend to use virtual environment, if you consider to install package to main environment, skip this section.

```bash
python -m venv venv
venv/scripts/activate
```

## Install Requirements packages

```bash
python -m pip install -r requirements.txt
```

## Running the script

On opened new tab of Microsoft edge, open terminal, and then run this:

```bash
python AutoBingSearch.py
```

Or you can run using Powershell script on `search.ps1` script. `Note` that if you not use virtual environment, delete the first line of code

```shell
venv/scripts/activate // delete this line
python AutoBingSearch.py
```

and just type on your terminal.

```bash
./search.ps1
```

Minimize your terminal, and wait until the process finished. the estimation time of running this is among 9 minutes.

# Build Windows Executable (.exe)

Kamu bisa langsung menggunakan file executable yang tersedia di folder `release` jika tidak ingin repot build manual. Cukup download dan jalankan file `.exe` tersebut.

Jika ingin build sendiri, ikuti langkah berikut untuk membuat single-file Windows executable menggunakan PyInstaller (bundling semua dependencies dan config files):

1. Pastikan sudah install PyInstaller:
   ```bash
   pip install pyinstaller
   ```
2. Jalankan perintah berikut dari folder project:
   ```pwsh
   D:/KERJA/python/auto-bing-search/venv/Scripts/python.exe -m PyInstaller --onefile --add-data "resources/config.yml;random_word" --add-data "resources/database/words.json;random_word/database" AutoBingSearch.py
   ```
3. File hasil build akan ada di folder `dist/AutoBingSearch.exe`.
4. Copy file config.json (dan resource lain yang dibutuhkan) ke folder `dist` jika diperlukan.
5. Jalankan `AutoBingSearch.exe` dari folder `dist`.

# Configuring The Pointer Position

Konfigurasi pointer dan jumlah pencarian diatur melalui file `config.json`.

Contoh isi default `config.json`:

```json
{
  "global_setting": {
    "delay": { "min": 3, "max": 7 },
    "total_search": 32
  },
  "data": [
    {
      "name": "screen-left",
      "config": { "pos_x": 400, "pos_y": 50, "d_x": 150, "d_y": 5 }
    }
  ]
}
```

- `pos_x`, `pos_y`: posisi search bar (X dan Y)
- `d_x`, `d_y`: toleransi acak posisi
- `total_search`: jumlah pencarian
- `delay.min`, `delay.max`: jeda antar aksi (detik)

Ubah nilai pada file `config.json` sesuai kebutuhan dan resolusi layar kamu. Jika file tidak ditemukan, aplikasi akan menggunakan nilai default di atas.

Untuk mendapatkan posisi search bar, lihat bagian berikut:

## Get Search bar Location

- Install [Microsoft Power Toys](https://learn.microsoft.com/en-us/windows/powertoys/install)
- Buka Microsoft Edge
- Aktifkan `Screen Ruler` dari Power Toys dengan menekan `Windows + Shift + M`
- Ukur posisi search bar

![obtain-serach-bar-location](resources/configure-searchbar-location.png)
