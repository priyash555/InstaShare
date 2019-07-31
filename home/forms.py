from .models import Post
from django import forms

class postform(forms.ModelForm):
    
    class Meta:
        model = Post 
        fields = ['title',
                'content',
                ]


class commentform(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
                  'content',
                  ]