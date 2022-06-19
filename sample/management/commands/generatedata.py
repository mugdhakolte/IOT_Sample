import pytz
import random
import logging

from faker import Faker

from django.core.management.base import BaseCommand

from sample.models import *

logger = logging.getLogger('django')


class Command(BaseCommand):
    help = "Command to dump data in database."

    def get_count(self):
        """
            function to return count of Models.
        """
        company_count = Company.objects.all().count()
        sensor_count = Sensor.objects.all().count()
        measurement_count = Measurement.objects.all().count()
        return company_count, sensor_count, measurement_count

    def handle(self, *args, **options):
        fake = Faker()

        company_count, sensor_count, measurement_count = self.get_count()
        logger.info(
            "Before Inserting data in company {} ".format(company_count))
        logger.info("Before Inserting data in Sensor {} ".format(sensor_count))
        logger.info("Before Inserting data in Measurement {} ".format(
            measurement_count))

        print("Before Inserting data in company {} ".format(company_count))
        print("Before Inserting data in Sensor {} ".format(sensor_count))
        print("Before Inserting data in Measurement {} ".format(
            measurement_count))

        n = 100

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

        company_count_new, sensor_count_new, measurement_count_new = self.get_count(
        )

        logger.info(
            "Records Inserted in Company {} ".format(company_count_new))
        logger.info("Records Inserted in Sensor {} ".format(sensor_count_new))
        logger.info("Records Inserted in Measurement {} ".format(
            measurement_count_new))

        print("Records Inserted in Company {} ".format(company_count_new))
        print("Records Inserted in Sensor {} ".format(sensor_count_new))
        print("Records Inserted in Measurement {} ".format(
            measurement_count_new))
