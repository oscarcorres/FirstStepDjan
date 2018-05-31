from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
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


class GeneroUpdate(UpdateView):

    model = Genero
    fields = ['genero']
    template_name_suffix = '_update_form'


class GeneroDelete(DeleteView):

    model = Genero
    success_url = reverse_lazy('genero-list')