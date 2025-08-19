from django import forms
from .models import StudentApplication, TouristInquiry


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
