from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Persona
from .forms import PersonaForm

class PersonaListView(ListView):
    model = Persona
    template_name = 'personas/lista.html'
    context_object_name = 'personas'
    ordering = ['id']

class PersonaCreateView(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/formulario.html'
    success_url = reverse_lazy('lista_personas')

class PersonaUpdateView(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'personas/formulario.html'
    success_url = reverse_lazy('lista_personas')

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'personas/confirmar_eliminar.html'
    success_url = reverse_lazy('lista_personas')