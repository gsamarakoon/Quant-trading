#if you do not have already installed you have to do so
install.packages("quantmod")

#this is how we can fetch finance related date from the web
require(quantmod)

#we download AAPL stock prices from Yahoo Finance
getSymbols("AAPL",src="yahoo")

#there are several columns: high (Hi), low (Lo), closing price (Cl), adjusted closing price(Ad)
Ad(AAPL)
#we want to plot the adjusted closing prices
plot(Ad(AAPL))

#this is the auto-correlation function ... get rid of the NA values
acf(diff(Ad(AAPL)),na.action=na.omit)

#statistics: mean, variance and standard deviation
mean(Ad(AAPL))
var(Ad(AAPL))
sd(Ad(AAPL))