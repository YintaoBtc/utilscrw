from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomeBlockView(TemplateView):
    template_name =  "core/home.html"


class SampleBlockView(TemplateView):
    template_name = "core/sample.html"