import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from datetime import datetime

st.set_page_config(page_title="Portfolio Analyzer", layout="wide", initial_sidebar_state="expanded")
st.title("📊 Portfolio Return Visualizer")
st.markdown("""
This app visualizes the 5-year cumulative returns of a custom portfolio with adjustable allocations to:
- Equities (Index of your choice)
- Bonds (Index of your choice)
- Mezzanine finance (simulated)
""")

# --- Sidebar Inputs ---
st.sidebar.header("📁 Upload Your CSVs")
equity_file = st.sidebar.file_uploader("Upload your Equities Index CSV", type="csv")
bond_file = st.sidebar.file_uploader("Upload your Bond Index CSV", type="csv")

st.sidebar.header("⚖️ Portfolio Allocation")
equity_pct = st.sidebar.slider("Equity Allocation (%)", 0, 100, 33)
bond_pct = st.sidebar.slider("Bond Allocation (%)", 0, 100, 33)
mezz_pct = st.sidebar.slider("Mezzanine Allocation (%)", 0, 100, 34)

total_pct = equity_pct + bond_pct + mezz_pct
if total_pct != 100:
    st.sidebar.error("Total allocation must equal 100%.")

st.sidebar.header("⚙️ Mezzanine Return")
mezz_return = st.sidebar.slider("Annual Return (%)", 5.0, 20.0, 10.5, 0.1)

st.sidebar.header("📅 Date Frequency")
date_freq = st.sidebar.radio("Select View", ["Daily", "Monthly", "Yearly"], horizontal=True)

# --- Load Data ---
def load_csv(file):
    df = pd.read_csv(file, parse_dates=['Date'])
    df = df[['Date', 'Adj Close']].dropna()
    df.set_index('Date', inplace=True)
    df = df.sort_index()
    return df['Adj Close']

if equity_file and bond_file and total_pct == 100:
    equity = load_csv(equity_file)
    bond = load_csv(bond_file)

    # Align and trim to 5 years
    end_date = datetime.now()
    start_date = end_date.replace(year=end_date.year - 5)

    equity = equity[(equity.index >= start_date) & (equity.index <= end_date)]
    bond = bond[(bond.index >= start_date) & (bond.index <= end_date)]
    common_idx = equity.index.intersection(bond.index)

    equity = equity.loc[common_idx]
    bond = bond.loc[common_idx]

    # Simulated mezzanine
    daily_return = (1 + mezz_return / 100) ** (1 / 252)
    mezz = pd.Series(np.full(len(common_idx), daily_return), index=common_idx).cumprod()
    mezz *= 100  # normalize to 100

    # Normalize equities/bonds
    equity_cum = (equity / equity.iloc[0]) * 100
    bond_cum = (bond / bond.iloc[0]) * 100

    # Frequency Resampling
    if date_freq == "Monthly":
        equity_cum = equity_cum.resample('M').last()
        bond_cum = bond_cum.resample('M').last()
        mezz = mezz.resample('M').last()
    elif date_freq == "Yearly":
        equity_cum = equity_cum.resample('Y').last()
        bond_cum = bond_cum.resample('Y').last()
        mezz = mezz.resample('Y').last()

    # Compute portfolio cumulative
    weights = np.array([equity_pct / 100, bond_pct / 100, mezz_pct / 100])
    df = pd.DataFrame({
        'Equity': equity_cum,
        'Bond': bond_cum,
        'Mezz': mezz
    })
    portfolio_cum = (df * weights).sum(axis=1)

    # Pie chart
    st.subheader("📊 Allocation Breakdown")
    alloc_fig = go.Figure(data=[go.Pie(
        labels=['Bonds', 'Equities', 'Mezzanine'],
        values=[bond_pct, equity_pct, mezz_pct],  # <-- fixed here
        hole=0.5
    )])
    alloc_fig.update_layout(template="plotly_dark", width=500, height=400)
    st.plotly_chart(alloc_fig, use_container_width=False)

    # --- Metrics ---
    def cagr(series):
        total = series.iloc[-1] / series.iloc[0]
        years = (series.index[-1] - series.index[0]).days / 365.25
        return (total ** (1 / years)) - 1

    def volatility(series):
        returns = series.pct_change().dropna()
        return returns.std() * np.sqrt(252)

    def max_drawdown(series):
        cummax = series.cummax()
        drawdown = (series - cummax) / cummax
        return drawdown.min()

    st.subheader("📌 Portfolio Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("CAGR", f"{cagr(portfolio_cum)*100:.2f}%")
    col2.metric("Volatility", f"{volatility(portfolio_cum):.2%}")
    col3.metric("Max Drawdown", f"{max_drawdown(portfolio_cum)*100:.2f}%")


    # --- Plotly Chart with Toggle ---
    st.subheader("📈 Cumulative Returns (" + date_freq + ")")
    show_portfolio_overlay = st.toggle("Show Total Portfolio Overlay", value=True)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=equity_cum.index, y=equity_cum, name="Equities", line=dict(width=2, color='#1f77b4')))
    fig.add_trace(go.Scatter(x=bond_cum.index, y=bond_cum, name="Bonds", line=dict(width=2, color='#2ca02c')))
    fig.add_trace(go.Scatter(x=mezz.index, y=mezz, name="Mezzanine (Simulated)", line=dict(width=2, dash='dot', color='#ff7f0e')))

    if show_portfolio_overlay:
        fig.add_trace(go.Scatter(
            x=portfolio_cum.index,
            y=portfolio_cum,
            name="Total Portfolio",
            line=dict(width=4, color='aqua'),
            mode='lines',
            hovertemplate='%{y:.2f}%<br>%{x|%Y-%m-%d}<extra>Total Portfolio</extra>'
        ))

    fig.update_layout(
        title="Portfolio Components Over Time",
        xaxis_title="Date",
        yaxis_title="Cumulative Return (%)",
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5),
        template="plotly_dark",
        height=500,
        margin=dict(l=20, r=20, t=60, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Please upload both CSV files and ensure your allocation totals 100%.")
