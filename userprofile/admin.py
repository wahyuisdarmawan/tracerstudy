from django.contrib import admin
from .models import Userprofile, Alumnibio
from django.contrib.auth.models import User

# Register your models here.
class ProfileUser(admin.ModelAdmin):
    list_display = ['user', 'role']

admin.site.register(Userprofile, ProfileUser)
admin.site.register(Alumnibio)