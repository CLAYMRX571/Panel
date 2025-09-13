from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    file = models.ImageField(upload_to='project', blank=True, null=True)
    project_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pro', blank=True, null=True)

    def __str__(self):
        return self.name