from django.db import models

class Education(models.Model):
    name = models.CharField(max_length=200)
    see_more = models.CharField(max_length=50)
    category_name = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='technical', blank=True, null=True)
    edu_name = models.CharField(max_length=200)
    edu_desc = models.TextField()
    
    def __str__(self):
        return self.name
    
