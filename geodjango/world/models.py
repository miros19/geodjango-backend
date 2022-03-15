from django.contrib.gis.db import models

class WorldBorder(models.Model):
    # Regular Django fields corresponding to the attributes in the
    # world borders shapefile.
    name = models.CharField(max_length=50)
    area = models.IntegerField()
    pop2005 = models.IntegerField('Population 2005')
    fips = models.CharField('FIPS Code', max_length=2, null=True)
    iso2 = models.CharField('2 Digit ISO', max_length=2)
    iso3 = models.CharField('3 Digit ISO', max_length=3)
    un = models.IntegerField('United Nations Code')
    region = models.IntegerField('Region Code')
    subregion = models.IntegerField('Sub-Region Code')
    lon = models.FloatField()
    lat = models.FloatField()

    # GeoDjango-specific: a geometry field (MultiPolygonField)
    mpoly = models.MultiPolygonField()

    # Returns the string representation of the model.
    def __str__(self):
        return self.name


class Voivodships(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    nazwa = models.CharField(max_length=100, blank=True, null=True)
    wkb_geometry = models.PolygonField(blank=True, null=True)

    def __str__(self):
        return self.nazwa

    class Meta:
        managed = False
        db_table = 'wojewodztwa'


class Ariports(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    scalerank = models.IntegerField(blank=True, null=True)
    featurecla = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    abbrev = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    gps_code = models.CharField(max_length=100, blank=True, null=True)
    iata_code = models.CharField(max_length=100, blank=True, null=True)
    wikipedia = models.CharField(max_length=100, blank=True, null=True)
    natlscale = models.IntegerField(blank=True, null=True)
    cartodb_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'lotniska'


class Districts(models.Model):
    ogc_fid = models.AutoField(primary_key=True)
    id = models.IntegerField(blank=True, null=True)
    nazwa = models.CharField(max_length=100, blank=True, null=True)
    wkb_geometry = models.GeometryField(blank=True, null=True)

    def __str__(self):
        return self.nazwa

    class Meta:
        managed = False
        db_table = 'powiaty'