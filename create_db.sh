#!/usr/bin/env bash

sudo -u postgres psql -c "CREATE USER firesquad WITH PASSWORD 'firesquad';"
sudo -u postgres createdb firesquad
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE firesquad to firesquad;"
sudo -u postgres psql -c "ALTER USER firesquad CREATEDB;"
sudo apt-get install postgresql-10-postgis-2.4
sudo -u postgres psql firesquad -c "CREATE EXTENSION postgis;"
