from django.contrib import admin
from .models import Booking, Contact

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("full_name", "event_date", "event_type", "guests")

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "message")