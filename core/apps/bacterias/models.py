from django.db import models

class ConfigVariable(models.Model):
    name_config = models.CharField(max_length=150, unique=True)

    days_maduration = models.PositiveIntegerField()
    days_reproduction = models.PositiveIntegerField()
    number_divisions = models.PositiveIntegerField()