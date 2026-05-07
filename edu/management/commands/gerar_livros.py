from django.core.management.base import BaseCommand
from edu.models import Livro, Editora
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Comando para gerar 100 registros de livros' 

    def handle(self, *args, **options): 
        fake = Faker()
        lista_editoras = list(Editora.objects.values_list('id', flat=True))
        if not lista_editoras:
            proximo_id_editora = (Editora.objects.order_by('-id').values_list('id', flat=True).first() or 0) + 1
            for indice in range(5):
                Editora.objects.create(
                    id=proximo_id_editora + indice,
                    nome=fake.company()[:100]
                )
            lista_editoras = list(Editora.objects.values_list('id', flat=True))
            self.stdout.write(self.style.WARNING('Nenhuma editora cadastrada. Editoras de exemplo foram criadas automaticamente.'))

        proximo_id_livro = (Livro.objects.order_by('-id').values_list('id', flat=True).first() or 0) + 1
        for i in range(100): 
            Livro.objects.create(
                id=proximo_id_livro + i,
                titulo=fake.sentence(nb_words=3)[:20], 
                isbn=fake.isbn13(),
                publicado=fake.date_this_century(),
                preco=random.uniform(20.0, 150.0),     
                estoque=random.randint(1, 50),        
                editora=Editora.objects.get(id=random.choice(lista_editoras))
            )

        self.stdout.write(self.style.SUCCESS('Livros criados com sucesso!'))
