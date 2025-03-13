from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'year', 'genre', 'cover_image', 'synopsis']
        labels = {
            'title': 'Título',
            'author': 'Autor',
            'year': 'Publicação',
            'genre': 'Gênero',
            'cover_image': 'Capa do Livro',
            'synopsis': 'Sinopse'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ano de Publicação'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gênero'}),
            'cover_image': forms.FileInput(attrs={'class': 'form-control'}),
            'synopsis': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Sinopse'})
        }