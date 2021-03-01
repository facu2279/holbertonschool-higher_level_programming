-- Create by Facundo Diaz to Holberton School 2021
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY AVG(value) DESC