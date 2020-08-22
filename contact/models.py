from django.db import models
from django.core.validators import RegexValidator

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)

# Create your models here.
class Address(models.Model):
    location = models.CharField(max_length=200, null=True)
    begin_day = models.CharField(max_length=20, null=True, choices=DAYS_OF_WEEK)
    end_day = models.CharField(max_length=20, null=True, choices=DAYS_OF_WEEK)
    begin_time = models.TimeField(auto_now=False)
    end_time = models.TimeField(auto_now=False)
    email = models.CharField(max_length=100, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    status = models.BooleanField()
    created_on = models.DateField(auto_now_add=True, null=True)

    class Meta: verbose_name_plural = 'Address'

    def __str__(self):
        return {self.location} + ' ' + {self.email} + ' ' + {self.phone_number}


class Contact(models.Model):
    office_phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    website = models.CharField(max_length=100)
    postal = models.TextField()
    publish = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=1000)
    response = models.TextField(blank=True)
    has_responded = models.BooleanField(default=False)
    has_message = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
