# Django-and-Django-REST-Framework

## Setup
### Installing docker compose

1. Download the Docker compose package:
>  sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
2. Apply executable permissions to the binary:
> sudo chmod +x /usr/local/bin/docker-compose
3. Test the installation:
> docker-compose --version

## Buillding your Container
1. Building your new image using your Dockerfile:
> docker build -t my-django-image:your-image-tag .
2. Open your docker-compose.yml file and change the 'XX' to your corresponding port. Also change 'YOUR_USER' with your UNIX username:
```
version: '3'
services:
  web:
    build: .
    command: bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:80XX"
    container_name: "djangoXX"
    volumes:
      - "/home/YOUR_USER/django/library:/usr/src/django/library"
    ports:
      - "90XX:80XX"
``` 
2. Using docker-compose in order to deploy your container:
> docker-compose up

## Django development
4. Create a new virtual environment:
```
python -m venv django_env
```
2. Use this virtual env:
```
source ./django_env/bin/activate
```
3. Install dependencies:
```
pip install django
pip install django_rest_framework
```
4. Create a new project:
```
django-admin startproject library
```
5. Create a new application of the project:
```
django-admin startapp editorial
```
6. Run your migrations:
```
python manage.py migrate
```
7. Add your application to the INSTALLED_APPS section:

```
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
    'editorial'
]
```
8. Create the files serializers.py and urls.py inside library/editorial directory:

```
cd library/editorial
touch serializers.py urls.py
```

## Solving your issues
- Issue #1 Running docker-compose up shows "Database found: skipping initial configuration": Postgres images runs some configuration only the first time we build and run our container. In order for solving this issue we must stop our current container with CTRL C, then enter following commands:
```
docker-compose rm web
docker-compose rm postgres_db
docker-compose up --build
```

- Issue #2 Password authentication failed for your user and also Issue #3 Connection refused, Is the server running on that host and accepting TCP/IP connections: These errors occurs when we are trying to access to an unavailable instance of Postgres or if we tried to access Postgres in some IP server that doesn't have Postgres expose on any port, we must use the right IP for postgres. We need to obtain our IP address of our network containers, in order for that we need to write the following commands:

```
# First we need to obtain our container ID
docker ps | grep YOUR_PORT

# Once you grep some instance with your related port, copy the ID 
# and paste it on the next command
docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' YOUR_CONTAINER_ID
```
Then we need to use that IP address in our docker-compose.yml because it corresponds to the IP address of our Docker network.

## Assignment
1. Add between 2-4 models, obviously make their serializers, views and routers also; you can do it inside your book application (Our you can create another app inside our project with the command ```django-admin startapp your_app_name```).
2. Populate your book app and also your new models.
3. Try your application with Postman (Do every HTTP method of every Model in our project: GET, POST, PUT DELETE and PATCH).
- Tip: If you got some issues to send your Http Request you should check out the Django and Django REST Frameworkd documentation.

## References
- (DB normalization)[https://www.guru99.com/database-normalization.html]
- (Django documentation)[https://docs.djangoproject.com/en/4.0/]
- (Django REST Framework)[https://www.django-rest-framework.org/#example]
- (HTTP methods example)[https://www.bezkoder.com/django-rest-api/]
