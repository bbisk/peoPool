from django.shortcuts import render
from django.views.generic.base import View

TEMPLATE = 'base.html'
class ContactsView(View):
    def get(self, request):
        return render(request, TEMPLATE, {})
