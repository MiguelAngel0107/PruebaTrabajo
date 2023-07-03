from django.db import models


class ConfigVariable(models.Model):
    name_config = models.CharField(max_length=150, unique=True)

    days_maduration = models.PositiveIntegerField()
    days_reproduction = models.PositiveIntegerField()
    number_divisions = models.PositiveIntegerField()


class Lote(models.Model):
    id_lote = models.CharField()
    id_collection = models.CharField(max_length=999)
    nivel_iter = models.CharField(max_length=4)
    array = models.JSONField()
    status = models.BooleanField(default=False)
    size = models.PositiveBigIntegerField(default=0)
    size_end = models.PositiveBigIntegerField(default=0)
