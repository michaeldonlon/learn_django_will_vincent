# pages/views.py

from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class HomePageView(TemplateView):
    template_name = 'home.html'

# I changed this to test pages requiring permission
#
#class AboutPageView(PermissionRequiredMixin, TemplateView):
#    permission_required = 'sites.view_site'
#    login_url = '/accounts/login'
#    raise_exception = True
#    permission_denied_message = "You don't have access"

class AboutPageView(TemplateView):
    template_name = 'about.html'

class RestrictedPageView(TemplateView):
    template_name = 'restricted.html'
