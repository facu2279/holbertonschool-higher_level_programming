-- Create by Facundo Diaz to Holberton School 2021

SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id