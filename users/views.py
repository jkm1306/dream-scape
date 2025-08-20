from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect("services:home")
    else:
        form = SignUpForm()
    return render(request, "users/signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("services:home")
        else:
            messages.error(request, "Invalid email or password")
            return redirect("users:login")

    return render(request, "users/login.html")


def logout_view(request):
    logout(request)
    return redirect("services:home")


@login_required
def profile_view(request):
    """Display user profile information"""
    user = request.user
    
    # Get user's applications and inquiries (if they exist)
    student_applications = []
    tourist_inquiries = []
    testimonials = []
    
    try:
        from services.models import StudentApplication, TouristInquiry, Testimonial
        # Get applications related to this user's email
        student_applications = StudentApplication.objects.filter(email=user.email).order_by('-created_at')[:5]
        tourist_inquiries = TouristInquiry.objects.filter(email=user.email).order_by('-created_at')[:5]
        testimonials = Testimonial.objects.filter(submitted_by=user).order_by('-created_at')[:5]
    except:
        pass  # Models might not exist yet
    
    context = {
        'user': user,
        'student_applications': student_applications,
        'tourist_inquiries': tourist_inquiries,
        'testimonials': testimonials,
    }
    
    return render(request, "users/profile.html", context)