from rest_framework import serializers
from core.models import *

class Q10Serializer(serializers.Serializer):
    sentence = serializers.CharField()


class Q11Serializer(serializers.ModelSerializer):
    class Meta:
        model = Fake
        fields = ['image']

