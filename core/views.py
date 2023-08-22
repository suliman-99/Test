from rest_framework.generics import CreateAPIView
from core.serializers import *
from Q10 import check_sentence_meaning
from Q11 import compare_and_visualize_drawing_similarity


class Q10View(CreateAPIView):
    serializer_class = Q10Serializer()
    def create(self, request, *args, **kwargs):
        return check_sentence_meaning(request.data.get('sentence'))


class Q11View(CreateAPIView):
    serializer_class = Q11Serializer()
    def create(self, request, *args, **kwargs):
        fake = super().create(request, *args, **kwargs)
        return compare_and_visualize_drawing_similarity(fake.image.url)



