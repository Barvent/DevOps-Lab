#!/bin/bash

set -e
docker build -t webapp0 webapp0
docker build -t webapp1 webapp1
docker build -t nginxweb nginxWeb

docker run --name webapp0 --rm -d -p 5000:5000 webapp0
docker run --name webapp01 --rm -d -p 5001:5000 webapp0
docker run --name webapp1 --rm -d -p 5002:5000 webapp1
docker run --name nginxweb --rm -d -p 80:80 nginxweb
