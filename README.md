# Django-celery-boilerplate
This repo contains a simple django and celery setup with celery beat and celery flower configured.


Steps to start this project:

1. virtualenv -p python3.7 venv

2. source venv/bin/activate

3. pip install -r requirements.txt


<B>Setup Redis </B>

1. docker run -d -p 6379:6379 redis

2. redis-cli ping  # return PONG if working


<B> Start Celery flower </B>

Command: celery flower -A djangoproject --address=127.0.0.1 --port=5555

Open http://127.0.0.1:5555/ in browser to monitor your task and their status.




<B>Start Celery  Worker </B>

Command: celery -A djangoproject  worker -l info

<B> Start Celery Beat </B>

Command: celery -A djangoproject beat -l info

<B> Run the Django server </B>

python manage.py runserver



