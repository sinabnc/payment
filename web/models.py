from django.db import models

# Create your models here.
class Card(models.Model):
    card_number = models.IntegerField()
    cvv = models.IntegerField()
    ex = models.TextField(max_length=33)
