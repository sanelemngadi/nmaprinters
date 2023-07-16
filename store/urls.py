from django.urls import path
from store import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("services/", views.services_view, name="services"),
    path("about/", views.about_view, name="about-us"),
    path("contact/", views.contact_view, name="contact-us"),
    path("bulk-order/", views.bulk_order_view, name="bulk-order"),
    path("custom-design/", views.design_view, name="design"),
    path("shop-items/", views.shop_view, name="shop"),
    path("product-2/", views.product_detail_view, name="product-detail"),
    path("account-sanele-mngadi-23/", views.admin_view, name="admin"),
    path("cart/", views.cart_view, name="cart"),
]