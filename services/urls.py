from django.urls import path
from . import views

app_name = 'services' # For namespacing URLS.

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    path("testimonials/", views.testimonials, name="testimonials"),  # Add this line
]