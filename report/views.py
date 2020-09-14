from datetime import datetime, date
from django.utils.dateparse import parse_datetime, parse_date
from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse
from report.printing import MyPrint
from io import BytesIO

from booking.models import Booking
from contact.models import ContactMessage
from event.models import CustomerEvents


def print_users(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="My Users.pdf"'

    buffer = BytesIO()

    report = MyPrint(buffer, 'Letter')
    pdf = report.print_users()

    response.write(pdf)
    return response


def index(request):
    pass


def booking(request):
    template_name = 'report/booking.html'
    start_date = request.POST.get('start_date')
    if request.method == 'POST' and start_date:
        s_date = parse_date(start_date)
        end_date = request.POST.get('end_date')
        e_date = parse_date(end_date)
        title = 'Bookings from %s %s, %s to %s %s, %s' % \
                (s_date.strftime('%b'), s_date.strftime('%d'), s_date.strftime('%Y'),
                 e_date.strftime('%b'), e_date.strftime('%d'), e_date.strftime('%Y'),)

    else:
        current_date = date.today()
        start_date = date(current_date.year, current_date.month, 1)
        end_date = date(current_date.year, current_date.month, 30)
        title = 'Booking for the Month ' + current_date.strftime('%B')

    result_list = Booking.objects.filter(Q(book_date__gte=start_date) & Q(book_date__lte=end_date))

    context = {
        'title': title,
        'result_list': result_list,
    }
    return render(request, template_name, context)


def inquiry(request):
    template_name = 'report/inquiry.html'
    start_date = request.POST.get('start_date')
    if request.method == 'POST' and start_date:
        s_date = parse_date(start_date)
        end_date = request.POST.get('end_date')
        e_date = parse_date(end_date)
        title = 'Inquiries from %s %s, %s to %s %s, %s' % \
                (s_date.strftime('%b'), s_date.strftime('%d'), s_date.strftime('%Y'),
                 e_date.strftime('%b'), e_date.strftime('%d'), e_date.strftime('%Y'),)

    else:
        current_date = date.today()
        start_date = date(current_date.year, current_date.month, 1)
        end_date = date(current_date.year, current_date.month, 30)
        title = 'Inquiries for the Month ' + current_date.strftime('%B')

    result_list = ContactMessage.objects.filter(Q(created_on__gte=start_date) & Q(created_on__lte=end_date))

    context = {
        'title': title,
        'result_list': result_list,
    }
    return render(request, template_name, context)


def event(request):
    template_name = 'report/event.html'
    start_date = request.POST.get('start_date')
    if request.method == 'POST' and start_date:
        s_date = parse_date(start_date)
        end_date = request.POST.get('end_date')
        e_date = parse_date(end_date)
        title = 'Events from %s %s, %s to %s %s, %s' % \
                (s_date.strftime('%b'), s_date.strftime('%d'), s_date.strftime('%Y'),
                 e_date.strftime('%b'), e_date.strftime('%d'), e_date.strftime('%Y'),)

    else:
        current_date = date.today()
        start_date = date(current_date.year, current_date.month, 1)
        end_date = date(current_date.year, current_date.month, 30)
        title = 'Events for the Month of ' + current_date.strftime('%B')

    result_list = CustomerEvents.objects.filter(Q(event_date__gte=start_date) & Q(event_date__lte=end_date))

    context = {
        'title': title,
        'result_list': result_list,
    }
    return render(request, template_name, context)
