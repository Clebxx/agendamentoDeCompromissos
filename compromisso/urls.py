from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_view, name='pagina-inicial'),
    path('compromissos/', views.list_compromissos, name='lista-compromisso'),
    path('compromissos/novo', views.create_compromisso, name='cadastro-compromisso'),
    path('compromissos/edita/<int:pk>', views.edit_compromisso, name='atualiza-compromisso'),
    path('compromissos/deleta/<int:pk>', views.delete_compromisso, name='deleta-compromisso')
]