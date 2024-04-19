# bookings/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from django.http import JsonResponse
from datetime import datetime
from django.utils import timezone
from .models import SpecialEvent
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache

def get_trading_hours(selected_date):
    """
    Function to retrieve trading hours for the selected date.

    Args:
    - selected_date (datetime.date): The selected date.

    Returns:
    - dict: Trading hours for the selected date.
    """
    # Define default trading hours for each day of the week
    default_trading_hours = {
        0: {'start': '08:00', 'end': '17:00'},  # Monday
        1: {'start': '08:00', 'end': '17:00'},  # Tuesday
        2: {'start': '08:00', 'end': '17:00'},  # Wednesday
        3: {'start': '08:00', 'end': '17:00'},  # Thursday
        4: {'start': '08:00', 'end': '17:00'},  # Friday
        5: {'start': '10:00', 'end': '13:00'},  # Saturday
        6: None,  # Sunday (closed)
    }

    # Get the day of the week (Monday is 0, Sunday is 6)
    day_of_week = selected_date.weekday()

    # Retrieve trading hours for the selected day of the week
    trading_hours = default_trading_hours.get(day_of_week)

    return trading_hours

def booking_home(request):
    # View to render the booking home page
    return render(request, 'booking_home.html')

def is_time_slot_available(start_time):
    """
    Function to check if the given start time slot is available for booking.

    Args:
    - start_time (datetime.time): The start time slot.

    Returns:
    - bool: True if the time slot is available, False otherwise.
    """
    # Check if the start_time falls within an existing booking
    existing_bookings = Booking.objects.filter(start_time=start_time)
    
    # If there are no existing bookings at the same start_time, the slot is available
    return not existing_bookings.exists()

def get_special_hours(selected_date):
    """
    Function to retrieve special hours for the selected date.

    Args:
    - selected_date (datetime.date): The selected date.

    Returns:
    - dict: Special hours for the selected date.
    """
    # Retrieve special hours from the database for the selected date
    special_hours = SpecialEvent.objects.filter(date=selected_date).first()
    if special_hours:
        return {'start': special_hours.start_time, 'end': special_hours.end_time}
    return None

def retrieve_data():
    """
    Function to retrieve data from the database or another source.

    Returns:
    - QuerySet: QuerySet containing booking data.
    """
    # This function retrieves data from the database or another source
    return Booking.objects.all()

def get_data():
    """
    Function to retrieve cached data or fetch data from the database.

    Returns:
    - QuerySet: QuerySet containing booking data.
    """
    data = cache.get('my_data')
    if data is None:
        # Retrieve data from the database or another source
        data = retrieve_data()  # Assuming you have a function to retrieve data
        cache.set('my_data', data, timeout=3600)  # Cache for 1 hour
    return data

@login_required
def book_appointment(request):
    """
    View function to handle booking appointment requests.

    If the request method is POST, it validates the form data and saves the booking.
    If the request method is GET, it renders the booking form.

    Returns:
    - Rendered template for the booking form or redirect to booking success page.
    """
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=True)
            booking.user = request.user  # Set the current authenticated user as the booking user
            booking.save()
            messages.success(request, 'Your booking has been confirmed.')
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'book_appointment.html', {'form': form})

@login_required
def booking_list(request):
    """
    View function to retrieve and render the list of bookings for the current user.

    Returns:
    - Rendered template for the booking list page.
    """
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/booking_list.html', {'bookings': bookings})

def fullcalendar_view(request):
    """
    View function to render the FullCalendar view for appointments.

    Returns:
    - Rendered template for the FullCalendar view.
    """
    return render(request, 'fullcalendar.html')  # Corrected template path

def appointments_api_view(request):
    """
    API view function to retrieve appointments data for FullCalendar.

    Returns:
    - JsonResponse: JSON response containing appointment data.
    """
    appointments = Booking.objects.all()  # Fetch appointment data
    data = [{'title': appointment.title, 'start': appointment.start_date, 'end': appointment.end_date} for appointment in appointments]
    return JsonResponse(data, safe=False)

def create_booking(request):
    """
    View function to handle creating new bookings.

    If the request method is POST, it validates the form data and creates the booking.
    If the request method is GET, it renders the booking form.

    Returns:
    - Rendered template for the booking form or redirect to booking success/failure pages.
    """
    if request.method == 'POST':
        # Extract booking details from the form submission
        booking_date = request.POST.get('booking_date')
        # Assuming you have other booking details like time, massage type, etc.

        # Check if the booking date is within 30 days
        current_date = timezone.now().date()
        booking_date = timezone.datetime.strptime(booking_date, '%Y-%m-%d').date()
        thirty_days_from_now = current_date + timezone.timedelta(days=30)

        if booking_date <= thirty_days_from_now:
            # Check availability and automatically confirm the booking
            if is_time_slot_available(booking_date):
                # Create and save the booking with automatic confirmation
                booking = Booking(date=booking_date, status='confirmed')
                booking.save()
                
                # Send confirmation emails to client and owner
                #send_confirmation_emails_booking(booking)  # Updated function name
                
                messages.success(request, 'Your booking has been confirmed.')
                return redirect('booking_success')
            else:
                # Booking time slot is not available
                messages.error(request, 'Sorry, the selected time slot is not available.')
                return redirect('booking_failure')
        else:
            # Booking is more than 30 days from now, mark it as pending confirmation
            booking = Booking(date=booking_date, status='pending')
            booking.save()
            messages.success(request, 'Your booking is pending confirmation.')
            return redirect('booking_pending_confirmation')
    else:
        # Render the booking form
        data = get_data()  # Retrieve cached data
        return render(request, 'book_appointment.html', {'data': data})
    
def booking_success(request):
    """
    View function to render the booking success page.

    Returns:
    - Rendered template for the booking success page.
    """
    return render(request, 'booking_success.html')

def booking_failure(request):
    """
    View function to render the booking failure page.

    Returns:
    - Rendered template for the booking failure page.
    """
    return render(request, 'booking_failure.html')

def booking_list(request):
    """
    View function to retrieve and render the list of all bookings.

    Returns:
    - Rendered template for the booking list page.
    """
    bookings = Booking.objects.all()  # Retrieve all bookings from the database
    num_bookings = len(bookings)

    if num_bookings == 0:
        message = "You have no bookings."
    elif num_bookings == 1:
        message = "You have 1 booking."
    else:
        message = f"You have {num_bookings} bookings."
        
    booking_dates = [booking.date.strftime('%Y-%m-%d') for booking in bookings]
    booking_dates_str = ", ".join(booking_dates)
    
    context = {
        'message': message,
        'booking_dates': booking_dates_str,
    }
    return render(request, 'booking_list.html', context)

