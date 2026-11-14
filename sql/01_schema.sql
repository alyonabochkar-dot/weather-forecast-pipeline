CREATE TABLE IF NOT EXISTS weather_data (
    city VARCHAR(50) NOT NULL,
    forecast_time TIMESTAMP NOT NULL,
    temperature_2m FLOAT,
    apparent_temperature FLOAT,
    relative_humidity_2m  SMALLINT,
    precipitation_probability SMALLINT,
    wind_speed_10m FLOAT,
    surface_pressure FLOAT,
    cloud_cover SMALLINT,
    loaded_at TIMESTAMPTZ NOT NULL,
    PRIMARY KEY (city, forecast_time, loaded_at)
);