
from django.contrib import admin
from .models import Tour, Booking, UserProfile  # Make sure to import your models

# @admin.register(Tour)
# class TourAdmin(admin.ModelAdmin):
#     list_display = ('title', 'duration', 'created_at', 'price')  # Update with correct field names
#     list_filter = ('duration', 'price')

@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('title', 'duration', 'created_on', 'price', 'latitude', 'longitude')  # Include latitude and longitude in the list display
    list_filter = ('duration', 'price')
    fields = ('title', 'duration', 'created_on', 'price', 'latitude', 'longitude')  # Include latitude and longitude in the fields to be displayed in the form


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'tour', 'booked_on')  # Ensure 'booked_on' is valid
    search_fields = ('user__username', 'tour__title')
    list_filter = ('booked_on',)  # Ensure 'booked_on' is valid

@admin.register(UserProfile)  # If you have a UserProfile model
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar','phone_number', 'address')

