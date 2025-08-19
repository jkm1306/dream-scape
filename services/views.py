from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentApplicationForm, TouristInquiryForm

# Create your views here.
def home(request):
    return render(request, 'services/home.html')

def about(request):
    return render(request, 'services/about.html')

# def service(request):
#     return render(request, 'services/service.html')

# def contact(request):
#     return render(request, 'services/contact.html')

def students(request):
    return render(request, 'services/students.html')

def tourists(request):
    return render(request, 'services/tourists.html')



def student_application_view(request):
    if request.method == "POST":
        form = StudentApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.submitted_by = request.user
            application.save()
            messages.success(request, "Your scholarship application has been submitted successfully.")
            return redirect("services:home")
    else:
        form = StudentApplicationForm()
    return render(request, "services/student_application.html", {"form": form})


def tourist_inquiry_view(request):
    if request.method == "POST":
        form = TouristInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.submitted_by = request.user
            inquiry.save()
            messages.success(request, "Your inquiry has been submitted successfully.")
            return redirect("services:home")
    else:
        form = TouristInquiryForm()
    return render(request, "services/tourist_inquiry.html", {"form": form})
