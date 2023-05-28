from django.contrib import admin
from django.urls import path, include
from myApp import urls
from rest_framework import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApp.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
