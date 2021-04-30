from django import forms
from .models import ServiceProvider

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = (
            'name',
            'active',
        )