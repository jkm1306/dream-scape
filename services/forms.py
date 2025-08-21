from django import forms
from .models import StudentApplication, TouristInquiry, Testimonial


class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = [
            "first_name", "last_name", "sex", "age", "study_level", 
            "preferred_country", "course_of_interest", "passport_or_nrc",
            "phone", "email", "notes"
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'sex': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Your age', 'min': '16', 'max': '60'}),
            'study_level': forms.Select(attrs={'class': 'form-control'}),
            'preferred_country': forms.Select(attrs={'class': 'form-control'}),
            'course_of_interest': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Computer Science, Business Administration'}),
            'passport_or_nrc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Passport or NRC number'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+260 XXX XXX XXX'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tell us about your academic goals, achievements, or any special requirements...'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        country = kwargs.pop('country', None)
        super().__init__(*args, **kwargs)
        
        if user and user.is_authenticated:
            # Pre-populate fields with user data
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['phone'].initial = user.phone
            self.fields['email'].initial = user.email
        
        # Pre-select country if provided
        if country:
            self.fields['preferred_country'].initial = country


class TouristInquiryForm(forms.ModelForm):
    class Meta:
        model = TouristInquiry
        fields = [
            "first_name", "last_name", "email", "phone", 
            "destination", "travel_date", 
            "number_of_people", "notes"
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your.email@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+260 XXX XXX XXX'}),
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g., Nicosia, Kyrenia, Famagusta'}),
            'travel_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'number_of_people': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Number of travelers', 'min': '1', 'max': '20'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Tell us about special requirements, dietary needs, cultural preferences, or specific experiences you are looking for...'}),
        }

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