from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'your_name',
            'your_phone',
            'msgemail',
            'book_date',
            'book_time',
            'persons_number'
        ]


class BookingMessageForm(forms.ModelForm):
    pass
    # class Meta:
    #     model = ContactMessage
    #     fields = [
    #         'response',
    #     ]
