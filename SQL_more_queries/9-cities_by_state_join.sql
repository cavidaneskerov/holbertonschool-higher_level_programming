--
SELECT id, name, (SELECT name FROM states WHERE states.id = cities.state_id) AS state_name FROM cities;
