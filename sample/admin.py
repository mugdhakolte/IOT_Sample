from django.contrib import admin

from sample.models import *

admin.site.register(Company)
admin.site.register(Sensor)
admin.site.register(Measurement)
