from django.contrib import admin
from app.models import Contact, Address, PhoneNumber, Email, Group

admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(PhoneNumber)
admin.site.register(Email)
admin.site.register(Group)

