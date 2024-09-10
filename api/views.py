
from django.http import JsonResponse
import uuid
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import json

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

        return JsonResponse(banco[identificador], status=201)
    else:
        return JsonResponse({"error": "Método não permitido"}, status=405)

def listar_todas_noticias( request):
    return JsonResponse(banco)

@csrf_exempt
def editar_noticia(request):
    if request.method == "PUT":
        dados = json.loads(request.body)

        
        # Extrai os dados do request
        identificador = dados.get('id')
        titulo = dados.get('titulo')
        conteudo = dados.get('conteudo')
        publicado = dados.get('publicado') 
        autor = dados.get('autor')

        # Verifica se a notícia existe
        if identificador in banco:
            # Atualiza a notícia existente
            banco[identificador].update({
                'titulo': titulo,
                'conteudo': conteudo,
                'autor': autor,
                'publicado': publicado,
                'data_criacao': banco[identificador]['data_criacao']  # Mantém a data de criação original
            })
            return JsonResponse(banco[identificador])
        else:
            return JsonResponse({"error": "Notícia não encontrada"}, status=404)
    else:
        return JsonResponse({"error": "Método não permitido"}, status=405)

@csrf_exempt
def remover_noticia(request):
    if request.method == "DELETE":
        # Extrai dados do corpo da requisição JSON
        dados = json.loads(request.body)
        identificador = dados.get('id')

        # Verifica se a notícia existe
        if identificador in banco:
            # Remove a notícia
            del banco[identificador]
            return JsonResponse({"message": "Notícia removida com sucesso"})
        else:
            return JsonResponse({"error": "Notícia não encontrada"}, status=404)
    else:
        return JsonResponse({"error": "Método não permitido"}, status=405)

@csrf_exempt
def listar_noticia(request, identificador):
    if request.method == "GET":
        # Verifica se a notícia existe
        if identificador in banco:
            # Retorna a notícia
            return JsonResponse(banco[identificador])
        else:
            return JsonResponse({"error": "Notícia não encontrada"}, status=404)
    else:
        return JsonResponse({"error": "Método não permitido"}, status=405)

   