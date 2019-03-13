from django.db import models
from django.urls import reverse
from datetime import date

STATUS = (
    ('a', 'Active'),
    ('i', 'Injured'),
    ('r', 'Rest')
)


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

class Healing(models.Model):
    date = models.DateField('Status date')
    status = models.CharField(max_length=1, choices=STATUS, default=STATUS[0][0])

    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_status_display()} on {self.date}"

    class Meta:
        ordering = ['-date']