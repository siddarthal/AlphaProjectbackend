from django.db import models
from accounts.models import CustomUser

class Event(models.Model):
    EID = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    location = models.CharField(max_length=255)
    time = models.TimeField()
    require_volunteers = models.BooleanField(default=False)
    poster = models.ImageField(upload_to='event_posters/', null=True, blank=True)
    ticket_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.event_name

