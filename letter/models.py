from django.db import models

# Create your models here.
class Letter(models.Model):
    title = models.CharField(max_length=100)
    write = models.CharField(max_length=100)
    send = models.CharField(max_length=100)
    contents = models.TextField(blank=True)
    complete = models.BooleanField(default=False)

    def __str__(selfs):
        return self.title