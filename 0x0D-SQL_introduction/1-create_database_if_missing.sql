-- Script to create the database hbtn_0c_0
-- If the database exists, it will not fail

-- Check if the database exists
SET @db_name = 'hbtn_0c_0';
SELECT COUNT(*) INTO @db_exists FROM information_schema.schemata WHERE schema_name = @db_name;

-- Create the database if it does not exist
IF @db_exists = 0 THEN
	CREATE DATABASE `hbtn_0c_0`;
	SELECT CONCAT('Database "', @db_name, '" has been created.') AS Message;
ELSE
	SELECT CONCAT('Database "', @db_name, '" already exists. No action taken.') AS Message;
END IF;

