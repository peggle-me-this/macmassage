# macmassage_site/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    # View for rendering the homepage
    authenticated = request.user.is_authenticated
    return render(request, 'index.html', {'authenticated': authenticated})

def contact(request):
    # View for rendering the contact page
    return render(request, 'about_index.html')

def bookings(request):
    # View for rendering the services page
    authenticated = request.user.is_authenticated
    return render(request, 'bookings.html',{'authenticated': authenticated})

@login_required
def profile(request):
    # View for rendering the user profile page
    return render(request, 'dashboard.html')
    
def login_page(request):
    # View for rendering the login page
    return render(request, 'login.html')

def register(request):
    # View for rendering the registration page
    return render(request, 'register.html')
