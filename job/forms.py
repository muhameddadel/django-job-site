from django import forms
from .models import Application

class ApplyForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'email', 'website', 'cv', 'cover_letter']