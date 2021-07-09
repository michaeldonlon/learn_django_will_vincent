# pages/views.py

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

