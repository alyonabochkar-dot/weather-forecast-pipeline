import os

import psycopg2
from psycopg2.extras import execute_values
from dotenv import load_dotenv

load_dotenv(override=True)


def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )

COLUMNS = [
    "city",
    "forecast_time",
    "temperature_2m",
    "apparent_temperature",
    "relative_humidity_2m",
    "precipitation_probability",
    "wind_speed_10m",
    "surface_pressure",
    "cloud_cover",
    "loaded_at",
]


def load_dataframe(df):
    df = df[COLUMNS].astype(object).where(df[COLUMNS].notna(), None)
    rows = list(df.itertuples(index=False, name=None))

    query = f"INSERT INTO weather_data ({', '.join(COLUMNS)}) VALUES %s"

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            execute_values(cur, query, rows)
    return len(rows)

if __name__ == "__main__":
    print(
        "host:", repr(os.getenv("DB_HOST")),
        "port:", repr(os.getenv("DB_PORT")),
        "user:", repr(os.getenv("POSTGRES_USER")),
        "db:", repr(os.getenv("POSTGRES_DB")),
    )
    try:
        with get_db_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
                print(cur.fetchone())
    except UnicodeDecodeError as e:
        print("Server message:", e.object.decode("cp1251", errors="replace"))