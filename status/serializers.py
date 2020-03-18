from rest_framework import serializers
from .models import Status


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'content', 'image', 'user')
        extra_kwargs = {'user': {'read_only': True}}


