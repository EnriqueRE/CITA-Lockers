from django.contrib import admin
from Events.models import User, Locker, Event



class LockerAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'zone', 'description')

admin.site.register(Locker, LockerAdmin)

class LockerUserAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'lastname')

admin.site.register(User, LockerUserAdmin)

#admin.site.register(Locker, LockerUserAdmin)

class LockerEventAdmin(admin.ModelAdmin):
    # ...
    list_display = ('name', 'usergpf1','description', 'locker', 'zone', 'date')

    #list_display = ('name', 'usergpf1', 'locker', 'zone', 'date')

admin.site.register(Event,LockerEventAdmin)
