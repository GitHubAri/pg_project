from django.db import models
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Rooms(models.Model):
    room_no = models.PositiveIntegerField()
    floor = models.IntegerField()
    beds = models.PositiveIntegerField()
    free_beds = models.PositiveIntegerField()
    room_details = models.TextField()
    rent = models.PositiveIntegerField()


    def __str__(self):
        messages.success(request, f'Room NO room_no.   Created !')

    def get_absolute_url(self):
        return reverse('rooms-view')



class Peoples(models.Model):
    room_no = models.PositiveIntegerField()
    floor = models.IntegerField()
    rent = models.PositiveIntegerField()
    advanced_payment = models.PositiveIntegerField()
    name = models.CharField(max_length = 100)
    # phone_no = models.IntegerField()
    # email_id = models.EmailField()
    address = models.TextField()
    date_joined = models.DateTimeField(default = timezone.now)
    # passport_no = models.CharField(max_length=20)
    # work_place = models.CharField(max_length=30)
    # document_file = models.FileField()


    def __str__(self):
        messages.success(request, f'People Added !')

    def get_absolute_url(self):
        return reverse('people-view')