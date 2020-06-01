# WhatsbusyInternChallange

The problem I am trying  to solve is forecasting the data for the timeseries.
There are two coloumns in the dataset one is num of visitors and the other is date.
There are several models that can be used in forcasting.Amongst all of them ARIMA is widely used.
The model that can used for the dataset depends on several factors,One way to check which model 
gives the best accuracy is to check the mean squared error.
The model with less mean squared error can be taken as final model.
The two methods used in the current project are naive based,mean forecast, ARIMA model.
Suprisingly Naive based gave better accuracy than ARIMA and mean forcast.
Naive based depends on the previous day's value.
ARIMA model is rejected because of the high values of q and stationarity is not established at high values of q.
As a result the aic value is higher which indicates that is is bad model to fit into.


 