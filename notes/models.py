from django.db import models


class Note(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=50)


