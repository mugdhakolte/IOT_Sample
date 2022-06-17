# IOT_Sample
The sample application consists of three models-the Company, Sensor, and Measurements using DRF and Postgresql.

# Requirements

1) Python 3
2) Django 4
3) Postgresql 14

# Steps to configure Project

1) Create Virtualenv as follows:
    > virtualenv venv

    > source venv/bin/activate

2) install requirements.txt in virtualenv
    > pip install -r docs/requirements.txt

3) Migrations to database
    > python manage.py makemigrations sample

    > python manage.py migrate

4) Run the Project
    > python manage.py runserver


# API Documentation

    http://127.0.0.1:8000/api-docs/

# Admin Interface

    > python manage.py createsuperuser

    http://127.0.0.1:8000/admin/
    