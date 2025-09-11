from django.db import models

class News(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    links_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    title_link = models.CharField(max_length=50)
    image = models.ImageField(upload_to='news/', blank=True, null=True)

    def __str__(self):
        return self.name
    
