from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Course

class HomePageView(ListView):
    model = Course
    paginate_by = 8
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'