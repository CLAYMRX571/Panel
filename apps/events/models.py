from django.db import models

class Events(models.Model):
    name = models.CharField(max_length=25)
    title = models.CharField(max_length=50)
    date = models.DateTimeField()
    date_year = models.DateTimeField()
    events_name = models.CharField(max_length=200)
    events_desc = models.TextField()
    image = models.ImageField(upload_to='events', blank=True, null=True)

    def __str__(self):
        return self.name
