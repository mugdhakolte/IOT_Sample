from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from sample.viewsets import *


router = routers.DefaultRouter()
router.register(r'companies', CompanyViewset, basename='companies')
router.register(r'sensors', SensorViewset, basename='sensors')
router.register(r'measurements', MeasurementViewset, basename='measurements')

urlpatterns = [
    path('', include(router.urls)),
]
