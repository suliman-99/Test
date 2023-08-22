from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from core.serializers import *


class Q10View(CreateAPIView):
    serializer_class = Q10Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)


class Q11View(CreateAPIView):
    serializer_class = Q11Serializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data)

