# announcements/models.py
from django.db import models
from broadcast.models import Broadcast

class Announcement(models.Model):
    AID = models.AutoField(primary_key=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    broadcast = models.ForeignKey(Broadcast, on_delete=models.CASCADE)

    def __str__(self):
        return f"Announcement {self.AID} for {self.broadcast.event.event_name}"
