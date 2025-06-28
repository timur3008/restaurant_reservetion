from django.db import models

class ContactUs(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)

class Booking(models.Model):
    full_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)
    time = models.TimeField()
    date = models.DateField()
    number_of_people = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)