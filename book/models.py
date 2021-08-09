from django.db import models

class Books(models.Model):

    name = models.CharField(max_length = 500, default = 'name')
