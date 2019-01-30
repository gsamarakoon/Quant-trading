set.seed(1)

#generate values for w(t) white noise
w <- rnorm(1000)

#generate values for x(t) time series x(t=1)=0
x <- rep(0,1000)

#we simulate MA(1) with one coefficient (0.4)
for(t in 3:1000) x[t] <- w[t]+0.4*w[t-1]

plot(x,type="l")
acf(x)

#there is no ma() function in R so we use ARIMA model without the AR and Integrated parts
#thats why we set AR component to be 0 + integrated component to be 0 ... MA(1) model finally
x.ma <-arima(x,order=c(0,0,1)) 
x.ma

#the beta coefficient is 0.3757 + we have the standard error (0.0306)
0.3757+c(-1.96,1.96)*0.0306
