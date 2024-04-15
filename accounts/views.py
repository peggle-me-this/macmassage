# accounts/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import View
from .forms import ProfileEditForm
from .models import UserProfile
from django.core.cache import cache
from django.contrib.auth.views import LoginView, LogoutView 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
import logging
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

@login_required
def profile(request):
    """
    View function to render the user profile page.

    Returns:
    - Rendered template for the user profile page.
    """

    return render(request, 'accounts/dashboard.html')

logger = logging.getLogger(__name__)

def register(request):
    """
    View function to handle user registration.

    Returns:
    - Rendered template for the registration form.
    """

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/registration_success.html')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def registration_success(request):
    """
    View function to render the registration success page.

    Returns:
    - Rendered template for the registration success page.
    """

    return render(request, 'accounts/registration_success.html')

@login_required
def edit_profile(request):
    """
    View function to handle editing of user profile.

    Returns:
    - Rendered template for the profile edit form.
    """

    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileEditForm(instance=user_profile)
    return render(request, 'accounts/edit_profile.html', {'form': form})

def get_data():
    """
    Function to retrieve data from cache or database.

    Returns:
    - Retrieved data.
    """

    data = cache.get('my_data')
    if data is None:
        data = retrieve_data()
        cache.set('my_data', data, timeout=3600)  # Cache for 1 hour
    return data

def retrieve_data():
    """
    Function to retrieve data from the database or another source.

    Returns:
    - Retrieved data.
    """
    pass

class CustomLoginView(LoginView):
    """
    Custom LoginView for user login.

    Attributes:
    - template_name (str): Template name for login page.
    - redirect_authenticated_user (bool): Whether to redirect authenticated users.
    """

    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

def logout_view(request):
    """
    View function to handle user logout.

    Redirects to a success page after logout.
    """
    logout(request)
    # Redirect to a success page.
    
class Dashboard(LoginRequiredMixin, View):
    """
    View class for rendering the user dashboard.

    Attributes:
    - login_url (str): URL to redirect to if user is not logged in.
    """

    login_url = reverse_lazy('login')

    def get(self, request):
        """
        GET method for rendering the dashboard page.

        Returns:
        - Rendered template for the dashboard page.
        """

        try:
            user_profile = request.user.user_profile
        except UserProfile.DoesNotExist:
            user_profile = None
        data = get_data()
        return render(request, 'accounts/dashboard.html', {'user_profile': user_profile, 'data': data})

    def post(self, request):
        """
        POST method for handling form submissions on the dashboard page.

        This method is incomplete and can be implemented as per requirements.
        """
        pass

