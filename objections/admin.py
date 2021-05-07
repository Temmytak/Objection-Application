from django.contrib import admin
from .models import (
    User, ServiceProvider, Agent, ComplaintLanguage, StatusNote, 
    ReferencedCodeSection, ObjectionStatus, ObjectionAssessment, 
    ClosingLevel, CCTSAssistanceRequired, CustomerAssistanceRequired, 
    Objection)

# Register your models here.

# admin.site.register(User)
admin.site.register(ServiceProvider)
admin.site.register(Agent)
admin.site.register(ComplaintLanguage)
admin.site.register(StatusNote)
admin.site.register(ReferencedCodeSection)
admin.site.register(ObjectionStatus)
admin.site.register(ObjectionAssessment)
admin.site.register(ClosingLevel)
admin.site.register(CCTSAssistanceRequired)
admin.site.register(CustomerAssistanceRequired)
admin.site.register(Objection)