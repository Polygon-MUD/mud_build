from django.db import models

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=500, default="DEFAULT ITEM")
  description = models.CharField(max_length=500, default="DEFAULT DESC")
  value = models.IntegerField(default=0)