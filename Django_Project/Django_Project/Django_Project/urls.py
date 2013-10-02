from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from tastypie.api import Api
from Events.api import LockersResource, UserResource, EventResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(LockersResource())
v1_api.register(EventResource())

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_Project.views.home', name='home'),
    # url(r'^Django_Project/', include('Django_Project.foo.urls')),
    
    #Api URL
    (r'^api/', include(v1_api.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
