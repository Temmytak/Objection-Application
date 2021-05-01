from django.shortcuts import render
from .models import ServiceProvider, Agent
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import ServiceProviderForm, AgentForm

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
            )
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
            )
        else:
            agent_list = Agent.objects.all().order_by('user')
        return agent_list


