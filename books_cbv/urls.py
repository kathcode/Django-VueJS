from django.conf.urls import patterns, url

from books_cbv import views

urlpatterns = patterns('',
  url(r'^$', views.home, name='home'),
  # Cliente
  url(r'^clients', views.moduleClientes, name='moduleClientes'),
  url(r'^list$', views.ClienteList.as_view(), name='book_list'),
  url(r'^new$', views.ClienteCreate.as_view(), name='book_new'),
  url(r'^edit/(?P<pk>\d+)$', views.ClienteUpdate.as_view(), name='book_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.ClienteDelete.as_view(), name='book_delete'),
  # Animal
  url(r'^animal', views.moduleAnimal, name='moduleAnimal'),
  url(r'^list1$', views.AnimalList.as_view(), name='book_list_animal'),
  url(r'^new/animal$', views.AnimalCreate.as_view(), name='book_new_animal'),
  url(r'^edit/animal(?P<pk>\d+)$', views.AnimalUpdate.as_view(), name='book_edit_animal'),
  url(r'^delete/animal(?P<pk>\d+)$', views.AnimalDelete.as_view(), name='book_delete_animal'),
  # Cita
  url(r'^cita', views.moduleCitas, name='moduleCitas'),
  url(r'^list2$', views.CitaList.as_view(), name='book_list_cita'),
  url(r'^new/cita$', views.CitaCreate.as_view(), name='book_new_cita'),
  url(r'^edit/cita(?P<pk>\d+)$', views.CitaUpdate.as_view(), name='book_edit_cita'),
  url(r'^delete/cita(?P<pk>\d+)$', views.CitaDelete.as_view(), name='book_delete_cita'),
  # Historia clinica
  url(r'^historia', views.moduleHistoria, name='moduleHistoria'),
  url(r'^list3$', views.HistoriaList.as_view(), name='book_list_historia'),
  url(r'^new/historia$', views.HistoriaCreate.as_view(), name='book_new_historia'),
  url(r'^edit/historia(?P<pk>\d+)$', views.HistoriaUpdate.as_view(), name='book_edit_historia'),
  url(r'^delete/historia(?P<pk>\d+)$', views.HistoriaDelete.as_view(), name='book_delete_historia'),
)
