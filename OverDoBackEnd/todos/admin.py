from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Todos

# Register your models here.

admin.site.register(Todos)
