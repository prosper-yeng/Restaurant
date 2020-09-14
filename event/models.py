from django.db import models

from util.views import validate_file_size
# Create your models here.

event_category_choices = (
    ('Customer Event', 'Customer Event'),
    ('Restaurant Event', 'Restaurant Event'),
)


class EventBackground(models.Model):
    event_bg = models.FileField(upload_to='pics')

    class Meta:
        verbose_name_plural = 'EventBackground'


class Package(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Packages'


class CustomerEvents(models.Model):
    event_type = models.CharField(max_length=100)
    event_desc = models.TextField(max_length=1000, null=True)
    event_img = models.FileField(upload_to='pics', validators=[validate_file_size])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    package = models.ManyToManyField(Package)
    tagline = models.CharField(max_length=100, null=True)
    event_category = models.CharField(max_length=50, choices=event_category_choices, default='Customer Event')
    event_date = models.DateTimeField(auto_now_add=True)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' % (self.event_type, self.event_category)

    class Meta:
        verbose_name_plural = 'Events'
