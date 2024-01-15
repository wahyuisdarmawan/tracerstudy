from django.contrib import admin
from .models import Userprofile
from django.contrib.auth.models import User

# Register your models here.
class ProfileUser(admin.ModelAdmin):
    list_display = ['user', 'role']

admin.site.register(Userprofile, ProfileUser)