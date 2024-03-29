from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    date = models.DateTimeField()

    def __str__(self):
        return self.title
