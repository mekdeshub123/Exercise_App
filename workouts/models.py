from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=200)#tpe of workout
    focus = models.CharField(max_length=200)#workout goal
    like = models.BooleanField()#
    video_id = models.CharField(max_length=100)#youtube video ID

    def __str__(self):
        return f'{self.name}{self.focus}{self.like}{self.video_id}'
        
