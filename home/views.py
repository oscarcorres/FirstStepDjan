from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('home/index.html')
    tituloPlantilla = 'Título de la Plantilla'
    context = {'titulo': tituloPlantilla}
    return HttpResponse(template.render(context, request))


def detail(request):
    return None