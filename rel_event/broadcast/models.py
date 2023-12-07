# broadcast/models.py
from django.db import models
from events.models import Event

class Broadcast(models.Model):
    BID = models.AutoField(primary_key=True)
    event = models.OneToOneField(Event, on_delete=models.CASCADE)
    broadcast_name = models.CharField(max_length=255)

    def __str__(self):
        return self.broadcast_name
