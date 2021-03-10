from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,ProfileSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Profile


class ListUser(GenericAPIView , ListModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def get(self , request ,*args , **kwargs):
        return self.list(request,*args, **kwargs)

class CreateUser(GenericAPIView , CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self , request ,*args , **kwargs):
        return self.create(request,*args, **kwargs)