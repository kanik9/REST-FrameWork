from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import SnippetGenericAPIViewList ,SnippetGenericAPIViewDetail

urlpatterns = [
    path('', SnippetGenericAPIViewList.as_view(), name='list'),
    path('detail/<int:pk>/', SnippetGenericAPIViewDetail.as_view(),name='detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)