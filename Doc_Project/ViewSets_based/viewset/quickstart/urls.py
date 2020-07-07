from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import SnippetViewSet


router = DefaultRouter()
router.register('snippet', SnippetViewSet, basename='snippet')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
