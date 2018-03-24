from django.db import models
from django.urls.base import reverse


class Contact(models.Model):
    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_absolute_url(self):
        return reverse('contact_view', kwargs = {'pk': self.pk})

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, null=True, blank=True)
    address = models.ForeignKey('Address', null=True, blank=True)
    group = models.ManyToManyField('Group', blank=True)
    avatar = models.FileField(upload_to='images/', null=True, blank=True)


class Address(models.Model):
    def __str__(self):
        return "{}, {}".format(self.city, self.street)
    country = models.CharField(max_length=64)
    postal_code = models.CharField(max_length=16, null=True)
    city = models.CharField(max_length=32)
    street = models.CharField(max_length=64)
    building = models.CharField(max_length=8)
    flat = models.CharField(max_length=8, null=True)


class PhoneNumber(models.Model):
    PERSONAL = 'P'
    WORK = 'W'
    HOME = 'H'
    OTHER = 'O'
    TYPES = (
        (PERSONAL, 'Personal'),
        (WORK, 'Work'),
        (HOME, 'Home/family'),
        (OTHER, 'Other'),
    )
    def __str__(self):
        return self.phone_number
    phone_number = models.CharField(max_length=32, unique=True)
    phone_type = models.CharField(max_length=32, choices=TYPES, null=True)
    contact = models.ForeignKey('Contact')


class Email(models.Model):
    PERSONAL = 'P'
    WORK = 'W'
    HOME = 'H'
    OTHER = 'O'
    TYPES = (
        (PERSONAL, 'Personal'),
        (WORK, 'Work'),
        (HOME, 'Home/family'),
        (OTHER, 'Other'),
    )
    def __str__(self):
        return self.email
    email = models.EmailField(unique=True)
    email_type = models.CharField(max_length=32, choices=TYPES, null=True)
    contact = models.ForeignKey('Contact')


class Group(models.Model):
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group_view', kwargs = {'pk': self.pk})

    name = models.CharField(max_length=64)
    group_description = models.CharField(max_length=255)