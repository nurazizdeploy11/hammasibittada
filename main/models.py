from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=500)
    tel = models.CharField(max_length=500)
    text = models.TextField()

    def __str__(self) -> str:
        return self.name