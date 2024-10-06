from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ServiceForm 
from django.contrib import messages
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.dateparse import parse_date


def services(request):
  return render(request, 'services.html')


def redirect_to_homepage(request):
  return render(request, 'index.html')


def customers(request):
    users = User.objects.all()
    
    context = {
        'users': users,
    }

    return render(request, 'admin/customer_list.html', context)
    
       
def services_list(request):
    service = Services.objects.all()
    template = loader.get_template('blog/index.html')
    context = {
        'services' : service,
    }
    return HttpResponse(template.render(context, request))


def services_list_admin(request):
    service = Services.objects.all()
    template = loader.get_template('admin/services.html')
    context = {
        'services' : service,
    }
    return HttpResponse(template.render(context, request))



def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/services/')
    else:
        form = ServiceForm()
    return render(request, 'admin/add_service.html', {'form': form})

def update_service(request, id):
    service = get_object_or_404(Services, id=id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/services/')  # Redirect to the services list page
    else:
        form = ServiceForm(instance=service)
    return render(request, 'admin/update_service.html', {'form': form})


def delete_service(request, id):
    service = get_object_or_404(Services, id=id)
    if request.method == 'POST':
        service.delete()
        return redirect('/services/')  # Redirect to the services list page
    return render(request, 'admin/delete_service.html', {'service': service})
