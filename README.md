# This folder contains multiple trading models:
  1) SWENSEN - LONG ONLY ETF PORTFOLIO
  2) MOVING AVERAGES ON BITCOIN
  3) BOND ETF ANALYSYS- Find ETF Bond funds that move counter to SPY
  4) COMPARING LAZY PORTFOLIOS
  5) Comparing ONLINE PORTFOLIO SELECTION algorithms on a diversified set of ETFs
  6) BUYING AND HOLDING SPY

# SWENSEN: 
 This algorithm defines a long-only portfolio of 6 ETF's and rebalances all of 
    them when any one of them is off the target by a threshold of 5%.
    It is based on David Swensen's rationale for portfolio construction as defined in
    his book: "Unconventional Success: A Fundamental Approach to Personal Investment":
    http://www.amazon.com/Unconventional-Success-Fundamental-Approach-Investment/dp/0743228383 .
   
    The representative ETF's are defined here:
    http://seekingalpha.com/article/531591-swensens-6-etf-portfolio
    
    The target percents are defined here:
    https://www.yalealumnimagazine.com/articles/2398/david-swensen-s-guide-to-sleeping-soundly
    
    The rebalancing strategy is defined in the book and here:
    http://socialize.morningstar.com/NewSocialize/forums/p/102207/102207.aspx
    
    This is effectively a passive managment strategy or Lazy portfolio:
    http://en.wikipedia.org/wiki/Passive_management
    http://www.bogleheads.org/wiki/Lazy_portfolios
    
    Taxes are not modelled.
    
    NOTE: This algo can run in minute-mode simulation and is compatible with LIVE TRADING.

# MOVING AVERAGE:
this file movingavg.ipynb- contains a moving average tradng model being tested on BITCOIN

Commissions: Assumed no transaction costs, even though typical exchanges charge 25 basis point (bps) per dollar transacted. This would have negative impact on PnL.

Shorting: Assumed that we can openly short a cryptocurrency pair and that we pay no fees for holding short positions. In reality, some exchanges do not support shorting and if they do, other fees are associated with such transactions.

Slippage: Another assumption is that we can always get filled on the close price. Given how ‘thin’ some crypto pairs books are, other things being equal, we will get filled at progressively worse prices as our positions grow in size. In addition, as other traders may use similar signals, it will only increase the chances that the price may “run away” from us as we try and get a fill.

Market Impact: In our backtest, we assume that our trades have no impact on subsequent market dynamics. In reality, market can react positively or negatively to a trade. Backtesting market impact creates a never ending spiral of complexity, as it depends, upon other things on liquidity, number of market participants and different states of the market.

Biases:

Overfitting: When we optimised for the best possible combination of leading and lagging look-back periods, we have taken the available historical data and threw a bunch of numbers at it to see what sticks. Whilst we did find a pattern that suggested that best PnLs are the ones whose lead / lag ratio is around 1/8, we ultimately did that on historical data and there is no guarantee that the same results would hold for live performance. In order to overcome this phenomenon, we could split our data into two sets — the one we find the best parameters on and the one we test these parameters on. If the test PnL holds up, it is safe to assume that the parameters are significant. There is a whole study in Statistics dedicated primarily to mitigation of overfitting.

Exchange Risk:

Last but definitely not least, it is almost impossible to model exchange risk. Historically, a large portion of exchanges get hacked or otherwise compromised. Finding trustworthy exchanges requires further research.

# LAZY PORTFOLIOS
Comparing Lazy Portfolios
This Quantopian Research based notebook compares SPY to the following portfolios:

  SPY 100%
  VTI/AGG 50/50 (stocks and bonds 50% / 50%)
  VTI/AGG 60/40
  VTI/AGG 70/30
  The Swensen Portfolio: TIP 15%, TLT 15%, VNQ 15%, EEM 10%, EFA 15%, VTI 30%
  A variation (POP): EDV 30%,VNQ 15%,VWO','EFA','VBR','MDY','RSP') context.pcts = [ 0.30, 0.15, 0.1, 0.15, 0.10, 0.0, 0.2]

# Comparing OLPS algorithms on a diversified set of ETFs

Let's compare the state of the art in OnLine Portfolio Selection (OLPS) algorithms and determine if they can enhance a rebalanced passive strategy in practice. Online Portfolio Selection: A Survey by Bin Li and Steven C. H. Hoi provides the most comprehensive review of multi-period portfolio allocation optimization algorithms. The authors developed the OLPS Toolbox, but here we use Mojmir Vinkler's implementation and extend his comparison to a more recent timeline with a set of ETFs to avoid survivorship bias (as suggested by Ernie Chan) and idiosyncratic risk.

Vinkler does all the hard work in his thesis, and concludes that Universal Portfolios work practically the same as Constant Rebalanced Portfolios, and work better for an uncorrelated set of small and volatile stocks. Here I'm looking to find if any strategy is applicable to a set of ETFs.

The agorithms compared are:

Type	Name	Algo	Reference
Benchmark	BAH	Buy and Hold	
Benchmark	CRP	Constant Rebalanced Portfolio	T. Cover. Universal Portfolios, 1991.
Benchmark	UCRP	Uniform CRP (UCRP), a special case of CRP with all weights being equal	T. Cover. Universal Portfolios, 1991.
Benchmark	BCRP	Best Constant Rebalanced Portfolio	T. Cover. Universal Portfolios, 1991.
Follow-the-Winner	UP	Universal Portfolio	T. Cover. Universal Portfolios, 1991.
Follow-the-Winner	EG	Exponential Gradient	Helmbold, David P., et al. On‐Line Portfolio Selection Using Multiplicative Updates Mathematical Finance 8.4 (1998): 325-347.
Follow-the-Winner	ONS	Online Newton Step	A. Agarwal, E. Hazan, S. Kale, R. E. Schapire. Algorithms for Portfolio Management based on the Newton Method, 2006.
Follow-the-Loser	Anticor	Anticorrelation	A. Borodin, R. El-Yaniv, and V. Gogan. Can we learn to beat the best stock, 2005
Follow-the-Loser	PAMR	Passive Aggressive Mean Reversion	B. Li, P. Zhao, S. C.H. Hoi, and V. Gopalkrishnan. Pamr: Passive aggressive mean reversion strategy for portfolio selection, 2012.
Follow-the-Loser	CWMR	Confidence Weighted Mean Reversion	B. Li, S. C. H. Hoi, P. L. Zhao, and V. Gopalkrishnan.Confidence weighted mean reversion strategy for online portfolio selection, 2013.
Follow-the-Loser	OLMAR	Online Moving Average Reversion	Bin Li and Steven C. H. Hoi On-Line Portfolio Selection with Moving Average Reversion
Follow-the-Loser	RMR	Robust Median Reversion	D. Huang, J. Zhou, B. Li, S. C.vH. Hoi, S. Zhou Robust Median Reversion Strategy for On-Line Portfolio Selection, 2013.
Pattern Matching	Kelly	Kelly fractional betting	Kelly Criterion
Pattern Matching	BNN	nonparametric nearest neighbor log-optimal	L. Gyorfi, G. Lugosi, and F. Udina. Nonparametric kernel based sequential investment strategies. Mathematical Finance 16 (2006) 337–357.
Pattern Matching	CORN	correlation-driven nonparametric learning	B. Li, S. C. H. Hoi, and V. Gopalkrishnan. Corn: correlation-driven nonparametric learning approach for portfolio selection, 2011.


# A benchmark comparison to buying and holding SPY at 100%.
    NOTE: This algo can run in minute-mode simulation and is compatible with LIVE TRADING.
