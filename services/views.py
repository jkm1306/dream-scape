from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from student_travel.models import *

def home(request):
    # Get approved testimonials for the homepage
    testimonials = Testimonial.objects.filter(is_approved=True)[:6]  # Show latest 6
    
    # Get carousel images
    carousel_images = {}
    try:
        student_image = CarouselImage.objects.get(slide_type='student', is_active=True)
        carousel_images['student'] = student_image
    except CarouselImage.DoesNotExist:
        carousel_images['student'] = None
    
    try:
        tourist_image = CarouselImage.objects.get(slide_type='tourist', is_active=True)
        carousel_images['tourist'] = tourist_image
    except CarouselImage.DoesNotExist:
        carousel_images['tourist'] = None
    
    return render(request, 'services/home.html', {
        'testimonials': testimonials,
        'carousel_images': carousel_images
    })


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



