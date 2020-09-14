from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from .models import SendEmailInfo


def email_response(message, recipients):
    email_info = SendEmailInfo.objects.all()[:1].get()
    send_mail(
        email_info.subject,
        message,
        email_info.sender,
        recipients,
        fail_silently=email_info.fail_silently,
    )


def validate_file_size(file_field):
    file_size = file_field.file.size
    megabyte_limit = 3.0
    if file_size > megabyte_limit * 1024 * 1024:
        raise ValidationError("Max file size is %sMB" % str(megabyte_limit))
