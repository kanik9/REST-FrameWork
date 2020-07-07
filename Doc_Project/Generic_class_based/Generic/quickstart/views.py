from django.shortcuts import render


from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, UpdateModelMixin, RetrieveModelMixin,DestroyModelMixin ,CreateModelMixin



from .models import Snippet
from .serializer import SnippetModelSerializer

# Create your views here.

class SnippetGenericAPIViewList(GenericAPIView, ListModelMixin,  CreateModelMixin):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetGenericAPIViewDetail(GenericAPIView, UpdateModelMixin, RetrieveModelMixin , DestroyModelMixin):
    queryset = Snippet.objects.all()
    serializer_class = SnippetModelSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

