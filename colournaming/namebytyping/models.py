from __future__ import unicode_literals

from django.db import models

class Response(models.Model):

    def __str__(self):
        string = "[" + self.colour_name + ", " + str(self.image_number) + "]"
        return string

    colour_name = models.CharField(max_length = 200)
    image_number = models.IntegerField(default = -1)
