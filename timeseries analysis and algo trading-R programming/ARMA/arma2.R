
set.seed(3)

#we can construct an ARMA(p,q) simulation with the AR and MA components
x <- arima.sim(n=2000,model=list(ar=c(0.4,-0.2,0.6),ma=c(0.6,-0.4)))

plot(x)

#calculate the optimal q and p values with AIC
solution.aic <- Inf
solution.order <- c(0,0,0)

#we don't know the q and p parameters so lets generate several ARMA(p,q) models
#and choose the best according to the AIC
for(i in 1:4) for(j in 1:4) { 
  
  actual.aic <- AIC(arima(x,order=c(i,0,j),optim.control=list(maxit = 1000)))
  
  if( actual.aic < solution.aic){
    solution.aic <- actual.aic
    solution.order <- c(i,0,j)
    solution.arma <- arima(x,order=solution.order,optim.control=list(maxit = 1000))
  }
}

solution.aic
solution.order
solution.arma

#no serial correlation in the residual y(t) series
acf(resid(solution.arma))

#let's apply Ljung-Box test
#if the p-value>0.05 it means that the residuals are independent
#at the 95% level so ARMA model is a good model
Box.test(resid(solution.arma),lag=20,type="Ljung-Box")


