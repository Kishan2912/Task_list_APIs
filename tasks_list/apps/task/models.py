from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, blank=False) 
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title