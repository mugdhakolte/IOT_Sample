import django_filters

from sample.models import *


class SensorFilter(django_filters.FilterSet):
    labels = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Sensor
        fields = ['company', 'labels']
