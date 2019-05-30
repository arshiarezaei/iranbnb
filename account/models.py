from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_google_maps import fields as map_fields

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)

    def __str__(self):
        return 'profile for user {}'.format(self.user.username)


class RentOutAHome(models.Model):
    surface_area = models.IntegerField(blank=True)
    number_of_rooms = models.SmallIntegerField(blank=True)
    # location = map_fields.GeoLocationField(max_length=100)
    address = models.TextField(blank=True)
    is_available = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    start_date = models.DateField(blank=True)
    finale_date = models.DateField(blank=True)
    identity_docs = models.ImageField(blank=True)
    photo = models.ImageField(blank=True)   
    cost_per_day = models.FloatField(blank=True) 
    owner = models.ForeignKey(User,on_delete=models.CASCADE)


class ReservedHomes(models.Model):
    start_date = models.DateField()
    final_date = models.DateField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    homeID = models.ForeignKey(RentOutAHome,on_delete=models.CASCADE)
