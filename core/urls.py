from django.contrib import admin
from django.urls import path
from music.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qoshiqchilar/',QoshiqchilarAPI.as_view()),
    path('qoshiqlar/',QoshiqlarAPI.as_view()),
    path('albomlar/',AlbomlarAPI.as_view()),



    path('qoshiqchi/<int:pk>/',QoshiqchiAPI.as_view()),
]
