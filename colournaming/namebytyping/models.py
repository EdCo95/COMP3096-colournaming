from __future__ import unicode_literals

from django.db import models

class Response(models.Model):

    def __str__(self):
        return self.colour_name
        
    colour_name = models.CharField(max_length = 200)
    image_number = models.IntegerField(default = -1)
