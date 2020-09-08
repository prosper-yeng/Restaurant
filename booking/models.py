from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Booking(models.Model):
    your_name = models.CharField(max_length=100)
    your_phone = models.CharField(max_length=15, null=True)
    msgemail = models.EmailField(max_length=254)
    book_date = models.DateField(blank=True)
    book_time = models.TimeField(blank=False)
    msg = models.TextField(max_length=1500, null=True, blank=True)
    persons_number = models.IntegerField(null=True, blank=True)
    has_message = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    is_closed = models.BooleanField(default=False)
    modified_on = models.DateField(auto_now=True, null=True, blank=True)
    response = models.TextField(max_length=1500, null=True, blank=True)
    has_responded = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.your_name)

    class Meta:
        verbose_name_plural = 'Book a Table'

