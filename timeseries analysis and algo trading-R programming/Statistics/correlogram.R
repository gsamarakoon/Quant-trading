
#NOTE: the first value, acf(0)=1 the series correlates with itself perfectly !!!
#the autocorrelation is approximately 0: these values are independent from each other
set.seed(1)
x <- rnorm(1000, mean=0, sd=1)
plot(x)
acf(x)

#there is a trend: the acf() is approximately linear
x <-seq(1,1000)
plot(x)
acf(x)

set.seed(1)
var(rnorm(2000,mean=0,sd=1))


