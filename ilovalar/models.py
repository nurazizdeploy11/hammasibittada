from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
class Ilova(models.Model):
    rasm = models.ImageField(upload_to='ilova-rasmlar')
    title = models.CharField(max_length=500)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    apk = models.FileField(upload_to='apk/')

    def __str__(self):
        return self.title