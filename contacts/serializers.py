from rest_framework import serializers
from .models import *


class ContactSerializer(serializers.ModelSerializer):
    """
    Serializer for Contact Model
    """
    class Meta:
        model = Contact
        fields = ('id', 'name', 'surname', 'phone_num', 'pub_date',
            'description', 'is_active')
        extra_kwargs = {
            'name': {'required': False},
            'surname': {'required': False},
            'phone_num': {'required': False},
            'description': {'required': False},
        }