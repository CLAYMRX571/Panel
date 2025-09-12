from django.db import models

class Data(models.Model):
    name = models.CharField(max_length=250)
    desc = models.TextField()
    title = models.CharField(max_length=50)
    title_desc = models.TextField()
    image = models.ImageField(upload_to='data', blank=True, null=True)
    file = models.CharField(max_length=50)
    relate = models.CharField(max_length=100)
    relate_link = models.CharField(max_length=100)
    relate_desc = models.TextField()
    relate_image = models.ImageField(upload_to='relate', blank=True, null=True)

    def __str__(self):
        return self.name
