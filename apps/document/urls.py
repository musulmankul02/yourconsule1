from django.urls import path

    #My imports
from .views import document
urlpatterns = [
    path("document/", document, name="document")
]