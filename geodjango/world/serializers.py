from dataclasses import field
from pyexpat import model
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import *

class WorldBorderSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = WorldBorder
        fields = "__all__"
        geo_field = "mpoly"

class VoivodshipsSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Voivodships
        fields = "__all__"
        geo_field = "wkb_geometry"

class DistrictsSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Districts
        fields = "__all__"
        geo_field = "wkb_geometry"

class AriportsSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Ariports
        fields = "__all__"
        geo_field = "wkb_geometry"