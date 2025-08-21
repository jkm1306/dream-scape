from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentApplicationForm, TouristInquiryForm, Testimonial, TestimonialForm

def home(request):
    # Get approved testimonials for the homepage
    testimonials = Testimonial.objects.filter(is_approved=True)[:6]  # Show latest 6
    return render(request, 'services/home.html', {'testimonials': testimonials})


def testimonials(request):
    if request.method == "POST":
        form = TestimonialForm(request.POST, user=request.user)
        if form.is_valid():
            testimonial = form.save(commit=False)
            if request.user.is_authenticated:
                testimonial.submitted_by = request.user
            testimonial.save()
            messages.success(request, "Thank you for your testimonial! It will be reviewed and published soon.")
            return redirect("services:testimonials")
    else:
        form = TestimonialForm(user=request.user)
    
    # Get all approved testimonials for display
    all_testimonials = Testimonial.objects.filter(is_approved=True)
    
    return render(request, "services/testimonials.html", {
        "form": form, 
        "testimonials": all_testimonials
    })

def about(request):
    return render(request, 'services/about.html')


def students(request):
    return render(request, 'services/students.html')

def tourists(request):
    return render(request, 'services/tourists.html')


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
    
    return render(request, "services/student_application.html", {
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
    
    return render(request, "services/tourist_inquiry.html", {
        "form": form,
        "selected_destination": destination,
        "destination_display": destination_display
    })
