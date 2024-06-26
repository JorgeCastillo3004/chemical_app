from django.contrib.auth.models import User
from django.db import models

class TimeDeltaData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    delta_time = models.DurationField()

    def __str__(self):
        return f"{self.user.username} - {self.date}"
