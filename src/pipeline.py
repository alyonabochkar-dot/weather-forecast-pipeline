from datetime import datetime, timezone

from extract import fetch_forecast
from load import load_dataframe

CITIES = [
    ("Kryvyi Rih", 47.9056, 33.4191),
    ("Kyiv", 50.4501, 30.5234),
    ("Lviv", 49.8397, 24.0297),
]


def main():
    loaded_at = datetime.now(timezone.utc)
    for city, latitude, longitude in CITIES:
        df = fetch_forecast(city, latitude, longitude)
        df["loaded_at"] = loaded_at
        inserted = load_dataframe(df)
        print(f"Inserted {inserted} rows for {city}")


if __name__ == "__main__":
    main()