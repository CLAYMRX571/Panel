from django.db import models

class Home(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='itm/', blank=True, null=True)
    desc = models.TextField()
    button_name = models.CharField(max_length=100)
    abouts_button = models.CharField(max_length=100)
    more_button = models.CharField(max_length=100)
    support_desc = models.TextField()
    members = models.BigIntegerField(default=0)
    country_number = models.BigIntegerField(default=0)
    search_name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class News(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='news')
    title = models.TextField()
    desc = models.TextField()
    image = models.ImageField(upload_to='news/', blank=True, null=True)
    date = models.DateField()
    tag = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%d %B %Y')})"
    
class Publication(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='publications')
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='public/', blank=True, null=True)
    title = models.CharField(max_length=100)
    date = models.DateField()
    meta = models.CharField(max_length=50)
    view = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%B %Y')})"
    
class Event(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='events')
    title = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} - {self.location} ({self.date.strftime('%d %B')})"
    
class Video(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=50)
    desc = models.TextField()
    author = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    more = models.CharField(max_length=50)

    def __str__(self):
        return self.title

