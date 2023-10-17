from django.contrib import admin
from .models import Blog

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title',)  


admin.site.register(Blog, ProjectAdmin)