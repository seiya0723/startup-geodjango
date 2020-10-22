from django.db import models
# This is an auto-generated Django model module created by ogrinspect.

from django.contrib.gis.db import models
class Border(models.Model):
    n03_001 = models.CharField(max_length=10,null=True,blank=True)
    n03_002 = models.CharField(max_length=20,null=True,blank=True)
    n03_003 = models.CharField(max_length=20,null=True,blank=True)
    n03_004 = models.CharField(max_length=20,null=True,blank=True)
    n03_007 = models.CharField(max_length=5,null=True,blank=True)
    geom     = models.PolygonField(srid=6668)
