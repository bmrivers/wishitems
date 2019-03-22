from django.db import models

# Create your models here.
# only one model

class Item(models.Model):
    description = models.TextField(max_length=100)