import pytz
import json
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

        self.company_payload = {
            'name': "test",
            'location': "test"
        }

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

    def test_create_company(self):
        url = reverse("companies-list")
        response = self.client.post(url, data=self.company_payload)
        self.assertEqual(Company.objects.get(name='test').name, 'test')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_sensor(self):
        url = reverse("sensors-list")
        company = Company.objects.create(name='test_company', location='test_location')
        sensor_payload = {
            'sensor_id': "testsensor",
            'company': company.id,
            'is_active': True,
            'labels': ['test_label1', 'test_label2', 'test_label3']
        }

        response = self.client.post(url, data=sensor_payload)
        self.assertEqual(Sensor.objects.get(sensor_id='testsensor').sensor_id, 'testsensor')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_measurement(self):
        url = reverse("measurements-list")
        company = Company.objects.create(name='test_company', location='test_location')
        sensor = Sensor.objects.create(sensor_id="testsensor", company=company,
                                       is_active=True, labels=['test_label1', 'test_label2', 'test_label3'])

        measurement_payload = {
            'sensor': sensor.sensor_id,
            'date': "2022-06-21T22:23:30.756Z",
            'value':
                {
                    'temperature': 21.1,
                    'rssi': 3,
                    'humidity': 4.5
                }
        }
        response = self.client.post(url, data=measurement_payload)
        self.assertEqual(Measurement.objects.get(sensor=sensor).sensor.sensor_id, 'testsensor')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_company(self):
        url = reverse("companies-detail", kwargs={"pk": self.company.pk})
        data = {"name": "test_name", "location": "test_location"}
        response = self.client.put(url, data=data)
        response_data = json.loads(response.content)
        company = Company.objects.get(id=self.company.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.get("name"), company.name)

    def test_update_sensor(self):
        url = reverse("sensors-detail", kwargs={"pk": self.sensor_1.sensor_id})
        data = {
            'sensor_id': self.sensor_1.sensor_id,
            'company': self.company.id,
            'is_active': True,
            'labels': ['test_label4', 'test_label5', 'test_label5']
        }
        response = self.client.put(url, data=data)
        response_data = json.loads(response.content)
        sensor = Sensor.objects.get(sensor_id=self.sensor_1.sensor_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.get("labels"), sensor.labels)

    def test_partial_update_company(self):
        url = reverse("companies-detail", kwargs={"pk": self.company.pk})
        data = {"location": "test_location"}
        response = self.client.patch(url, data=data)
        response_data = json.loads(response.content)
        company = Company.objects.get(id=self.company.id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.get("name"), company.name)

    def test_partial_update_sensor(self):
        url = reverse("sensors-detail", kwargs={"pk": self.sensor_1.sensor_id})
        data = {
            'is_active': False,
            'labels': ['test_label4', 'test_label5', 'test_label5']
        }
        response = self.client.patch(url, data=data)
        response_data = json.loads(response.content)
        sensor = Sensor.objects.get(sensor_id=self.sensor_1.sensor_id)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data.get("labels"), sensor.labels)

    def test_delete_company(self):
        url = reverse("companies-detail", kwargs={"pk": self.company.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_sensor(self):
        url = reverse("sensors-detail", kwargs={"pk": self.sensor_1.sensor_id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

