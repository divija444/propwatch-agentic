from statsmodels.tsa.arima.model import ARIMA

def forecast_rent(series):

    model = ARIMA(series, order=(1,1,1))

    model_fit = model.fit()

    forecast = model_fit.forecast(steps=12)

    return forecast
