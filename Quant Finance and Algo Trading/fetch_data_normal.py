import numpy as np
import pandas_datareader.data as web
import matplotlib.pyplot as plt

stocks = ['AAPL']

start_date='01/01/2001'
end_date='01/01/2017'

data = web.DataReader(stocks, data_source='yahoo', start=start_date, end=end_date)['Adj Close']

daily_returns = (data/data.shift(1))-1

daily_returns.hist(bins=100)
plt.show()
