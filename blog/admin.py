from django.contrib import admin
from blog.models import MyModelName

def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Mark selected stories as published"

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    ordering = ['title']
    actions = [make_published]

admin.site.register(MyModelName, ArticleAdmin)