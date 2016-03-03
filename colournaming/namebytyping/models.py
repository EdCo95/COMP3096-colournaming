from __future__ import unicode_literals
import psycopg2
from django.db import models
from datetime import datetime

class Image(models.Model):
    url = models.CharField(max_length=200, null=True)
    path = models.FilePathField(path='.')
    width = models.IntegerField(default=0)
    height = models.IntegerField(default=0)

class Patch(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=True)
    radius = models.IntegerField(default=20)
    position_x = models.IntegerField(default=0)
    position_y = models.IntegerField(default=0)

class User(models.Model):
    FEMALE = 0
    MALE = 1
    NO_SAY = -1
    WILLING_TO_SPEAK = 1
    UNWILLING_TO_SPEAK = 0
    age = models.IntegerField(default=0)
    gender = models.IntegerField(default=0, choices=((FEMALE, 'female'), (MALE, 'male'), (NO_SAY, 'no_say')))
    nationality = models.CharField(max_length=200)
    willing_to_speak = models.IntegerField(default=0, choices=((WILLING_TO_SPEAK, 'willing_to_speak'), (UNWILLING_TO_SPEAK, 'unwilling_to_speak')))
    test_type = models.CharField(max_length=200, default="n/a")

class Response(models.Model):

    def __str__(self):
        string = "[" + self.colour_name + ", " + str(self.image_number) + "]"
        return string

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    colour_name = models.CharField(max_length=200)
    image_number = models.IntegerField(default=-1)
    # datetime = models.DateTimeField(default=datetime.now())
    input_type = models.IntegerField(default=0, choices=((0, 'spoken'), (1, 'typed')))

class Time(models.Model):

    def __str__(self):
        string = "Total time taken for 100 images: " + str(self.time_elapsed)
        return string

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    time_elapsed = models.IntegerField(default = -1)
