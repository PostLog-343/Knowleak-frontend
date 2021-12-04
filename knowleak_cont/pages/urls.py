from django.urls import path
from .views import AboutPageView, ContactPageView, HomePageView
urlpatterns = [
    path('', HomePageView.as_view(), name="index"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('contact/', ContactPageView.as_view(), name="contact")
]
