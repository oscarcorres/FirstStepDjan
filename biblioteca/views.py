from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from biblioteca.models import Genero


class GeneroListView(ListView):

    model = Genero
    paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GeneroDetailView(DetailView):

    model = Genero

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class GeneroCreate(CreateView):

    model = Genero
    fields = ['genero']