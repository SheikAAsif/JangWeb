from django.contrib import admin
from News.models import News

class newsAdmin(admin.ModelAdmin):
    new_list=('new_title','new_desc','new_image')

admin.site.register(News,newsAdmin)

# Register your models here.
