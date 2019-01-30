#if you do not have already installed you have to do so
install.packages("quantmod")
#this is how we can fetch finance related date from the web
require(quantmod)

#package needed for GARCH model
install.packages("tseries")
require("tseries")

#we download S&P500 prices from Yahoo Finance
data <- getSymbols("SP500",src="FRED", from="1990-01-01")

#log daily returns
returns <- diff(log((SP500)))

#we are courious about the returns aclusively (not dates included)
returns <- as.numeric(returns)
#do not include values with NA invalid values
returns <- returns[!is.na(returns)]

#finding the optimal coefficients for ARIMA(p,d,q)
result.aic <- Inf
result.order <- c(0,0,0)

for(p in 1:4) for(d in 0:1) for(q in 1:4){
  actual.aic <- AIC(arima(returns, order=c(p, d, q),optim.control=list(maxit = 1000))) 
  if (actual.aic < result.aic) { 
    result.aic <- actual.aic 
    result.order <- c(p, d, q) 
    result.arima <- arima(returns, order=result.order,optim.control=list(maxit = 1000)) 
  } 
}

#order of final ARIMA model
result.order

#it is very similar to white noise
acf(resid(result.arima))

#but we have to check the square ... there is some heteroskedastic behaviour
#because the variance is changing var(t) !!!
acf(resid(result.arima)^2)

#let's use GARCH model to explain autocorrelation in the residuals
#we apply GARCH on ARIMA model residuals
result.garch <- garch(resid(result.arima),trace=F)
#get rid of the first NA invalid value
result.residuals <- result.garch$res[-1]

#the residuals are OK but we have to check the squared residuals to make sure
#we can explain heteroskedastic behaviour
acf(result.residuals)

#squared residuals autocorrelation is like white noise: we can explain 
#heteroskedasticity 
acf(result.residuals^2)
