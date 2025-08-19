from django import forms
from .models import StudentApplication, TouristInquiry


class StudentApplicationForm(forms.ModelForm):
    class Meta:
        model = StudentApplication
        fields = [
            "full_name", "sex", "age", "study_level", 
            "course_of_interest", "passport_or_nrc",
            "phone", "email", "notes"
        ]


class TouristInquiryForm(forms.ModelForm):
    class Meta:
        model = TouristInquiry
        fields = [
            "full_name", "email", "phone", 
            "destination", "travel_date", 
            "number_of_people", "notes"
        ]
