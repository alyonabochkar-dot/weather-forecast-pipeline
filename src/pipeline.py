from datetime import datetime, timezone

from extract import fetch_forecast
from load import load_dataframe

CITY = "Kryvyi Rih"
LATITUDE = 47.9056
LONGITUDE = 33.4191


def main():
    df = fetch_forecast(CITY, LATITUDE, LONGITUDE)
    df["loaded_at"] = datetime.now(timezone.utc)
    inserted = load_dataframe(df)
    print(f"Inserted {inserted} rows for {CITY}")


if __name__ == "__main__":
    main()