import pytz
import random

from faker import Faker

from django.core.management.base import BaseCommand

from sample.models import *


class Command(BaseCommand):
    help = "Command to dump data in database."

    def handle(self, *args, **options):
        fake = Faker()
        print("Before Inserting data in company {} ".format(Company.objects.all().count()))
        print("Before Inserting data in Sensor {} ".format(Sensor.objects.all().count()))
        print("Before Inserting data in Measurement {} ".format(Measurement.objects.all().count()))

        n = 10

        for _ in range(n):
            name = fake.company()
            location = fake.city()
            company = Company.objects.get_or_create(name=name,
                                                    location=location)[0]

            sensor_id = fake.unique.bothify(text='????-#####')
            active = fake.pybool()
            labels = fake.pylist(nb_elements=6, value_types='str')

            sensor = Sensor.objects.get_or_create(sensor_id=sensor_id,
                                                  company=company,
                                                  is_active=active,
                                                  labels=labels)[0]

            date = fake.date_time(tzinfo=pytz.UTC)
            value = {
                'temperature': round(random.uniform(20, 38), 2),
                'rssi': random.randint(0, 46),
                'humidity': round(random.uniform(0, 101), 2)
            }

            measurement = Measurement.objects.get_or_create(sensor=sensor,
                                                            date=date,
                                                            value=value)[0]

        print("Records Inserted in company {} ".format(Company.objects.all().count()))
        print("Records Inserted in Sensor {} ".format(Sensor.objects.all().count()))
        print("Records Inserted in Measurement {} ".format(Measurement.objects.all().count()))


