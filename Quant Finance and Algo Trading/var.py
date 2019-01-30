import numpy as np
import pandas as pd
from scipy.stats import norm
import pandas_datareader.data as web
import datetime

#if we want to calculate VaR for tomorrow
def value_at_risk(position, c, mu, sigma):
	alpha=norm.ppf(1-c)
	var = position*(mu-sigma*alpha)
	return var
	
#we want to calculate VaR in n days time 10days
#we have to consider that the mean and standard deviation will change
#mu = mu*n and sigma=sigma*sqrt(n) we have to use these tranformations
def value_at_risk_long(S, c, mu, sigma,n):
	alpha=norm.ppf(1-c)
	var = S*(mu*n-sigma*alpha*np.sqrt(n))
	return var
	
if __name__ == "__main__":
	
	#historical data to approximate mean and standard deviation
	start_date = datetime.datetime(2014,1,1)
	end_date = datetime.datetime(2017,10,15)
	
	#download stock related data from Yahoo Finance
	citi = web.DataReader('C',data_source='yahoo',start=start_date,end=end_date)
	
	#we can use pct_change() to calculate daily returns
	citi['returns'] = citi['Adj Close'].pct_change()
	
	S = 1e6 	#this is the investment (stocks or whatever)
	c=0.95		#condifence level: this time it is 95%
	
	#we can assume daily returns to be normally sidtributed: mean and variance (standard deviation)
	#can describe the process
	mu = np.mean(citi['returns'])
	sigma = np.std(citi['returns'])

	print('Value at risk is: $%0.2f' % value_at_risk(S,c,mu,sigma))
	
	
