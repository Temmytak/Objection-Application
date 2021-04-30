from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

class ServiceProvider(models.Model):

    active_choices = (
        (True, True),
        (False, False)
    )

    name = models.CharField(max_length=100)
    active = models.BooleanField(default=1, choices = active_choices)

    def __str__(self):
        return self.name

class Agent(models.Model):
    user = models.OneToOneField(to = User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.email

class ComplaintLanguage(models.Model):
    name = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Complaint Language'
        verbose_name_plural = 'Complaint Language'

    def __str__(self):
        return self.name

class StatusNote(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ReferencedCodeSection(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class ObjectionStatus(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Objection Status'
        verbose_name_plural = 'Objection Status'

    def __str__(self):
        return self.name

class ObjectionAssessment(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name = 'Objection Assessment'
        verbose_name_plural = 'Objection Assessment'    

    def __str__(self):
        return self.name

class ClosingLevel(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class CCTSAssistanceRequired(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'CCTS Assistance Required'
        verbose_name_plural = 'CCTS Assistance Required'

    def __str__(self):
        return self.name

class CustomerAssistanceRequired(models.Model):
    name = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Customer Assistance Required'
        verbose_name_plural = 'Customer Assistance Required'    

    def __str__(self):
        return self.name

class Objection(models.Model):
    complaint_id = models.CharField(max_length=10)
    complaint_language = models.ForeignKey(to = ComplaintLanguage, on_delete = models.SET_NULL, null = True, blank = True)
    service_provider = models.ForeignKey(to = ServiceProvider, on_delete = models.SET_NULL, null = True, blank = True)    
    agent = models.ForeignKey(to = Agent, on_delete = models.SET_NULL, null = True, blank = True)     
    date_submitted = models.DateTimeField()
    date_processing_start = models.DateTimeField()   
    due_date = models.DateTimeField()   
    date_processing_end = models.DateTimeField()            
    status = models.CharField(max_length=10)   
    status_note = models.ForeignKey(to = StatusNote, on_delete = models.SET_NULL, null = True, blank = True) 
    psp_objection_referenced_code_section = models.ForeignKey(to = ReferencedCodeSection, on_delete = models.SET_NULL, null = True, blank = True, related_name='ReferencedCodeSectionPSP')    
    ccts_determination_referenced_code_section = models.ForeignKey(to = ReferencedCodeSection, on_delete = models.SET_NULL, null = True, blank = True, related_name='ReferencedCodeSectionCCTS')        
    objection_status = models.ForeignKey(to = ObjectionStatus, on_delete = models.SET_NULL, null = True, blank = True)   
    ccts_assessment = models.ForeignKey(to = ObjectionAssessment, on_delete = models.SET_NULL, null = True, blank = True)  
    closing_level = models.ForeignKey(to = ClosingLevel, on_delete = models.SET_NULL, null = True, blank = True)         
    ccts_assistance_required = models.ForeignKey(to = CCTSAssistanceRequired, on_delete = models.SET_NULL, null = True, blank = True)  
    customer_assistance_required = models.ForeignKey(to = CustomerAssistanceRequired, on_delete = models.SET_NULL, null = True, blank = True) 

    def __str__(self):
        return self.name

