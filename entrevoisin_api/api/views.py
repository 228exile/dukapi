# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Voisin, Favory
from .serializers import VoisinSerializers, FavorySerializers
from rest_framework.response import Response
# Create your views here.

class VoisinViewSet(viewsets.ViewSet):
    serializer_class = VoisinSerializers

    def get_object(self, pk):
        try:
            return Voisin.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def list(self, request):
        queryset= Voisin.objects.all()
        serializer = VoisinSerializers(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = VoisinSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def update(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = VoisinSerializers(instance, data=request.data, partial=True)
        # Vérification de renseignement des champs
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        queryset = Voisin.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = VoisinSerializers(user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response({'Message': "Voisin bien supprimé"})

#viewset du favori
class FavoryViewSet(viewsets.ViewSet):
    #queryset = Blog.objects.all()
    serializer_class = FavorySerializers

    def get_object(self, pk):
        try:
            return Favory.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def list(self, request):
        queryset = Favory.objects.all()
        serializer = FavorySerializers(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = FavorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def update(self, request, pk=None):
        instance = self.get_object(pk)
        serializer = FavoriSerializer(instance, data=request.data, partial=True)
        # Vérification de renseignement des champs
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        queryset = Favory.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = FavorySerializers(user)

        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response({'Message': " Favory bien supprimé"})
