from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    team_name = models.CharField(max_length=100)
    sap_id=models.CharField(max_length=20)
    branch=models.CharField(max_length=20)
    year=models.CharField(max_length=20)
    def __str__(self):
        return self.team_name


