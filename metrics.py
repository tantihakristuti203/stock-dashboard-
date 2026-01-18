import numpy as np
import pandas as pd

def compute_returns(price, rule="Y"):
    price_r = price.resample(rule).last()
    returns = np.log(price_r / price_r.shift(1)).dropna()
    cumulative = returns.cumsum().apply(np.exp)
    return price_r, returns, cumulative

def compute_portfolio(returns, tickers):
    weights = np.array([1/len(tickers)]*len(tickers))
    portfolio_return = (returns*weights).sum(axis=1)
    return portfolio_return

def compute_sharpe(returns, rf=0.05):
    mean_r = returns.mean()
    vol = returns.std()
    sharpe = (mean_r - rf)/vol
    return sharpe, vol

def compute_beta(returns, benchmark_returns):
    beta = {}
    for t in returns.columns:
        combined = pd.concat([returns[t], benchmark_returns], axis=1).dropna()
        if not combined.empty:
            cov = np.cov(combined.iloc[:,0], combined.iloc[:,1])[0,1]
            beta[t] = cov / np.var(combined.iloc[:,1])
        else:
            beta[t] = np.nan
    return beta
