from django.db import models

class About(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    adverb_desc = models.TextField()
    adverb_more = models.CharField(max_length=50)

    def __str__(self):
        return self.name
