from django.shortcuts import render

    #My imports
from apps.index.models import Setting
from .models import Document

# Create your views here.

def document(request):
    setting = Setting.objects.latest("id")
    document = Document.objects.all()
    context = {
        "setting":setting,
        "document":document
    }
    return render(request, "document/document.html", context)