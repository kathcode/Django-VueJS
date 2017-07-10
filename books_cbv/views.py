from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext

from books_cbv.models import Cliente, Animal, Cita, Historia

def login(request):
    return render_to_response('books_cbv/login.html', {}, RequestContext(request))

def home(request):
    return render_to_response('books_cbv/menu.html', {}, RequestContext(request))

def home2(request):
    return render_to_response('books_cbv/menu2.html', {}, RequestContext(request))

def moduleClientes(request):
    return render_to_response('books_cbv/cliente.html', {}, RequestContext(request))

def moduleCitas(request):
    return  render_to_response('books_cbv/cita.html', {}, RequestContext(request))

def moduleAnimal(request):
    return  render_to_response('books_cbv/animal.html', {}, RequestContext(request))

def moduleHistoria(request):
    return  render_to_response('books_cbv/historia.html', {}, RequestContext(request))

class ClienteList(ListView):
    model = Cliente

class ClienteCreate(CreateView):
    model = Cliente
    fields = ['name', 'identificacion', 'email', 'telefono', 'direccion', 'fecha_creacion']

    success_url = reverse_lazy('books_cbv:book_list')

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = ['name', 'identificacion', 'email', 'telefono', 'direccion', 'fecha_creacion']
    success_url = reverse_lazy('books_cbv:book_list')

class ClienteDelete(DeleteView):
    model = Cliente
    success_url = reverse_lazy('books_cbv:book_list')

# Animal
class AnimalList(ListView):
    model = Animal

class AnimalCreate(CreateView):
    model = Animal
    fields = ['name', 'color', 'fecha_nacim', 'id_cliente', 'fecha_creacion']

    success_url = reverse_lazy('books_cbv:book_list_animal')

class AnimalUpdate(UpdateView):
    model = Animal
    fields = ['name', 'color', 'fecha_nacim', 'id_cliente', 'fecha_creacion']
    success_url = reverse_lazy('books_cbv:book_list_animal')

class AnimalDelete(DeleteView):
    model = Animal
    success_url = reverse_lazy('books_cbv:book_list_animal')

# Cita
class CitaList(ListView):
    model = Cita

class CitaCreate(CreateView):
    model = Cita
    fields = ['id_animal', 'name', 'fecha_cita', 'descripcion', 'fecha_creacion']

    success_url = reverse_lazy('books_cbv:book_list_cita')

class CitaUpdate(UpdateView):
    model = Cita
    fields = ['id_animal', 'name', 'fecha_cita', 'descripcion', 'fecha_creacion']
    success_url = reverse_lazy('books_cbv:book_list_cita')

class CitaDelete(DeleteView):
    model = Cita
    success_url = reverse_lazy('books_cbv:book_list_cita')

# Historia
class HistoriaList(ListView):
    model = Historia
    
class HistoriaCreate(CreateView):
    model = Historia
    fields = ['id_historia', 'id_animal', 'name', 'descripcion', 'fecha_creacion']

    success_url = reverse_lazy('books_cbv:book_list_historia')

class HistoriaUpdate(UpdateView):
    model = Historia
    fields = ['id_historia', 'id_animal', 'name', 'descripcion', 'fecha_creacion']

    success_url = reverse_lazy('books_cbv:book_list_historia')

class HistoriaDelete(DeleteView):
    model = Historia
    success_url = reverse_lazy('books_cbv:book_list_historia')