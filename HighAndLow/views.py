import random
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"
    
class SoloView(TemplateView):
    template_name = "1p.html"
    
    def get_context_data(self, **kwargs):
        ctxt = super().get_context_data(**kwargs)
        
        
        return ctxt
    
class MultiView(TemplateView):
    template_name = "2p.html"