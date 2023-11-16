from django.contrib import admin
from .models import Category, New, ContactMessage, Comment, ReplyComment


# Register your models here.

class CommentTabular(admin.TabularInline):
    model = Comment
    extra = 0


class ReplyCommentTabular(admin.TabularInline):
    model = ReplyComment
    extra = 0


class ReplyCommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'user', 'create_time']
    list_filter = ['comment', 'user', 'create_time']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['news', 'user', 'create_time']
    list_filter = ['news', 'user', 'create_time']
    inlines = [ReplyCommentTabular]


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'category', 'publish_time', 'status']
    list_filter = ['category', 'status', 'publish_time']
    prepopulated_fields = {'slug': ('title', )}
    search_fields = ['title', 'body']
    date_hierarchy = 'publish_time'
    inlines = [CommentTabular]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(New, NewsAdmin)
admin.site.register(ContactMessage)
admin.site.register(Comment, CommentAdmin)
admin.site.register(ReplyComment, ReplyCommentAdmin)
