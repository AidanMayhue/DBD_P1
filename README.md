# DS 4320 Project 1

**Executive Summary**
This readme documents an asset class secondary dataset for DS 4320 Data By Design. This project includes completed project metadata such as a name, computing ID, DOI, analysis code links, and a license. A summary table is included additionally. A problem statement, rationale, references, terminology table, callout examples and code are also included. 

Name: Aidan Mayhue

NetID: xdw9vp

DOI:

Press Release: https://github.com/AidanMayhue/DBD_P1/blob/main/press_release.md

Data: https://myuva-my.sharepoint.com/:f:/g/personal/xdw9vp_virginia_edu/IgDWOpaNsqN1QYExPDeQ93AEASsN_uLnogjY5FR4LwzhXhc?e=AygUAl

Pipeline

License: MIT

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
This project lives in the domain of finance. It is primarily concerned with helping visualize and create potential investment strategies. This relates to the finance world where the field is focused on the study of assets and leveraging them for capital gain. This project wants to display the overall gains of multiple assets within each type of asset in order to leverage them for capital gain.

Background reading

Summary of data table
---

| Title | Description | Link |
|-------|-------------|------|
| StockData: An Open Investment Transaction Dataset | Presents a real-world, anonymised open dataset of over 2,700 brokerage transaction records spanning 2020–2024, covering stocks, ETFs, dividends, and multi-asset holdings. Designed to support research in portfolio analysis, performance measurement, and financial ML — a direct financial parallel to the SoccerMon dataset. | https://pmc.ncbi.nlm.nih.gov/articles/PMC12907104/ |
| Enhancing Portfolio Management Using Artificial Intelligence: Literature Review | A broad open-access review of how AI and deep learning — including LSTM, GRU, and reinforcement learning — are applied to portfolio management tasks such as asset allocation, risk assessment, and time-series forecasting. Covers both traditional assets (stocks, bonds) and modern approaches. | https://pmc.ncbi.nlm.nih.gov/articles/PMC11033520/ |
| Analyzing the Critical Steps in Deep Learning-Based Stock Forecasting: A Literature Review | A systematic review of deep learning stock prediction studies from 2020–2024, examining the full pipeline: data collection, feature selection, denoising, model architecture, and performance evaluation. Useful for understanding best practices when applying ML to financial time-series data. | https://pmc.ncbi.nlm.nih.gov/articles/PMC11623133/ |
| Forecasting Stock Market Prices Using Machine Learning and Deep Learning Models: A Systematic Review | Comprehensive review of ML and deep learning techniques — including supervised learning, ensemble methods, and time-series algorithms — applied to forecasting stocks, ETFs, bonds, and cryptocurrencies. Covers model comparisons, performance metrics, and practical investment applications. | https://www.mdpi.com/2227-7072/11/3/94 |
| How Effective is Machine Learning in Stock Market Predictions? | Empirical open-access study comparing multiple ML algorithms (e.g. random forests, SVMs, neural networks) for predicting movement directions across seven major global stock indices including the NYSE, FTSE 100, and DAX. Provides a concrete benchmark for evaluating ML model performance on financial data. | https://pmc.ncbi.nlm.nih.gov/articles/PMC10826674/ |

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
| Name | Min | Max | Precision | Sources of Uncertainty |
|---|---|---|---|---|
| Open | 0.001 | Unbounded | 6 decimal places | Reflects the first transaction price which may not represent true market open due to pre-market trading activity |
| High | 0.001 | Unbounded | 6 decimal places | May underrepresent true intraday high if data provider missed transactions |
| Low | 0.001 | Unbounded | 6 decimal places | May overrepresent true intraday low if data provider missed transactions |
| Close | 0.001 | Unbounded | 6 decimal places | Adjusted by yfinance for splits and dividends which introduces rounding error. Adjustment methodology may differ from other data providers |
| Volume | 0 | Unbounded | Whole integer | Crypto volume is particularly unreliable due to wash trading and exchange reporting inconsistencies. ETF volume excludes dark pool transactions |
| TotalReturn | -1.0 | Unbounded | 4 decimal places | Sensitive to the exact start and end date chosen. Survivorship bias means poor performing delisted assets are excluded, inflating average returns |
| AnnualizedReturn | -1.0 | Unbounded | 4 decimal places | Assumes 252 trading days per year which varies in practice. Compounds the uncertainty of TotalReturn |
| Volatility | 0.0 | Unbounded | 4 decimal places | Based on historical daily returns which may not reflect future volatility. Crypto volatility is especially unstable due to thin markets and 24/7 trading |
| SharpeRatio | Unbounded | Unbounded | 4 decimal places | Assumes a fixed 4% risk free rate which changes over time. Negative Sharpe ratios are difficult to interpret meaningfully. Highly sensitive to the volatility estimate |
| MaxDrawdown | 0.0 | 1.0 | 4 decimal places | Only captures drawdowns within the selected period window. A longer period would likely reveal larger drawdowns for most assets |
