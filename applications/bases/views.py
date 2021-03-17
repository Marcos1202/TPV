from django.shortcuts import render
from django.views.generic import TemplateView

#mixins
from django.contrib.auth.mixins import LoginRequiredMixin

#Mixin siempre se pones a la izquierda
class Home(LoginRequiredMixin, TemplateView):
    template_name = "bases/home.html"
    login_url = 'login/'