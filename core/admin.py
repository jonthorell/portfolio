from django.contrib import admin
from .models import project

# Register your models here.

class projectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'description',
        'created_on',
     )

admin.site.register(project,projectAdmin)
