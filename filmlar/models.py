from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
class Film(models.Model):
    nomi = models.CharField(max_length=500)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    yoshChegarasi = models.CharField(max_length=500)
    film_joylashuvi = models.FileField(upload_to='tvlar/')
    yili = models.CharField(max_length=500)
    malumot = models.TextField()
    rasmi = models.ImageField(upload_to='film-rasmlar')

    def __str__(self):
        return self.nomi