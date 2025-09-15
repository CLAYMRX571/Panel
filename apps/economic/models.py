from django.db import models

class Eco(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    eco_desc = models.TextField()
    image = models.ImageField(upload_to='eco', blank=True, null=True)

    def __str__(self):
        return self.name
    
