# 🔥 Binance Historical Data Downloader

<img src="https://img.shields.io/badge/Author-Code--Pearl-blue?style=for-the-badge" alt="Code-Pearl">
<img src="https://img.shields.io/badge/Python-3.7+-green?style=for-the-badge" alt="Python">
<img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" alt="Status">

**Download historical Binance spot market data**  
**Multi-ticker • Multi-timeframe • Append mode • Zero overwrites**

---

## 📌 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Output Format](#-output-format)
- [File Naming](#-file-naming)
- [Append Mode](#-append-mode)
- [Supported Tickers](#-supported-tickers)
- [Supported Timeframes](#-supported-timeframes)
- [Project Structure](#-project-structure)
- [License](#-license)
- [Author](#-author)

## ✨ Features

| Feature              | Description |
|----------------------|-----------|
| 📥 **Multi-Ticker**   | Download up to 15+ tickers in one run (comma-separated) |
| ⏱️ **Multi-Timeframe**| 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M |
| 📅 **Smart Dates**    | Default: 1 year back → today. Fully customizable |
| 📦 **Append Mode**    | Never overwrites — only adds new data |
| 🔄 **Duplicate Detection** | Skips rows that already exist |
| 📊 **CSV/TXT Output** | Clean format: `Ticker,Date,Open,High,Low,Close,Volume` |
| 🖥️ **Terminal UI**    | Live progress per ticker and page |
| ⚡ **Rate-Limit Friendly** | Built-in delays to respect Binance API limits |


## 📥 Installation

### Prerequisites
- Python 3.7 or higher
- `pip` package manager

### Step 1: Clone the repository
```bash
git clone https://github.com/Code-Pearl/binance-data-downloader.git
cd binance-data-downloader
```

### Step 2: Install dependencies
```bash
pip install requests
```

## 🚀 Quick Start

```bash
python binance_data_downloader.py
```

Press **ENTER** 3 times to use all defaults:
- **Tickers**: Top 15 assets (BTC, ETH, BNB, etc.)
- **Timeframe**: 1d (Daily)
- **Dates**: 1 year ago → today

You’ll get multiple `.txt` files ready for backtesting.

## 📖 Usage

The script runs in interactive mode with clear prompts.

**Example:**
- Tickers: `BTCUSDT, SOLUSDT, DOGEUSDT`
- Interval: `4h`
- Dates: `2024-01-01` to `2025-06-15`

## 📊 Output Format

Each file contains:

```csv
Ticker,Date,Open,High,Low,Close,Volume
BTCUSDT,2024-01-01,42265.15,42420.00,42050.00,42305.50,12450.320
BTCUSDT,2024-01-02,42305.50,42500.00,42200.00,42450.00,9870.150
```

**Compatible** with pandas, Excel, TradingView, backtesting libraries, etc.

## 📁 File Naming

Format: `{TICKER}_{TIMEFRAME}_Binance.txt`

Examples:
- `BTCUSDT_1d_Binance.txt`
- `ETHUSDT_4h_Binance.txt`
- `SOLUSDT_15m_Binance.txt`

## 📦 Append Mode (No Overwrites!)

This is the **killer feature**:
- First run → creates file with historical data
- Subsequent runs → appends only new data (skips duplicates)
- Different timeframes → creates separate files

**Zero data loss. Zero overwrites.**

## 🪙 Supported Tickers (Top 15 by Volume)

1. **BTCUSDT** - Bitcoin  
2. **ETHUSDT** - Ethereum  
3. **BNBUSDT** - Binance Coin  
4. **XRPUSDT** - Ripple  
5. **SOLUSDT** - Solana  
6. **DOGEUSDT** - Dogecoin  
7. **ADAUSDT** - Cardano  
8. **AVAXUSDT** - Avalanche  
9. **DOTUSDT** - Polkadot  
10. **MATICUSDT** - Polygon  
11. **LINKUSDT** - Chainlink  
12. **UNIUSDT** - Uniswap  
13. **LTCUSDT** - Litecoin  
14. **ATOMUSDT** - Cosmos  
15. **ETCUSDT** - Ethereum Classic  

You can use any Binance spot pair.

## ⏱️ Supported Timeframes

| #  | Interval | Description    |
|----|----------|----------------|
| 1  | 1m       | 1 minute       |
| 2  | 3m       | 3 minutes      |
| 3  | 5m       | 5 minutes      |
| 4  | 15m      | 15 minutes     |
| 5  | 30m      | 30 minutes     |
| 6  | 1h       | 1 hour         |
| 7  | 2h       | 2 hours        |
| 8  | 4h       | 4 hours        |
| 9  | 6h       | 6 hours        |
| 10 | 8h       | 8 hours        |
| 11 | 12h      | 12 hours       |
| 12 | 1d       | 1 day (default)|
| 13 | 3d       | 3 days         |
| 14 | 1w       | 1 week         |
| 15 | 1M       | 1 month        |

## 📂 Project Structure

```
binance-data-downloader/
├── binance_data_downloader.py    # Main script
├── README.md                     # This file
├── requirements.txt              # Dependencies
├── .gitignore
└── output/                       # Generated data files
    ├── BTCUSDT_1d_Binance.txt
    ├── ETHUSDT_4h_Binance.txt
    └── ...
```

## 🛠️ Requirements

**`requirements.txt`**
```txt
requests>=2.28.0
```

## 📜 License

This project is licensed under the **MIT License**.

## 👤 Author

**Code-Pearl** 💎  
Building tools for algorithmic traders.

- GitHub: [Code-Pearl](https://github.com/Code-Pearl)

---

⭐ **If this tool helps you, please give it a star on GitHub!**

Made with ❤️ by Code-Pearl
```
