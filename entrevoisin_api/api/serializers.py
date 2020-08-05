from rest_framework import serializers
from .models import Voisin, Favory

class VoisinSerializers(serializers.ModelSerializer):
    class Meta:
        model = Voisin
        fields = ('id','name','phone','adress','about')

class FavorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Favory
        fields = ('id','id_voisin','Favory')