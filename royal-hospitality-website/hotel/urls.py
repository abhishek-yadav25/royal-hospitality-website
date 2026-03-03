from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('halls/', views.halls, name='halls'),
    path('rooms/', views.rooms, name='rooms'),
    path('bookings/', views.bookings, name='bookings'),
    path('booking/', views.booking_contact, name='booking_contact'),  # form submission
]