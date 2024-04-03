# macmassage/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('appointment/', include('appointment.urls')),
    path('about_macmassage/', views.contact, name='contact'),
    path('bookings/', include('bookings.urls')),
    path('accounts/', include('accounts.urls')),
    path('docs/', include('docs.urls')),

]

