
set.seed(2)

#we can construct an ARMA(p,q) simulation with the AR and MA components
x <- arima.sim(n=2000,model=list(ar=0.4,ma=-0.2))

plot(x)

#fit an ARIMA model with AR(1) and MA(1)
arima(x,order=c(1,0,1))

#let's calculate the confidence intervals for the parameters (wide intervals!!!)
0.5201+c(-1.96,1.96)*0.0762
-0.3158+c(-1.96,1.96)*0.0846
