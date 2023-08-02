from django import forms
from .models import user,contact

class signupForm(forms.ModelForm):
    class Meta:
        model=user
        fields='__all__'

class contactForms(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'

    
