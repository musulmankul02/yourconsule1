from django.contrib import admin

    #My imports
from .models import About,History,Number,Contact

# Register your models here.
admin.site.register(About)
admin.site.register(History)
admin.site.register(Number)
admin.site.register(Contact)



