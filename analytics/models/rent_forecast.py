import pandas as pd
from statsmodels.tsa.arima.model import ARIMA


def forecast_rent(df, city="Los Angeles, CA"):

    city_df = df[df["RegionName"] == city].copy()

    city_df["Date"] = pd.to_datetime(city_df["Date"])

    city_df = city_df.sort_values("Date")

    # Set Date as index
    city_df = city_df.set_index("Date")

    ts = city_df["Rent"]

    if len(ts) < 12:
        print("Not enough data for forecasting")
        return None

    model = ARIMA(ts, order=(1,1,1))
    model_fit = model.fit()

    forecast = model_fit.forecast(steps=6)

    print("\nRent Forecast for", city)
    print(forecast)

    return forecast