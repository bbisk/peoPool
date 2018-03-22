from django.db import models

class Contact(models.Model):
    def __str__(self):
        return self.last_name
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    address = models.ForeignKey('Address', null=True)
    group = models.ManyToManyField('Group')
    avatar = models.FileField(upload_to='images/', null=True)


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
    def __str__(self):
        return self.phone_number
    phone_number = models.SmallIntegerField()
    phone_type = models.CharField(max_length=32, null=True)
    contact = models.ForeignKey('Contact')


class Email(models.Model):
    def __str__(self):
        return self.email
    email = models.EmailField()
    email_type = models.CharField(max_length=32, null=True)
    contact = models.ForeignKey('Contact')

class Group(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=64)
    group_description = models.CharField(max_length=255)