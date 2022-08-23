#Warning, it kills all the Dockers running in the system
docker ps -q | xargs docker kill
