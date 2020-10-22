from django.contrib import admin
from django.contrib.gis import admin
from .models import Border

admin.site.register(Border,admin.OSMGeoAdmin)
#admin.site.register(Border)
