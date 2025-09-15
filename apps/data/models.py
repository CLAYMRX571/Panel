from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=250)
    more_name = models.CharField(max_length=50)
    desc = models.TextField()
    image = models.ImageField(upload_to='data', blank=True, null=True)
    title = models.CharField(max_length=50)
    title_desc = models.TextField()
    file = models.FileField(upload_to='pdf', blank=True, null=True)
    file_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Related(models.Model):
    relate_name = models.CharField(max_length=200)
    relate_more = models.CharField(max_length=100)
    relate_image = models.ImageField(upload_to='relate', blank=True, null=True)
    relate_title = models.CharField(max_length=100)

    def __str__(self):
        return self.relate_name


