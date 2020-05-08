from celery import shared_task
from djangoproject.celery import app
from celery.task import periodic_task
from celery.schedules import crontab


# @shared_task
@periodic_task(run_every=crontab(hour="*", minute="*", day_of_week="*"), name="hello there", ignore_result=True)
def hello():
    print("Hello there!")


@periodic_task(run_every=crontab(minute="*"), name="hello world", ignore_result=True)
def hello_world():
    print("Hello World!! ")


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y
