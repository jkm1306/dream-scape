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
    DESTINATION_CHOICES = [
        ('zambia', 'Zambia'),
        ('ghana', 'Ghana'),
        ('eswatini', 'Eswatini'),
        ('zimbabwe', 'Zimbabwe'),
        ('china', 'China'),
        ('dubai', 'Dubai, UAE'),
        ('nigeria', 'Nigeria'),
    ]

    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    preferred_destination = models.CharField(max_length=20, choices=DESTINATION_CHOICES, help_text="Your preferred travel destination")
    attraction = models.CharField(max_length=255, blank=True, null=True)  # If I want to know whicj attraction was applied for.
    destination_details = models.CharField(max_length=255, blank=True, null=True, help_text="Specific cities or attractions you'd like to visit")
    travel_date = models.DateField()
    number_of_people = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tourist_inquiries")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry - {self.first_name} {self.last_name} ({self.get_preferred_destination_display()})"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()


class CarouselImage(models.Model):
    SLIDE_CHOICES = [
        ('student', 'Student Slide'),
        ('tourist', 'Tourist Slide'),
    ]
    
    title = models.CharField(max_length=200)
    slide_type = models.CharField(max_length=20, choices=SLIDE_CHOICES, unique=True)
    image = models.ImageField(upload_to='carousel_images/')
    alt_text = models.CharField(max_length=255, help_text="Alternative text for accessibility")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Carousel Image"
        verbose_name_plural = "Carousel Images"
        ordering = ['slide_type']

    def __str__(self):
        return f"{self.get_slide_type_display()} - {self.title}"

    @property
    def image_url(self):
        """Return image URL or empty string if no image"""
        if self.image:
            return self.image.url
        return ''
    


class StudentDestination(models.Model):
    name = models.CharField(max_length=100)
    country_flag = models.CharField(max_length=10, blank=True, help_text="Emoji flag or leave blank")
    description = models.TextField()
    
    # Optional cost info
    tuition_fee = models.CharField(max_length=100, blank=True, null=True)
    living_cost = models.CharField(max_length=100, blank=True, null=True)
    
    # Scholarship info
    scholarship_title = models.CharField(max_length=200, blank=True, null=True)
    scholarship_details = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class StudentDestinationImage(models.Model):
    destination = models.ForeignKey(StudentDestination, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="student_destinations/")
    
    def __str__(self):
        return f"Image for {self.destination.name}"


class TouristDestination(models.Model):
    """
    Represents a country (or main tourist destination).
    """
    name = models.CharField(max_length=100)
    country_flag = models.CharField(max_length=10, blank=True, help_text="Emoji or leave blank")
    description = models.TextField()

    def __str__(self):
        return self.name


class TouristDestinationImage(models.Model):
    """
    Images for the country itself (general images, not attraction-specific).
    """
    destination = models.ForeignKey(
        TouristDestination,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="tourist_destinations/")

    def __str__(self):
        return f"Image for {self.destination.name}"


class AttractionSite(models.Model):
    """
    Specific attraction sites inside a country.
    """
    destination = models.ForeignKey(
        TouristDestination,
        related_name="attractions",
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200, blank=True, null=True)  # optional
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.destination.name})"


class AttractionSiteImage(models.Model):
    """
    Images for each attraction site.
    """
    attraction = models.ForeignKey(
        AttractionSite,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="attraction_sites/")

    def __str__(self):
        return f"Image for {self.attraction.name}"
