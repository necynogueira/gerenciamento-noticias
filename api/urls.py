from django.urls import path
from .views import  listar_todas_noticias, adicionar_noticia

urlpatterns = [
    path('listar-noticias/',listar_todas_noticias, name='listar-noticias'),
    path('adicionar-noticia/', adicionar_noticia, name='adicionar_noticia'),
]

