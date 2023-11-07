# `import os` helps me to define, get environmental variables and set some more configurations
import os
from celery import Celery

# First I import my django settings in celery file
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_redis.settings')
# I instantiate a Celery with a string parameter of the name of my project
# We utilize that to send the tasks to the message broker (Django)
app = Celery("django_celery_redis")

# Here I make celery app to look into configuration from settings.py 
# starting with a namespace (without _ sign)=CELERY
app.config_from_object("django.conf:settings", namespace="CELERY")

# By using app.task I am registering a task, so I can execute this task whenever
# it is requested
@app.task
def add_numers():
    return

# I am informing Celery to look into all the installed apps and look for a file
# tasks.py
app.autodiscover_tasks()