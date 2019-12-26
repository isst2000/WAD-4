from django.contrib import admin
from .blog.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('post_text', 'publication_date')
    list_filter = ['publication_date']
    search_fields = ['post_head']


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)