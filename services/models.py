from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class StudentApplication(models.Model):
    POSTGRAD = "Postgraduate"
    UNDERGRAD = "Undergraduate"
    STUDY_LEVEL_CHOICES = [
        (POSTGRAD, "Postgraduate"),
        (UNDERGRAD, "Undergraduate"),
    ]

    full_name = models.CharField(max_length=255)
    sex = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
    age = models.PositiveIntegerField()
    study_level = models.CharField(max_length=20, choices=STUDY_LEVEL_CHOICES)
    course_of_interest = models.CharField(max_length=255)
    passport_or_nrc = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    notes = models.TextField(blank=True, null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_applications")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application - {self.full_name} ({self.study_level})"


class TouristInquiry(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    destination = models.CharField(max_length=255)
    travel_date = models.DateField()
    number_of_people = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tourist_inquiries")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry - {self.full_name} ({self.destination})"
