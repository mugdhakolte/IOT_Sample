from django.db import models
from django.contrib.postgres.fields import ArrayField


class Company(models.Model):
    """
        Class representing a Company.
    """
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=30)

    class Meta:
        """Meta class for Company."""
        db_table = 'Company'

    def __str__(self):
        """
        Company and location.
        :return: name-location
        """
        return "{}-{}".format(self.name, self.location)


class Sensor(models.Model):
    """
        Class representing a Sensor.
    """
    sensor_id = models.CharField(primary_key=True, max_length=10)
    company = models.ForeignKey('Company',
                                related_name='sensors',
                                on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    labels = ArrayField(models.CharField(max_length=200))

    class Meta:
        """Meta class for Company."""
        db_table = 'Sensor'

    def __str__(self):
        """
        Sensor_id and Company Name.
        :return: Sensor_id-Company name
        """
        return "{}-{}".format(self.sensor_id, self.company.name)


class Measurement(models.Model):
    """
        Class representing a Measurement.
    """
    sensor = models.ForeignKey('Sensor',
                               related_name='measurements',
                               on_delete=models.CASCADE)
    date = models.DateTimeField()
    value = models.JSONField()

    class Meta:
        """Meta class for Measurement."""
        db_table = 'Measurement'
        ordering = ['id']

    def __str__(self):
        """
        Measurement ID and Sensor Name.
        :return: Measurement-Sensor name
        """
        return "{}-{}".format(self.id, self.sensor.sensor_id)
