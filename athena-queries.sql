SELECT airport, AVG(arr_del15 * 1.0) AS delay_rate
FROM flights
GROUP BY airport;

SELECT
  SUM(weather_delay) * 1.0 /
  (
    SUM(weather_delay)
  + SUM(carrier_delay)
  + SUM(nas_delay)
  + SUM(security_delay)
  + SUM(late_aircraft_delay)
  ) AS weather_share
FROM flights;

SELECT
  month,
  SUM(weather_delay) AS weather_delay,
  SUM(arr_delay) AS total_delay
FROM flights
GROUP BY month
ORDER BY month;