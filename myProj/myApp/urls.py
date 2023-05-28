from rest_framework.routers import DefaultRouter
from django.urls import path, include
from myApp import views

router = DefaultRouter()
router.register('essay', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls))
]
