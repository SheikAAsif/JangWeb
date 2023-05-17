from django.contrib import admin
from contactEnquiry.models import contactEnquiry

class contactEnquiryAdmin(admin.ModelAdmin):
    contactEnquiry_list=('user_name','user_last_name','user_address','user_old_address','user_city')


admin.site.register(contactEnquiry,contactEnquiryAdmin)

# Register your models here.
