from datetime import datetime
from django import forms
from .models import Book, Author


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

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['author'].queryset = Author.objects.all().order_by('first_name')

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.strip() == '':
            raise forms.ValidationError('O título não pode ser vazio ou somente espaços em branco')
        return title
    
    def clean_genre(self):
        genre = self.cleaned_data.get('genre')
        if any(char.isdigit() for char in genre):
            raise forms.ValidationError('O gênero não pode conter números')
        if genre.strip() == '':
            raise forms.ValidationError('O gênero não pode ser vazio ou somente espaços em branco')
        return genre
    
    def clean_year(self):
        actual_year = datetime.now().year
        year = self.cleaned_data.get('year')
        if year.strip() == '':
            raise forms.ValidationError('O ano de publicação não pode ser vazio ou somente espaços em branco')
        if not year.isdigit():
            raise forms.ValidationError('O ano de publicação deve conter somente números')
        if int(year) > actual_year:
            raise forms.ValidationError('O ano de publicação não pode ser maior que o ano atual')
        return year