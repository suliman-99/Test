from rest_framework import serializers
from core.models import *
from Q10 import check_sentence_meaning
from Q11 import compare_and_visualize_drawing_similarity

class Q10Serializer(serializers.Serializer):
    sentence = serializers.CharField()

    def validate(self, attrs):
        return {"data": check_sentence_meaning(attrs.get('sentence'))}


class Q11Serializer(serializers.Serializer):
    image = serializers.CharField()

    def validate(self, attrs):
        return {"data": compare_and_visualize_drawing_similarity(attrs.get('image'))}

