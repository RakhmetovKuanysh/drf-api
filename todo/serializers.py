from rest_framework import serializers
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task Model
    """
    name = serializers.CharField(required=False)

    class Meta:
        model = Task
        fields = ('id', 'name', 'pub_date', 'done', 'is_active')