from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/', width_field='width', height_field='height')
    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)
