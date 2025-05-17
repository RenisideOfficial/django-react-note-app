from django.urls import path
from . import views

#parsing the rest of the path, and if it matches anything here
#it will be handled and it will go to the views we have within this app
urlpatterns = [
    path("notes/", views.NoteListCreate.as_view(), name="note-list"),
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name="delete-note"),
]