#!/bin/bash
#sudo docker run -it --name mongobdnr -v $PWD/flaskr/seeders:/seeders -p 27017:27017 --rm -e MONGO_INITDB_DATABASE=moviesbdnr mongo
docker-compose up
