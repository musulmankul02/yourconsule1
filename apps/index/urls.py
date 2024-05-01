from django.urls import path

    #My imports
from .views import index
urlpatterns = [
    path('', index, name="index"),
]