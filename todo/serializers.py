from rest_framework import serializers
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task Model
    """
    class Meta:
        model = Task
        fields = ('id', 'name', 'pub_date', 'done', 'is_active')
        extra_kwargs = {'name': {'required': False}}