from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    title = models.CharField(blank=False, null=False, max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + "-" +self.user