from dataclasses import field
from rest_framework import serializers
from vocs import models

class VocSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','vocabulary','hant']
            
        model = models.Voc