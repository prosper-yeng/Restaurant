from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]


class ContactResponseForm(forms.ModelForm):

    class Meta:
        model = ContactMessage
        fields = [
            'response',
        ]
