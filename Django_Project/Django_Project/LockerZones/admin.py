__author__ = 'enrique'

from django.contrib import admin
from LockerZones.models import LockerZone

class LockerZoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

admin.site.register(LockerZone,LockerZoneAdmin)