from django.http import HttpResponse
from django.template import loader
from random import randint

# Create your views here.
def index(request):
    template = loader.get_template('home/index.html')
    tituloPlantilla = 'Título de la Plantilla'
    context = {'titulo': tituloPlantilla, 'numero': randint(1,49)}
    return HttpResponse(template.render(context, request))


def detail(request,numero):
    template = loader.get_template('home/detail.html')
    context = {'numero': numero}
    return HttpResponse(template.render(context, request))