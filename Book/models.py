
from django.db import models

# Create your models here.

class Book(models.Model):
    Name = models.CharField(max_length=100)
    price = models.IntegerField()
    qynt = models.IntegerField()


    class Meta:
        db_table = 'Ebook'

    def __str__(self):
        return self.Name
