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
