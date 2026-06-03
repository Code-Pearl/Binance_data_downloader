markdown \# 🔥 Binance Historical Data Downloader

```{=html}
<p align="center">
```
`<img src="https://img.shields.io/badge/Author-Code--Pearl-blue?style=for-the-badge" alt="Code-Pearl">`{=html}
`<img src="https://img.shields.io/badge/Python-3.7+-green?style=for-the-badge" alt="Python">`{=html}
`<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">`{=html}
`<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
`<b>`{=html}Download historical Binance spot market
data`</b>`{=html}`<br>`{=html} `<i>`{=html}Multi-ticker •
Multi-timeframe • Append mode • Zero overwrites`</i>`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 📌 Table of Contents

-   [Features](#-features)
-   [Installation](#-installation)
-   [Quick Start](#-quick-start)
-   [Usage](#-usage)
-   [Output Format](#-output-format)
-   [File Naming](#-file-naming)
-   [Append Mode](#-append-mode)
-   [Supported Tickers](#-supported-tickers)
-   [Supported Timeframes](#-supported-timeframes)
-   [Project Structure](#-project-structure)
-   [License](#-license)
-   [Author](#-author)

------------------------------------------------------------------------

## ✨ Features

  ------------------------------------------------------------------------
  Feature                       Description
  ----------------------------- ------------------------------------------
  📥 **Multi-Ticker**           Download up to 15+ tickers in one run
                                (comma-separated)

  ⏱️ **Multi-Timeframe**        1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h,
                                12h, 1d, 3d, 1w, 1M

  📅 **Smart Dates**            Default: 1 year back → today. Fully
                                customizable

  📦 **Append Mode**            ✅ Never overwrites --- only adds NEW data

  🔄 **Duplicate Detection**    Skips rows that already exist in the file

  📊 **CSV/TXT Output**         Clean
                                `Ticker,Date,Open,High,Low,Close,Volume`
                                format

  📁 **Auto-Save**              Files saved in the same folder as the
                                script

  🖥️ **Terminal UI**            Live progress per ticker, per page ---
                                full visibility

  ⚡ **Rate-Limit Friendly**    Built-in delays to respect Binance API
                                limits
  ------------------------------------------------------------------------

------------------------------------------------------------------------

## 📥 Installation

### Prerequisites

``` bash
Python 3.7 or higher
pip (Python package manager)
Step 1: Clone the Repo
bash
git clone https://github.com/Code-Pearl/binance-data-downloader.git
cd binance-data-downloader
Step 2: Install Dependencies
bash
pip install requests
That's it! 🎉

🚀 Quick Start
bash
python binance_data_downloader.py
Then just press ENTER 3 times to use all defaults:

Prompt  Default What It Does
Tickers 15 major assets BTC, ETH, BNB, XRP, SOL, DOGE, ADA, AVAX, DOT, MATIC, LINK, UNI, LTC, ATOM, ETC
Timeframe   1d (Daily)  15 options available
Dates   1 year → today  Auto-filled, customizable
Result: 15 .txt files ready for your backtesting software 🎯

📖 Usage
Interactive Mode
============================================================
   🔥 BINANCE HISTORICAL DATA DOWNLOADER 🔥
   📦 Append mode — no overwrites!
============================================================

📌 Default top 15 assets loaded:
   BTCUSDT, ETHUSDT, BNBUSDT, XRPUSDT, SOLUSDT, ...

📝 Enter tickers separated by commas (press ENTER to keep defaults):
   Tickers [BTCUSDT, ETHUSDT, ...]: 
   → Just press ENTER

⏱️  Available intervals:
   1. 1m
   2. 3m
   ...
  12. 1d

   Choose interval [default: 12 (1d)]: 8
   ✅ Timeframe: 4h

📅 Default dates: 2024-06-15 → 2025-06-15 (1 year)
   Use defaults? (y/n) [default: y]: y

============================================================
🚀 STARTING DOWNLOAD (APPEND MODE)
============================================================
Custom Example
Tickers: BTCUSDT, SOLUSDT, DOGEUSDT
Interval: 4h
Dates: 2024-01-01 → 2025-06-15
📊 Output Format
Every .txt file follows this exact structure:

Ticker,Date,Open,High,Low,Close,Volume
BTCUSDT,2024-01-01,42265.15,42420.00,42050.00,42305.50,12450.320
BTCUSDT,2024-01-01,42305.50,42500.00,42200.00,42450.00,9870.150
ETHUSDT,2024-01-01,2250.30,2280.00,2240.00,2270.50,45000.100
Column  Type    Description
Ticker  string  e.g. BTCUSDT
Date    YYYY-MM-DD  UTC date
Open    float   Opening price
High    float   Highest price
Low float   Lowest price
Close   float   Closing price
Volume  float   Trading volume
✅ 100% compatible with backtesting software, Excel, pandas, etc.

📁 File Naming
{TICKER}_{TIMEFRAME}_Binance.txt
Example Meaning
BTCUSDT_1d_Binance.txt  Bitcoin daily data
ETHUSDT_4h_Binance.txt  Ethereum 4-hour data
SOLUSDT_15m_Binance.txt Solana 15-minute data
📂 All files are saved in the same folder as the script.

📦 Append Mode (No Overwrites!)
This is the killer feature 🔥

Scenario    What Happens
First run   Creates .txt file with all historical data
Second run (next day)   ✅ Reads existing file → skips duplicates → appends only new rows
Third run (next day)    ✅ Same — adds 1 new row, keeps everything else
Run with different timeframe    ✅ Creates a NEW file (e.g. BTCUSDT_4h_Binance.txt)
Day 1 → BTCUSDT_1d_Binance.txt (365 rows)
Day 2 → BTCUSDT_1d_Binance.txt (366 rows) ← +1 new row
Day 3 → BTCUSDT_1d_Binance.txt (367 rows) ← +1 new row
Zero data loss. Zero overwrites. Ever. 🛡️

🪙 Supported Tickers (Top 15 by Volume)
#   Ticker  Asset
1   BTCUSDT Bitcoin
2   ETHUSDT Ethereum
3   BNBUSDT Binance Coin
4   XRPUSDT Ripple
5   SOLUSDT Solana
6   DOGEUSDT    Dogecoin
7   ADAUSDT Cardano
8   AVAXUSDT    Avalanche
9   DOTUSDT Polkadot
10  MATICUSDT   Polygon
11  LINKUSDT    Chainlink
12  UNIUSDT Uniswap
13  LTCUSDT Litecoin
14  ATOMUSDT    Cosmos
15  ETCUSDT Ethereum Classic
💡 You can type any Binance spot pair (e.g. PEPEUSDT, ARBUSDT, etc.)

⏱️ Supported Timeframes
#   Interval    Description
1   1m  1 minute
2   3m  3 minutes
3   5m  5 minutes
4   15m 15 minutes
5   30m 30 minutes
6   1h  1 hour
7   2h  2 hours
8   4h  4 hours
9   6h  6 hours
10  8h  8 hours
11  12h 12 hours
12  1d  1 day ⭐ (default)
13  3d  3 days
14  1w  1 week
15  1M  1 month
📂 Project Structure
binance-data-downloader/
├── binance_data_downloader.py    # 📜 Main script
├── README.md                      # 📄 This file
├── requirements.txt               # 📦 Dependencies
├── .gitignore                     # 🚫 Git ignore
└── output/                        # 📁 (Optional) Your .txt files land here
    ├── BTCUSDT_1d_Binance.txt
    ├── ETHUSDT_1d_Binance.txt
    ├── SOLUSDT_4h_Binance.txt
    └── ...
🛠️ Requirements
txt
requests>=2.28.0
Or install with:

bash
pip install -r requirements.txt
📜 License
This project is licensed under the MIT License.

See 
LICENSE
 for details.

👤 Author
Code-Pearl 💎
Building tools for algorithmic traders.

GitHub
 | 
Website
 | 
Contact

⭐ Show Your Support
If this tool helps you, give it a ⭐ on GitHub!

Made with ❤️ by Code-Pearl
```

📁 Also Create These Files requirements.txt txt requests\>=2.28.0
.gitignore txt **pycache**/ *.pyc *.pyo *.pyd .Python env/ venv/ *.txt
!README.md .DS_Store LICENSE (MIT) txt MIT License

Copyright (c) 2025 Code-Pearl

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. Now you have a
complete GitHub-ready repo 💎🚀

Just do:

bash git init git add . git commit -m "Initial commit - Binance Data
Downloader by Code-Pearl" git remote add origin
https://github.com/Code-Pearl/binance-data-downloader.git git push -u
origin main
