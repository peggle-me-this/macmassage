from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Dashboard, edit_profile, registration_success, profile, register

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('register/', register, name='register'),  # Corrected path for registration
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('edit-profile/', edit_profile, name='edit_profile'),  # Profile editing URL
    path('registration_success/', registration_success, name='registration_success'),
    path('profile/', profile, name='profile'),  # Profile view URL
]

