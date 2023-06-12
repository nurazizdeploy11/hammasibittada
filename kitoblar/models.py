from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
class Kitob(models.Model):
    rasm = models.ImageField(upload_to='ilova-rasmlar')
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    pdf = models.FileField(upload_to='pdf/')

    def __str__(self):
        return self.title