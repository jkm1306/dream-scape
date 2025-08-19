from django.urls import path
from . import views

app_name = 'services' # For namespacing URLS.

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'), 
    # path('service/', views.service, name='service'), 
    # path('contact/', views.contact, name='contact'), 
    path('students/', views.students, name='students'), 
    path('tourists/', views.tourists, name='tourists'), 
    path("students/student-application/", views.student_application_view, name="student_application"),
    path("tourists/tourist-inquiry/", views.tourist_inquiry_view, name="tourist_inquiry"),
]