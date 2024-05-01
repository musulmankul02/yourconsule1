from django.shortcuts import render,redirect
from django.core.mail import send_mail

    #My imports
from .models import About,History,Number,Contact
from apps.index.models import Setting
# Create your views here.

def contact(request):
    setting = Setting.objects.latest("id")
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name = name,email = email,message = message)
        send_mail(
            f'{message}',

            f'Здравствуйте {name},Спасибо за обратную связь, Мы скоро свами свяжемся.Ваще сообщение: {message} Ваша почта: {email}',
            "noreply@somehost.local",
            [email])
        
        return redirect('index')
    context = {
        "setting":setting
    }
    return render(request, "setting/contact.html", context)

def about(request):
    setting = Setting.objects.latest("id")
    about = About.objects.latest("id")
    histor = History.objects.all()
    numbers = Number.objects.latest("id")
    context = {
        "setting":setting,
        "about":about,
        "histor":histor,
        "numbers":numbers,
    }
    return render(request, "setting/about.html", context)