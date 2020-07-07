from django.urls import path
from .views import SnippetList, SnippetDetail

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('',SnippetList.as_view() , name='list'),
    path('detail/<int:pk>/', SnippetDetail.as_view(), name='details')
]

urlpatterns = format_suffix_patterns(urlpatterns)