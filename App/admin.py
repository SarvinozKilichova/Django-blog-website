from django.contrib import admin

# Register your models here.
from .models import Post, user_profile


class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'status', 'created_on')
  list_filter = ('status', 'created_on', 'author')
  search_fields = ['title', 'content']
  
admin.site.register(Post, PostAdmin)
admin.site.register(user_profile)