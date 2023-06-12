from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Darslar(models.Model):
    name = models.CharField(max_length=500)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    vidio = models.FileField(upload_to='darslar/')

    def __str__(self):
        return self.name
    