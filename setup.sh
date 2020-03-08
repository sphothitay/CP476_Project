#!/bin/bash

cd app

echo "Setting up mysql service"
export MYSQL_PASSWORD=$(cat /dev/urandom | tr -cd a-zA-Z0-9 | head -c 32)

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
