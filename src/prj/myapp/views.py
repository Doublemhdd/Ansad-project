from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from .models.module import *
from .models.schedule import *
from django.shortcuts import get_object_or_404

# Create your views here.

class ModuleListView(ListView):
    model = Module 

class ModuleDetailView(DetailView):
    model = Module 

class ModuleCreateView(CreateView):
    model = Module 
    fields = '__all__'
    success_url = reverse_lazy('module_list')

class ModuleDeleteView(DeleteView):
    model = Module 
    success_url = reverse_lazy('module_list')

class ModuleUpdateView(UpdateView):
    model = Module 
    fields = '__all__'
    success_url = reverse_lazy('module_list')


class ScheduleListView(ListView):
    model = Schedule 

class ScheduleDetailView(DetailView):
    model = Schedule 

class ScheduleCreateView(CreateView):
    model = Schedule 
    fields = '__all__'
    success_url = reverse_lazy('schedule_list')

class ScheduleDeleteView(DeleteView):
    model = Schedule 
    success_url = reverse_lazy('schedule_list')

class ScheduleUpdateView(UpdateView):
    model = Schedule 
    fields = '__all__'
    success_url = reverse_lazy('schedule_list')

def home(request):
    return render(request, 'home.html')

def import_module_csv(request):
    if "GET" == request.method:
        return render(request, "csv_import.html", {'oname': "Module", 'opath': "modules"})
    try:
        object_list = []
        csv_file = request.FILES["formFile"]
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:			
            fields = line.split(",")
            if len(fields) < 5:
                print('Hello!')
                continue
            ob = Module()
            ob.code = fields[0]
            ob.name = fields[1]
            ob.cm_hours = fields[2]
            ob.td_hours = fields[3]
            ob.tp_hours = fields[4]
            object_list.append(ob)
        
        Module.objects.bulk_create(object_list)

    except Exception as e:
        print("Error! Unable to upload file. " + repr(e))
        return HttpResponseRedirect(reverse("module_import"))

    return HttpResponseRedirect(reverse("module_list"))

def import_schedule_csv(request):
    if "GET" == request.method:
        return render(request, "csv_import.html", {'oname': "Schedule", 'opath': "schedules"})
    try:
        object_list = []
        csv_file = request.FILES["formFile"]
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        for line in lines:			
            fields = line.split(",")
            if len(fields) < 6:
                continue
            
            ob = Schedule()
            ob.plage = fields[0]
            ob.semestre = fields[1]
            ob.day = fields[2]
            ob.date = fields[3]
            ob.name = fields[4]
            mcode = fields[5]
            print('Hello!')
            module = get_object_or_404(Module, code=mcode)
            ob.module = module
            
            object_list.append(ob)
        
        Schedule.objects.bulk_create(object_list)

    except Exception as e:
        print("Error! Unable to upload file. " + repr(e))
        return HttpResponseRedirect(reverse("schedule_import"))

    return HttpResponseRedirect(reverse("schedule_list"))

def get_stats(request):
    modules = Module.objects.all()

    # Prepare data for Chart.js
    labels = [module.code for module in modules]
    cm_data = [module.cm_hours for module in modules]
    td_data = [module.td_hours for module in modules]
    tp_data = [module.tp_hours for module in modules]

    context = {
        'labels': labels,
        'cm_data': cm_data,
        'td_data': td_data,
        'tp_data': tp_data,
    }
    return render(request, 'module_hours_chart.html', context)
