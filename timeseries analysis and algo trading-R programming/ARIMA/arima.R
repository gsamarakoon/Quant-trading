
set.seed(3)

#simulate an ARIMA process with AR(1),I(1) and MA(1) and the coefficients
x <- arima.sim(n=2000,list(order=c(1,1,1),ar=0.5,ma=0.1))

#plot the generated time series
plot(x)

#let's fit an ARIMA model with order (1,1,1)
x.arima <- arima(x,order=c(1,1,1))
x.arima

#check the confidence intervals
0.4483+c(-1.96,1.96)*0.0341
0.1731+c(-1.96,1.96)*0.0372

#basically no autocorrelation
acf(resid(x.arima))

#Ljung-Box test 
Box.test(resid(x.arima),lag=25,type="Ljung-Box")
