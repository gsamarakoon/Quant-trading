
#package needed for GARCH model
install.packages("tseries")
require("tseries")

set.seed(1)

#these are the coefficients for GARCH(1,1) model
alpha0 <- 0.1
alpha1 <- 0.4
beta1 <- 0.2

#white noise term values
w <- rnorm(2000)

#the actual x(t) time series
x <-rep(0,2000)
#volatility squared values
sigma2 <- rep(0,2000)

#GARCH(1,1) model simulation
for(t in 2:2000){
  sigma2[t] <- alpha0+alpha1*(x[t-1]^2)+beta1*sigma2[t-1]
  x[t] <- w[t]*sqrt(sigma2[t])
}

#autocorrelation plot it seems to be OK 
acf(x)

#but the squared residuals shows there is volatility clustering
acf(x*x)

#use the GARCH function
x.garch <- garch(x,trace=FALSE)
#show the condifence intervals for the parameters
confint(x.garch)
