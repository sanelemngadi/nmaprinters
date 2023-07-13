from django.shortcuts import render
from store.forms import ContactForm

# Create your views here.

def home_view(request):
    return render(request, "nma-home.html", {})

def services_view(request):
    return render(request, "pages/services.html",{})

def contact_view(request):
    form = ContactForm()
    return render(request, "pages/contact.html",{"form": form})

def about_view(request):
    return render(request, "pages/about.html",{})