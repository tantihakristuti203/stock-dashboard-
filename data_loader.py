import yfinance as yf
import pandas as pd

def download_stock_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end, progress=False)
    
    # Ambil Adjusted Close
    if isinstance(data.columns, pd.MultiIndex):
        if 'Adj Close' in data.columns.get_level_values(0):
            price = data['Adj Close']
        else:
            price = data['Close']
    else:
        if 'Adj Close' in data.columns:
            price = data['Adj Close']
        else:
            price = data['Close']
    
    return price

def download_benchmark_data(benchmark="^JKSE", start=None, end=None):
    data = yf.download(benchmark, start=start, end=end, progress=False)
    if isinstance(data.columns, pd.MultiIndex):
        if 'Adj Close' in data.columns.get_level_values(0):
            price = data['Adj Close']
        else:
            price = data['Close']
    else:
        if 'Adj Close' in data.columns:
            price = data['Adj Close']
        else:
            price = data['Close']
    return price
