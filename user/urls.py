from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
urlpatterns = [
    path('register/', views.CreateUser.as_view(), name='account-create'),
    path('get/', views.ListUser.as_view(), name='user-list'),
]
