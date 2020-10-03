from django.contrib.auth.models import User
from django.db import models


class Information(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False)
    text = models.TextField(blank=False)
    date = models.DateField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
