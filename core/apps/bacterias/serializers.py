from rest_framework import serializers
from .models import ConfigVariable

class ConfigVariableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigVariable
        fields = '__all__'