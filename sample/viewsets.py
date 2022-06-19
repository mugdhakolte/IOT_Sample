from django.db.models import Q

from rest_framework import viewsets, mixins
from rest_framework.viewsets import ModelViewSet

from sample.models import *
from sample.filters import *
from sample.paginate import *
from sample.serializers import *


class CompanyViewset(ModelViewSet):
    """
        list:
            Lists Companies.

        create:
            Create new Company.

        retrieve:
            retrieves company by its ID.

        update:
            updates company by its ID.

        partial_update:
            updates company by its ID.

        destroy:
            deletes company by its ID.

    """
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class SensorViewset(ModelViewSet):
    """
        list:
            Lists Sensors.

        create:
            Create new Sensor.

        retrieve:
            retrieves Sensor by its ID.

        update:
            updates Sensor by its ID.

        partial_update:
            updates Sensor by its ID.

        destroy:
            deletes Sensor by its ID.

    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    filterset_class = SensorFilter


class MeasurementViewset(mixins.CreateModelMixin, mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    """
        list:
            Lists Measurements.

        create:
            Creates new Measurement.
    """

    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        paginator = self.pagination_class()

        sensor = self.request.query_params.get('sensor')
        company = self.request.query_params.get('company')
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        if sensor:
            queryset = queryset.filter(sensor=sensor)
        if company:
            queryset = queryset.filter(sensor__company=company)
        if start and end:
            queryset = queryset.filter(date__range=(start, end))

        objects = paginator.paginate_queryset(queryset, request)
        serializer = self.get_serializer(objects, many=True)
        return paginator.get_paginated_response(serializer.data)
