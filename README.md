# IOT_Sample
The sample application consists of three models-the Company, Sensor, and Measurements using DRF and Postgresql.

Following is the API list which sample application provides:
- CRUD Company.
- CRUD Sensor for a Company.
- Create a Measurement for a Sensor.
- List Sensors with the filter Company and labels[] (Multi labels possible).
- List measurements and filter with Sensor, Company, and Datetime range, paging 50 items per page.


## Requirements

1) Python 3
2) Django 4
3) Postgresql 14 
4) Ubuntu 20.04

### Steps to configure Project

1) Create Virtualenv as follows:
    > virtualenv venv

    > source venv/bin/activate

2) Install requirements.txt in virtualenv
    > pip install -r docs/requirements.txt

3) create .env file in Project same as .env.develop format and replace Database credentials in it.


4) Migrations to database
    > python manage.py makemigrations sample

    > python manage.py migrate

5) To Populate sample data in Database (Run Custom Management Command)

   > python manage.py generatedata

6) Run the Project
    > python manage.py runserver


## API Documentation

    http://127.0.0.1:8000/api-docs/

### Admin Interface

   > python manage.py createsuperuser
 
    http://127.0.0.1:8000/admin/

## To Configure Project Using Docker

   Take a look into setting.py file to change database configuration for docker.

   > sudo docker-compose up --build

   > sudo docker-compose exec web_rest python manage.py migrate

   > sudo docker-compose exec web_rest python manage.py generatedata 


# Example API List

1) [CRUD Company](http://127.0.0.1:8000/api/companies/)
2) [CRUD Sensor for a Company](http://127.0.0.1:8000/api/sensors/)
3) [Create a Measurement for a Sensor](http://127.0.0.1:8000/api/measurements/)
4) [List Sensors with the filter Company and labels[]](http://127.0.0.1:8000/api/sensors/?company=1&labels=YFsmKSGcfqXTAgOloAFB,snCMdbcBdOanNcTaGAgT)
5) [List measurements and filter with Sensor, Company, and Datetime range, paging 50 items per page](http://127.0.0.1:8000/api/measurements/?company=1&sensor=VpnL-00959&start=1999-05-01&end=2000-05-01)
   