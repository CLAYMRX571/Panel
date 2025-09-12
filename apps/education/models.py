from django.db import models

class Education(models.Model):
    name = models.CharField(max_length=200)
    category_name = models.CharField(max_length=50)
    desc = models.TextField()
    technical_name = models.CharField(max_length=200)
    technical_desc = models.TextField()
    technical_image = models.ImageField(upload_to='technical', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
