import pytz
import random

from faker import Faker

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from sample.models import *
from sample.viewsets import *
from sample.serializers import *


class CompanyTestcase(APITestCase):
    def setUp(self):
        self.fake = Faker()
        self.company = Company.objects.create(name=self.fake.company(),
                                              location=self.fake.city())

        self.sensor_1 = Sensor.objects.create(sensor_id=self.fake.unique.bothify(text='????-#####'),
                                              company=self.company,
                                              is_active=self.fake.pybool(),
                                              labels=self.fake.pylist(nb_elements=6, value_types='str'))

        self.measurement_1 = Measurement.objects.create(sensor=self.sensor_1,
                                                        date=self.fake.date_time(tzinfo=pytz.UTC),
                                                        value={
                                                            'temperature': round(random.uniform(20, 38), 2),
                                                            'rssi': random.randint(0, 46),
                                                            'humidity': round(random.uniform(0, 101), 2)
                                                        })

        self.sensor_2 = Sensor.objects.create(sensor_id=self.fake.unique.bothify(text='????-#####'),
                                              company=self.company,
                                              is_active=self.fake.pybool(),
                                              labels=self.fake.pylist(nb_elements=6, value_types='str'))

        self.measurement_2 = Measurement.objects.create(sensor=self.sensor_2,
                                                        date=self.fake.date_time(tzinfo=pytz.UTC),
                                                        value={
                                                            'temperature': round(random.uniform(20, 38), 2),
                                                            'rssi': random.randint(0, 46),
                                                            'humidity': round(random.uniform(0, 101), 2)
                                                        })

    def test_companies(self):
        url = reverse("companies-list")
        response = self.client.get(url)
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_company(self):
        url = reverse("companies-detail", kwargs={'pk': self.company.pk})
        response = self.client.get(url)
        company = Company.objects.get(pk=self.company.pk)
        serializer = CompanySerializer(company)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_company(self):
        url = reverse("companies-detail", kwargs={'pk': 10})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_sensors(self):
        url = reverse("sensors-list")
        response = self.client.get(url)
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_sensor(self):
        url = reverse("sensors-detail", kwargs={'pk': self.sensor_1.sensor_id})
        response = self.client.get(url)
        sensor = Sensor.objects.get(pk=self.sensor_1.sensor_id)
        serializer = SensorSerializer(sensor)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_sensor(self):
        url = reverse("sensors-detail", kwargs={'pk': 'lejkljkl'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_measurements(self):
        url = reverse("measurements-list")
        response = self.client.get(url)
        measurements = Measurement.objects.all()
        serializer = MeasurementSerializer(measurements, many=True)
        self.assertEqual(response.data['results'], serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

