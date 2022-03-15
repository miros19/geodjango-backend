from re import L
from django.contrib.gis import admin
from .models import *

admin.site.register(WorldBorder, admin.ModelAdmin)
admin.site.register(Voivodships, admin.ModelAdmin)
admin.site.register(Districts, admin.ModelAdmin)
admin.site.register(Ariports, admin.ModelAdmin)
