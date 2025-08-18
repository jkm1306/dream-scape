from django.urls import path
from . import views

app_name = 'services' # For namespacing URLS.

urlpatterns = [
    path('', views.home, name='home'), # Root URL points to home.
    path('', views.about, name='about'), # Root URL points to home.
    path('', views.service, name='service'), # Root URL points to home.
    path('', views.contact, name='contact'), # Root URL points to home.
]