from django.urls import path

    #My imports
from .views import contact,about
urlpatterns = [
    path("about", about, name="about"),
    path("contact", contact, name="contact"),
]