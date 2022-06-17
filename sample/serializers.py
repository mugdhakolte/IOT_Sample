from rest_framework import serializers

from sample.models import *


class CompanySerializer(serializers.ModelSerializer):
    """Company model serializer class for Company."""

    class Meta:
        """Meta class for Company model serializer."""
        model = Company
        fields = '__all__'


class SensorSerializer(serializers.ModelSerializer):
    """Sensor model serializer class for Sensor."""

    labels = serializers.ListField(child=serializers.CharField(max_length=255))

    class Meta:
        """Meta class for Sensor model serializer."""
        model = Sensor
        fields = '__all__'


class ValueSerializer(serializers.Serializer):
    """Value JSONField serializer class for Measurement."""

    temperature = serializers.FloatField(required=True, min_value=20, max_value=38)
    rssi = serializers.IntegerField(required=True, min_value=0, max_value=46)
    humidity = serializers.FloatField(required=True, min_value=0, max_value=100)


class MeasurementSerializer(serializers.ModelSerializer):
    """Measurement model serializer class for Measurement."""
    value = serializers.JSONField()

    class Meta:
        """Meta class for Measurement model serializer."""
        model = Measurement
        fields = '__all__'

    def validate_value(self, value):
        serializer = ValueSerializer(data=value)
        serializer.is_valid(raise_exception=True)
        return value
