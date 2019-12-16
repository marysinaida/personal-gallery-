from django.contrib import admin
from .models import category,location,Image

# Register your models here.

class categoryAdmin(admin.ModelAdmin):
    filter_horizontal =('location',)

admin.site.register(category)
admin.site.register(location)
admin.site.register(Image)
