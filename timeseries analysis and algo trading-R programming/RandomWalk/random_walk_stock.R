#if you do not have already installed you have to do so
install.packages("quantmod")

#this is how we can fetch finance related date from the web
require(quantmod)

#we download AAPL stock prices from Yahoo Finance
getSymbols("^GSPC",src="yahoo")

#there are several columns: high (Hi), low (Lo), closing price (Cl), adjusted closing price(Ad)
Ad(AAPL)
#we want to plot the adjusted closing prices
plot(Ad(AAPL))

#if the process is indeed a random walk: the diff series
#has no serial correlation !!! so the residuals is something like white noise
acf(diff(Ad(GSPC)),na.action=na.omit)
