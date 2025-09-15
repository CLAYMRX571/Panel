from django.db import models

class Part(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.name
