from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),   
    path('subscribe/',views.subscribe_newsletter, name="subscribe_newsletter"),   
    path('contact/',views.contact, name="contact"),   
    path('about-us/',views.about, name="about"),   
    path('services/',views.service, name="service"),   
    path('gallery/',views.gallery, name="gallery"),
    path('contact-us',views.contact_page,name="contact_us")   
]