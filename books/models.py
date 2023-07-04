from django.db import models

# Create your models here.

class Author(models.Model):
    def __str__(self):
          return self.name

    name = models.CharField(max_length=55)
    created = models.DateTimeField('olusturuldu')

class Book(models.Model):
        def __str__(self):
          return self.name
         
        name = models.CharField(max_length=60)
        created = models.DateTimeField('olusturuldu')
        author =  models.ForeignKey(Author,on_delete=models.CASCADE)
        price = models.DecimalField(decimal_places=2,max_digits=4,null=True)