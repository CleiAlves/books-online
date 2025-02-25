from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='authors/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'