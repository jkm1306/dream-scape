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

    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
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
        return f"Application - {self.first_name} {self.last_name} ({self.study_level})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class TouristInquiry(models.Model):
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    destination = models.CharField(max_length=255)
    travel_date = models.DateField()
    number_of_people = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tourist_inquiries")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry - {self.first_name} {self.last_name} ({self.destination})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()
