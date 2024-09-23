from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Noticia


class NoticiaAPITestCase(APITestCase):

    def setUp(self):
        # Criar uma notícia para os testes
        self.noticia = Noticia.objects.create(
            titulo="Notícia de Teste",
            conteudo="Conteúdo de teste",
            publicado=True,
            autor="Autor Teste"
        )
        self.noticia_url = reverse('noticia-detail', args=[self.noticia.id])
        self.list_url = reverse('noticia-list')

    def test_listar_todas_noticias(self):
        """Testa o endpoint GET /noticias/"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_obter_uma_noticia(self):
        """Testa o endpoint GET /noticias/:id/"""
        response = self.client.get(self.noticia_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], "Notícia de Teste")

    def test_criar_nova_noticia(self):
        """Testa o endpoint POST /noticias/"""
        data = {
            "titulo": "Nova Notícia",
            "conteudo": "Conteúdo da nova notícia",
            "publicado": False,
            "autor": "Novo Autor"
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titulo'], "Nova Notícia")

    def test_atualizar_noticia(self):
        """Testa o endpoint PUT /noticias/:id/"""
        data = {
            "titulo": "Notícia Atualizada",
            "conteudo": "Conteúdo atualizado",
            "publicado": False,
            "autor": "Autor Atualizado"
        }
        response = self.client.put(self.noticia_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['titulo'], "Notícia Atualizada")

    def test_remover_noticia(self):
        """Testa o endpoint DELETE /noticias/:id/"""
        response = self.client.delete(self.noticia_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Noticia.objects.filter(id=self.noticia.id).exists())
