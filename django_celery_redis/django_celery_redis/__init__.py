from .celery import app as celery_app
# I have a connection problems even in settings.py connection info is correct (ports, etc)
# It can be as I need to import the Celery instance and have it available in all the
# application, it should be a tuple, don't forget the , at the end
# So everytime I start the project, it will initialize this Message Provider and 
# have access inside the project.
__all__ = ("celery_app",)