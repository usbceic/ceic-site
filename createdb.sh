#!/bin/bash

sudo -u postgres dropdb ceic_site >> /dev/null
sudo -u postgres dropuser ceicsite >> /dev/null
sudo -u postgres createuser ceicsite
sudo -u postgres createdb ceic_site
sudo -u postgres psql << EOF
alter user ceicsite with encrypted password 'ceicsite';
alter role ceicsite set client_encoding to 'utf8';
alter role ceicsite set default_transaction_isolation to 'read committed';
alter role ceicsite set timezone to 'utc';
alter role ceicsite createdb;
grant all privileges on database ceic_site to ceicsite ;\q
EOF