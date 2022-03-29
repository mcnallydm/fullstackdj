from django import forms
from .models import *
from django.core.exceptions import ValidationError

class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        fields = ('name', 'lastname', 'description')
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'lastname': forms.TextInput(attrs={"class": "form-control"}),
            'description': forms.Textarea(attrs={"class": "form-control mb-5"})
        }
        labels = {
            'name': 'First Name:',
            'lastname': 'Last Name:'
        }
    def clean_description(self):
        desc = self.cleaned_data['description']
        if len(desc)<200:
            raise forms.ValidationError("Description must be 200+ characters.")
        return desc

    def clean_name(self):
        name = self.cleaned_data['name']
        if not name[0].isupper():
            raise forms.ValidationError("First letter should be in capital!")
        return name