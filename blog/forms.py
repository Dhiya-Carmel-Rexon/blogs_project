from .models import blogs
from django import forms


class blogsforms(forms.ModelForm):
    title=forms.CharField(max_length=200)
    description=forms.TextField()

    def __str__(self):
        model = blogs
        fields = ['self.title', 'self.description']