
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


{"date":1483920000,"high":916.41833046,"low":880,"open":916.41832969,"close":902,"volume":1561326.5181909,"quoteVolume":1743.42476903,"weightedAverage":895.55141462}


# In[8]:


def CryptoData(symbol, frequency):
    #Params: String symbol, int frequency = 300,900,1800,7200,14400,86400
    #Returns: df from first available date
    url ='https://poloniex.com/public?command=returnChartData&currencyPair='+symbol+'&end=9999999999&period='+str(frequency)+'&start=0'
    df = pd.read_json(url)
    df.set_index('date',inplace=True)
    return df


# In[10]:


df = CryptoData('USDT_BTC', 86400)['close']


# In[17]:


df.head()


# In[15]:


df.plot()


# In[16]:


df.pct_change().describe()


# In[18]:


df.pct_change().hist(bins=100)


# In[19]:


def CryptoDataCSV(symbol, frequency):
    #Params: String symbol, int frequency = 300,900,1800,7200,14400,86400
    #Returns: df from first available date
    url ='https://poloniex.com/public?command=returnChartData&currencyPair='+symbol+'&end=9999999999&period='+str(frequency)+'&start=0'
    df = pd.read_json(url)
    df.set_index('date',inplace=True)
    df.to_csv(symbol + '.csv')
    print('Processed: ' + symbol)


# In[20]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[22]:


tickers = ['USDT_BTC','USDT_BCH','USDT_ETC','USDT_XMR','USDT_ETH','USDT_DASH',
 'USDT_XRP','USDT_LTC','USDT_NXT','USDT_STR','USDT_REP','USDT_ZEC']


# In[25]:


# CryptoDataCSV()
for ticker in tickers:
    CryptoDataCSV(ticker, 86400)


# In[26]:


tickers =  ['USDT_BTC','USDT_ETC','USDT_XMR','USDT_ETH','USDT_DASH',
 'USDT_XRP','USDT_LTC','USDT_NXT','USDT_STR','USDT_REP','USDT_ZEC']


# In[27]:


crypto_df = pd.DataFrame()
for ticker in tickers:
    crypto_df[ticker] = pd.read_csv(ticker+'.csv', index_col = 'date')['close']
crypto_df.dropna(inplace=True)


# In[28]:


crypto_df.head()


# In[30]:


crypto_df_norm = crypto_df.divide(crypto_df.iloc[0])


# In[31]:


crypto_df_norm.plot()


# In[32]:


crypto_df_pct = crypto_df.pct_change().dropna()


# In[34]:


corr = crypto_df_pct.corr()


# In[37]:


import seaborn as sns
sns.heatmap(corr, 
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)


# In[38]:


corr['USDT_XMR']['USDT_DASH']


# In[39]:


plt.scatter(crypto_df_pct['USDT_DASH'],crypto_df_pct['USDT_XMR'])
plt.xlabel('USDT_DASH % Return')
plt.ylabel('USDT_XMR % Return')


# In[40]:


import statsmodels.api as sm
model = sm.OLS(crypto_df_pct['USDT_XMR'],
               crypto_df_pct['USDT_DASH']).fit()
model.summary()


# In[43]:


'XMR % ret = DASH % ret * 0.6451'


# In[42]:


line=[model.params[0]*i for i in crypto_df_pct['USDT_DASH'].values]
plt.plot(crypto_df_pct['USDT_DASH'], line, c = 'r')
plt.scatter(crypto_df_pct['USDT_DASH'],crypto_df_pct['USDT_XMR'])
plt.xlabel('USDT_DASH % Return')
plt.ylabel('USDT_XMR % Return')


# In[44]:


def CryptoData(symbol, frequency):
    #Params: String symbol, int frequency = 300,900,1800,7200,14400,86400
    #Returns: df from first available date
    url ='https://poloniex.com/public?command=returnChartData&currencyPair='+symbol+'&end=9999999999&period='+str(frequency)+'&start=0'
    df = pd.read_json(url)
    df.set_index('date',inplace=True)
    return df


# In[45]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[46]:


df = CryptoData(symbol = 'BTC_LTC', frequency = 300)


# In[47]:


df['SMA_1000'] = df['close'].rolling(1000).mean()
df['SMA_5000'] = df['close'].rolling(5000).mean()
df[['close','SMA_1000','SMA_5000']][270000:].plot(figsize = (16,10))


# In[48]:


def test_ma(df, lead, lag, pc_thresh = 0.025):
    ma_df = df.copy()
    ma_df['lead'] = ma_df['close'].rolling(lead).mean()
    ma_df['lag'] = ma_df['close'].rolling(lag).mean()
    ma_df.dropna(inplace = True)
    ma_df['lead-lag'] = ma_df['lead'] - ma_df['lag']
    ma_df['pc_diff'] = ma_df['lead-lag'] / ma_df['close']
    ma_df['regime'] = np.where(ma_df['pc_diff'] > pc_thresh, 1, 0)
    ma_df['regime'] = np.where(ma_df['pc_diff'] < -pc_thresh, -1, ma_df['regime'])
    ma_df['Market'] = np.log(ma_df['close'] / ma_df['close'].shift(1))
    ma_df['Strategy'] = ma_df['regime'].shift(1) * ma_df['Market']
    ma_df[['Market','Strategy']] = ma_df[['Market','Strategy']].cumsum().apply(np.exp)
    return ma_df


# In[49]:


ma_df = test_ma(df, 1000, 5000).dropna()


# In[50]:


ma_df['regime'].plot(figsize=(16,5))


# In[ ]:


ma_df[['Market','Strategy']].iloc[-1]


# In[ ]:


'''Market       0.422360
Strategy    10.384434
Name: 2017-10-11 13:10:00, dtype: float64'''


# In[51]:


ma_df[['Market','Strategy']][200000:].plot(figsize = (16,10))


# In[52]:


leads = np.arange(100, 4100, 100)
lags = np.arange(4100, 8100, 100)
lead_lags = [[lead,lag] for lead in leads for lag in lags]
pnls = pd.DataFrame(index=lags,columns = leads)


# In[ ]:


for lead, lag in lead_lags:
    pnls[lead][lag] = test_ma(df, lead, lag)['Strategy'][-1]
    print(lead,lag,pnls[lead][lag])


# In[ ]:


PNLs = pnls[pnls.columns].astype(float)
plt.subplots(figsize = (14,10))
'''sns.heatmap(PNLs,cmap=’PiYG’)'''


# In[ ]:


PNLs.max()


# In[ ]:


PNLs[900][6600]


# In[ ]:


'''Transaction Costs

Commissions. We have assumed no transaction costs, even though typical exchanges charge 25 basis point (bps) per dollar transacted. This would have negative impact on PnL.

Shorting. We assume that we can openly short a cryptocurrency pair and that we pay no fees for holding short positions. In reality, some exchanges do not support shorting and if they do, other fees are associated with such transactions.

Slippage. Another assumption is that we can always get filled on the close price. Given how ‘thin’ some crypto pairs books are, other things being equal, we will get filled at progressively worse prices as our positions grow in size. In addition, as other traders may use similar signals, it will only increase the chances that the price may “run away” from us as we try and get a fill.

Market Impact. In our backtest, we assume that our trades have no impact on subsequent market dynamics. In reality, market can react positively or negatively to a trade. Backtesting market impact creates a never ending spiral of complexity, as it depends, upon other things on liquidity, number of market participants and different states of the market.

Biases

Overfitting. When we optimised for the best possible combination of leading and lagging look-back periods, we have taken the available historical data and threw a bunch of numbers at it to see what sticks. Whilst we did find a pattern that suggested that best PnLs are the ones whose lead / lag ratio is around 1/8, we ultimately did that on historical data and there is no guarantee that the same results would hold for live performance. In order to overcome this phenomenon, we could split our data into two sets — the one we find the best parameters on and the one we test these parameters on. If the test PnL holds up, it is safe to assume that the parameters are significant. There is a whole study in Statistics dedicated primarily to mitigation of overfitting.

Exchange Risk

Last but definitely not least, it is almost impossible to model exchange risk. Historically, a large portion of exchanges get hacked or otherwise compromised. Finding trustworthy exchanges requires further research.'''

