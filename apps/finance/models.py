from django.db import models

class Finance(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    image = models.ImageField(upload_to='finance', blank=True, null=True)
    finance_desc = models.TextField()

    def __str__(self):
        return self.name
    

