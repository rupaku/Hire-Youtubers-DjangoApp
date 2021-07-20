### Hire-Youtubers-DjangoApp

#### pip install pipenv

### activate pip file

#### pipenv shell

#### pipenv install pillow

#### Document :https://docs.djangoproject.com/

#### pipenv install Django

### Create Django Project

#### django-admin startproject tubers

### Run server

#### python manage.py runserver

### Install Postgres and pg-admin from https://www.postgresql.org/ and https://www.pgadmin.org/download/

#### DB password dbname:postgres username:postgres password:admin

### Install psycopg2 as DB adapter for postgresql for python

#### pipenv install psycopg2

#### to use postgresql -> postgresql, pg-admin and psycopg2 needed

### Migration

#### python manage.py makemigrations

#### python manage.py migrate

### create admin user in gitbash and virtual env

#### winpty python manage.py createsuperuser

#### lco password:lco

### Django package url

### https://djangopackages.org/

### install djangocms-admin-style for admin css styling

#### pipenv install djangocms-admin-style

#### add in settings.py installed apps, 1st line djangocms_admin_style

#### run command

#### python manage.py migrate

#### python manage.py migrate djangocms_admin_style

### Github repo for django admin styling

#### https://github.com/django-cms/djangocms-admin-style

### settings.py file change for static files

### create folder under tubers and then run command

#### python manage.py collectstatic

<!-- STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR,'tubers/static')] -->

### create app

#### python manage.py startapp webpages

#### {% load static %}

#### <link rel="stylesheet" href="{% static './css/base.css' %}" />

#### {% include 'includes/footer.html' %}

#### pipenv install django-ckeditor // description with detailed edit

#### add ckeditor to settings.py file under installed apps

#### python manage.py startapp accounts

#### pipenv install django-allauth

#### https://django-allauth.readthedocs.io/en/latest/installation.html

#### settings.py -> apps -> django.contrib.sites

'allauth',
'allauth.account',
'allauth.socialaccount',
'allauth.socialaccount.providers.google',
'allauth.socialaccount.providers.facebook',

SITE_ID=1

#### makemigrations and migrate

### Configure facebook

#### developer.facebook.com

#### create app -> consumer ->app connected -> name -> add product as facebook -> web -> site url localhost:8000 ->save ->

dashboard->settings->basic-> app id

#### Go to admin ->Add social applications-> facebook client id -> example.com to right->add site as localhost:8000

#### https://django-allauth.readthedocs.io/en/latest/providers.html#facebook

#### {% load socialaccount %} {% providers_media_js %}

#### settings.py -> LOGIN_REDIRECT_URL ='dashboard'

#### Google -> https://django-allauth.readthedocs.io/en/latest/providers.html#google

#### python manage.py startapp hiretubers
