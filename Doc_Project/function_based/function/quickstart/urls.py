from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.snippet_list, name='list'),
    path('detail/<int:pk>', views.snippet_detail, name='details')
]

urlpatterns = format_suffix_patterns(urlpatterns)