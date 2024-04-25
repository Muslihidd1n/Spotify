from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter



from music.views import *


router = DefaultRouter()
router.register("albomlar", AlbomModelViewSet)
router.register("singer", QoshiqchiModelViewSet)
router.register("music", QoshiqModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('qoshiqchilar/',QoshiqchilarAPI.as_view()),
    path('qoshiqlar/',QoshiqlarAPI.as_view()),
    path('albomlar/',AlbomlarAPI.as_view()),



    path('qoshiqchi/<int:pk>/',QoshiqchiAPI.as_view()),
]
