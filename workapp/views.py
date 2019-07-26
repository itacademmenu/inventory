from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Worker, Tools


# Create your views here.


class WorkersListView(generic.ListView):
    queryset = Worker.objects.all()
    template_name = 'workapp/index.html'


class WorkerDetailView(generic.DetailView): #используй DetailView если хочешь отобразить инфу по одному работнику
    model = Worker
    template_name = 'workapp/tools_list.html'


class WorkerCreateView(generic.CreateView):
    model = Worker
    template_name = 'workapp/create_worker.html'
    fields = ['name', 'name_fam', 'years_old']
    success_url = reverse_lazy('home')


class ToolsCreateView(generic.CreateView):
    model = Tools
    template_name = 'workapp/create_tools.html'
    fields = ['name', 'worker', 'inv_number', 'cost']
    success_url = reverse_lazy('home')

