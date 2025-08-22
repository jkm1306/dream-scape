from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

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
    



