'''📈 Time Series Analysis with Pandas
'''
import pandas as pd

# Load time series data
df = pd.read_csv("stock_prices.csv", parse_dates=['Date'], index_col='Date')

# Resample to monthly average
monthly_avg = df['Close'].resample('M').mean()

# Rolling mean (moving average)
df['MA_30'] = df['Close'].rolling(window=30).mean()

# Detect daily returns
df['Daily_Return'] = df['Close'].pct_change()

print(monthly_avg.head())
print(df[['Close','MA_30','Daily_Return']].head())