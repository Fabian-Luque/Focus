from django.db import models
from django.utils import timezone
from django.conf import settings
import datetime
# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField(default=timezone.now)
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return self.name

    def was_published_rencetly(self):
        return self.date >= timezone.now() - datetime.timedelta(days=1) 