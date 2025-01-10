#!/bin/bash
# Run using docker-compose
BIN='sudo docker-compose exec mongo mongoimport'
# Uncomment to run on docker 
#BIN='sudo docker exec mongobdnr mongoimport'
# Uncomment to run locally
#BIN=mongoimport
$BIN --db moviesbdnr -c user --file seeders/user.json --jsonArray
$BIN --db moviesbdnr -c movie --file seeders/movie.json --jsonArray
$BIN --db moviesbdnr -c production --file seeders/production.json --jsonArray
