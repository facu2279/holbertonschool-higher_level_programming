-- Create by Facundo Diaz to Holberton School 2021
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC