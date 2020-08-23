from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from util.views import email_response
from .models import ContactMessage
from .form import ContactMessageForm, ContactResponseForm


def success(request):
    content = {
        'message': 'Your email has been sent. If your email contain any enquiry, '
                   'we will respond you as soon as possible through the email you provided'
    }
    return render(request, 'contact/success.html/',  content)


def index(request):

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)

        if form.is_valid():
            form.save()
            form = ContactMessageForm(None)

            content = {
                'success': 'Your email has been sent. If your email contain any enquiry, '
                           'we will respond you as soon as possible through the email you provided',
                'form': form,
            }

        else:
            error = 'Invalid form'
            content = {
                'error': error,
                'form': form,
            }
    else:
        form = ContactMessageForm(None)
        content = {
            'form': form,
        }
    return redirect(reverse('home:index') + '#contact')

    # return redirect('home:index#contact')



# return redirect(reverse('home.views.home') + '#first')


class ListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'contact.can.view.contact'
    template_name = 'contact/list.html'
    context_object_name = 'result_list'

    def get_queryset(self):
        return ContactMessage.objects.filter(has_responded=False)


class ContactMessageFormView(View):
    form_class = ContactMessageForm
    template_name = 'contact/message.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        success_msg = None
        if form.is_valid():
            form.save()
            success_msg = 'Thank you for contacting us.'
            form = self.form_class(None)
            # add the thank you page redirect here
        return render(request, self.template_name, {'form': form, 'success_msg': success_msg})


def contact_message_form_view(request):

    form = ContactMessageForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('contact:success')

    else:
        error = 'Invalid form'
        content = {
            'error': error,
            'form': form,
        }
        return render(request, 'home/index.html/', content)


def respond(request, mid):

    if request.method == 'POST':
        contact_message = ContactMessage.objects.get(id=mid)
        contact_message.has_responded = True
        contact_message.response = request.POST.get('response')

        msg = request.POST.get('response')
        recipient = [contact_message.email]
        if recipient:
            email_response(message=msg, recipients=recipient)
            contact_message.save()

        return redirect('contact:list')

    else:
        form = ContactResponseForm(None)
        contact_message = ContactMessage.objects.get(id=mid)
        content = {
            'form': form,
            'mid': mid,
            'contact_message': contact_message,
        }
    return render(request, 'contact/response.html/',  content)
