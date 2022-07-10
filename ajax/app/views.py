from django.shortcuts import render
from . models import Personne 
from django.views.generic import CreateView
from django.contrib import messages
from .form import UserForm

class appCreateView(CreateView):
    model = Personne
    form_class = UserForm
    template_name = 'appCreateView.html'
    success_url = '/appCreateView'
  
       




