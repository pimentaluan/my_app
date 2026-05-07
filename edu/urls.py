from django.urls import path

from . import views

urlpatterns = [
    path('livros/', views.list_livros, name='list_livros'),
    path('livros/novo/', views.livro_create, name='livro_create'),
    path('livros/<int:id>/editar/', views.edit_livros, name='edit_livros'),
    path('editoras/', views.list_editoras, name='list_editoras'),
    path('editoras/nova/', views.editora_create, name='editora_create'),
    path('editoras/<int:id>/editar/', views.edit_editoras, name='edit_editoras'),
    path('autores/', views.list_autores, name='list_autores'),
    path('autores/novo/', views.autor_create, name='autor_create'),
    path('autores/<int:id>/editar/', views.edit_autores, name='edit_autores'),
]
