-- A script that displays the average temperature
-- by city

USE hbtn_0c_0;

SELECT city, AVG(value) AS avg_temp
	FROM temperatures
	WHERE month BETWEEN 7 AND 8
	GROUP BY city
	ORDER BY avg_temp DESC
	LIMIT 3;
