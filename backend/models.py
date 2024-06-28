from django.db import models

# Create your models here.

class Number(models.Model):
    number = models.IntegerField()
    letter = models.CharField()

class Pokemon(models.Model):
    pokedex_number = models.IntegerField(primary_key=True) #ahora es la llave primaria
    name = models.CharField(max_length=20)
    primary_type = models.CharField(max_length=15)
    secondary_type = models.CharField(max_length=15, null=True, blank=True)
    image_url = models.URLField(max_length=200, default='') #url de la imagen pokemon

