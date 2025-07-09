import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

"""
What is Value at Risk? Value at Risk or Var is an estimate with a given degree of confidence, 
of how much one can lose from one's portfolio over a given time
"""

# Load adj close prices
prices = pd.read_csv("adj_close_prices.csv", parse_dates=["Date"], index_col="Date")
prices = prices.sort_index()

# compute log returns
log_returns = np.log(prices / prices.shift(1)).dropna()

# create log returns csv
# log_returns.to_csv("log_returns.csv")
"""
Log returns are continuously compunded returns, a way of measuring how much an assets 
price changes over time. Useful for quantitative finance because of mathmatical properties. 
"""

# sample portfolio weight vector
weights = np.array([1/6] * 6)

# computing volitility
daily_vol = log_returns.std()
annualized_vol = daily_vol * np.sqrt(252)

# calculating correlation matrix
correlation_matrix = log_returns.corr()


def Historical_VaR(weights, log_returns, amount_invested, confidence, lookback_days=520):
    p = 1 - confidence
    portfolio_returns = log_returns.dot(weights)
    hist_Var = np.percentile(portfolio_returns, p)

