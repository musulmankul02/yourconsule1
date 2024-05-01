from django.urls import path

    #My imports
from .views import team
urlpatterns = [
    path("team/", team, name="team")
]