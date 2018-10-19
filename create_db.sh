#!/usr/bin/env bash

sudo -u postgres psql -c "CREATE USER firesquad WITH PASSWORD 'firesquad';"
sudo -u postgres createdb firesquad
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE firesquad to firesquad;"
sudo -u postgres psql -c "ALTER USER firesquad CREATEDB;"