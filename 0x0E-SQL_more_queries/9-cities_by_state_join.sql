-- Script that list all cities in a database

SELECT cities.id AS id,
		cities.name AS name,
		states.name AS name
	FROM cities JOIN states
		ON states.id = cities.states_id
	ORDER BY cities.id ASC;
