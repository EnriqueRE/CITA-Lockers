from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from LockerZones.models import LockerZone

from django.conf.urls import url

class LockerZoneResourse(ModelResourse):
  class Meta:
    queryset = LockerZone.objects.all()
    resourse_name = 'LockerZone'
    fields = ['name', 'description', 'total', 'occupied', 'free']
    authorization = Authorization()
    allowed_methods = ['get', 'post', 'delete', 'put']
    include_resourse_uri = False
    include_resourse_uri = False
