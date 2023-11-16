from django.contrib import admin
from .models import Profile

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth_of_day']
    list_filter = ['user', 'birth_of_day']


admin.site.register(Profile, ProfileAdmin)
