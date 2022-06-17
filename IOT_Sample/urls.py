"""IOT_Sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
from django.conf.urls import include

from rest_framework import permissions, routers

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


router = routers.DefaultRouter()

schema_view = get_schema_view(
   openapi.Info(
      title="Sample API",
      default_version='v1',
      description="The sample application consists of three models-the Company, "
                  "Sensor, and Measurements using DRF and Postgresql.",
   ),
   public=True,
   permission_classes=(permissions.AllowAny, )
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include('sample.urls')),

    re_path(r'api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
