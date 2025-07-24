from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(TemplateView):
    template_name = 'main/index.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'main/profile.html'
    login_url = reverse_lazy('login')

class RegisterView(CreateView):
    template_name = 'main/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
