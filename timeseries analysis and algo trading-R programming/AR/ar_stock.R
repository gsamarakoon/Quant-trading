#if you do not have already installed you have to do so
install.packages("quantmod")

#this is how we can fetch finance related date from the web
require(quantmod)

#we download AAPL stock prices from Yahoo Finance
getSymbols("AAPL",src="yahoo")

#we want to plot the adjusted closing prices
plot(Ad(AAPL))

#log daily returns of AAPL stock (for adjusted closing price)
aaplreturn = diff(log(Ad(AAPL)))

#plot the returns
plot(aaplreturn)

#autocorrelation function plot
acf(aaplreturn,na.action=na.omit)

#use autoregressive model to approximate the coefficients
aaplreturn.ar <- ar(aaplreturn,na.action=na.omit)
#the order of AR(p) model (so the value of p)
aaplreturn.ar$order
#the coefficients: as many as the value of p
aaplreturn.ar$ar
#calculate the variance for the coefficients to be able to calculate the error
aaplreturn.ar$asy.var

#we can caclculate standard error and confidence intervals for the parameters
#sqrt() to end up with the standard error
#we can construct 95% confidence intervals for each parameter
#the value of 1.96 is based on the fact that 95% of the area of a normal 
#distribution is within 1.96 standard deviations of the mean
0.004535038+c(-1.96,1.96)*sqrt(3.644595e-04)
-0.035878800+c(-1.96,1.96)*sqrt(3.644595e-04)
0.002494075+c(-1.96,1.96)*sqrt(3.644595e-04)
0.053281380+c(-1.96,1.96)*sqrt(3.644595e-04)

#the first parameter is out of the confidence interval so this model is not able to grasp the serial correlation NOT A GOOD MODEL!
#AR(4) is certainly not the underlying model 