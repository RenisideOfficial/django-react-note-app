from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

#view for creating a note
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)
            
#view for deleting a note
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    serializer_class = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

# Create your views here.
class CreateUserView(generics.CreateAPIView):
    # look at all objects to be sure we aren't creating new user
    queryset = User.objects.all()
    serializer_class = UserSerializer  # what kind of data to be accepted i.e (username, password)
    permission_classes = [AllowAny]   # who can call this, by default allow anyone