from django.shortcuts import redirect
from django.urls.base import reverse_lazy, reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from app.forms import ContactCreateForm, AddressCreateForm, EmailCreateForm, PhoneCreateForm, GroupCreateForm
from app.models import Address, Contact, Email, PhoneNumber, Group
from peoPool.settings import MEDIA_URL

FORM_TEMPLATE = 'form.html'
VIEW_TEMPLATE = 'contact.html'
DEL_TEMPLATE = 'delete.html'
GROUP_TEMPLATE = 'group.html'
FORM_GROUP_TEMPLATE = 'form_group.html'
CONTACTS_VIEW_TEMPLATE = 'contact_list.html'
GROUPS_VIEW_TEMPLATE = 'group_list.html'


class ContactsView(ListView):
    template_name = CONTACTS_VIEW_TEMPLATE
    queryset = Contact.objects.order_by('last_name')


class SearchView(ListView):
    template_name = CONTACTS_VIEW_TEMPLATE

    def get_queryset(self):
        query = self.request.GET.get('query', default="")
        return Contact.objects.filter(first_name__icontains=query) or \
               Contact.objects.filter(last_name__icontains=query) or \
               Contact.objects.filter(phonenumber__phone_number__contains=query) or \
               Contact.objects.filter(email__email__icontains=query)


class GroupsView(ListView):
    template_name = GROUPS_VIEW_TEMPLATE

    def get_queryset(self):
        query = self.request.GET.get('query', default="")
        return Group.objects.filter(name__icontains=query) or \
               Group.objects.filter(contact__first_name__icontains=query) or \
               Group.objects.filter(contact__last_name__icontains=query)


class ContactDetailView(DetailView):
    template_name = VIEW_TEMPLATE
    queryset = Contact.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['path'] = MEDIA_URL
        return context


class GroupView(DetailView):
    template_name = GROUP_TEMPLATE
    queryset = Group.objects.all()


class AddContactView(CreateView):
    form_class = ContactCreateForm
    template_name = FORM_TEMPLATE


class AddGroupView(CreateView):
    form_class = GroupCreateForm
    template_name = FORM_TEMPLATE


class AddAddressView(FormView):
    form_class = AddressCreateForm
    template_name = FORM_TEMPLATE

    def form_valid(self, form):
        contact_update = Contact.objects.get(**self.kwargs)
        form_save = form.save()
        contact_update.address_id = form_save.id
        contact_update.save()

        return redirect('contact_view', contact_update.id)


class AddEmailView(FormView):
    form_class = EmailCreateForm
    template_name = FORM_TEMPLATE

    def form_valid(self, form):
        contact = Contact.objects.get(**self.kwargs)
        form_edit = form.save(commit=False)
        form_edit.contact = contact
        form_edit.save()
        return redirect('contact_view', contact.id)


class AddPhoneView(FormView):
    form_class = PhoneCreateForm
    template_name = FORM_TEMPLATE

    def form_valid(self, form):
        contact = Contact.objects.get(**self.kwargs)
        form_edit = form.save(commit=False)
        form_edit.contact = contact
        form_edit.save()
        return redirect('contact_view', contact.id)


class EditAddressView(UpdateView):
    model = Address
    fields = '__all__'
    template_name = FORM_TEMPLATE

    def get_success_url(self):
        contact = Contact.objects.get(address_id=self.get_object().id)
        return reverse('contact_view', kwargs={'pk': contact.id})


class EditContactView(UpdateView):
    model = Contact
    fields = '__all__'
    template_name = FORM_TEMPLATE


class EditEmailView(UpdateView):
    model = Email
    fields = [
        'email',
        'email_type'
    ]
    template_name = FORM_TEMPLATE

    def get_success_url(self):
        return reverse('contact_view', kwargs={'pk': self.object.contact_id})


class EditPhoneView(UpdateView):
    model = PhoneNumber
    fields = [
        'phone_number',
        'phone_type'
    ]
    template_name = FORM_TEMPLATE

    def get_success_url(self):
        return reverse('contact_view', kwargs={'pk': self.object.contact_id})


class EditGroupView(UpdateView):
    model = Group
    fields = '__all__'
    template_name = FORM_TEMPLATE

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_ex'] = "group.html"
        return context


class DeleteContactView(DeleteView):
    model = Contact
    template_name = DEL_TEMPLATE
    success_url = reverse_lazy('contacts_view')


class DeleteGroupView(DeleteView):
    model = Group
    template_name = DEL_TEMPLATE
    success_url = reverse_lazy('groups_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['template_ex'] = "group.html"
        return context


class DeleteEmailView(DeleteView):
    model = Email
    template_name = DEL_TEMPLATE

    def get_success_url(self):
        return reverse('contact_view', kwargs={'pk': self.object.contact_id})


class DeletePhoneView(DeleteView):
    model = PhoneNumber
    template_name = DEL_TEMPLATE

    def get_success_url(self):
        return reverse('contact_view', kwargs={'pk': self.object.contact_id})
