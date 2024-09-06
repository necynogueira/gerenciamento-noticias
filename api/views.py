
from django.http import JsonResponse
import uuid
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
banco = {}

@csrf_exempt
def adicionar_noticia(request):
    if request.method == "POST":
        # Extrai dados do corpo da requisição JSON
        dados = request.POST
        
        # Extrai dados
        titulo = dados.get('titulo')
        conteudo = dados.get('conteudo')
        publicado = dados.get('publicado') == 'true'
        autor = dados.get('autor')

        # Gera um identificador único e data de criação
        identificador = uuid.uuid4().hex
        data_criacao = str(datetime.now())

        # Adiciona ao "banco" de dados
        banco[identificador] = {
            'id': identificador,
            'titulo': titulo,
            'conteudo': conteudo,
            'autor': autor,
            'publicado': publicado,
            'data_criacao': data_criacao
        }

        return JsonResponse(banco[identificador])
    else:
        return JsonResponse({"error": "Método não permitido"}, status=405)

def listar_todas_noticias( request):
    return JsonResponse(banco)



   