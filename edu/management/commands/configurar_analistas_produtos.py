from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand

from edu.models import Livro


GROUP_NAME = 'Analistas de cadastro de produtos'
TEST_USERS = (
    ('analista1', 'senha12345', True, True),
    ('analista2', 'senha12345', True, True),
    ('apoio1', 'senha12345', False, True),
    ('visitante1', 'senha12345', False, False),
)


class Command(BaseCommand):
    help = 'Cria o grupo de analistas de cadastro de produtos e usuarios de teste.'

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Livro)
        permissions = Permission.objects.filter(
            content_type=content_type,
            codename__in=('add_livro', 'change_livro', 'delete_livro'),
        )

        group, created = Group.objects.get_or_create(name=GROUP_NAME)
        group.permissions.set(permissions)

        if created:
            self.stdout.write(self.style.SUCCESS(f'Grupo "{GROUP_NAME}" criado.'))
        else:
            self.stdout.write(self.style.WARNING(f'Grupo "{GROUP_NAME}" ja existia e foi atualizado.'))

        for username, password, is_analyst, is_staff in TEST_USERS:
            user, user_created = User.objects.get_or_create(username=username)
            user.is_staff = is_staff
            user.set_password(password)
            user.save()

            if is_analyst:
                user.groups.add(group)
                role = 'analista'
            else:
                user.groups.remove(group)
                role = 'nao analista'

            status = 'criado' if user_created else 'reutilizado'
            self.stdout.write(
                self.style.SUCCESS(
                    f'Usuario "{username}" ({role}, staff={is_staff}) {status}. Senha: {password}'
                )
            )
