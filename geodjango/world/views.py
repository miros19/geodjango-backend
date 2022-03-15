from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import GEOSGeometry,Point

from .models import *
from .serializers import *

class WorldBorderViewSet(viewsets.ModelViewSet):
    serializer_class = WorldBorderSerializer
    queryset = WorldBorder.objects.all()

class VoivodshipsViewSet(viewsets.ModelViewSet):
    serializer_class = VoivodshipsSerializer
    queryset = Voivodships.objects.all()

class DistrictsViewSet(viewsets.ModelViewSet):
    serializer_class = DistrictsSerializer
    queryset = Districts.objects.all()

class AriportsViewSet(viewsets.ModelViewSet):
    serializer_class = AriportsSerializer
    queryset = Ariports.objects.all()