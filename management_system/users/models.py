from django.contrib.auth.models import User
from django.db import models


class Staff_member(models.Model):
    POSITION = (
        ('operator', 'Operator'),
        ('manager', 'Manager'),
        ('mechanic', 'Mechanic'),
        ('welder', 'Welder'),
        ('other', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(choices=POSITION, max_length=100, blank=True)
    image = models.ImageField(default='media/profile_pictures/default.gif', upload_to='media/profile_pictures')