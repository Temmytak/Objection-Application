from django import forms
from django.forms.widgets import DateTimeInput
from .models import (
    ServiceProvider, Agent, ComplaintLanguage, StatusNote, ReferencedCodeSection, 
    ObjectionStatus, ObjectionAssessment, ClosingLevel, CCTSAssistanceRequired, CustomerAssistanceRequired, Objection
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


class ObjectionCreateForm(forms.ModelForm):
    class Meta:
        model = Objection
        fields = (
            'complaint_id',
            'complaint_language',
            'service_provider',
            'agent',
            'date_submitted',
            'date_processing_start',
            'due_date',
            'status_note',
            'psp_objection_referenced_code_section',
            'ccts_determination_referenced_code_section',
            'objection_status',
            'ccts_assessment',
            'closing_level',
            'ccts_assistance_required',
            'customer_assistance_required',
            'date_processing_end',            
        )

        widgets = {
            'date_submitted': forms.DateTimeInput(format = ('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),
            'date_processing_start': forms.DateTimeInput(format = ('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),
            'due_date': forms.DateTimeInput(format = ('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),
            'date_processing_end': forms.DateTimeInput(format = ('%Y-%m-%dT%H:%M'), attrs={'type': 'datetime-local'}),
		}

        labels = {
            'complaint_id': 'IMS Complaint ID',
            'complaint_language': 'Complaint Language',
            'service_provider': 'Service Provider',
            'agent': 'Agent',
            'date_submitted': 'Date Submitted',
            'date_processing_start': 'Start Date of Processing',
            'due_date': 'Due Date',
            'status_note': 'Status Note',
            'psp_objection_referenced_code_section': 'PSP Objection Referenced Code Section',
            'ccts_determination_referenced_code_section': 'CCTS Determination Referenced Code Section',
            'objection_status': 'Objection Status',
            'ccts_assessment': 'CCTS Assessment',
            'closing_level': 'Closing Level',
            'ccts_assistance_required': 'CCTS Assistance Required',
            'customer_assistance_required': 'Customer Assistance Required',
            'date_processing_end': 'End Date of Processing'
        }