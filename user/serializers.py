from rest_framework import  serializers
from django.contrib.auth.models import User
from .models import Profile

## Serializer to viewProfile
class ProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Profile
        fields = ('name' , 'gender' ,'dob' , 'about')

## Serializer to Register new User --
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    profile = ProfileSerializer(required= True)

    def create(self ,validated_data):
        user = User(email=validated_data['email'],
                username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        profile_data = validated_data.pop('profile')
        profile = Profile.objects.create(user = user, 
                    name= profile_data['name'], gender = profile_data['gender'],
                    dob = profile_data['dob'] , about=profile_data['about'] )
 
        return user
    class Meta:
        model = User
        fields = ('id', 'profile','username', 'email','password')
