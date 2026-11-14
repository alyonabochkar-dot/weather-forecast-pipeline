import os

import psycopg2
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