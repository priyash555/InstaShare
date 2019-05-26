from .models import Post
from django import forms

class postform(forms.ModelForm):
    
    class Meta:
        model = Post 
        fields = ['title',
                'content',
                ]
