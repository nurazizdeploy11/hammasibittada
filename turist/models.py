from django.db import models

# Create your models here.
class Manzil(models.Model):
    name = models.CharField(max_length=500)
    joylashuv = models.CharField(max_length=500)
    vidio = models.FileField(upload_to='manzil-vidios/')

    def __str__(self):
        return self.name