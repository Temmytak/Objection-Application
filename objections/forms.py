from django import forms
from .models import (
    ServiceProvider, Agent, ComplaintLanguage, StatusNote, ReferencedCodeSection, 
    ObjectionStatus, ObjectionAssessment, ClosingLevel, CCTSAssistanceRequired, CustomerAssistanceRequired
    )

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


class RefCodeForm(forms.ModelForm):
    class Meta:
        model = ReferencedCodeSection
        fields = (
            'name',
            'active',
        )


class ObjectionStatusForm(forms.ModelForm):
    class Meta:
        model = ObjectionStatus
        fields = (
            'name',
            'active',
        )


class ObjectionAssessmentForm(forms.ModelForm):
    class Meta:
        model = ObjectionAssessment
        fields = (
            'name',
            'active',
        )


class ClosingLevelForm(forms.ModelForm):
    class Meta:
        model = ClosingLevel
        fields = (
            'name',
            'active',
        )

class CctsAssistanceForm(forms.ModelForm):
    class Meta:
        model = CCTSAssistanceRequired
        fields = (
            'name',
            'active',
        )        


class CustomerAssistanceForm(forms.ModelForm):
    class Meta:
        model = CustomerAssistanceRequired
        fields = (
            'name',
            'active',
        )                