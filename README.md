# Django-celery-boilerplate
This repo contains a simple django and celery setup with celery beat and celery flower configured.


## Steps to start this project: 

1. Create virtual environment
```
virtualenv -p python3.7 venv
```
2. Activate Virtual environment
```
source venv/bin/activate
```
3. Install all the dependencies
```
pip install -r requirements.txt
```

### Setup Redis 


<B> run a docker container </B>
```
1. docker run -d -p 6379:6379 redis

2. redis-cli ping  # return PONG if working
```
<B> Install redis on local </B>

```
1. brew install redis

2. brew services start redis

3. redis-cli ping
```

<B>Start Celery  Worker </B>
```
 celery -A djangoproject  worker -l info
```


<B> Start Celery flower </B>
```
 celery flower -A djangoproject --address=127.0.0.1 --port=5555
```

Open http://127.0.0.1:5555/ in browser to monitor your task and their status.




<B> Start Celery Beat </B>
```
 celery -A djangoproject beat -l info
```
<B> Run the Django server </B>
```
python manage.py runserver
```


