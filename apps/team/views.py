from django.shortcuts import render

    #My imports
from apps.index.models import Setting
from .models import AboutTeam,Team
# Create your views here.

def team(request):
    setting = Setting.objects.latest("id")
    about = AboutTeam.objects.latest("id")
    team = Team.objects.all()
    context = {
        "setting":setting,
        "about":about,
        "team":team,
    }
    return render(request,"team/team.html", context)