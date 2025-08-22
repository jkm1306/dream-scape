from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def students(request):
    destinations = StudentDestination.objects.prefetch_related("images").all()
    return render(request, 'student_travel/students.html', {"destinations": destinations})

def tourists(request):
    destinations = TouristDestination.objects.prefetch_related("images").all()
    return render(request, 'student_travel/tourists.html', {"destinations": destinations})

def student_application_view(request):
    # Get the country from URL parameter
    country = request.GET.get('country', None)
    
    if request.method == "POST":
        form = StudentApplicationForm(request.POST, user=request.user, country=country)
        if form.is_valid():
            application = form.save(commit=False)
            if request.user.is_authenticated:
                application.submitted_by = request.user
            application.save()
            messages.success(request, "Your scholarship application has been submitted successfully. Our team will review your application and contact you soon!")
            return redirect("services:home")
    else:
        form = StudentApplicationForm(user=request.user, country=country)
    
    # Get country display name for template
    country_display = None
    if country:
        country_choices = dict(form.fields['preferred_country'].choices)
        country_display = country_choices.get(country, country.title())
    
    return render(request, "student_travel/student_application.html", {
        "form": form,
        "selected_country": country,
        "country_display": country_display
    })


def tourist_inquiry_view(request):
    # Get the destination from URL parameter
    destination = request.GET.get('destination', None)
    
    if request.method == "POST":
        form = TouristInquiryForm(request.POST, user=request.user, destination=destination)
        if form.is_valid():
            inquiry = form.save(commit=False)
            if request.user.is_authenticated:
                inquiry.submitted_by = request.user
            inquiry.save()
            messages.success(request, "Your travel inquiry has been submitted successfully. Our team will contact you soon to plan your perfect trip!")
            return redirect("services:home")
    else:
        form = TouristInquiryForm(user=request.user, destination=destination)
    
    # Get destination display name for template
    destination_display = None
    if destination:
        destination_choices = dict(form.fields['preferred_destination'].choices)
        destination_display = destination_choices.get(destination, destination.title())
    
    return render(request, "student_travel/tourist_inquiry.html", {
        "form": form,
        "selected_destination": destination,
        "destination_display": destination_display
    })
