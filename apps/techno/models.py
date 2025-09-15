from django.db import models

class Techno(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='techno', blank=True, null=True)
    techno_desc = models.TextField()

    def __str__(self):
        return self.name