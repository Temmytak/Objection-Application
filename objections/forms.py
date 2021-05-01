from django import forms
from .models import ServiceProvider, Agent, ComplaintLanguage, StatusNote

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


class LanguageForm(forms.ModelForm):
    class Meta:
        model = ComplaintLanguage
        fields = (
            'name',
            'active',
        )


class StatusNoteForm(forms.ModelForm):
    class Meta:
        model = StatusNote
        fields = (
            'name',
            'active',
        )

