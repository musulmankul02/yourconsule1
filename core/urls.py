from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("apps.setting.urls")),
    path('', include("apps.team.urls")),
    path('', include("apps.document.urls")),
    path('', include("apps.index.urls")),
    
    
]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)