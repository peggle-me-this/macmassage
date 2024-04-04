# bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.booking_list, name='booking_list'),
    path('', views.booking_home, name='booking_home'),  # Home page for bookings
    path('book/', views.book_appointment, name='book_appointment'),  # Make a new booking
    path('api/appointments/', views.appointments_api_view, name='booking-events'),
    path('fullcalendar/', views.fullcalendar_view, name='fullcalendar'),
    path('booking/success/', views.booking_success, name='booking_success'),
    path('booking/failure/', views.booking_failure, name='booking_failure'),
]

