# macmassage_site/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    """
    View function for rendering the homepage.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The rendered HTML response for the homepage.
    """
    # View for rendering the homepage
    authenticated = request.user.is_authenticated
    return render(request, 'index.html', {'authenticated': authenticated})

def contact(request):
    """
    View function for rendering the contact page.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The rendered HTML response for the contact page.
    """
    # View for rendering the contact page
    return render(request, 'about_index.html')

def bookings(request):
    """
    View function for rendering the services page.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The rendered HTML response for the services page.
    """
    # View for rendering the services page
    authenticated = request.user.is_authenticated
    return render(request, 'bookings.html',{'authenticated': authenticated})

@login_required
def profile(request):
    """
    View function for rendering the user profile page.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The rendered HTML response for the user profile page.
    """
    # View for rendering the user profile page
    return render(request, 'dashboard.html')
    
def login_page(request):
    """
    View function for rendering the login page.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The rendered HTML response for the login page.
    """
    # View for rendering the login page
    return render(request, 'login.html')

def register(request):
    """
    View function for rendering the registration page.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - HttpResponse: The rendered HTML response for the registration page.
    """
    # View for rendering the registration page
    return render(request, 'register.html')
