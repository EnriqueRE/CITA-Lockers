from django.contrib import admin
from Events.models import User, Locker, Event, Zone

class LockerAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'zone', 'description')

admin.site.register(Locker, LockerAdmin)

class LockerUserAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'lastname')

admin.site.register(User, LockerUserAdmin)

class LockerEventAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'usergpf1','Description', 'locker', 'zone', 'date')

admin.site.register(Event,LockerEventAdmin)
