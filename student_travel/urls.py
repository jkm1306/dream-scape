from django.urls import path
from . import views

app_name = 'student_travel'

urlpatterns = [
    path('students/', views.students, name='students'), 
    path('tourists/', views.tourists, name='tourists'), 
    path('students/student-application/', views.student_application_view, name='student_application'),
    path('tourists/tourist-inquiry/', views.tourist_inquiry_view, name='tourist_inquiry'),
]

