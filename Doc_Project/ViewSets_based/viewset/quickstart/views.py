from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet


from .models import Snippet
from .serializer import SnippetModelSerializer

# Create your views here.


class SnippetViewSet(ModelViewSet):
    serializer_class = SnippetModelSerializer
    queryset = Snippet.objects.all()

