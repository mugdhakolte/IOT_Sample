import pytz
import random

from django.core.management.base import BaseCommand

import faker.providers
from faker import Faker

from sample.models import *

fake = Faker()
sensor_ids = set([fake.bothify(text='????-#####') for _ in range(50)])


class Provider(faker.providers.BaseProvider):

    def get_sensor_id(self):
        return self.random_element(sensor_ids)


class Command(BaseCommand):
    help = "Command to dump data in database."

    def handle(self, *args, **options):
        fake.add_provider(Provider)

        for _ in range(50):
            name = fake.company()
            location = fake.city()
            Company.objects.create(name=name, location=location)

        for _ in range(50):
            sensor_id = fake.unique.get_sensor_id()
            active = fake.pybool()
            labels = fake.pylist(nb_elements=6, value_types='str')
            companies = list(Company.objects.values_list('id', flat=True))

            for company in companies:
                try:
                    company = Company.object.get(id=company)
                    Sensor.objects.create(sensor_id=sensor_id, company_id=company, is_active=active, labels=labels)
                except ModuleNotFoundError:
                    print("This company with {} id is not present in DB".format(company))

        for _ in range(50):
            date = fake.date_time(tzinfo=pytz.UTC)
            value = {
                'temperature': round(random.uniform(20, 38), 2),
                'rssi': random.randint(0, 46),
                'humidity': round(random.uniform(0, 101), 2)
            }
            sensors = list(Sensor.objects.values_list('sensor_id', flat=True))

            for sensor in sensors:
                try:
                    sensor = Sensor.objects.get(sensor_id=sensor)
                    Measurement.objects.create(sensor=sensor, date=date, value=value)
                except ModuleNotFoundError:
                    print("This Sensor with {} id is not present in DB".format(sensor))



