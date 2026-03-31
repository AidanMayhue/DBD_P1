# DS 4320 Project 1

**Executive Summary**
This readme documents an asset class secondary dataset for DS 4320 Data By Design. This project includes completed project metadata such as a name, computing ID, DOI, analysis code links, and a license. A summary table is included additionally. A problem statement, rationale, references, terminology table, callout examples and code are also included. 

Name: Aidan Mayhue

NetID: xdw9vp

DOI:10.5281/zenodo.19357351

Press Release: https://github.com/AidanMayhue/DBD_P1/blob/main/press_release.md

Data: https://myuva-my.sharepoint.com/:f:/g/personal/xdw9vp_virginia_edu/IgDWOpaNsqN1QYExPDeQ93AEASsN_uLnogjY5FR4LwzhXhc?e=AygUAl

Pipeline

License: https://github.com/AidanMayhue/DBD_P1/blob/main/LICENSE

## Problem Definition

Initial General Problem
The general problem is predicting stock prices. To extrapolate on this problem, there are multiple types of assets that can be tracked in a portfolio, so identifying asset types that see the highest return increases potential ROI.
Additionally, many assets are more risky than others, meaning many are not useful for long term investment. Furthermore, identifying the goal of the investor is important, do they want to increase their potential to make money in a high risk portfolio? Or are they just planning for retirement? With all of these in mind, the specific problem is identifying assets among a list of asset types that have the highest return on investment given a strategy of buying and holding.

Rationale

The general problem is describing the main risk for investing. If you make poor decisions for your portfolio there is a strong chance at losing money. The specific problem shifts to identifying what the best investment options are for users. I chose to explore ETFs because they are generally considered low risk and beginner friendly. Crypto currencies are high risk and I'm hoping the data will reflect that. The specific problem for this project will revolve around creating a dataset of the highest percentage return on investment within ETFs, stocks, crypto, and bonds. This will solve the issue of identifying safe long term investments.


Motivation

As someone who has personally started investing it can be difficult to make decisions that are logically driven and not in some ways dependent on emotion. Part of this is due to my lack of knowledge on the subject. I primarily choose to invest in Exchange Traded funds, but I have some money in stocks which can be difficult to navigate. The motivation behind this project is to create a comprehensive overview of highest performing assets in each category in order for long term traders to create logical plans that are not informed by emotion, but rather statistics. Ideally a new trader could explore this dataset and make decisions for how much risk they are willing to accept in a long term portfolio.

Beginner friendly financial asset modeling tool

https://github.com/AidanMayhue/DBD_P1/blob/main/press_release.md

## Domain Exposition

Terminology
| Term | Summary |
|------|---------|
| ETF (Exchange Traded Fund) | A basket of assets (stocks, bonds, commodities) that trades on an exchange like a single stock, offering built-in diversification. |
| Expense ratio | The annual fee charged by the fund, expressed as a percentage of your investment. Lower is better — e.g. 0.03% vs 1.00%. |
| Index ETF | An ETF designed to mirror a market index (e.g. S&P 500), holding the same securities in roughly the same proportions. |
| Passive vs active ETF | Passive ETFs track an index automatically; active ETFs are managed by a portfolio manager who selects holdings. |
| NAV (Net Asset Value) | The total value of an ETF's underlying holdings per share, calculated at market close. The ETF's market price trades near but not always at NAV. |
| Bid-ask spread | The difference between the highest price a buyer will pay and the lowest a seller will accept. Wider spreads mean higher trading costs. |
| Tracking error | How closely an ETF's returns match its benchmark index — a smaller tracking error means the ETF is more faithfully replicating the index. |
| Sector ETF | An ETF focused on a specific industry segment (e.g. technology, healthcare), allowing targeted exposure without picking individual stocks. |
| Bond | A debt instrument where the investor lends money to an issuer (government or corporation) in exchange for regular interest payments and return of principal at maturity. |
| Coupon rate | The annual interest rate a bond pays, expressed as a percentage of its face value. A $1,000 bond with a 5% coupon pays $50/year. |
| Maturity date | The date when the bond issuer repays the principal (face value) to the bondholder. |
| Yield to maturity (YTM) | The total expected return if a bond is held until maturity, accounting for current price, coupon payments, and time remaining. |
| Credit rating | A grade (e.g. AAA, BBB, junk) assigned by agencies like Moody's or S&P reflecting the issuer's likelihood of repaying its debt. |
| Duration | A measure of a bond's sensitivity to interest rate changes — the longer the duration, the more the bond's price will fluctuate when rates move. |
| Investment grade vs high yield | Investment grade bonds (BBB or higher) carry lower default risk; high-yield (junk) bonds offer higher interest to compensate for greater risk. |
| Par value (face value) | The principal amount paid back at maturity, typically $1,000. A bond trading above par is at a premium; below par is at a discount. |
| Cryptocurrency | A decentralised digital currency secured by cryptography and recorded on a blockchain, operating independently of central banks. |
| Blockchain | The distributed ledger technology underlying most cryptocurrencies — a chain of verified transaction blocks replicated across thousands of computers. |
| Wallet | Software or hardware that stores the private keys used to access and transact your cryptocurrency holdings. |
| Private key / public key | A paired cryptographic system: the public key is your address (shareable), the private key is your password (never share it). Losing your private key means losing access to your funds. |
| DeFi (Decentralised Finance) | Financial services — lending, trading, earning yield — built on blockchain protocols without traditional intermediaries like banks. |
| Stablecoin | A cryptocurrency pegged to a stable asset (usually the US dollar) to reduce price volatility, e.g. USDC or Tether (USDT). |
| Market cap | Total value of a cryptocurrency in circulation (price × circulating supply), used to compare the relative size of different coins. |
| Volatility | The degree to which a crypto asset's price fluctuates — crypto markets are notably more volatile than traditional equities or bonds. |
| Gas fees | Transaction fees paid to network validators (on Ethereum and similar chains) to process and confirm a transaction on the blockchain. |
| Stock (equity/share) | A unit of ownership in a company. Shareholders are entitled to a portion of profits and, in some cases, voting rights. |
| P/E ratio (Price-to-Earnings) | A company's share price divided by its earnings per share — a common valuation metric. A higher P/E implies investors expect higher future growth. |
| Dividend | A portion of a company's profits distributed to shareholders, typically quarterly. Not all stocks pay dividends. |
| Market capitalisation | The total market value of a company's outstanding shares (share price × shares outstanding). Categorised as large-cap, mid-cap, or small-cap. |
| Earnings per share (EPS) | A company's net profit divided by the number of outstanding shares — a key measure of profitability per unit of ownership. |
| Bull vs bear market | A bull market is a sustained period of rising prices (typically 20%+ gain); a bear market is a sustained decline (typically 20%+ drop) from recent highs. |
| Volatility / beta | Beta measures how much a stock moves relative to the broader market. A beta above 1 means the stock swings more than the market; below 1 means it's more stable. |
| Diversification | Spreading investments across different companies, sectors, or asset classes to reduce the impact of any single holding performing poorly. |
| Short selling | Borrowing shares and selling them with the intent to buy them back later at a lower price — a strategy that profits when a stock falls. |


Project Domain
This project lives in the domain of finance. It is primarily concerned with helping visualize and create potential investment strategies. This relates to the finance world where the field is focused on the study of assets and leveraging them for capital gain. This project wants to display the overall gains of multiple assets within each type of asset in order to leverage them for capital gain. Specifically, this project is interested assets leveraged for long term gain by using a strategy commonly referred to as buying and holding.

Background reading

Summary of data table
---

| Title | Description | Link |
|-------|-------------|------|
| StockData: An Open Investment Transaction Dataset | Presents a real-world, anonymised open dataset of over 2,700 brokerage transaction records spanning 2020–2024, covering stocks, ETFs, dividends, and multi-asset holdings. Designed to support research in portfolio analysis, performance measurement, and financial ML | https://myuva-my.sharepoint.com/:b:/g/personal/xdw9vp_virginia_edu/IQAMBG83HsHGR5xBG_i-aiNmAaH1vHcCf5xrGEZq0jLeR9I?e=XFiR7m |
| Enhancing Portfolio Management Using Artificial Intelligence: Literature Review | A broad open-access review of how AI and deep learning — including LSTM, GRU, and reinforcement learning — are applied to portfolio management tasks such as asset allocation, risk assessment, and time-series forecasting. Covers both traditional assets (stocks, bonds) and modern approaches. | https://myuva-my.sharepoint.com/:b:/g/personal/xdw9vp_virginia_edu/IQAY6UG1NkeGSZC6qygXWhmBAZrwQ7FPhmSdqUiFLWtibY4?e=fCYiat |
| Analyzing the Critical Steps in Deep Learning-Based Stock Forecasting: A Literature Review | A systematic review of deep learning stock prediction studies from 2020–2024, examining the full pipeline: data collection, feature selection, denoising, model architecture, and performance evaluation. Useful for understanding best practices when applying ML to financial time-series data. | https://myuva-my.sharepoint.com/:b:/g/personal/xdw9vp_virginia_edu/IQBw-HJXHIrzQae6fR7AZQ6tAU1rsKFYPfcT8EdSYeJ1uSE?e=r6n2Ky |
| Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models: A Systematic Review | Comprehensive review of ML and deep learning techniques — including supervised learning, ensemble methods, and time-series algorithms — applied to forecasting stocks, ETFs, bonds, and cryptocurrencies. Covers model comparisons, performance metrics, and practical investment applications. |https://myuva-my.sharepoint.com/:b:/g/personal/xdw9vp_virginia_edu/IQDbQ1MVa-jOSqindHn1TH25AX2h1AMupJwxYSd0aAQvqRI?e=ApIFAG |
| How Effective is Machine Learning in Stock Market Predictions? | Empirical open-access study comparing multiple ML algorithms (e.g. random forests, SVMs, neural networks) for predicting movement directions across seven major global stock indices including the NYSE, FTSE 100, and DAX. Provides a concrete benchmark for evaluating ML model performance on financial data. | https://myuva-my.sharepoint.com/:b:/g/personal/xdw9vp_virginia_edu/IQBRfN4nXvkzQJOYtCzb373CATUEXm7G3HjQUx4iBVO70R8?e=rIHZoI |

## Data Creation

Paragraph
For the Data collection process I primarily collected data from the yfinance package, a python package connected to yahoo finance's API.I can select from a wide range of entries. I do not have the ability to sort by asset type, so I curated a list of and wrote a script to select the top performing assets in each asset category. This was gathered from sources that most people may navigate towards for a comprehensive view, such as etfdb.com or wikipedia.

From then I wrote a script to pull data for each asset across several years using the yfinance package. These then needed to be reformatted into a usable way where the stock was on the rows rather than the columns. Two new tables were then derived, one to track every asset and their ticker, and another to track some generalizable statistics for each asset (such as capital gains). These were all then downloaded as separate CSVs.

Code

Bias Identification
Since I am primarily pulling from the yahoo finance API via yfinance issues with yahoo finance will impact the accuracy of my data. Yahoo Finance has issues with significant amounts of missing data across asset types. Additionally, bias may come about through the assets I chose. Getting a list of every asset is not feasible so I tried to create a comprehensive list that was composed of different kinds of assets within each asset types. For example I have some leveraged ETFS in the ETF dataset which may heavily skew the way regression analysis performs.

Bias Mitigation
Since the dataset is large I can mitigate this issue by selectively ignoring missing data or choosing to remove particularly troublesome entries. If one day of data happens to be missing then the opening value from the days surrounding the missing value can be averaged to estimate the gain or loss from the missing day. Addressing the point on leveraged/inverse assets, I can remove these from the dataset for a more comprehensive view of the broad market ETFs that generally do outperform individual stocks.

Rationale
Since each entry on the table represents a day for that particular asset, if one happens to be missing data eschewing it from the data will pose minimal risk as long as its not several years of data missing. The rationale behind removing leveraged ETFS is that they are not considered a long term investment since they depend on the market declining to see any decent ROI. This can be great in financial crises (such as the current one) but introduces a lot of risk should the market rally. These are not safe for the average long term investor and as such could reasonably be removed from the data.

## Metadata

Schema ERD
<img width="1410" height="708" alt="image" src="https://github.com/user-attachments/assets/a4ae909d-e446-4f0b-a9d4-5dbc74b36ac0" />

Data tables
| Tables | description | link |
|---|---|---|
|stock_prices.csv| Table for stock prices within the S&P 500 across several years | https://myuva-my.sharepoint.com/:u:/g/personal/xdw9vp_virginia_edu/IQDolNqUdibaSpIEe4RDRxX6ARo8F4Spwi20jVQ2kNE0MiM?e=OBP7nS |
|bond_prices.csv| Table for bond prices across several years | https://myuva-my.sharepoint.com/:u:/g/personal/xdw9vp_virginia_edu/IQBju1NfAXHlRYWG9EnIqg0sAQKnRCKloE8mg3mp0Y6tjPs?e=kAfYiE|
|crypto_prices.csv| Table for multiple cryptocurrency prices across several years| https://myuva-my.sharepoint.com/:u:/g/personal/xdw9vp_virginia_edu/IQABwvLkY6fQQpkHkFkTSpJvAUVZJFGSlYCHtAm7gKsPOSQ?e=POj8Dl |
| etf_prices.csv | Table for multiple ETF prices across several years |https://myuva-my.sharepoint.com/:u:/g/personal/xdw9vp_virginia_edu/IQBMtKvXw2SsRYz596p0u0EVAdydi_BsiMPmsAdeTgjQxOA?e=WDvpWQ|
|performance_metrics.csv|Table for aggregate statistics for each asset type| https://myuva-my.sharepoint.com/:u:/g/personal/xdw9vp_virginia_edu/IQDCTx6fpvvfS4Y1LMWYfkcjAX6I-iSkCq2JobUb6oQeTJw?e=6MqWDO |
|asset_table.csv|Table cataloging each asset name |https://myuva-my.sharepoint.com/:u:/g/personal/xdw9vp_virginia_edu/IQANKLqkFtdFQpHbHdW52rihAQ8KqiV2ErL6-RfWF7LNitk?e=djihdT|
Data Dictionary Table
| Name | Data Type | Description | Example |
|---|---|---|---|
| Ticker | String | Unique symbol identifying the asset across all tables. Primary key in ASSET, foreign key in all other tables | SPY |
| AssetClass | String | Broad classification of the asset into one of four categories | ETF |
| Category | String | Sub-classification within the asset class. For ETFs this is the fund strategy, for stocks this is the GICS sector, for crypto this is the token type, for bonds this is the bond type | US_Equity_Sector |
| Name | String | Full name of the asset. Currently null, can be populated via yfinance metadata | SPDR S&P 500 ETF Trust |
| Currency | String | Currency in which the asset is priced. All assets in this database are USD denominated | USD |
| InceptionDate | Date | The date the asset was first listed or issued. Currently null, can be populated via yfinance metadata | 1993-01-22 |
| Date | Date | The trading date for a given price record. Part of composite primary key with Ticker | 2024-12-30 |
| Open | Float | The price of the asset at market open on the given date | 584.12 |
| High | Float | The highest price reached by the asset during the trading day | 589.45 |
| Low | Float | The lowest price reached by the asset during the trading day | 581.33 |
| Close | Float | The price of the asset at market close, adjusted for splits and dividends via yfinance auto_adjust | 587.82 |
| Volume | Integer | The total number of shares or units traded on the given date | 34444400 |
| Period | String | The time horizon over which performance metrics are calculated. Part of composite primary key with Ticker | 1Y |
| TotalReturn | Float | The raw percentage return of the asset over the given period, calculated as (final price - initial price) / initial price | 0.2341 |
| AnnualizedReturn | Float | The total return scaled to a yearly rate using compound annualization | 0.1823 |
| Volatility | Float | The annualized standard deviation of daily returns, measuring price variability | 0.1542 |
| SharpeRatio | Float | Risk-adjusted return calculated as (annualized return - 4% risk free rate) / volatility | 1.2341 |
| MaxDrawdown | Float | The largest peak-to-trough percentage decline over the period | 0.1823 |

---
Data Dictionary Quantification of Uncertainty
## BONDS
**Rows:** 378,639 | **Columns:** 9

**Column names:** Date, Ticker, Open, High, Low, Close, Volume, AssetClass, Category

| Column | Mean | Median | Std Dev | Variance | Min | Max | Range | IQR | Skewness | Kurtosis | Null Count | Null % |
|--------|------|--------|---------|----------|-----|-----|-------|-----|----------|----------|------------|--------|
| Open | 4.36e+01 | 37.2465 | 3.58e+01 | 1.28e+03 | 0.6034 | 9.74e+02 | 9.74e+02 | 33.7690 | 7.1717 | 110.7620 | 0 | 0.0 |
| High | 4.38e+01 | 37.3158 | 3.62e+01 | 1.31e+03 | 0.6034 | 1.01e+03 | 1.01e+03 | 33.8930 | 7.3316 | 114.7056 | 0 | 0.0 |
| Low | 4.35e+01 | 37.1640 | 3.54e+01 | 1.25e+03 | 0.6034 | 9.17e+02 | 9.17e+02 | 33.6586 | 7.0044 | 106.7783 | 0 | 0.0 |
| Close | 4.36e+01 | 37.2395 | 3.57e+01 | 1.28e+03 | 0.6034 | 9.58e+02 | 9.57e+02 | 33.7769 | 7.1590 | 110.5335 | 0 | 0.0 |
| Volume | 1.21e+06 | 160300.00 | 3.69e+06 | 1.36e+13 | 0.0 | 1.51e+08 | 1.51e+08 | 849800.00 | 9.2461 | 137.5463 | 0 | 0.0 |

---

## CRYPTO
**Rows:** 177,425 | **Columns:** 9

**Column names:** Date, Ticker, Open, High, Low, Close, Volume, AssetClass, Category

| Column | Mean | Median | Std Dev | Variance | Min | Max | Range | IQR | Skewness | Kurtosis | Null Count | Null % |
|--------|------|--------|---------|----------|-----|-----|-------|-----|----------|----------|------------|--------|
| Open | 6.34e+02 | 1.8839 | 4.72e+03 | 2.23e+07 | 0.0 | 1.06e+05 | 1.06e+05 | 17.4589 | 11.0421 | 143.0770 | 1997 | 1.13 |
| High | 6.53e+02 | 1.9709 | 4.85e+03 | 2.36e+07 | 0.0 | 1.08e+05 | 1.08e+05 | 18.1651 | 10.9954 | 141.5830 | 1997 | 1.13 |
| Low | 6.14e+02 | 1.7997 | 4.58e+03 | 2.10e+07 | 0.0 | 1.05e+05 | 1.05e+05 | 16.6495 | 11.1118 | 145.3389 | 1997 | 1.13 |
| Close | 6.28e+02 | 1.7950 | 4.70e+03 | 2.21e+07 | 0.0 | 1.06e+05 | 1.06e+05 | 16.8127 | 11.1115 | 144.9231 | 0 | 0.00 |
| Volume | 8.92e+08 | 5.05e+07 | 4.79e+09 | 2.29e+19 | 0.0 | 6.13e+11 | 6.13e+11 | 2.25e+08 | 22.5947 | 1786.6952 | 0 | 0.00 |

---

## ETF
**Rows:** 954,091 | **Columns:** 9

**Column names:** Date, Ticker, Open, High, Low, Close, Volume, AssetClass, Category

| Column | Mean | Median | Std Dev | Variance | Min | Max | Range | IQR | Skewness | Kurtosis | Null Count | Null % |
|--------|------|--------|---------|----------|-----|-----|-------|-----|----------|----------|------------|--------|
| Open | 3.01e+07 | 33.3991 | 2.61e+09 | 6.83e+18 | 0.06 | 6.07e+11 | 6.07e+11 | 44.7617 | 120.3645 | 16607.7473 | 0 | 0.0 |
| High | 3.16e+07 | 33.6078 | 2.75e+09 | 7.54e+18 | 0.07 | 6.12e+11 | 6.12e+11 | 45.0056 | 119.5795 | 16198.6896 | 0 | 0.0 |
| Low | 2.87e+07 | 33.1572 | 2.49e+09 | 6.18e+18 | 0.05 | 5.15e+11 | 5.15e+11 | 44.5121 | 118.2719 | 15710.8395 | 0 | 0.0 |
| Close | 2.98e+07 | 33.3946 | 2.58e+09 | 6.65e+18 | 0.06 | 5.15e+11 | 5.15e+11 | 44.7574 | 117.7037 | 15450.7471 | 0 | 0.0 |
| Volume | 7.13e+06 | 434100.00 | 4.87e+07 | 2.38e+15 | 0.0 | 5.97e+09 | 5.97e+09 | 2.78e+06 | 38.6928 | 2433.9813 | 0 | 0.0 |

---

## STOCKS
**Rows:** 3,486,691 | **Columns:** 9

**Column names:** Date, Ticker, Open, High, Low, Close, Volume, AssetClass, Category

| Column | Mean | Median | Std Dev | Variance | Min | Max | Range | IQR | Skewness | Kurtosis | Null Count | Null % |
|--------|------|--------|---------|----------|-----|-----|-------|-----|----------|----------|------------|--------|
| Open | 5.57e+01 | 22.9500 | 1.62e+02 | 2.63e+04 | 0.0065 | 9.91e+03 | 9.91e+03 | 45.8627 | 22.5808 | 826.6881 | 0 | 0.0 |
| High | 5.63e+01 | 23.2532 | 1.64e+02 | 2.69e+04 | 0.0065 | 9.96e+03 | 9.96e+03 | 46.3275 | 22.5700 | 825.0982 | 0 | 0.0 |
| Low | 5.50e+01 | 22.6405 | 1.60e+02 | 2.57e+04 | 0.0062 | 9.79e+03 | 9.79e+03 | 45.3739 | 22.6102 | 829.0880 | 0 | 0.0 |
| Close | 5.57e+01 | 22.9555 | 1.62e+02 | 2.63e+04 | 0.0065 | 9.92e+03 | 9.92e+03 | 45.8655 | 22.5797 | 826.2415 | 0 | 0.0 |
| Volume | 7.60e+06 | 1.80e+06 | 4.52e+07 | 2.05e+15 | 0.0 | 9.23e+09 | 9.23e+09 | 3.91e+06 | 28.3274 | 1737.5321 | 0 | 0.0 |

---

## PERFORMANCE METRICS
**Rows:** 3,532 | **Columns:** 7

**Column names:** Ticker, Period, TotalReturn, AnnualizedReturn, Volatility, SharpeRatio, MaxDrawdown

| Column | Mean | Median | Std Dev | Variance | Min | Max | Range | IQR | Skewness | Kurtosis | Null Count | Null % |
|--------|------|--------|---------|----------|-----|-----|-------|-----|----------|----------|------------|--------|
| TotalReturn | 2.3194 | 0.2331 | 48.1237 | 2315.8927 | -1.0000 | 2001.9891 | 2002.9891 | 0.8600 | 40.7404 | 1688.8703 | 0 | 0.0 |
| AnnualizedReturn | 0.0910 | 0.0634 | 0.2877 | 0.0827 | -0.9903 | 7.4161 | 8.4064 | 0.1504 | 7.6341 | 146.8278 | 0 | 0.0 |
| Volatility | 8.5692 | 0.2726 | 181.7796 | 33043.8277 | 0.0024 | 7039.0750 | 7039.0726 | 0.1813 | 29.1395 | 967.4316 | 0 | 0.0 |
| SharpeRatio | 0.1283 | 0.0940 | 0.7786 | 0.6062 | -11.5768 | 9.4198 | 20.9966 | 0.6382 | -0.4724 | 32.7652 | 0 | 0.0 |
| MaxDrawdown | 0.4024 | 0.3777 | 0.2458 | 0.0604 | 0.0000 | 1.0000 | 1.0000 | 0.3330 | 0.5951 | -0.2139 | 0 | 0.0 |
