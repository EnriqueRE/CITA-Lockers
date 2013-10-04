from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from LockerZones.models import LockerZone

from django.conf.urls import url

class LockerZoneResource(ModelResource):
  class Meta:
    queryset = LockerZone.objects.all()
    resource_name = 'LockerZone'
    fields = ['name', 'description', 'total', 'occupied', 'free']
    authorization = Authorization()
    allowed_methods = ['get', 'post', 'delete', 'put']
    include_resource_uri = False
    include_absolute_uri = False
