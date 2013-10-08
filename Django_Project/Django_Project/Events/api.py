from tastypie import fields
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from Events.models import Locker, User, Event

from django.conf.urls import url

class LockersResource(ModelResource):
    class Meta:
        queryset = Locker.objects.all()
        resource_name = 'Locker'
        fields = ['name', 'lastname', 'zone', 'description']
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'delete', 'put']
        include_resource_uri = False
        include_absolute_uri = False

class UserResource(ModelResource):
    locker = fields.ToOneField('LockersApp.api.LockersResource', attribute='locker', related_name='locker', full=True,
                               null=True)
    class Meta:
        queryset = User.objects.all()
        resource_name = 'User'
        fields = ['name', 'lastname']
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'delete', 'put']
        include_resource_uri = False
        include_absolute_uri = False

class EventResource(ModelResource):
    
    class Meta:
        queryset = Event.objects.all().order_by('date')

        resource_name = 'Event'
        fields = ['name', 'usergpf1','description', 'locker', 'zone', 'date', 'count_event']
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'delete', 'put']
        detail_uri_name = 'usergpf1'

        filtering = {'usergpf1':['exact']}
