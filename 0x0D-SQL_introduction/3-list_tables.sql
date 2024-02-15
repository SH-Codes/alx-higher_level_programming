-- List all tables from a database
-- in this example the name of the datebase is 'mysql'

SELECT table_name
FROM information_schema.tables
WHERE table_schema = 'mysql';
