import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
import sklearn
import pandas_datareader.data as web
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix

def create_dataset(stock_symbol, start_date, end_date, lags=5):

    #fetch the stock data from Yahoo Finance
	df = web.DataReader(stock_symbol,"yahoo",start_date,end_date)

    #create a new dataframe
	#we want to use additional features: lagged returns...today's returns, yesterday's returns etc
	tslag = pd.DataFrame(index=df.index)
	tslag["Today"] = df["Adj Close"]
	tslag["Volume"] = df["Volume"]

    # Create the shifted lag series of prior trading period close values
	for i in range(0, lags):
		tslag["Lag%s" % str(i+1)] = df["Adj Close"].shift(i+1)

    #create the returns DataFrame
	dfret = pd.DataFrame(index=tslag.index)
	dfret["Volume"] = tslag["Volume"]
	dfret["Today"] = tslag["Today"].pct_change()*100.0

    #create the lagged percentage returns columns
	for i in range(0, lags):
		dfret["Lag%s" % str(i+1)] = tslag["Lag%s" % str(i+1)].pct_change()*100.0

    #"Direction" column (+1 or -1) indicating an up/down day
	dfret["Direction"] = np.sign(dfret["Today"])
	
	#because of the shifts there are NaN values ... we want to get rid of those NaNs
	dfret.drop(dfret.index[:5], inplace=True)

	return dfret


if __name__ == "__main__":
    
	# Create a lagged series of the S&P500 US stock market index
	data = create_dataset("AAPL", datetime(2012,1,1), datetime(2017,5,31), lags=5)

    # Use the prior two days of returns as predictor 
    # values, with direction as the response
	X = data[["Lag1","Lag2","Lag3","Lag4"]]
	y = data["Direction"]

    # The test data is split into two parts: Before and after 1st Jan 2005.
	start_test = datetime(2017,1,1)

    # Create training and test sets
	X_train = X[X.index < start_test]
	X_test = X[X.index >= start_test]
	y_train = y[y.index < start_test]
	y_test = y[y.index >= start_test]
   
    #we use Logistic Regression as the machine learning model
	model = LinearSVC()
	
    #train the model on the training set
	model.fit(X_train, y_train)

    #make an array of predictions on the test set
	pred = model.predict(X_test)

    #output the hit-rate and the confusion matrix for the model
	print("Accuracy of SVM model: %0.3f" % model.score(X_test, y_test))
	print("Confusion matrix: \n%s" % confusion_matrix(pred, y_test))