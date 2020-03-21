# Autoregressive Inegrated Moving Average
from statsmodels.tsa.arima_model import ARIMA
from random import random

# contrived dataset
data = [x + random() for x in range(1, 100)]
# fit model
model = ARIMA(data, order=(1, 1, 1))
model_fit = model.fit(disp=False)
# make prediction
yhat = model_fit.predict(len(data), len(data), typ="levels")
print(yhat)
