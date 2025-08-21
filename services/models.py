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
    
    COUNTRY_CHOICES = [
        ('poland', 'Poland'),
        ('northern_cyprus', 'Northern Cyprus'),
        ('denmark', 'Denmark'),
    ]

    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    sex = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")])
    age = models.PositiveIntegerField()
    study_level = models.CharField(max_length=20, choices=STUDY_LEVEL_CHOICES)
    preferred_country = models.CharField(max_length=20, choices=COUNTRY_CHOICES, help_text="Your preferred study destination")
    course_of_interest = models.CharField(max_length=255)
    passport_or_nrc = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    notes = models.TextField(blank=True, null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_applications")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application - {self.first_name} {self.last_name} ({self.get_preferred_country_display()})"

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


class Testimonial(models.Model):
    RATING_CHOICES = [
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    ]
    
    SERVICE_CHOICES = [
        ('student', 'Student Services'),
        ('tourist', 'Tourist Services'),
        ('both', 'Both Services'),
        ('general', 'General Experience'),
    ]
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service_type = models.CharField(max_length=20, choices=SERVICE_CHOICES)
    rating = models.IntegerField(choices=RATING_CHOICES)
    message = models.TextField(max_length=500)
    location = models.CharField(max_length=100, help_text="e.g., Lusaka, Zambia")
    is_approved = models.BooleanField(default=False)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="testimonials", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.rating} stars ({self.service_type})"
    
    @property
    def star_display(self):
        return '★' * self.rating + '☆' * (5 - self.rating)