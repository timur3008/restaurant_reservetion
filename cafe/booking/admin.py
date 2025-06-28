from django.contrib import admin

from . import models


@admin.register(models.ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'email', 'date']

@admin.register(models.Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['pk', 'full_name', 'time', 'date', 'number_of_people', 'has_comment']
    ordering = ['-created_at']

    def has_comment(self, obj):
        if len(obj.comment) > 0:
            return '✅' 
        else:
            return '❌'