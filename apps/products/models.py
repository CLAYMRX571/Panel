from django.db import models

class Indexs(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    about_name = models.CharField(max_length=255)
    about_desc = models.TextField()
    service_name = models.CharField(max_length=255)
    service_desc = models.TextField()
    service_image = models.ImageField(upload_to='services', blank=True, null=True)
    project_name = models.CharField(max_length=255)
    project_desc = models.TextField()
    project_image = models.ImageField(upload_to='projects', blank=True, null=True)
    project_link = models.URLField(verbose_name='url', blank=True, null=True)
    team_name = models.CharField(max_length=255)
    team_jobs = models.CharField(max_length=100)
    team_image = models.ImageField(upload_to='teams', blank=True, null=True)
    telegram = models.URLField(verbose_name='telegram', blank=True, null=True)
    linkedin = models.URLField(verbose_name='linkedin', blank=True, null=True)
    insta = models.URLField(verbose_name='insta', blank=True, null=True)
    custom_count = models.BigIntegerField(default=1)
    project_count = models.BigIntegerField(default=1)
    win_count = models.BigIntegerField(default=1)
    works_count = models.BigIntegerField(default=1)

    def __str__(self):
        return self.name