from celery import shared_task


@shared_task
# @app.task I can also do it this way, but it is much better to use @shared_task
# so I can work easier with work or create tasks, this way I don't need to import
# a function from a main app django_celery_redis

# to add this function to the task queue, I should call this function in a shell
# or anywhere in the project with utilizing 'delay'
# Applyasync is to apply more options and control more over the task 
# for example: ./manage.py shell -> sharedtask.delay()
def sharedtask():
    return