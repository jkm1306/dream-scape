from django import forms
from .models import StudentApplication, TouristInquiry, Testimonial


class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = [
            "first_name", "last_name", "sex", "age", "study_level", 
            "course_of_interest", "passport_or_nrc",
            "phone", "email", "notes"
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user and user.is_authenticated:
            # Pre-populate fields with user data
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['phone'].initial = user.phone
            self.fields['email'].initial = user.email


class TouristInquiryForm(forms.ModelForm):
    class Meta:
        model = TouristInquiry
        fields = [
            "first_name", "last_name", "email", "phone", 
            "destination", "travel_date", 
            "number_of_people", "notes"
        ]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user and user.is_authenticated:
            # Pre-populate fields with user data
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['phone'].initial = user.phone
            self.fields['email'].initial = user.email



class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'email', 'service_type', 'rating', 'message', 'location']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your full name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com'
            }),
            'service_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'rating': forms.Select(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Share your experience with DreamScape...'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., Lusaka, Zambia'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user and user.is_authenticated:
            # Pre-populate fields with user data
            self.fields['name'].initial = f"{user.first_name} {user.last_name}".strip()
            self.fields['email'].initial = user.email

# Your existing forms remain the same...