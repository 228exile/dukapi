#from django.urls import path
from .views import VoisinViewSet, FavoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('voisin', VoisinViewSet, basename='voisin')
router.register('favory', FavoryViewSet, basename='favory')

urlpatterns = router.urls