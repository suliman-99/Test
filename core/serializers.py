from rest_framework import serializers
from core.models import *
from Q10 import check_sentence_meaning
from Q11 import compare_and_visualize_drawing_similarity

class Q10Serializer(serializers.Serializer):
    sentence = serializers.CharField()

    def create(self, request, *args, **kwargs):
        return {"data": check_sentence_meaning(request.data.get('sentence'))}


class Q11Serializer(serializers.ModelSerializer):
    class Meta:
        model = Fake
        fields = ['image']

    def create(self, validated_data):
        fake = super().create(validated_data)
        return {"data": compare_and_visualize_drawing_similarity(fake.image.url)}

