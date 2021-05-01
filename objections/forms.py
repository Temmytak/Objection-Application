from django import forms
from .models import ServiceProvider, Agent

class ServiceProviderForm(forms.ModelForm):
    class Meta:
        model = ServiceProvider
        fields = (
            'name',
            'active',
        )


class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = '__all__'
