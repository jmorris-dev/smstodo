from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserText

# Register your models here.

admin.site.register(UserText)
