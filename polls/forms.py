from django.core import validators
from django import forms
from .models import Syndrome 

class Ajoutcode(forms.ModelForm):
    class Meta:

        model = Syndrome
        fields = ['code_envoyé','code_reçu']
        widgets={
            'code_envoyé':forms.TextInput(attrs={'class': 'form-control'}),
            'code_reçu':forms.TextInput(attrs={'class': 'form-control'}),

        }



 
