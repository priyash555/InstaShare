from django import forms
from .models import city

class city(forms.ModelForm):
    
    class Meta:
        model = city 
        fields = ("city",)
