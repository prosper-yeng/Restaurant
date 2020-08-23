from django.shortcuts import render, redirect, reverse
from django.views import generic
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from util.views import email_response
from .models import Booking
from .form import BookingForm, BookingMessageForm



def success(request):
    content = {
        'message': 'Your email has been sent. If your email contain any enquiry, '
                   'we will respond you as soon as possible through the email you provided'
    }
    return render(request, 'booking/success.html/',  content)


def index(request):

    if request.method == 'POST':
        form = BookingForm(request.POST)

        if form.is_valid():
            form.save()

        else:
            error = 'Invalid form'
            content = {
                'error': error,
                'form': form,
            }
    else:
        pass
    return redirect(reverse('home:index') + '#booking')

    # return redirect('home:index#contact')



# return redirect(reverse('home.views.home') + '#first')


class ListView(PermissionRequiredMixin, generic.ListView):
    permission_required = 'contact.can.view.contact'
    template_name = 'booking/list.html'
    context_object_name = 'result_list'

    def get_queryset(self):
        return Booking.objects.filter(has_responded=False)


class BooingMessageFormView(View):
    form_class = BookingMessageForm
    template_name = 'booking/message.html'

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


def booking_message_form_view(request):

    form = BookingForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('contact:success')

    else:
        error = 'Invalid form'
        content = {
            'error': error,
            'form': form,
        }
        return render(request, 'booking/index.html/', content)


def respond(request, mid):

    if request.method == 'POST':
        booking_message = Booking.objects.get(id=mid)
        booking_message.has_responded = True
        booking_message.response = request.POST.get('response')

        msg = request.POST.get('response')
        recipient = [booking_message.msgemail]
        if recipient:
            email_response(message=msg, recipients=recipient)
            booking_message.save()

        return redirect('booking:list')

    else:
        form = BookingMessageForm(None)
        booking_message = Booking.objects.get(id=mid)
        content = {
            'form': form,
            'mid': mid,
            'booking_message': booking_message,
        }
    return render(request, 'booking/response.html/',  content)