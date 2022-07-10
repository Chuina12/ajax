from distutils.command.upload import upload
from django import forms
from .models import Personne

class UserForm(forms.ModelForm):
    class Meta:
        model =Personne
        fields = '__all__'
  
    