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
    command: bash -c "python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
    container_name: "djangoXX"
    volumes:
      - "/home/YOUR_USER/django/library:/usr/src/django/library"
    ports:
      - "90XX:8000"
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

## References
(DB normalization)[https://www.guru99.com/database-normalization.html]
