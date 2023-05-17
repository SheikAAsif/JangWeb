from django.contrib import admin
from services.models import services

class serviceAdmin(admin.ModelAdmin):
    list_display = ('services_pic','servicew_title','services_des','services_links','services_mini_title')

admin.site.register(services, serviceAdmin)

# Register your models here.
