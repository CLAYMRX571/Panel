from django.db import models

class Membership(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    date = models.IntegerField()
    members_title = models.CharField(max_length=50)
    country_name = models.CharField(max_length=200)
    disclaimer_name = models.CharField(max_length=50)
    disclaimer_desc = models.TextField()

    def __str__(self):
        return self.name
