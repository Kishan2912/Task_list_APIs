from django.db import models 

# Create your models here.

# Task model
class Task(models.Model):
    # fields of the model
    title = models.CharField(max_length=100, blank=False)  # task's title
    is_completed = models.BooleanField(default=False) # task's completion status

    # renames the instances of the model with their title name
    def __str__(self):
        return self.title