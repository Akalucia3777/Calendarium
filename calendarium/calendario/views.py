from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def error404(request):
    return render(request,'calendario/error404.html')

def inicio(request):
    home = loader.get_template('calendario/index.html')
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('error404'))
    # Resto de la lógica de la vista protegida
    return HttpResponse(home.render())

def vistamensual(request):
    mensual = loader.get_template('calendario/mensual.html')
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('error404'))
    # Resto de la lógica de la vista protegida
    return HttpResponse(mensual.render())

def vistatrackers(request):
    trackers = loader.get_template('calendario/trackers.html')
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('error404'))
    # Resto de la lógica de la vista protegida
    return HttpResponse(trackers.render())

