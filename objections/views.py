from django.shortcuts import render, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponse
from .models import (
    ServiceProvider, Agent, ComplaintLanguage, StatusNote, ReferencedCodeSection, 
    ObjectionStatus, ObjectionAssessment, ClosingLevel, CCTSAssistanceRequired, CustomerAssistanceRequired, Objection, User
    )
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import (
    ServiceProviderForm, AgentForm, LanguageForm, StatusNoteForm, RefCodeForm, ObjectionStatusForm, 
    ObjectionAssessmentForm, ClosingLevelForm, CctsAssistanceForm, CustomerAssistanceForm, ObjectionCreateForm
    )
import datetime
from datetime import date  
from excel_response import ExcelResponse
from django.db.models import F, Q, Count, Avg
from django.db.models.functions import TruncMonth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from .decorators import unauthenticater_user, allowed_users
from dateutil.relativedelta import relativedelta

# Create your views here.
#@ login_required(login_url = 'login-page')
#def home_page(request):
#    return render(request, "objections/home_page.html")

@ unauthenticater_user
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            # return redirect('home-page')
            return redirect(request.GET.get('next', 'home-page'))
        else:
            messages.info(request, 'username or password is incorrect')

    return render(request, "objections/login_page.html")
    

def logout_user(request):
    logout(request)
    return redirect('login-page')


@ login_required()
# @ allowed_users(allowed_roles=['supervisor','superuser'])
def administrative_tasks(request):
    return render(request, "objections/administrative_tasks.html")


class serviceprovider_list(LoginRequiredMixin, ListView):
    template_name = 'objections/serviceprovider_list.html'
    model = ServiceProvider
    context_object_name = 'serviceproviders'

    def get_queryset(self):
        try:
            a = self.request.GET.get('name',)
        except KeyError:
            a = None
        if a:
            serviveprovider_list = ServiceProvider.objects.filter(
                name__icontains=a
            ).order_by('name')
        else:
            serviveprovider_list = ServiceProvider.objects.all().order_by('name')
        return serviveprovider_list


class serviceprovider_detail(LoginRequiredMixin, DetailView):
    template_name = 'objections/serviceprovider_detail.html'
    model = ServiceProvider
    context_object_name = 'serviceprovider'


class serviceprovider_update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ServiceProvider
    context_object_name = 'serviceprovider'
    template_name = 'objections/serviceprovider_update.html'
    success_message = "Record updated successfully"
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("service-provider")


#class serviceprovider_delete(LoginRequiredMixin, DeleteView):
#    model = ServiceProvider
#    context_object_name = 'serviceprovider'
#    template_name = 'objections/serviceprovider_delete.html'

#    success_url = reverse_lazy("service-provider")


class serviceprovider_create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'objections/serviceprovider_create.html'
    success_message = "Record added successfully"
    form_class = ServiceProviderForm

    success_url = reverse_lazy("service-provider")


class agent_create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'objections/agent_create.html'
    success_message = "Record added successfully"
    form_class = AgentForm
    success_url = reverse_lazy("agent-home")

    def get_form(self, *args, **kwargs):
        form = super(agent_create, self).get_form(*args, **kwargs)
        form.fields['user'].queryset = User.objects.filter(is_active = True)
        return form    

class agent_update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Agent
    context_object_name = 'agent'
    template_name = 'objections/agent_update.html'
    success_message = "Record updated successfully"
    fields = [
        "user",
        "active"
    ]
    success_url = reverse_lazy("agent-home")

#class agent_delete(LoginRequiredMixin, DeleteView):
#    model = Agent
#    context_object_name = 'agents'
#    template_name = 'objections/agent_delete.html'

#    success_url = reverse_lazy("agent-home")    


class agent_detail(LoginRequiredMixin, DetailView):
    template_name = 'objections/agent_detail.html'
    model = Agent
    context_object_name = 'agent'


class agent_list(LoginRequiredMixin, ListView):
    template_name = 'objections/agent_list.html'
    model = Agent
    context_object_name = 'agents'

    def get_queryset(self):
        try:
            a = self.request.GET.get('user',)
        except KeyError:
            a = None
        if a:
            agent_list = Agent.objects.filter(
                user__username__icontains=a
            ).order_by('user')
        else:
            agent_list = Agent.objects.all().order_by('user')
        return agent_list


class language_list(LoginRequiredMixin, ListView):
    template_name = 'objections/language_list.html'
    model = ComplaintLanguage
    context_object_name = 'languages'

    def get_queryset(self):
        try:
            a = self.request.GET.get('name',)
        except KeyError:
            a = None
        if a:
            language_list = ComplaintLanguage.objects.filter(
                name__icontains=a
            ).order_by('name')
        else:
            language_list = ComplaintLanguage.objects.all().order_by('name')
        return language_list


class language_detail(LoginRequiredMixin, DetailView):
    template_name = 'objections/language_detail.html'
    model = ComplaintLanguage
    context_object_name = 'language'


class language_update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ComplaintLanguage
    context_object_name = 'language'
    template_name = 'objections/language_update.html'
    success_message = "Record updated successfully"
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("language-list")


class language_create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'objections/language_create.html'
    success_message = "Record added successfully"
    form_class = LanguageForm

    success_url = reverse_lazy("language-list")


class statusnote_list(LoginRequiredMixin, ListView):
    template_name = 'objections/statusnote_list.html'
    model = StatusNote
    context_object_name = 'statusnotes'

    def get_queryset(self):
        try:
            a = self.request.GET.get('name',)
        except KeyError:
            a = None
        if a:
            statusnote_list = StatusNote.objects.filter(
                name__icontains=a
            ).order_by('name')
        else:
            statusnote_list = StatusNote.objects.all().order_by('name')
        return statusnote_list


class statusnote_detail(LoginRequiredMixin, DetailView):
    template_name = 'objections/statusnote_detail.html'
    model = StatusNote
    context_object_name = 'statusnote'


class statusnote_update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = StatusNote
    context_object_name = 'statusnote'
    template_name = 'objections/statusnote_update.html'
    success_message = "Record updated successfully"
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("statusnote-list")


class statusnote_create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'objections/statusnote_create.html'
    success_message = "Record added successfully"
    form_class = StatusNoteForm

    success_url = reverse_lazy("statusnote-list")


class refcode_list(LoginRequiredMixin, ListView):
    template_name = 'objections/refcode_list.html'
    model = ReferencedCodeSection
    context_object_name = 'refcodes'

    def get_queryset(self):
        try:
            a = self.request.GET.get('name',)
        except KeyError:
            a = None
        if a:
            refcode_list = ReferencedCodeSection.objects.filter(
                name__icontains=a
            ).order_by('name')
        else:
            refcode_list = ReferencedCodeSection.objects.all().order_by('name')
        return refcode_list


class refcode_detail(LoginRequiredMixin, DetailView):
    template_name = 'objections/refcode_detail.html'
    model = ReferencedCodeSection
    context_object_name = 'refcode'


class refcode_update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ReferencedCodeSection
    context_object_name = 'refcode'
    template_name = 'objections/refcode_update.html'
    success_message = "Record updated successfully"
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("refcode-list")


class refcode_create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'objections/refcode_create.html'
    success_message = "Record added successfully"
    form_class = RefCodeForm

    success_url = reverse_lazy("refcode-list")


class objectionstatus_list(LoginRequiredMixin, ListView):
    template_name = 'objections/objectionstatus_list.html'
    model = ObjectionStatus
    context_object_name = 'objectionstatus'

    def get_queryset(self):
        try:
            a = self.request.GET.get('name',)
        except KeyError:
            a = None
        if a:
            objectionstatus_list = ObjectionStatus.objects.filter(
                name__icontains=a
            ).order_by('name')
        else:
            objectionstatus_list = ObjectionStatus.objects.all().order_by('name')
        return objectionstatus_list


class objectionstatus_detail(LoginRequiredMixin, DetailView):
    template_name = 'objections/objectionstatus_detail.html'
    model = ObjectionStatus
    context_object_name = 'objectionstatus'


class objectionstatus_update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ObjectionStatus
    context_object_name = 'objectionstatus'
    template_name = 'objections/objectionstatus_update.html'
    success_message = "Record updated successfully"
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("objectionstatus-list")


class objectionstatus_create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'objections/objectionstatus_create.html'
    success_message = "Record added successfully"
    form_class = ObjectionStatusForm

    success_url = reverse_lazy("objectionstatus-list")


class objectionassessment_list(LoginRequiredMixin, ListView):
    template_name = 'objections/objectionassessment_list.html'
    model = ObjectionAssessment
    context_object_name = 'objectionassessments'

    def get_queryset(self):
        try:
            a = self.request.GET.get('name',)
        except KeyError:
            a = None
        if a:
            objectionassessment_list = ObjectionAssessment.objects.filter(
                name__icontains=a
            ).order_by('name')
        else:
            objectionassessment_list = ObjectionAssessment.objects.all().order_by('name')
        return objectionassessment_list


class objectionassessment_detail(LoginRequiredMixin, DetailView):
    template_name = 'objections/objectionassessment_detail.html'
    model = ObjectionAssessment
    context_object_name = 'objectionassessment'


class objectionassessment_update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ObjectionAssessment
    context_object_name = 'objectionassessment'
    template_name = 'objections/objectionassessment_update.html'
    success_message = "Record updated successfully"
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("objectionassessment-list")


class objectionassessment_create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'objections/objectionassessment_create.html'
    success_message = "Record added successfully"
    form_class = ObjectionAssessmentForm

    success_url = reverse_lazy("objectionassessment-list")


class closinglevel_list(LoginRequiredMixin, ListView):
    template_name = 'objections/closinglevel_list.html'
    model = ClosingLevel
    context_object_name = 'closinglevels'

    def get_queryset(self):
        try:
            a = self.request.GET.get('name',)
        except KeyError:
            a = None
        if a:
            closinglevel_list = ClosingLevel.objects.filter(
                name__icontains=a
            ).order_by('name')
        else:
            closinglevel_list = ClosingLevel.objects.all().order_by('name')
        return closinglevel_list


class closinglevel_detail(LoginRequiredMixin, DetailView):
    template_name = 'objections/closinglevel_detail.html'
    model = ClosingLevel
    context_object_name = 'closinglevel'


class closinglevel_update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = ClosingLevel
    context_object_name = 'closinglevel'
    template_name = 'objections/closinglevel_update.html'
    success_message = "Record updated successfully"
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("closinglevel-list")


class closinglevel_create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'objections/closinglevel_create.html'
    success_message = "Record added successfully"
    form_class = ClosingLevelForm

    success_url = reverse_lazy("closinglevel-list")


class cctsassistance_list(LoginRequiredMixin, ListView):
    template_name = 'objections/cctsassistance_list.html'
    model = CCTSAssistanceRequired
    context_object_name = 'cctsassistances'

    def get_queryset(self):
        try:
            a = self.request.GET.get('name',)
        except KeyError:
            a = None
        if a:
            cctsassistance_list = CCTSAssistanceRequired.objects.filter(
                name__icontains=a
            ).order_by('name')
        else:
            cctsassistance_list = CCTSAssistanceRequired.objects.all().order_by('name')
        return cctsassistance_list


class cctsassistance_detail(LoginRequiredMixin, DetailView):
    template_name = 'objections/cctsassistance_detail.html'
    model = CCTSAssistanceRequired
    context_object_name = 'cctsassistance'


class cctsassistance_update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CCTSAssistanceRequired
    context_object_name = 'cctsassistance'
    template_name = 'objections/cctsassistance_update.html'
    success_message = "Record updated successfully"
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("cctsassistance-list")


class cctsassistance_create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'objections/cctsassistance_create.html'
    success_message = "Record added successfully"
    form_class = CctsAssistanceForm

    success_url = reverse_lazy("cctsassistance-list")


class customerassistance_list(LoginRequiredMixin, ListView):
    template_name = 'objections/customerassistance_list.html'
    model = CustomerAssistanceRequired
    context_object_name = 'customerassistances'

    def get_queryset(self):
        try:
            a = self.request.GET.get('name',)
        except KeyError:
            a = None
        if a:
            customerassistance_list = CustomerAssistanceRequired.objects.filter(
                name__icontains=a
            ).order_by('name')
        else:
            customerassistance_list = CustomerAssistanceRequired.objects.all().order_by('name')
        return customerassistance_list


class customerassistance_detail(LoginRequiredMixin, DetailView):
    template_name = 'objections/customerassistance_detail.html'
    model = CustomerAssistanceRequired
    context_object_name = 'customerassistance'


class customerassistance_update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = CustomerAssistanceRequired
    context_object_name = 'customerassistance'
    template_name = 'objections/customerassistance_update.html'
    success_message = "Record updated successfully"
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("customerassistance-list")


class customerassistance_create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'objections/customerassistance_create.html'
    success_message = "Record added successfully"
    form_class = CustomerAssistanceForm

    success_url = reverse_lazy("customerassistance-list")


class objection_create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'objections/objection_create.html'
    form_class = ObjectionCreateForm
    success_message = "Objection was added successfully"

    success_url = reverse_lazy("objection-list")  

    def get_form(self, *args, **kwargs):
        form = super(objection_create, self).get_form(*args, **kwargs)
        form.fields['complaint_language'].queryset = ComplaintLanguage.objects.filter(active = True)
        form.fields['service_provider'].queryset = ServiceProvider.objects.filter(active = True)
        form.fields['agent'].queryset = Agent.objects.filter(active = True)
        form.fields['status_note'].queryset = StatusNote.objects.filter(active = True)
        form.fields['psp_objection_referenced_code_section'].queryset = ReferencedCodeSection.objects.filter(active = True)
        form.fields['ccts_determination_referenced_code_section'].queryset = ReferencedCodeSection.objects.filter(active = True)
        form.fields['objection_status'].queryset = ObjectionStatus.objects.filter(active = True)
        form.fields['ccts_assessment'].queryset = ObjectionAssessment.objects.filter(active = True)
        form.fields['closing_level'].queryset = ClosingLevel.objects.filter(active = True)
        form.fields['ccts_assistance_required'].queryset = CCTSAssistanceRequired.objects.filter(active = True)
        form.fields['customer_assistance_required'].queryset = CustomerAssistanceRequired.objects.filter(active = True)
        return form


class objection_list(LoginRequiredMixin, ListView):
    template_name = 'objections/objection_list.html'
    model = Objection
    context_object_name = 'objections'

    fields = [
        "complaint_id",
        'complaint_language',
        "service_provider",
        "agent",
        "date_submitted",
        "date_processing_start",
        "due_date",
        "date_processing_end"
    ]

    def get_queryset(self):
        sixMonthsAgo = (date.today() - datetime.timedelta(days=1) + relativedelta(months=-6)).replace(day = 1)       
        objection_list = Objection.objects.filter(
            date_submitted__gte = sixMonthsAgo
            ).order_by('-date_submitted').order_by('-date_submitted')
        return objection_list


class objection_detail(LoginRequiredMixin, DetailView):
    template_name = 'objections/objection_detail.html'
    model = Objection
    context_object_name = 'objection'


class objection_update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Objection
    context_object_name = 'objection'
    form_class = ObjectionCreateForm
    template_name = 'objections/objection_update.html'
    success_message = "Record updated successfully"
    success_url = reverse_lazy("objection-list")

    def get_form(self, *args, **kwargs):
        form = super(objection_update, self).get_form(*args, **kwargs)
        form.fields['complaint_language'].queryset = ComplaintLanguage.objects.filter(active = True)
        form.fields['service_provider'].queryset = ServiceProvider.objects.filter(active = True)
        form.fields['agent'].queryset = Agent.objects.filter(active = True)
        form.fields['status_note'].queryset = StatusNote.objects.filter(active = True)
        form.fields['psp_objection_referenced_code_section'].queryset = ReferencedCodeSection.objects.filter(active = True)
        form.fields['ccts_determination_referenced_code_section'].queryset = ReferencedCodeSection.objects.filter(active = True)
        form.fields['objection_status'].queryset = ObjectionStatus.objects.filter(active = True)
        form.fields['ccts_assessment'].queryset = ObjectionAssessment.objects.filter(active = True)
        form.fields['closing_level'].queryset = ClosingLevel.objects.filter(active = True)
        form.fields['ccts_assistance_required'].queryset = CCTSAssistanceRequired.objects.filter(active = True)
        form.fields['customer_assistance_required'].queryset = CustomerAssistanceRequired.objects.filter(active = True)
        return form    


class objection_pastdue(LoginRequiredMixin, ListView):
    template_name = 'objections/objection_pastdue.html'
    model = Objection
    context_object_name = 'objections'

    fields = [
        "complaint_id",
        'complaint_language',        
        "service_provider",
        "agent",
        "date_submitted",
        "date_processing_start",
        "due_date",
        "date_processing_end"
    ]

    def get_queryset(self):
        today_min = datetime.datetime.combine(date.today(), datetime.time.min)
        try:
            a = self.request.GET.get('complaint_id',)
        except KeyError:
            a = None
        if a:
            objection_list = Objection.objects.filter(
                due_date__lt =  today_min,
                date_processing_end__isnull = True,
                complaint_id__icontains=a
            ).order_by('-date_submitted')
        else:
            objection_list = Objection.objects.filter(
                due_date__lt =  today_min,
                date_processing_end__isnull = True
                ).order_by('-date_submitted')
        return objection_list



class objection_unassigned(LoginRequiredMixin, ListView):
    template_name = 'objections/objection_unassigned.html'
    model = Objection
    context_object_name = 'objections'

    fields = [
        "complaint_id",
        'complaint_language',        
        "service_provider",
        "agent",
        "date_submitted",
        "date_processing_start",
        "due_date",
        "date_processing_end"
    ]

    def get_queryset(self):
        try:
            a = self.request.GET.get('complaint_id',)
        except KeyError:
            a = None
        if a:
            objection_list = Objection.objects.filter(
                agent__isnull = True,
                complaint_id__icontains=a
            ).order_by('-date_submitted')
        else:
            objection_list = Objection.objects.filter(
                agent__isnull = True
                ).order_by('-date_submitted')
        return objection_list

     
class objection_delete(LoginRequiredMixin, DeleteView):
    model = Objection
    context_object_name = 'objection'
    template_name = 'objections/objection_delete.html'
    success_message = "Record deleted successfully"
    success_url = reverse_lazy("objection-list") 

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(objection_delete, self).delete(request, *args, **kwargs)


@ login_required(login_url = 'login-page')
@ allowed_users(allowed_roles=['supervisor','superuser'])
def objection_report_date_submitted(request):
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        if fromdate > todate:
            return render(request, 'objections/objection_report.html')
        else:
            reportresult = Objection.objects.filter(date_submitted__date__gte = fromdate, date_submitted__date__lte = todate).values(
                'complaint_id',
                'complaint_language__name',
                'service_provider__name',
                'agent__user__username',
                'date_submitted',
                'date_processing_start',
                'due_date',
                'status_note__name',
                'psp_objection_referenced_code_section__name',
                'ccts_determination_referenced_code_section__name',
                'objection_status__name',
                'ccts_assessment__name',
                'closing_level__name',
                'ccts_assistance_required__name',
                'customer_assistance_required__name',
                'date_processing_end'
                ).annotate(
                    ComplaintID=F('complaint_id'),   
                    ComplaintLanguage=F('complaint_language__name'),                    
                    ServiceProvider=F('service_provider__name'), 
                    Agent=F('agent__user__username'), 
                    DateSubmitted=F('date_submitted'), 
                    ProcessingStartDate=F('date_processing_start'), 
                    DueDate=F('due_date'), 
                    StatusNote=F('status_note__name'), 
                    PSPObjectionRefCodeSection=F('psp_objection_referenced_code_section__name'), 
                    CCTSDeterminationRefCodeSection=F('ccts_determination_referenced_code_section__name'),
                    ObjectionStatus=F('objection_status__name'),                     
                    CCTSAssessment=F('ccts_assessment__name'), 
                    ClosingLevel=F('closing_level__name'), 
                    CCTSAssistanceRequired=F('ccts_assistance_required__name'), 
                    CustomerAssistanceRequired=F('customer_assistance_required__name'), 
                    ProcessingEndDate=F('date_processing_end') 
                    ).values(
                        'ComplaintID',
                        'ComplaintLanguage',
                        'ServiceProvider',
                        'Agent',
                        'DateSubmitted',
                        'ProcessingStartDate',
                        'DueDate',
                        'StatusNote',
                        'PSPObjectionRefCodeSection',
                        'CCTSDeterminationRefCodeSection',
                        'ObjectionStatus',
                        'CCTSAssessment',
                        'ClosingLevel',
                        'CCTSAssistanceRequired',
                        'CustomerAssistanceRequired',
                        'ProcessingEndDate'
                    )
            return ExcelResponse(
                data = reportresult,
                output_filename = 'objection_report_based_on_date_submitted' + str(datetime.datetime.now()),
                worksheet_name = 'objection-report'
                )
    else:
        return render(request, 'objections/objection_report.html')


class objection_myobjections(LoginRequiredMixin, ListView):
    template_name = 'objections/objection_myobjections.html'
    model = Objection
    context_object_name = 'objections'

    fields = [
        "complaint_id",
        'complaint_language',
        "service_provider",
        "agent",
        "date_submitted",
        "date_processing_start",
        "due_date",
        "date_processing_end"
    ]

    def get_queryset(self):
        try:
            a = self.request.GET.get('complaint_id',)
        except KeyError:
            a = None
        if a:
            objection_list = Objection.objects.filter(
                agent__user__username = self.request.user.username,
                date_processing_end__isnull = True,
                complaint_id__icontains=a
            ).order_by('-date_submitted')
        else:
            objection_list = Objection.objects.filter(
                agent__user__username = self.request.user.username,
                date_processing_end__isnull = True
                ).order_by('-date_submitted')
        return objection_list


class objection_view(LoginRequiredMixin, ListView):
    template_name = 'objections/objection_view.html'
    model = Objection
    context_object_name = 'objections'

    fields = [
        "complaint_id",
        'complaint_language',
        "service_provider",
        "agent",
        "date_submitted",
        "date_processing_start",
        "due_date",
        "date_processing_end"
    ]

    def get_queryset(self):
        try:
            a = self.request.GET.get('complaint_id',)
        except KeyError:
            a = None
        if a:
            objection_list = Objection.objects.filter(
                complaint_id__icontains=a
            )
        else:
            objection_list = None
        return objection_list


class objection_open(LoginRequiredMixin, ListView):
    template_name = 'objections/objection_open.html'
    model = Objection
    context_object_name = 'objections'

    fields = [
        "complaint_id",
        'complaint_language',
        "service_provider",
        "agent",
        "date_submitted",
        "date_processing_start",
        "due_date",
        "date_processing_end"
    ]

    def get_queryset(self):
        try:
            a = self.request.GET.get('complaint_id',)
        except KeyError:
            a = None
        if a:
            objection_list = Objection.objects.filter(
                date_processing_end__isnull = True,
                complaint_id__icontains=a
            ).order_by('-date_submitted')
        else:
            objection_list = Objection.objects.filter(
                date_processing_end__isnull = True
                ).order_by('-date_submitted')
        return objection_list        


@ login_required(login_url = 'login-page')
def home_page(request):
    data = []
    today_min = datetime.datetime.combine(date.today(), datetime.time.min)
    month_start_i = (date.today()).replace(day = 1)
    month_start = datetime.datetime.combine(month_start_i, datetime.time.min)

    unassignedObj = Objection.objects.filter(agent__isnull = True).count()
    data.append(unassignedObj)

    pastDue = Objection.objects.filter(due_date__lt = today_min, date_processing_end__isnull = True).count()
    data.append(pastDue)

    #submittedObj = Objection.objects.filter(date_submitted__gte = month_start).count()
    #data.append(submittedObj)

    openObj = Objection.objects.filter(date_processing_end__isnull = True).count()
    data.append(openObj)    

    completedObj = Objection.objects.filter(date_processing_end__gte = month_start).count()
    data.append(completedObj)

    acceptedObj = Objection.objects.filter(date_processing_end__gte = month_start, objection_status__name__icontains = 'Accepted').count()
    data.append(acceptedObj)

    rejectedObj = Objection.objects.filter(date_processing_end__gte = month_start, objection_status__name__icontains = 'Rejected').count()
    data.append(rejectedObj)

    closed91E = Objection.objects.filter(date_processing_end__gte = month_start, objection_status__name__icontains = 'Closed 9.1 (e)').count()
    data.append(closed91E)  

    CloseMtd = Objection.objects.filter(date_processing_end__gte = month_start)
    AHTSubmitClose = CloseMtd.aggregate(duration=Avg(F('date_processing_end') - F('date_submitted')))
    data.append(str(AHTSubmitClose['duration']).split(".")[0]) 
 
    AHTStartClose = CloseMtd.aggregate(duration=Avg(F('date_processing_end') - F('date_processing_start')))
    data.append(str(AHTStartClose['duration']).split(".")[0]) 

    sixMonthsAgo = (date.today() - datetime.timedelta(days=1) + relativedelta(months=-6)).replace(day = 1)
    Submitted6Months = Objection.objects.filter(date_submitted__gte = sixMonthsAgo)
    subgroupedData = Submitted6Months.annotate(month=TruncMonth('date_submitted')).values('month').order_by('month').annotate(c=Count('complaint_id')).values('month', 'c') 
    submitted_label = []
    submitted_data = []
    for chart_data in subgroupedData:
        submitted_label.append(datetime.datetime.strftime(chart_data['month'], '%b'))
        submitted_data.append(chart_data['c']) 
  
    Closed6Months = Objection.objects.filter(date_processing_end__gte = sixMonthsAgo)
    clgroupedData = Closed6Months.annotate(month=TruncMonth('date_processing_end')).values('month').order_by('month').annotate(c=Count('complaint_id')).values('month', 'c') 
    closed_label = []
    closed_data = []
    for chart_data in clgroupedData:
        closed_label.append(datetime.datetime.strftime(chart_data['month'], '%b'))
        closed_data.append(chart_data['c']) 

    objections = {
        'unassObj': data[0],
        'pastDue': data[1],
        #'submittedObj': data[2],
        'openObj': data[2],        
        'completedObj': data[3],
        'acceptedObj': data[4],   
        'rejectedObj': data[5],
        'closed91E': data[6],
        'AHTSubmitClose': data[7],
        'AHTStartClose': data[8],
        'submitted_label': submitted_label,
        'submitted_data': submitted_data,
        'closed_label': closed_label,
        'closed_data': closed_data,        
        'subchart_colours':['rgba(255, 99, 132, 0.2)'] * len(subgroupedData),
        'subchart_border_colours': ['rgba(255, 99, 132, 0.5)'] * len(subgroupedData),
        'clchart_colours':['rgba(0, 209, 178, 0.55)'] * len(clgroupedData),
        'clchart_border_colours': ['rgba(0, 209, 178, 0.9)'] * len(clgroupedData)                  
        }
    return render(request, 'objections/home_page.html', objections)


class objection_submitted(LoginRequiredMixin, ListView):
    template_name = 'objections/objection_submitted.html'
    model = Objection
    context_object_name = 'objections'

    fields = [
        "complaint_id",
        'complaint_language',
        "service_provider",
        "agent",
        "date_submitted",
        "date_processing_start",
        "due_date",
        "date_processing_end"
    ]
 
 
    def get_queryset(self):
        month_start_i = (date.today()).replace(day = 1)
        month_start = datetime.datetime.combine(month_start_i, datetime.time.min)
        try:
            a = self.request.GET.get('complaint_id',)
        except KeyError:
            a = None
        if a:
            objection_list = Objection.objects.filter(
                date_submitted__gte = month_start,
                complaint_id__icontains=a
            ).order_by('-date_submitted')
        else:
            objection_list = Objection.objects.filter(
                date_submitted__gte = month_start
                ).order_by('-date_submitted')
        return objection_list


class objection_accepted(LoginRequiredMixin, ListView):
    template_name = 'objections/objection_accepted.html'
    model = Objection
    context_object_name = 'objections'

    fields = [
        "complaint_id",
        'complaint_language',
        "service_provider",
        "agent",
        "date_submitted",
        "date_processing_start",
        "due_date",
        "date_processing_end"
    ]

    def get_queryset(self):
        month_start_i = (date.today()).replace(day = 1)
        month_start = datetime.datetime.combine(month_start_i, datetime.time.min)
        try:
            a = self.request.GET.get('complaint_id',)
        except KeyError:
            a = None
        if a:
            objection_list = Objection.objects.filter(
                date_processing_end__gte = month_start, 
                objection_status__name__icontains = 'Accepted',
                complaint_id__icontains=a
            ).order_by('-date_submitted')
        else:
            objection_list = Objection.objects.filter(
                date_processing_end__gte = month_start, 
                objection_status__name__icontains = 'Accepted'
                ).order_by('-date_submitted')
        return objection_list


class objection_rejected(LoginRequiredMixin, ListView):
    template_name = 'objections/objection_rejected.html'
    model = Objection
    context_object_name = 'objections'

    fields = [
        "complaint_id",
        'complaint_language',
        "service_provider",
        "agent",
        "date_submitted",
        "date_processing_start",
        "due_date",
        "date_processing_end"
    ]

    def get_queryset(self):
        month_start_i = (date.today()).replace(day = 1)
        month_start = datetime.datetime.combine(month_start_i, datetime.time.min)
        try:
            a = self.request.GET.get('complaint_id',)
        except KeyError:
            a = None
        if a:
            objection_list = Objection.objects.filter(
                date_processing_end__gte = month_start, 
                objection_status__name__icontains = 'Rejected',
                complaint_id__icontains=a
            ).order_by('-date_submitted')
        else:
            objection_list = Objection.objects.filter(
                date_processing_end__gte = month_start, 
                objection_status__name__icontains = 'Rejected'
                ).order_by('-date_submitted')
        return objection_list                


class objection_closed91e(LoginRequiredMixin, ListView):
    template_name = 'objections/objection_closed_91e.html'
    model = Objection
    context_object_name = 'objections'

    fields = [
        "complaint_id",
        'complaint_language',
        "service_provider",
        "agent",
        "date_submitted",
        "date_processing_start",
        "due_date",
        "date_processing_end"
    ]

    def get_queryset(self):
        month_start_i = (date.today()).replace(day = 1)
        month_start = datetime.datetime.combine(month_start_i, datetime.time.min)
        try:
            a = self.request.GET.get('complaint_id',)
        except KeyError:
            a = None
        if a:
            objection_list = Objection.objects.filter(
                date_processing_end__gte = month_start, 
                objection_status__name__icontains = 'Closed 9.1 (e)',
                complaint_id__icontains=a
            ).order_by('-date_submitted')
        else:
            objection_list = Objection.objects.filter(
                date_processing_end__gte = month_start, 
                objection_status__name__icontains = 'Closed 9.1 (e)'
                ).order_by('-date_submitted')
        return objection_list


def error_404_view(request, exception):
    return render(request, "objections/error_404.html")

def error_500_view(request):
    return render(request, "objections/error_500.html")
