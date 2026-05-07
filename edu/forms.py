from django import forms
from .models import Autor, Editora, Livro

class LivroForm(forms.ModelForm):
    autores = forms.ModelMultipleChoiceField(
        queryset=Autor.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Livro
        fields = ['isbn', 'titulo', 'publicado', 'preco', 'estoque', 'editora']
        widgets = {
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'publicado': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'estoque': forms.NumberInput(attrs={'class': 'form-control'}),
            'editora': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['autores'].initial = Autor.objects.filter(livros=self.instance)

    def save(self, commit=True):
        livro = super().save(commit=commit)
        if commit:
            autores = self.cleaned_data['autores']
            for autor in Autor.objects.filter(livros=livro).exclude(pk__in=autores.values_list('pk', flat=True)):
                autor.livros.remove(livro)
            for autor in autores:
                autor.livros.add(livro)
        return livro

class EditoraForm(forms.ModelForm):
    class Meta:
        model = Editora
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
        }
    
class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'})
        }
