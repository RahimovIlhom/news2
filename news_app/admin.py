from django.contrib import admin
from .models import Category, New, ContactMessage

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'category', 'publish_time', 'status']
    list_filter = ['category', 'status', 'publish_time']
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ['title', 'body']
    date_hierarchy = 'publish_time'


admin.site.register(Category)
admin.site.register(New, NewsAdmin)
admin.site.register(ContactMessage)
