from django.contrib.auth.models import User
from django.db import models


class Information(models.Model):

    STATUS = (
        ('normal', 'Normal'),
        ('important', 'Important'),
    )
    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    text = models.TextField(blank=False)
    date = models.DateField(auto_now_add=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS, default='normal')

    class Meta:
        ordering = ('date',)
    
    def __str__(self):
        return self.title

    