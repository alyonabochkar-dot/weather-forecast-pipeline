# Weather Forecast Data Pipeline

A small end-to-end data engineering project: it collects hourly weather
forecasts from the Open-Meteo API for several Ukrainian cities, stores every
forecast version in PostgreSQL and exposes analytics through SQL views.

## Architecture

Open-Meteo API -> Python (requests, pandas) -> PostgreSQL (Docker) -> SQL views

The pipeline is run daily by Windows Task Scheduler.

## Tech stack

- Python 3.13 (requests, pandas, psycopg2, python-dotenv)
- PostgreSQL 16 in Docker (docker-compose)
- SQL (views, window functions)
- Git / GitHub

## Data

- Source: [Open-Meteo Forecast API](https://open-meteo.com/en/docs) (free, no key)
- Cities: Kryvyi Rih, Kyiv, Lviv
- Variables: temperature, apparent temperature, humidity, precipitation
  probability, wind speed, surface pressure, cloud cover
- Table `weather_data`: one row per city, forecast hour and load time.
  Primary key: `(city, forecast_time, loaded_at)`.

## Design decisions

- **Every forecast version is kept.** Each run adds new rows with its own
  `loaded_at`, so it is possible to compare how the forecast for the same
  hour changed over time.
- **Raw layer and analytics layer are separated.** `weather_data` stores raw
  data; `v_latest_forecast` returns the newest forecast for each hour and
  `v_daily_summary` aggregates it by day.
- **Secrets are kept out of the repository.** Credentials live in `.env`
  (see `.env.example`).

## How to run

1. Clone the repository and create a virtual environment:
   `python -m venv .venv`, activate it, then
   `python -m pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and fill in the values.
3. Start the database: `docker compose up -d`
4. Run the pipeline: `python src/pipeline.py`
5. Apply the analytics views:
   `Get-Content sql/02_analytics.sql | docker compose exec -T db sh -c 'psql -U "$POSTGRES_USER" -d "$POSTGRES_DB"'`

## Example queries

```sql
SELECT * FROM v_daily_summary ORDER BY city, day;
```

## Limitations and next steps

- The scheduled run needs the computer and Docker Desktop to be running.
- Planned: data quality checks, an orchestrator (Airflow), a dashboard.