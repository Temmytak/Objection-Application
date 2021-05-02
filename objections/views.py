from django.shortcuts import render
from .models import (
    ServiceProvider, Agent, ComplaintLanguage, StatusNote, ReferencedCodeSection, 
    ObjectionStatus, ObjectionAssessment, ClosingLevel, CCTSAssistanceRequired, CustomerAssistanceRequired
    )
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import (
    ServiceProviderForm, AgentForm, LanguageForm, StatusNoteForm, RefCodeForm, ObjectionStatusForm, 
    ObjectionAssessmentForm, ClosingLevelForm, CctsAssistanceForm, CustomerAssistanceForm
    )

# Create your views here.
def home_page(request):
    return render(request, "objections/home_page.html")


def administrative_tasks(request):
    return render(request, "objections/administrative_tasks.html")


class serviceprovider_list(ListView):
    template_name = 'objections/serviceprovider_list.html'
    model = ServiceProvider
    context_object_name = 'serviceproviders'
    paginate_by = 20

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


class serviceprovider_detail(DetailView):
    template_name = 'objections/serviceprovider_detail.html'
    model = ServiceProvider
    context_object_name = 'serviceprovider'


class serviceprovider_update(UpdateView):
    model = ServiceProvider
    context_object_name = 'serviceprovider'
    template_name = 'objections/serviceprovider_update.html'
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("service-provider")


#class serviceprovider_delete(DeleteView):
#    model = ServiceProvider
#    context_object_name = 'serviceprovider'
#    template_name = 'objections/serviceprovider_delete.html'

#    success_url = reverse_lazy("service-provider")


class serviceprovider_create(CreateView):
    template_name = 'objections/serviceprovider_create.html'
    form_class = ServiceProviderForm

    success_url = reverse_lazy("service-provider")


class agent_create(CreateView):
    template_name = 'objections/agent_create.html'
    form_class = AgentForm

    success_url = reverse_lazy("agent-home")


#class agent_delete(DeleteView):
#    model = Agent
#    context_object_name = 'agents'
#    template_name = 'objections/agent_delete.html'

#    success_url = reverse_lazy("agent-home")    


class agent_detail(DetailView):
    template_name = 'objections/agent_detail.html'
    model = Agent
    context_object_name = 'agent'


class agent_list(ListView):
    template_name = 'objections/agent_list.html'
    model = Agent
    context_object_name = 'agents'
    paginate_by = 10

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


class language_list(ListView):
    template_name = 'objections/language_list.html'
    model = ComplaintLanguage
    context_object_name = 'languages'
    paginate_by = 10

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


class language_detail(DetailView):
    template_name = 'objections/language_detail.html'
    model = ComplaintLanguage
    context_object_name = 'language'


class language_update(UpdateView):
    model = ComplaintLanguage
    context_object_name = 'language'
    template_name = 'objections/language_update.html'
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("language-list")


class language_create(CreateView):
    template_name = 'objections/language_create.html'
    form_class = LanguageForm

    success_url = reverse_lazy("language-list")


class statusnote_list(ListView):
    template_name = 'objections/statusnote_list.html'
    model = StatusNote
    context_object_name = 'statusnotes'
    paginate_by = 10

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


class statusnote_detail(DetailView):
    template_name = 'objections/statusnote_detail.html'
    model = StatusNote
    context_object_name = 'statusnote'


class statusnote_update(UpdateView):
    model = StatusNote
    context_object_name = 'statusnote'
    template_name = 'objections/statusnote_update.html'
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("statusnote-list")


class statusnote_create(CreateView):
    template_name = 'objections/statusnote_create.html'
    form_class = StatusNoteForm

    success_url = reverse_lazy("statusnote-list")


class refcode_list(ListView):
    template_name = 'objections/refcode_list.html'
    model = ReferencedCodeSection
    context_object_name = 'refcodes'
    paginate_by = 10

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


class refcode_detail(DetailView):
    template_name = 'objections/refcode_detail.html'
    model = ReferencedCodeSection
    context_object_name = 'refcode'


class refcode_update(UpdateView):
    model = ReferencedCodeSection
    context_object_name = 'refcode'
    template_name = 'objections/refcode_update.html'
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("refcode-list")


class refcode_create(CreateView):
    template_name = 'objections/refcode_create.html'
    form_class = RefCodeForm

    success_url = reverse_lazy("refcode-list")


class objectionstatus_list(ListView):
    template_name = 'objections/objectionstatus_list.html'
    model = ObjectionStatus
    context_object_name = 'objectionstatus'
    paginate_by = 10

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


class objectionstatus_detail(DetailView):
    template_name = 'objections/objectionstatus_detail.html'
    model = ObjectionStatus
    context_object_name = 'objectionstatus'


class objectionstatus_update(UpdateView):
    model = ObjectionStatus
    context_object_name = 'objectionstatus'
    template_name = 'objections/objectionstatus_update.html'
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("objectionstatus-list")


class objectionstatus_create(CreateView):
    template_name = 'objections/objectionstatus_create.html'
    form_class = ObjectionStatusForm

    success_url = reverse_lazy("objectionstatus-list")


class objectionassessment_list(ListView):
    template_name = 'objections/objectionassessment_list.html'
    model = ObjectionAssessment
    context_object_name = 'objectionassessments'
    paginate_by = 10

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


class objectionassessment_detail(DetailView):
    template_name = 'objections/objectionassessment_detail.html'
    model = ObjectionAssessment
    context_object_name = 'objectionassessment'


class objectionassessment_update(UpdateView):
    model = ObjectionAssessment
    context_object_name = 'objectionassessment'
    template_name = 'objections/objectionassessment_update.html'
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("objectionassessment-list")


class objectionassessment_create(CreateView):
    template_name = 'objections/objectionassessment_create.html'
    form_class = ObjectionAssessmentForm

    success_url = reverse_lazy("objectionassessment-list")


class closinglevel_list(ListView):
    template_name = 'objections/closinglevel_list.html'
    model = ClosingLevel
    context_object_name = 'closinglevels'
    paginate_by = 10

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


class closinglevel_detail(DetailView):
    template_name = 'objections/closinglevel_detail.html'
    model = ClosingLevel
    context_object_name = 'closinglevel'


class closinglevel_update(UpdateView):
    model = ClosingLevel
    context_object_name = 'closinglevel'
    template_name = 'objections/closinglevel_update.html'
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("closinglevel-list")


class closinglevel_create(CreateView):
    template_name = 'objections/closinglevel_create.html'
    form_class = ClosingLevelForm

    success_url = reverse_lazy("closinglevel-list")


class cctsassistance_list(ListView):
    template_name = 'objections/cctsassistance_list.html'
    model = CCTSAssistanceRequired
    context_object_name = 'cctsassistances'
    paginate_by = 10

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


class cctsassistance_detail(DetailView):
    template_name = 'objections/cctsassistance_detail.html'
    model = CCTSAssistanceRequired
    context_object_name = 'cctsassistance'


class cctsassistance_update(UpdateView):
    model = CCTSAssistanceRequired
    context_object_name = 'cctsassistance'
    template_name = 'objections/cctsassistance_update.html'
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("cctsassistance-list")


class cctsassistance_create(CreateView):
    template_name = 'objections/cctsassistance_create.html'
    form_class = CctsAssistanceForm

    success_url = reverse_lazy("cctsassistance-list")


class customerassistance_list(ListView):
    template_name = 'objections/customerassistance_list.html'
    model = CustomerAssistanceRequired
    context_object_name = 'customerassistances'
    paginate_by = 10

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


class customerassistance_detail(DetailView):
    template_name = 'objections/customerassistance_detail.html'
    model = CustomerAssistanceRequired
    context_object_name = 'customerassistance'


class customerassistance_update(UpdateView):
    model = CustomerAssistanceRequired
    context_object_name = 'customerassistance'
    template_name = 'objections/customerassistance_update.html'
    fields = [
        "name",
        "active"
    ]
    success_url = reverse_lazy("customerassistance-list")


class customerassistance_create(CreateView):
    template_name = 'objections/customerassistance_create.html'
    form_class = CustomerAssistanceForm

    success_url = reverse_lazy("customerassistance-list")