from django.db import models

class Employ(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='employ', blank=True, null=True)
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=200)
    value_image = models.ImageField(upload_to='value', blank=True, null=True)
    value_name = models.CharField(max_length=100)
    value_desc = models.TextField()
    strategy_name = models.CharField(max_length=255)
    strategy_title = models.CharField(max_length=100)
    strategy_desc = models.TextField()
    file = models.FileField(upload_to='pdf/', verbose_name="files")

    def __str__(self):
        return self.name


