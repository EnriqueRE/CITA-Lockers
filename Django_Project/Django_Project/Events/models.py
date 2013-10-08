from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Locker(models.Model):
    lockerUser = models.OneToOneField(User)
    name = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=200)
    usergpf1 = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    locker = models.CharField(max_length=200)
    zone = models.CharField(max_length=200)
    date = models.CharField(max_length=200)