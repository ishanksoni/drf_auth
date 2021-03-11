from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views

router1 = DefaultRouter()
router1.register('PageApi', views.PageModelViewSet, basename = 'Page')

urlpatterns = [
    path('',include(router1.urls)),
]