from django.db import models

class Events(models.Model):
    name = models.CharField(max_length=25)
    date = models.IntegerField()
    location = models.CharField(max_length=200)
    title = models.CharField()

    def __str__(self):
        return self.name
    
    def __str_(self):
        return self.date.strftime("%d-%m")

class Elent(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='events', blank=True, null=True)

    def __str__(self):
        return self.name