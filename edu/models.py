from django.db import models

class Autor(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    livros = models.ManyToManyField('Livro')
    
    def __str__(self):
        return self.nome

class Livro(models.Model):
    id = models.IntegerField(primary_key=True)
    isbn = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=20)
    publicado = models.DateField()
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()
    editora = models.ForeignKey('Editora', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo
    
class Editora(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    