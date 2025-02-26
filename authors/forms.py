from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'photo']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'photo': 'Foto do Autor'
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sobrenome'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'})
        }
