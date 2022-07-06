-- displays the average temperature (Fahrenheit) by city ordered by temperature
SELECT city, AVG(value) as avg_temp from hbtn_0c_0.temperatures GROUP BY city ORDER BY avg_temp DESC;
