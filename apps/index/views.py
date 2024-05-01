from django.shortcuts import render,redirect
from django.core.mail import send_mail

    #My imports
from apps.setting.models import About
from .models import Setting,Slide,Service,Review
# Create your views here.
def index(request):
    setting = Setting.objects.latest("id")
    about = About.objects.latest("id")
    slide = Slide.objects.all()
    service = Service.objects.all()
    review = Review.objects.all()
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Review.objects.create(name = name,email = email,message = message)
        send_mail(
            f'{message}',

            f'Здравствуйте {name},Спасибо за ваш отзыв, Мы скоро свами свяжемся.Ваш отзыв: {message} Ваша почта: {email}',
            "noreply@somehost.local",
            [email])
        
        return redirect('index')
    context = {
        "setting":setting,
        "about":about,
        "slide":slide,
        "service":service,
        "review":review,
    }
    return render(request, "setting/index-3.html", context)

