from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'services/home.html')

def about(request):
    return render(request, 'services/about.html')

def service(request):
    return render(request, 'services/service.html')

def contact(request):
    return render(request, 'services/contact.html')