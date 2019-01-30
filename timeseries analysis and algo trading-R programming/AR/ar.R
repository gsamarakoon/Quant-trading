set.seed(1)

#generate values for w(t) white noise
w <- rnorm(1000)

#generate values for x(t) time series x(t=1)=0
x <- rep(0,1000)

#we simulate AR(2) with two coefficients (0.6 and -0.4)
for(t in 3:1000) x[t] <- 0.6*x[t-1]-0.4*x[t-2]+w[t]

plot(x,type="l")
acf(x)

#let's try to use AR(2) to figure out the coefficients
#we use Maximum Likelihood Estimator to find out the coefficients
x.ar <- ar(x,method="mle")

#print out the order of AR (it should be 2 of course)
x.ar$order

#print out the coefficients we calculate with MLE
x.ar$ar
