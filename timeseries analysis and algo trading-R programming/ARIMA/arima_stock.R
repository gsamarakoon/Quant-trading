#if you do not have already installed you have to do so
install.packages("quantmod")
#install 'forecast' library to be able to make predictions in the future
install.packages("forecast")

#this is how we can fetch finance related date from the web
require(quantmod)
#this is how we can make predictions in the future
require(forecast)

#we download IBM stock prices from Yahoo Finance
getSymbols("IBM",src="yahoo")

#log daily returns
returns <- diff(log(Ad(IBM)))

#first value is NA so get rid of it
returns <- returns[-1]

#let's find the optimal p,d,q values with AIC 
result.aic <- Inf
result.order <- c(0,0,0)

for (p in 1:4) for (d in 0:1) for (q in 1:4){
  actual.aic <- AIC(arima(returns, order=c(p, d, q),optim.control=list(maxit = 1000))) 
  if (actual.aic < result.aic) { 
    result.aic <- actual.aic 
    result.order <- c(p, d, q) 
    result.arima <- arima(returns, order=result.order,optim.control=list(maxit = 1000)) 
  } 
}

#order of ARIMA model
result.order

#check autocorrelation
acf(resid(result.arima),na.action=na.omit)

#check Ljung-Box p-value
Box.test(resid(result.arima),lag=25,type="Ljung-Box")

#let's forecast the log daily returns in the coming 50 days!!!
plot(forecast(result.arima,h=50))
