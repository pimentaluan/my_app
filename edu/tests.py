from datetime import date

from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.test import Client, TestCase
from django.urls import reverse

from .models import Editora, Livro


class LivroPermissionTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.editora = Editora.objects.create(id=1, nome='Editora Central')
        self.livro = Livro.objects.create(
            id=1,
            isbn='1234567890123',
            titulo='Django Essencial',
            publicado=date(2024, 1, 10),
            preco='79.90',
            estoque=8,
            editora=self.editora,
        )

        self.group = Group.objects.create(name='Analistas de cadastro de produtos')
        content_type = ContentType.objects.get_for_model(Livro)
        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=('add_livro', 'change_livro', 'delete_livro'),
        )
        self.group.permissions.set(permissions)

        self.analista = User.objects.create_user(username='analista', password='senha12345')
        self.analista.groups.add(self.group)

        self.comum = User.objects.create_user(username='comum', password='senha12345')

    def test_lista_esconde_acoes_de_usuario_sem_permissao(self):
        self.client.login(username='comum', password='senha12345')
        response = self.client.get(reverse('list_livros'))

        self.assertContains(response, 'Bloqueado')
        self.assertNotContains(response, 'Novo livro')
        self.assertNotContains(response, 'Remover')

    def test_analista_consegue_acessar_tela_de_cadastro(self):
        self.client.login(username='analista', password='senha12345')
        response = self.client.get(reverse('livro_create'))

        self.assertEqual(response.status_code, 200)

    def test_usuario_sem_permissao_recebe_403_ao_tentar_editar(self):
        self.client.login(username='comum', password='senha12345')
        response = self.client.get(reverse('edit_livros', args=[self.livro.id]))

        self.assertEqual(response.status_code, 403)

    def test_analista_consegue_remover_livro(self):
        self.client.login(username='analista', password='senha12345')
        response = self.client.post(reverse('delete_livros', args=[self.livro.id]))

        self.assertRedirects(response, reverse('list_livros'))
        self.assertFalse(Livro.objects.filter(id=self.livro.id).exists())
