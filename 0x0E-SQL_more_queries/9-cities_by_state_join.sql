-- Script that lists all cities contained in a database

SELECT cities.id, cities.name AS name, states.name AS name
FROM cities
INNER JOIN states ON cities.state_id=states.id;
