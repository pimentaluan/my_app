from django.contrib import admin

from edu.models import Autor, Livro, Editora

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    
@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn', 'titulo', 'publicado', 'preco', 'estoque', 'editora')

@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')