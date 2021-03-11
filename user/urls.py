from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

from . import views
urlpatterns = [
    path('register/', views.CreateUser.as_view(), name='account-create'),
    path('get/all/', views.ListUser.as_view(), name='user-list'),
    path('get/<int:pk>', views.DetailUser.as_view(), name='user-list'),
    path('login_token/' ,obtain_auth_token, name='api_token_auth' ),
]
