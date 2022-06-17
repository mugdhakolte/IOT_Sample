from rest_framework.viewsets import ModelViewSet

from sample.models import *
from sample.filters import *
from sample.paginate import *
from sample.serializers import *


class CompanyViewset(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class SensorViewset(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filterset_class = SensorFilter


class MeasurementViewset(ModelViewSet):
    serializer_class = MeasurementSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Measurement.objects.all()
        sensor = self.request.query_params.get('sensor')
        company = self.request.query_params.get('company')
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        if sensor:
            queryset = queryset.filter(sensor=sensor)
        elif company:
            queryset = queryset.filter(sensor__company=company)
        elif start and end:
            queryset = queryset.filter(date__range=(start, end))

        return queryset
