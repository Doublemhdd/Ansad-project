from django.db import models

# Create your models here.

class Module(models.Model):
    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=256)
    cm_hours = models.FloatField()
    td_hours = models.FloatField()
    tp_hours = models.FloatField()

    def __str__(self):
        return str(self.code) + ' --- ' + str(self.name)