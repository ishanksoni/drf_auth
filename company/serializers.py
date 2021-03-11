from rest_framework import serializers
from .models  import Page

class PageSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
    read_only=True, 
    default=serializers.CurrentUserDefault())

    class Meta:
        model = Page
        fields = ('id','user','name' ,'city','about')

