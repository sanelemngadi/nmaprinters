from django.urls import path
from store import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("services/", views.services_view, name="services"),
    path("about/", views.about_view, name="about-us"),
    path("contact/", views.contact_view, name="contact-us"),
]