from re import template
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'main.html'

class AboutView(TemplateView):
    template_name = 'about.html'