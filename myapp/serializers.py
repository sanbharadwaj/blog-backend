from rest_framework import serializers
from .models import DummyData

class DummyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DummyData
        fields = ['column1', 'column2', 'column3', 'column4']