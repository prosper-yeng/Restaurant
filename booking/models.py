from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Booking(models.Model):
    your_name = models.CharField(max_length=100, null=True)
    your_phone = models.CharField(max_length=15, null=True)
    msgemail = models.EmailField(max_length=254, null=True)
    book_date = models.DateTimeField(blank=True, null=True)
    book_time = models.TimeField(blank=False, null=True)
    msg = models.TextField(null=True, blank=True)
    persons_number = models.IntegerField(null=True, blank=True)
    has_message = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True, null=True,blank=True)
    modified_on = models.DateField(auto_now=True, null=True,blank=True)

    response = models.TextField(null=True,blank=True)
    has_responded = models.BooleanField(null=True,blank=True,default=False)

    def __str__(self):
        return '{} {}'.format(self.your_name,self.your_phone)

    class Meta:
        verbose_name_plural = 'Book a Table'

