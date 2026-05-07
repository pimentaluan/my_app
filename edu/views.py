from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AutorForm, EditoraForm, LivroForm
from .models import Autor, Editora, Livro

@login_required
def livro_create(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_livros')
    else:
        form = LivroForm()
    return render(request, 'edu/cadastro_livro.html', {'form': form})

def editora_create(request):
    if request.method == 'POST':
        form = EditoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_editoras')
    else:
        form = EditoraForm()
    return render(request, 'edu/cadastro_editora.html', {'form': form})

def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_autores')
    else:
        form = AutorForm()
    return render(request, 'edu/cadastro_autor.html', {'form': form})

@login_required
def edit_livros(request, id):
    livro = get_object_or_404(Livro, id=id)
    if request.method == 'POST':
        form = LivroForm(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('list_livros')
    else:
        form = LivroForm(instance=livro)
    return render(request, 'edu/cadastro_livro.html', {'form': form})

def edit_editoras(request, id):
    editora = get_object_or_404(Editora, id=id)
    if request.method == 'POST':
        form = EditoraForm(request.POST, instance=editora)
        if form.is_valid():
            form.save()
            return redirect('list_editoras')
    else:
        form = EditoraForm(instance=editora)
    return render(request, 'edu/cadastro_editora.html', {'form': form})

def edit_autores(request, id):
    autor = get_object_or_404(Autor, id=id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('list_autores')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'edu/cadastro_autor.html', {'form': form})

def list_livros(request):
    livros = Livro.objects.all().order_by('titulo')
    page = request.GET.get('page', 1)
    paginator = Paginator(livros, 5)  
    try:
        livros = paginator.page(page)
    except PageNotAnInteger:
        livros = paginator.page(1)
    except EmptyPage:
        livros = paginator.page(paginator.num_pages)
        
    return render(request, 'edu/livro_list.html', {'livros': livros})

def list_editoras(request):
    editoras = Editora.objects.all()
    return render(request, 'edu/editora_list.html', {'editoras': editoras})

def list_autores(request):
    autores = Autor.objects.all()
    return render(request, 'edu/autor_list.html', {'autores': autores})
