from django.db import models

# Create your models here.

class BookData(models.Model):
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=128, default="none")
    description = models.CharField(max_length=2048)
    rating = models.FloatField(max_length=128)
    image = models.ImageField(upload_to="images", default="images/none/notfound.jpg")
