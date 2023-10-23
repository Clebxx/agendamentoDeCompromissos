from django.urls import path 
from . import views

urlpatterns = [
    path('', views.hello_view, name='pagina-inicial'),
    path('lista/', views.list_compromissos, name='pagina-inicial'),
]