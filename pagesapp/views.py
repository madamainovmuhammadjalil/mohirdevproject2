from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomepageViews(TemplateView):
    template_name = 'home.html'
class AboutpageViews(TemplateView):
    template_name = 'about.html'

class Telpageviews(TemplateView):
    template_name = 'tel.html'