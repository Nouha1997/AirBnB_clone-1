--script that prepares a MySQL server for AirBnB Console v2
--create database

CREATE DATABASE IF NOT EXISTShbnb_dev_db;

--create user if not exist
--user should be identified with passwordhbnb_dev_pwd
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost'IDENTIFIED BY 'hbnb_dev_pwd';

--grant hbnb_dev all privileges on hbnb_dev_db
FRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

-grant select privileges on perfermance_schema
GRANT SELECT ON perfermance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
