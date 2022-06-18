# IOT_Sample
The sample application consists of three models-the Company, Sensor, and Measurements using DRF and Postgresql.

# Requirements

1) Python 3
2) Django 4
3) Postgresql 14
4) Ubuntu 20.04

# Steps to configure Project

1) Create Virtualenv as follows:
    > virtualenv venv

    > source venv/bin/activate

2) Install requirements.txt in virtualenv
    > pip install -r docs/requirements.txt

4) Migrations to database
    > python manage.py makemigrations sample

    > python manage.py migrate

5) To Populate sample data in Database (Run Custom Management Command)

   > python manage.py generatedata

6) Run the Project
    > python manage.py runserver


# API Documentation

    http://127.0.0.1:8000/api-docs/

# Admin Interface

   > python manage.py createsuperuser
 
    http://127.0.0.1:8000/admin/

# To Configure Project Using Docker

   > sudo docker-compose up --build

   > sudo docker-compose exec web_rest python manage.py migrate

   > sudo docker-compose exec web_rest python manage.py generatedata 