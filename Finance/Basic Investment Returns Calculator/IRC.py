import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# --- User Inputs ---
try:
    bond_proportion = float(input("Enter the proportion of bonds in your portfolio (0-100): ")) / 100
    equity_proportion = float(input("Enter the proportion of equities in your portfolio (0-100): ")) / 100
    mezzanine_proportion = float(input("Enter the proportion of mezzanine finance in your portfolio (0-100): ")) / 100

    total_proportion = bond_proportion + equity_proportion + mezzanine_proportion
    if not np.isclose(total_proportion, 1.0):
        raise ValueError("The total allocation must equal 100%.")
except ValueError as e:
    print(f"Invalid input: {e}")
    exit(1)

# --- Load CSV Data ---
def load_adj_close_from_csv(filename):
    df = pd.read_csv(filename, parse_dates=['Date'])
    df = df[['Date', 'Adj Close']].dropna()
    df.set_index('Date', inplace=True)
    df = df.sort_index()
    return df['Adj Close']

try:
    equity_hist = load_adj_close_from_csv("VEA.csv")
    bond_hist = load_adj_close_from_csv("BND.csv")
except Exception as e:
    print(f"Error loading CSV data: {e}")
    exit(1)

# --- Trim to 5-Year Period ---
end_date = datetime.now()
start_date = end_date.replace(year=end_date.year - 5)
equity_hist = equity_hist.loc[(equity_hist.index >= start_date) & (equity_hist.index <= end_date)]
bond_hist = bond_hist.loc[(bond_hist.index >= start_date) & (bond_hist.index <= end_date)]

# --- Align Dates ---
common_index = equity_hist.index.intersection(bond_hist.index)
equity_hist = equity_hist.loc[common_index]
bond_hist = bond_hist.loc[common_index]

# --- Cumulative Returns ---
equity_cum = (equity_hist / equity_hist.iloc[0]) * 100
bond_cum = (bond_hist / bond_hist.iloc[0]) * 100

# --- Simulated Mezzanine Returns (10.5% p.a.) ---
annual_return = 0.105
daily_return = (1 + annual_return) ** (1 / 252)
mezz_cum = pd.Series(np.full(len(common_index), daily_return), index=common_index).cumprod() * 100

# --- Portfolio Cumulative Return ---
portfolio_cum = (
    equity_cum * equity_proportion +
    bond_cum * bond_proportion +
    mezz_cum * mezzanine_proportion
)

# --- Plot ---
plt.figure(figsize=(14, 7))
plt.plot(equity_cum, label='Equities (VEA)')
plt.plot(bond_cum, label='Bonds (BND)')
plt.plot(mezz_cum, label='Mezzanine Finance (Simulated 10.5% p.a.)', linestyle='--')
plt.plot(portfolio_cum, label='Total Portfolio', color='black', linewidth=2)

plt.title('5-Year Cumulative Returns of Portfolio Components and Total Portfolio')
plt.xlabel('Date')
plt.ylabel('Cumulative Return (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
