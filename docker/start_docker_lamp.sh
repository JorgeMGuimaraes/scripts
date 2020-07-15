#!/usr/bin/env bash

server_path=""

if [ $# = 0 ]; then
    #echo "Starting script in local folder"
    server_path="$(pwd)"
else
	server_path=$1
fi

code "${server_path}/app"

docker run -i -t \
-p "80:80" -v ${server_path}/app:/app \
-v ${server_path}/mysql:/var/lib/mysql \
-v ${server_path}/logs:/var/log/apache2 \
mattrayner/lamp

