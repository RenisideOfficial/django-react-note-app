from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    """The model that we want to serialize as the user model
    The models are well build into django and it well represents
    the user""" 
    class Meta:
        model = User
        """fields to be serialized when accepting a new user 
        and when returning a new user"""
        fields = ["id", "username", "password"]
        # accept password during creation but don't give for security
        extra_kwargs = {"password": {"write_only": True}}
        
    """when all the fields are validated, we will pass in the field data
    then use the data to create a new user"""
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}
        
        