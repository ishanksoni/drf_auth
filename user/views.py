from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer,ProfileSerializer
from rest_framework.mixins import ListModelMixin, CreateModelMixin , RetrieveModelMixin
from .models import Profile
from rest_framework.permissions import AllowAny

class ListUser(GenericAPIView , ListModelMixin , RetrieveModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    def get(self , request ,*args , **kwargs):
        return self.list(request,*args, **kwargs)

class DetailUser(GenericAPIView, RetrieveModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    
    def get(self , request ,*args , **kwargs):
        return self.retrieve(request,*args, **kwargs)
        
class CreateUser(GenericAPIView , CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    def post(self , request ,*args , **kwargs):
        return self.create(request,*args, **kwargs)