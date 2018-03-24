"""peoPool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from app.views import ContactsView, AddAddressView, EditAddressView, AddContactView, ContactDetailView, EditContactView, \
    DeleteContactView, AddEmailView, AddPhoneView, SearchView, EditEmailView, EditPhoneView, DeleteEmailView, \
    DeletePhoneView, GroupsView, GroupView, EditGroupView, DeleteGroupView, AddGroupView

from peoPool.settings import MEDIA_URL, MEDIA_ROOT, DEBUG

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', ContactsView.as_view(), name="contacts_view"),
    url(r'^show/(?P<pk>(\d)+)/$', ContactDetailView.as_view(), name="contact_view"),
    url(r'^modify/(?P<pk>(\d)+)/$', EditContactView.as_view(), name="edit_contact_view"),
    url(r'^delete/(?P<pk>(\d)+)/$', DeleteContactView.as_view(), name="delete_view"),
    url(r'^new/$', AddContactView.as_view(), name="add_contact_view"),
    url(r'^(?P<pk>(\d)+)/add_email/$', AddEmailView.as_view(), name="add_email"),
    url(r'^(?P<pk>(\d)+)/modify_email/$', EditEmailView.as_view(), name="modify_email"),
    url(r'^(?P<pk>(\d)+)/delete_email/$', DeleteEmailView.as_view(), name="delete_email"),
    url(r'^(?P<pk>(\d)+)/add_phone/$', AddPhoneView.as_view(), name="add_phone"),
    url(r'^(?P<pk>(\d)+)/modify_phone/$', EditPhoneView.as_view(), name="modify_phone"),
    url(r'^(?P<pk>(\d)+)/delete_phone/$', DeletePhoneView.as_view(), name="delete_phone"),
    url(r'^(?P<pk>(\d)+)/add_address/$', AddAddressView.as_view(), name="add_address_view"),
    url(r'^address/modify/(?P<pk>(\d)+)/$', EditAddressView.as_view(), name="edit_address_view"),
    url(r'^search/$', SearchView.as_view(), name="search"),
    url(r'^groups/$', GroupsView.as_view(), name="groups_view"),
    url(r'^groups/(?P<pk>(\d)+)/$', GroupView.as_view(), name="group_view"),
    url(r'^groups/modify/(?P<pk>(\d)+)/$', EditGroupView.as_view(), name="edit_group_view"),
    url(r'^groups/delete/(?P<pk>(\d)+)/$', DeleteGroupView.as_view(), name="delete_group_view"),
    url(r'^groups/new/$', AddGroupView.as_view(), name="add_group_view"),

]

if DEBUG is True:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)