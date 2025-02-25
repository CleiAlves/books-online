from django.db import models
from authors.models import Author

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=50)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)


    def __str__(self):
        return self.title