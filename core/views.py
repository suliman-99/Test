from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from core.serializers import *


class Q10View(CreateAPIView):
    serializer_class = Q10Serializer


class Q11View(CreateAPIView):
    serializer_class = Q11Serializer

