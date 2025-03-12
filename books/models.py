from django.db import models
from authors.models import Author
from PIL import Image
import os

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)



    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # salva a imagem original

        if self.cover_image:
            img_path = self.cover_image.path
            img = Image.open(img_path)

            # Define o tamanho máximo para a miniatura
            max_size = (200, 250)  
            img.thumbnail(max_size)  # Redimensiona mantendo a proporção
            
            img.save(img_path, format="JPEG", quality=80)  # Salva a imagem otimizada

    def __str__(self):
        return self.title