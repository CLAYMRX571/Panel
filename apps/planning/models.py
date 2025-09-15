from django.db import models

class Plan(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='plan', blank=True, null=True)
    long_desc = models.TextField()

    def __str__(self):
        return self.name
    
    
