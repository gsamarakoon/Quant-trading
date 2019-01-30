
set.seed(2)

#first we generate 100 white noise values
w <- rnorm(2000,mean=0,sd=1)

#we create 100 items with value 0 for the x(t) time series  ... x(1)=0 first items value
x <- rep(0,2000)

#random walk is x(t) = x(t-1) (previous value) +w (white noise)
for(t in 2:2000) x[t] <- x[t-1] + w[t]

#lets plot the random walk with lines ("l")
plot(x,type="l")

#autocorrelation plot
acf(x)

#ok random walk is not stationary process but we can make
#it stationary by using differencing transformation
acf(diff(x), na.action=na.omit)
