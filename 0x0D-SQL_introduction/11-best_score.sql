-- This script lists all records with score >= 10 in a table of a database in your MySQL server.
SELECT score, name FROM second_table
WHERE score >= 10 ORDER BY score DESC
