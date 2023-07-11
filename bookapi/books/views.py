from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData

# Create your views here.
class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category="none")
    serializer_class = BookSerializer

class SpaceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category="space")
    serializer_class = BookSerializer

class ScienceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category="science")
    serializer_class = BookSerializer

class MedievalViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category="medieval")
    serializer_class = BookSerializer

class EngineeringViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category="engineering")
    serializer_class = BookSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category="medicine")
    serializer_class = BookSerializer

class ProgrammingViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category="programming")
    serializer_class = BookSerializer

class TechnologyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category="technology")
    serializer_class = BookSerializer

class BiologyViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category="biology")
    serializer_class = BookSerializer

class ArtViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category="art")
    serializer_class = BookSerializer