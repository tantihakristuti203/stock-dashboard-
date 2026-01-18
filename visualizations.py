import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set_style("whitegrid")

def plot_prices(price_r):
    fig, ax = plt.subplots()
    price_r.plot(ax=ax)
    ax.set_title("Fluktuasi Harga Saham")
    st.pyplot(fig)

def plot_returns(returns):
    fig, ax = plt.subplots()
    returns.plot(kind="bar", ax=ax)
    ax.axhline(0, color="black")
    ax.set_title("Return Log per Periode")
    st.pyplot(fig)

def plot_cumulative(cumulative):
    fig, ax = plt.subplots()
    cumulative.plot(ax=ax)
    ax.set_title("Cumulative Return")
    st.pyplot(fig)

def plot_correlation(returns):
    fig, ax = plt.subplots()
    sns.heatmap(returns.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)
