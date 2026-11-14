import pandas as pd
import requests

API_URL = "https://api.open-meteo.com/v1/forecast"

HOURLY_VARIABLES = [
    "temperature_2m",
    "apparent_temperature",
    "relative_humidity_2m",
    "precipitation_probability",
    "wind_speed_10m",
    "surface_pressure",
    "cloud_cover",
]


def fetch_forecast(city, latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ",".join(HOURLY_VARIABLES),
        "timezone": "auto",
    }
    response = requests.get(API_URL, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data["hourly"])
    df["time"] = pd.to_datetime(df["time"])
    df = df.rename(columns={"time": "forecast_time"})
    df["city"] = city
    return df

