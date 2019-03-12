from django.db import models
from django.urls import reverse

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    jerseyNumber = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'player_id': self.id})