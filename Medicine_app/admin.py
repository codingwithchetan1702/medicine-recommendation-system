from django.contrib import admin

# Register your models here.
from .models import Signup,Contact

admin.site.register(Signup)
admin.site.register(Contact)