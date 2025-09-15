from django.db import models

class Outlook(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='outlook', blank=True, null=True)
    focus_name = models.CharField(max_length=100)
    focus_desc = models.TextField()
    file = models.FileField(upload_to='pdf', blank=True, null=True)
    
    def __str__(self):
        return self.name
