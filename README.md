# Dockerized Django-postgres Celery and Redis setup
This repo contains a simple django and postgres DB setup configured with celery workers, celery flower and celery beat with redis as broker.

#### Run this project with 
```
docker-compose build
docker-compose up -d
```
#### To check logs
```
docker-compose logs -f
```

tasks configured for every minute with celery-beat.


#### To check django project

Open http://127.0.0.1:8000/ in Browser to check if setup is working.

#### to monitor celery workers

http://127.0.0.1:13001


<B> To connect with postgres db </B> : ```docker exec -it postgres psql -U postgres```
