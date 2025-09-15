from django.db import models

class News(models.Model):
    category_name = models.CharField(max_length=50)
    all_name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    date = models.IntegerField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)

    def __str__(self):
        return self.name
    
    def __str__(self):
        return self.date.strftime("%d-%m-%y")    
    
class NewsAdver(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    button_name = models.CharField(max_length=50)
    desc = models.TextField()

    def __str__(self):
        return self.name
