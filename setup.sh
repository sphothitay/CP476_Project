#!/bin/bash

cd app

echo "Setting MySQL root user password"
service mysql start
echo "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '${MYSQL_PASSWORD}';" > reset_pass.sql
mysql -u root < reset_pass.sql
rm reset_pass.sql
service mysql restart

echo "Creating SQL tables"
mysql -u root --password="${MYSQL_PASSWORD}" < ./sql/build_database.sql

echo "Starting flask app"
export FLASK_APP=main.py
python3 -m flask run --host=0.0.0.0
