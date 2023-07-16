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

def bulk_order_view(request):
    return render(request, "pages/bulk-order.html",{})

def design_view(request):
    return render(request, "pages/design.html",{})

def shop_view(request):
    return render(request, "pages/shop.html",{})

def product_detail_view(request):
    return render(request, "pages/product-detail.html",{})

def admin_view(request):
    return render(request, "pages/admin.html",{})

    
def cart_view(request):
    return render(request, "pages/cart.html",{})