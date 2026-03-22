import yfinance as yf
import pandas as pd
import numpy as np
import requests
import time
import os
from io import StringIO
from google.colab import files

os.makedirs("data/raw", exist_ok=True)

# ── TICKER DICTIONARIES ───────────────────────────────────────────────────────
etf_tickers = {
    "US_Equity_Broad": ["SPY","IVV","VOO","VTI","IWM","IWB","IWF","IWD","MDY","IJH","IJR","ITOT","SCHB","SCHA","SCHX","VXF","QQQ","ONEQ","QQQM","VONE","VTWO","VTWG","VTWV"],
    "US_Equity_Sector": ["XLF","XLK","XLE","XLV","XLI","XLY","XLP","XLU","XLB","XLRE","XLC","VFH","VGT","VDE","VHT","VIS","VCR","VDC","VPU","VAW","VOX","ARKK","ARKW","ARKG","ARKF","ARKQ","DRIV","BOTZ","ROBO","AIQ"],
    "International_Equity": ["EFA","IEFA","VEA","EEM","IEMG","VWO","ACWI","VT","EWJ","EWG","EWU","EWC","EWA","EWZ","EWY","EWT","EWH","EWS","EWL","EWP","EWQ","EWI","EWD","EWN","FXI","MCHI","KWEB","CNYA","ASHR","GXC"],
    "Fixed_Income_Broad": ["AGG","BND","BNDX","BNDW","FBND","BOND","GBF","IUSB","SCHZ","SPAB","USAG","NUBD","TOTL"],
    "Fixed_Income_Treasury": ["TLT","IEF","SHY","GOVT","VGSH","VGIT","VGLT","SCHO","SCHR","SCHQ","SPTS","SPTI","SPTL","VFISX","VFITX","VUSTX","TBT","TMF","TMV","TBF"],
    "Fixed_Income_Corporate": ["LQD","VCIT","VCSH","VCLT","IGIB","IGSB","IGLB","USIG","SPIB","SPSB","SPLB","QLTA","CBND","FCOR"],
    "Fixed_Income_HighYield": ["HYG","JNK","USHY","FALN","HYLB","HYDB","SHYG","SJNK","BSJO","BSJP","BSJQ","BSJR","BSJS"],
    "Commodity": ["GLD","IAU","GLDM","SGOL","BAR","OUNZ","SLV","SIVR","PSLV","USO","BNO","UCO","DBO","UNG","BOIL","KOLD","DJP","PDBC","COMT","BCI","COMB","CORN","WEAT","SOYB","COW","NIB"],
    "Real_Estate": ["VNQ","IYR","SCHH","RWR","USRT","REZ","REM","MORT","BBRE","PPTY","INDS","HOMZ","ROOF","NURE"],
    "Dividend": ["VYM","DVY","HDV","DGRO","SCHD","SDY","RDVY","FVD","DGRW","LVHD","SPHD","FDVV","DHS","PFF"],
    "Factor_Smart_Beta": ["MTUM","VLUE","USMV","QUAL","SIZE","LRGF","SMLF","INTF","ICVT","DYNF","BATT","ESGU","ESGV","SUSL"],
    "Leveraged_Inverse": ["TQQQ","SQQQ","UPRO","SPXU","SSO","SDS","QLD","QID","TNA","TZA","UDOW","SDOW","SPXL","SPXS"],
    "Volatility_Alternatives": ["VIXY","UVXY","SVXY","VXX","VIXM","TVIX","TAIL","BTAL","HDGE","DBMF","KMLM","CTA"],
}
crypto_tickers = {
    "Layer1": ["BTC-USD","ETH-USD","SOL-USD","ADA-USD","AVAX-USD","DOT-USD","ATOM-USD","NEAR-USD","ALGO-USD","FTM-USD","ONE-USD","EGLD-USD","HBAR-USD","XTZ-USD","EOS-USD"],
    "Layer2": ["MATIC-USD","ARB-USD","OP-USD","IMX-USD","LRC-USD","METIS-USD","BOBA-USD","SKL-USD"],
    "DeFi": ["UNI-USD","AAVE-USD","MKR-USD","CRV-USD","COMP-USD","SNX-USD","YFI-USD","SUSHI-USD","BAL-USD","1INCH-USD","DYDX-USD","GMX-USD","LDO-USD","RPL-USD","FXS-USD"],
    "Exchange": ["BNB-USD","CRO-USD","FTT-USD","OKB-USD","HT-USD","KCS-USD","GT-USD","MX-USD"],
    "Stablecoin_adjacent": ["XRP-USD","XLM-USD","XDC-USD","CELO-USD"],
    "Meme": ["DOGE-USD","SHIB-USD","PEPE-USD","FLOKI-USD","BONE-USD","BABYDOGE-USD","WIF-USD","BONK-USD"],
    "Storage_Privacy": ["FIL-USD","AR-USD","SC-USD","STORJ-USD","XMR-USD","ZEC-USD","DASH-USD","SCRT-USD"],
    "Gaming_NFT": ["AXS-USD","SAND-USD","MANA-USD","ENJ-USD","GALA-USD","ILV-USD","ALICE-USD","SLP-USD","GODS-USD","YGG-USD"],
    "Oracle_Data": ["LINK-USD","BAND-USD","TRB-USD","API3-USD","UMA-USD"],
    "Legacy_Altcoin": ["LTC-USD","BCH-USD","ETC-USD","ZIL-USD","VET-USD","ICX-USD","WAVES-USD","NEO-USD","ONT-USD","QTUM-USD"],
}
bond_tickers = {
    "Treasury_Short": ["SHY","SCHO","SCHR","VGSH","VGIT","SPTS","SPTI","BIL","SGOV","CLTL","TBLL","TFLO","USFR"],
    "Treasury_Long": ["TLT","IEF","GOVT","VGLT","SPTL","SCHQ","TBT","TMF","TMV","TBF","EDV","ZROZ","VUSTX"],
    "Corporate_IG": ["LQD","VCIT","VCSH","VCLT","IGIB","IGSB","IGLB","USIG","SPIB","SPSB","SPLB","QLTA","CBND","FCOR","IBND","GHYG","FLOT","FLRN","ICSH"],
    "Corporate_HY": ["HYG","JNK","USHY","FALN","HYLB","HYDB","SHYG","SJNK","BSJO","BSJP","BSJQ","BSJR","BSJS","BSJT","BSJU","ANGL","HYEM","EMHY"],
    "Municipal": ["MUB","VTEB","TFI","HYD","SMB","SHM","ITM","MLN","HYMB","MUNI","IBMK","IBML","IBMM","IBMN"],
    "International": ["BNDX","IAGG","BWX","IGOV","ISHG","PICB","IBND","EMB","PCY","VWOB","LEMB","EBND","EMAG"],
    "Inflation_Protected": ["TIP","SCHP","STIP","VTIP","PBTP","LTPZ","TIPX","FIPDX","TDTT","TDTF"],
    "Aggregate": ["AGG","BND","BNDW","FBND","BOND","GBF","IUSB","SCHZ","SPAB","NUBD","TOTL","DIAL","DFCF"],
}

# Build ticker -> category map
ticker_to_category = {}
for category, tickers in etf_tickers.items():
    for t in tickers:
        ticker_to_category[t] = category
for category, tickers in crypto_tickers.items():
    for t in tickers:
        ticker_to_category[t] = category
for category, tickers in bond_tickers.items():
    for t in tickers:
        ticker_to_category[t] = category

# Get S&P 500 tickers and sectors from Wikipedia
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies", headers=headers)
sp500 = pd.read_html(StringIO(response.text))[0]
sp500_tickers = sp500["Symbol"].str.replace(".", "-", regex=False).tolist()
for _, row in sp500.iterrows():
    ticker = row["Symbol"].replace(".", "-")
    ticker_to_category[ticker] = row["GICS Sector"]

print(f"Category map built — {len(ticker_to_category)} tickers")

# ── HELPER: DOWNLOAD AND CONVERT TO LONG FORMAT ───────────────────────────────
def download_and_convert(tickers_dict, asset_class, start, end, chunk_size=50):
    all_dfs = []
    items = list(tickers_dict.items()) if isinstance(tickers_dict, dict) else [("default", tickers_dict)]
    
    for category, tickers in items:
        chunks = [tickers[i:i+chunk_size] for i in range(0, len(tickers), chunk_size)]
        for i, chunk in enumerate(chunks):
            print(f"  [{asset_class}] {category} chunk {i+1}/{len(chunks)}...")
            try:
                df = yf.download(chunk, start=start, end=end, auto_adjust=True, progress=False)
                if df.empty:
                    continue
                # Stack to long format
                long = df.stack(level=1, future_stack=True).reset_index()
                long.columns.name = None
                long = long.rename(columns={"level_0": "Date", "level_1": "Ticker"})
                price_cols = [c for c in ["Open","High","Low","Close","Volume"] if c in long.columns]
                long = long.dropna(subset=price_cols, how="all")
                long = long[["Date","Ticker"] + price_cols]
                long["AssetClass"] = asset_class
                long["Category"]   = long["Ticker"].map(ticker_to_category)
                all_dfs.append(long)
            except Exception as e:
                print(f"    Failed: {e}")
            time.sleep(2)
    
    return pd.concat(all_dfs) if all_dfs else pd.DataFrame()

# ── DOWNLOAD ALL FOUR ASSET CLASSES ───────────────────────────────────────────
print("\n=== Downloading ETFs ===")
etf_long = download_and_convert(etf_tickers, "ETF", "1990-01-01", "2024-12-31")
etf_long.to_csv("data/etf_prices.csv", index=False)
print(f"ETF: {etf_long.shape[0]:,} rows — {os.path.getsize('data/etf_prices.csv')/1e9:.2f} GB")

print("\n=== Downloading Crypto ===")
crypto_long = download_and_convert(crypto_tickers, "Crypto", "2015-01-01", "2024-12-31")
crypto_long.to_csv("data/crypto_prices.csv", index=False)
print(f"Crypto: {crypto_long.shape[0]:,} rows — {os.path.getsize('data/crypto_prices.csv')/1e9:.2f} GB")

print("\n=== Downloading Bonds ===")
bond_long = download_and_convert(bond_tickers, "Bond", "1990-01-01", "2024-12-31")
bond_long.to_csv("data/bond_prices.csv", index=False)
print(f"Bond: {bond_long.shape[0]:,} rows — {os.path.getsize('data/bond_prices.csv')/1e9:.2f} GB")

print("\n=== Downloading Stocks (S&P 500) ===")
stock_chunks = {f"chunk_{i}": sp500_tickers[i:i+50] for i in range(0, len(sp500_tickers), 50)}
stock_long = download_and_convert(stock_chunks, "Stock", "1990-01-01", "2024-12-31", chunk_size=50)

# Stocks are large — save in chunks to avoid crash
output_file = "data/stock_prices.csv"
first = True
CHUNK = 500000
for i in range(0, len(stock_long), CHUNK):
    stock_long.iloc[i:i+CHUNK].to_csv(output_file, mode="w" if first else "a", index=False, header=first)
    first = False
print(f"Stock: {stock_long.shape[0]:,} rows — {os.path.getsize('data/stock_prices.csv')/1e9:.2f} GB")

# ── BUILD ASSET TABLE ─────────────────────────────────────────────────────────
print("\n=== Building Asset Table ===")
all_prices = pd.concat([etf_long, crypto_long, bond_long, stock_long])
asset = (all_prices
    .groupby("Ticker")
    .agg(AssetClass=("AssetClass","first"))
    .reset_index()
)
asset["Category"]      = asset["Ticker"].map(ticker_to_category)
asset["Name"]          = None
asset["Currency"]      = "USD"
asset["InceptionDate"] = None
asset.to_csv("data/asset_table.csv", index=False)
print(f"Asset table: {asset.shape[0]} tickers")

# ── BUILD PERFORMANCE METRICS TABLE ──────────────────────────────────────────
print("\n=== Building Performance Metrics ===")
all_prices["Date"] = pd.to_datetime(all_prices["Date"])
all_prices = all_prices.sort_values(["Ticker","Date"])
all_prices["CapitalGain"] = (all_prices["Close"] - all_prices["Open"]) / all_prices["Open"]
all_prices = all_prices.replace([np.inf,-np.inf], np.nan).dropna(subset=["CapitalGain"])

def calculate_metrics(df, ticker, period_label, period_days):
    df = df.tail(period_days)
    if len(df) < 2:
        return None
    closes = df["Close"].dropna().values
    if len(closes) < 2:
        return None
    daily_returns      = np.diff(closes) / closes[:-1]
    total_return       = (closes[-1] - closes[0]) / closes[0]
    years              = period_days / 252
    annualized_return  = (1 + total_return) ** (1/years) - 1
    volatility         = np.std(daily_returns) * np.sqrt(252)
    sharpe             = (annualized_return - 0.04) / volatility if volatility > 0 else None
    peak               = closes[0]
    max_drawdown       = 0
    for price in closes:
        if price > peak:
            peak = price
        drawdown = (peak - price) / peak
        if drawdown > max_drawdown:
            max_drawdown = drawdown
    return {
        "Ticker":           ticker,
        "Period":           period_label,
        "TotalReturn":      round(total_return, 4),
        "AnnualizedReturn": round(annualized_return, 4),
        "Volatility":       round(volatility, 4),
        "SharpeRatio":      round(sharpe, 4) if sharpe else None,
        "MaxDrawdown":      round(max_drawdown, 4),
    }

periods  = {"1Y":252,"3Y":756,"5Y":1260,"10Y":2520}
tickers  = all_prices["Ticker"].unique()
met_file = "data/performance_metrics.csv"
first    = True
CHUNK    = 100

for i in range(0, len(tickers), CHUNK):
    chunk_tickers = tickers[i:i+CHUNK]
    print(f"  Metrics {i+1}-{min(i+CHUNK, len(tickers))} of {len(tickers)}...")
    rows = []
    for ticker in chunk_tickers:
        tdf = all_prices[all_prices["Ticker"]==ticker][["Date","Close"]].dropna()
        for label, days in periods.items():
            result = calculate_metrics(tdf, ticker, label, days)
            if result:
                rows.append(result)
    pd.DataFrame(rows).to_csv(met_file, mode="w" if first else "a", index=False, header=first)
    first = False

print(f"Metrics: {os.path.getsize(met_file)/1e9:.3f} GB")

# ── SUMMARY ───────────────────────────────────────────────────────────────────
print("\n=== Final File Sizes ===")
total = 0
for name, path in [
    ("ETF prices",          "data/etf_prices.csv"),
    ("Crypto prices",       "data/crypto_prices.csv"),
    ("Bond prices",         "data/bond_prices.csv"),
    ("Stock prices",        "data/stock_prices.csv"),
    ("Asset table",         "data/asset_table.csv"),
    ("Performance metrics", "data/performance_metrics.csv"),
]:
    size = os.path.getsize(path)/1e9
    total += size
    print(f"  {name}: {size:.2f} GB")
print(f"\n  Total: {total:.2f} GB")

# ── DOWNLOAD ALL ──────────────────────────────────────────────────────────────
print("\n=== Downloading files to your computer ===")
for path in [
    "data/etf_prices.csv",
    "data/crypto_prices.csv",
    "data/bond_prices.csv",
    "data/stock_prices.csv",
    "data/asset_table.csv",
    "data/performance_metrics.csv",
]:
    print(f"  Downloading {path}...")
    files.download(path)