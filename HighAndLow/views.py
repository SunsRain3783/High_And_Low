from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import SignUpForm

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class IndexView(TemplateView):
    template_name = "registration/top.html"
    
class SoloView(TemplateView):
    template_name = "1p.html"
    
class LoginView(TemplateView):
    template_name = "1p_user.html"
    
class MultiView(TemplateView):
    template_name = "2p.html"
    
class HowView(TemplateView):
    template_name = "how.html"
