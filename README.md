# This folder contains multiple trading models.

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
