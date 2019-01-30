from math import exp

def zero_bond_price(par_value,market_rate,n):
	return par_value/(1+market_rate)**n
	
def bond_price(par_value,coupon, market_rate,n):
	c = par_value*coupon
	return c/market_rate*(1-(1/(1+market_rate)**n))+par_value/(1+market_rate)**n
	
if __name__ == "__main__":
    
	par_value=1000   #par value of the bond
	coupon=0.05		 #bond yield - coupon 
	n=3	 			 #years
	market_rate=0.04 #market rate of return
	
	print("Price of the zero-coupon bond: $%0.2f" % zero_bond_price(par_value,market_rate,n))
	print("Price of the coupon bond: $%0.2f" % bond_price(par_value,coupon,market_rate,n))
	
