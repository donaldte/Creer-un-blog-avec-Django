from django.contrib import admin
from .models import CreateBlog, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'intro', 'slug', 'date_added')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('body', 'email', 'date_added')    


admin.site.register(CreateBlog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)