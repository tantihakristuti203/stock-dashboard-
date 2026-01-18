import streamlit as st
import numpy as np
from data_loader import download_stock_data, download_benchmark_data
from metrics import compute_returns, compute_portfolio, compute_sharpe, compute_beta
from visualizations import plot_prices, plot_returns, plot_cumulative, plot_correlation
from utils import scoring

st.set_page_config("Stock Dashboard Pro", layout="wide")
st.title("📊 Stock Dashboard Pro")

# ======= Sidebar =======
st.sidebar.title("⚙️ Kontrol Analisis")
tickers = st.sidebar.multiselect(
    "Pilih Saham",
    ["MNCN.JK","SCMA.JK","VIVA.JK","TMPO.JK","ABBA.JK","MDIA.JK","MSIN.JK","DOOH.JK","FORU.JK","IPTV.JK"],
    default=["MNCN.JK","ABBA.JK"]
)
year_range = st.sidebar.slider("Rentang Tahun", 2015, 2025, (2015,2024))
periode = st.sidebar.radio("Periode", ["Tahunan","Kuartalan","Mingguan"])
benchmark_on = st.sidebar.checkbox("Bandingkan dengan IHSG", True)

if not tickers:
    st.stop()

start = f"{year_range[0]}-01-01"
end = f"{year_range[1]}-12-31"

# ======= Data =======
price = download_stock_data(tickers, start, end)
if benchmark_on:
    ihsg = download_benchmark_data(start=start, end=end)

# ======= Metrics =======
rule = {"Tahunan":"Y","Kuartalan":"Q","Mingguan":"W"}[periode]
price_r, returns, cumulative = compute_returns(price, rule=rule)
portfolio_return = compute_portfolio(returns, tickers)
sharpe, vol = compute_sharpe(returns)

if benchmark_on:
    _, ihsg_returns, _ = compute_returns(ihsg, rule=rule)
    beta = compute_beta(returns, ihsg_returns)
else:
    beta = {t:np.nan for t in tickers}

score = {t:scoring(sharpe[t], vol[t], beta[t]) for t in tickers}

# ======= Tabs =======
tab1, tab2, tab3, tab4 = st.tabs(["📈 Harga","📊 Return","📈 Cumulative","📊 Korelasi"])

with tab1:
    st.subheader("📌 Harga Saham")
    plot_prices(price_r)

with tab2:
    st.subheader("📌 Return Log")
    plot_returns(returns)

with tab3:
    st.subheader("📌 Cumulative Return")
    plot_cumulative(cumulative)

with tab4:
    st.subheader("📌 Korelasi Antar Saham")
    plot_correlation(returns)

st.subheader("📋 Portfolio & Scoring")
st.write("Score tiap saham berdasarkan Sharpe, Volatilitas, dan Beta")
st.dataframe(pd.DataFrame(score, index=["Score"]).T)
