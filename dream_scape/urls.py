from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include ('services.urls')), #For home and other services related urls
    path('users/', include ('users.urls')), 
]
