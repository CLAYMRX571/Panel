from django.db import models

class Policy(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='policy', blank=True, null=True)
    policy_desc = models.TextField()

    def __str__(self):
        return self.name
