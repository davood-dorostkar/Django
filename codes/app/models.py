from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/")
    upload_date = models.DateTimeField(auto_now_add=True)