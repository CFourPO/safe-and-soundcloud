from django.contrib import admin
from djongo.admin import ModelAdmin

from .models import User

# Register your models here.
class CustomUserAdmin(ModelAdmin):
    def get_by_natural_key(username):
        return User.objects.get(username=username)

admin.site.register(User, CustomUserAdmin)