import re
from django import forms
from app.models import Contact, Address, Group, Email, PhoneNumber


class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'description',
            'avatar'
        ]

    def clean(self):
        cleaned_data = super().clean()
        fname = cleaned_data.get('first_name')
        lname = cleaned_data.get('last_name')

        if re.match(r"(\d+)", fname) or re.match(r"(\d+)", lname) :
            raise forms.ValidationError('Are you a robot? Please check your name')


class AddressCreateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = '__all__'


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'


class EmailCreateForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email', 'email_type']


class PhoneCreateForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number', 'phone_type']

    def clean(self):
        cleaned_data = super().clean()
        phonenumber = cleaned_data.get('phone_number')
        if not re.match(r"(?<!\w)(\(?(\+|00)?[0-9]{2}\)?)?[ -]?\d{3}[ -]?\d{3}[ -]?\d{3}(?!\w)", phonenumber):
            raise forms.ValidationError('Phone number seems to be wrong! Please check and try again')
