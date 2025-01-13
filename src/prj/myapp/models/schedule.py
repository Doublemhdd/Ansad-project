from django.db import models

# Create your models here.
from .module import Module

class Schedule(models.Model):
    plage = models.CharField(max_length=2)
    semestre = models.CharField(max_length=2)
    day =  models.CharField(max_length=3)
    date = models.DateField()
    name = models.CharField(max_length=256)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    class Meta:
        unique_together = (('plage', 'semestre', 'day'),)

    def __str__(self):
        return str(self.semestre) + ' --- ' + str(self.day) + ' --- ' + str(self.plage)