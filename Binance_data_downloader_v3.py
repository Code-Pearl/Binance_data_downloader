import requests
import csv
import os
from datetime import datetime, timedelta
import time

BASE_URL = "https://api.binance.com/api/v3/klines"

# 🏆 Top 15 most liquid crypto assets on Binance by volume
DEFAULT_TICKERS = [
    "BTCUSDT",
    "ETHUSDT",
    "BNBUSDT",
    "XRPUSDT",
    "SOLUSDT",
    "DOGEUSDT",
    "ADAUSDT",
    "AVAXUSDT",
    "DOTUSDT",
    "MATICUSDT",
    "LINKUSDT",
    "UNIUSDT",
    "LTCUSDT",
    "ATOMUSDT",
    "ETCUSDT",
]

INTERVALS = {
    "1":  "1m",
    "2":  "3m",
    "3":  "5m",
    "4":  "15m",
    "5":  "30m",
    "6":  "1h",
    "7":  "2h",
    "8":  "4h",
    "9":  "6h",
    "10": "8h",
    "11": "12h",
    "12": "1d",
    "13": "3d",
    "14": "1w",
    "15": "1M",
}


def get_klines(symbol, interval, start_time, end_time):
    """Fetch kline data from Binance with progress."""
    url = BASE_URL
    klines = []
    page = 0

    while True:
        page += 1
        params = {
            "symbol": symbol.upper(),
            "interval": interval,
            "startTime": start_time,
            "endTime": end_time,
            "limit": 1000,
        }
        resp = requests.get(url, params=params, timeout=30)
        data = resp.json()

        if not data:
            break

        klines.extend(data)

        print(f"   📥 [{symbol}] Page {page} → {len(data)} candles fetched (total: {len(klines)})")

        start_time = data[-1][0] + 1
        if len(data) < 1000:
            break

        time.sleep(0.1)

    return klines


def load_existing_dates(filepath):
    """Load existing (date) set from file to avoid duplicates."""
    existing_dates = set()
    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', newline='') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    existing_dates.add(row['Date'])
            print(f"   📂 File exists. Loaded {len(existing_dates)} existing rows.")
        except Exception:
            pass
    return existing_dates


def save_to_txt(klines, symbol, interval, folder_path, existing_dates):
    """Append NEW rows only (skip duplicates) to TICKER_timeFRAME_Binance.txt"""
    filename = f"{symbol}_{interval}_Binance.txt"
    filepath = os.path.join(folder_path, filename)

    # Filter out rows that already exist
    new_rows = []
    for k in klines:
        ts = k[0] / 1000
        dt = datetime.utcfromtimestamp(ts).strftime("%Y-%m-%d")
        if dt not in existing_dates:
            new_rows.append([
                symbol,
                dt,
                k[1],  # Open
                k[2],  # High
                k[3],  # Low
                k[4],  # Close
                k[5]   # Volume
            ])

    if not new_rows:
        print(f"   #  No new data for {symbol} (all already downloaded)")
        return 0

    # Append mode
    with open(filepath, 'a', newline='') as f:
        writer = csv.writer(f)
        for row in new_rows:
            writer.writerow(row)

    print(f"   ✅ Appended {len(new_rows)} NEW rows → {filename}")
    return len(new_rows)


def parse_date(date_str):
    """Parse YYYY-MM-DD into ms timestamp"""
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    return int(dt.timestamp() * 1000)


def main():
    print("=" * 60)
    print("   🔥 BINANCE HISTORICAL DATA DOWNLOADER 🔥")
    print("   📦 Append mode — no overwrites!")
    print("=" * 60)

    # ── TICKER SELECTION ──────────────────────────────────
    print("\n📌 Default top 15 assets loaded:")
    print(f"   {', '.join(DEFAULT_TICKERS)}")

    print("\n📝 Enter tickers separated by commas (press ENTER to keep defaults):")
    print("   Example: BTCUSDT, ETHUSDT, SOLUSDT")
    raw = input(f"   Tickers [{', '.join(DEFAULT_TICKERS)}]: ").strip()

    if raw:
        tickers = [t.strip().upper() for t in raw.split(",") if t.strip()]
    else:
        tickers = DEFAULT_TICKERS.copy()

    print(f"\n🎯 Downloading {len(tickers)} tickers: {', '.join(tickers)}")

    # ── TIMEFRAME SELECTION ───────────────────────────────
    print("\n⏱️  Available intervals:")
    for num, iv in INTERVALS.items():
        print(f"   {num:>2}. {iv}")

    choice = input(f"\n   Choose interval [default: 12 (1d)]: ").strip()

    if choice in INTERVALS:
        interval = INTERVALS[choice]
    elif choice in INTERVALS.values():
        interval = choice
    else:
        print(f"   ⚠️  Invalid choice '{choice}', using default: 1d")
        interval = "1d"

    print(f"   ✅ Timeframe: {interval}")

    # ── DATE SELECTION ────────────────────────────────────
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=365)).strftime("%Y-%m-%d")

    print(f"\n📅 Default dates: {start_date} → {end_date} (1 year)")
    use_default = input("   Use defaults? (y/n) [default: y]: ").strip().lower()

    if use_default != "n":
        raw_start = input(f"   Start date [{start_date}]: ").strip()
        if raw_start:
            start_date = raw_start
        raw_end = input(f"   End date [{end_date}]: ").strip()
        if raw_end:
            end_date = raw_end
    else:
        raw_start = input(f"   Start date [{start_date}]: ").strip()
        if raw_start:
            start_date = raw_start
        raw_end = input(f"   End date [{end_date}]: ").strip()
        if raw_end:
            end_date = raw_end

    start_ts = parse_date(start_date)
    end_ts = parse_date(end_date) + 86400000

    print("\n" + "=" * 60)
    print(f"🚀 STARTING DOWNLOAD (APPEND MODE)")
    print(f"   Date: {start_date} → {end_date}")
    print(f"   Interval: {interval}")
    print(f"   Tickers: {len(tickers)}")
    print("=" * 60 + "\n")

    # ── DOWNLOAD LOOP ─────────────────────────────────────
    folder_path = os.path.dirname(os.path.abspath(__file__))
    total_new_rows = 0
    failed = []
    skipped = []

    for i, symbol in enumerate(tickers, 1):
        print(f"\n{'─' * 40}")
        print(f"  [{i}/{len(tickers)}] 🔄 Fetching {symbol} @ {interval}...")
        print(f"{'─' * 40}")

        try:
            # ✅ Load existing dates BEFORE fetching
            filepath = os.path.join(folder_path, f"{symbol}_{interval}_Binance.txt")
            existing_dates = load_existing_dates(filepath)

            klines = get_klines(symbol, interval, start_ts, end_ts)

            if not klines:
                print(f"   ⚠️  No data found for {symbol}")
                failed.append(symbol)
                continue

            new_count = save_to_txt(klines, symbol, interval, folder_path, existing_dates)
            total_new_rows += new_count

            if new_count == 0:
                skipped.append(symbol)

        except Exception as e:
            print(f"   ❌ ERROR downloading {symbol}: {e}")
            failed.append(symbol)

        time.sleep(0.3)

    # ── SUMMARY ───────────────────────────────────────────
    print("\n" + "=" * 60)
    print("   🏁 DOWNLOAD COMPLETE")
    print("=" * 60)
    print(f"   ✅ New rows appended: {total_new_rows:,}")
    print(f"   ⏭️  Skipped (already exist): {len(skipped)}")
    print(f"   📁 Files saved in: {folder_path}")

    if failed:
        print(f"   ❌ Failed tickers: {', '.join(failed)}")
    else:
        print(f"   🎉 Done! {len(tickers) - len(skipped)} tickers updated.")

    print("=" * 60)


if __name__ == "__main__":
    main()
