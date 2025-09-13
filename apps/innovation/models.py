from django.db import models

class Inno(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='inno', blank=True, null=True)

    def __str__(self):
        return self.name