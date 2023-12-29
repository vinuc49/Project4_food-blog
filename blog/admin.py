from django.contrib import admin
from .models import Post, Comment, Restaurant
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Restaurant)
class RestaurantAdmin(SummernoteModelAdmin):
    list_display = ('name', 'city', 'phone', 'created_on')
    search_fields = ['name', 'city']
    list_filter = ('city', 'county')

@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('post', 'author', 'approved')
    list_filter = ('author',)