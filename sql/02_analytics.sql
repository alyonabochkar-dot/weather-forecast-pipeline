
CREATE OR REPLACE VIEW v_latest_forecast AS
SELECT DISTINCT ON (city, forecast_time) *
FROM weather_data
ORDER BY city, forecast_time, loaded_at DESC;


CREATE OR REPLACE VIEW v_daily_summary AS
SELECT
    city,
    forecast_time::date AS day,
    ROUND(MIN(temperature_2m)::numeric, 1) AS min_temp,
    ROUND(MAX(temperature_2m)::numeric, 1) AS max_temp,
    ROUND(AVG(temperature_2m)::numeric, 1) AS avg_temp,
    MAX(precipitation_probability) AS max_precip_prob
FROM v_latest_forecast
GROUP BY city, forecast_time::date;