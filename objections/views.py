from django.shortcuts import render
from .models import ServiceProvider
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .forms import ServiceProviderForm

# Create your views here.
def home_page(request):
    return render(request, "objections/home_page.html")

def administrative_tasks(request):
    return render(request, "objections/administrative_tasks.html")

class serviceprovider_list(ListView):
    template_name = 'objections/serviceprovider_list.html'
    model = ServiceProvider
    context_object_name = 'serviceproviders'
    paginate_by = 10

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

class serviceprovider_delete(DeleteView):
    model = ServiceProvider
    context_object_name = 'serviceprovider'
    template_name = 'objections/serviceprovider_delete.html'

    success_url = reverse_lazy("service-provider")

class serviceprovider_create(CreateView):
    template_name = 'objections/serviceprovider_create.html'
    form_class = ServiceProviderForm

    success_url = reverse_lazy("service-provider")
