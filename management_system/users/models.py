from django.contrib.auth.models import User
from django.db import models


class Worker(models.Model):
    POSITION = (
        ('operator', 'Operator'),
        ('manager', 'Manager'),
        ('mechanic', 'Mechanic'),
        ('welder', 'Welder'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(choices=POSITION, blank=False)
    image = models.ImageField(default='media/profile.gif')