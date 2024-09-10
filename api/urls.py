from django.urls import path
from .views import  listar_todas_noticias, adicionar_noticia, editar_noticia, remover_noticia, listar_noticia

urlpatterns = [
    path('listar-noticias/',listar_todas_noticias, name='listar-noticias'),
    path('adicionar-noticia/', adicionar_noticia, name='adicionar_noticia'),
    path('editar-noticia/', editar_noticia, name='editar_noticia'),  
    path('remover-noticia/', remover_noticia, name='remover_noticia'),
    path('listar-noticia/<str:identificador>/', listar_noticia, name='listar_noticia')
]

