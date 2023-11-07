pip freeze > requirements.txt
chmod +x ./entrypoint.sh

###### As I mapped volumes, I can create an application with:
`docker exec -it django_celery_redis/bin/sh`
`./manage.py startapp newapp`

activate a shell inside an image
`./manage.py shell`
