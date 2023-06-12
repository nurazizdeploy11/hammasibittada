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
class Music(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    musiqa = models.FileField(upload_to='music/')
    def __str__(self):
        return self.title