from django.db import models


# Create your models here.
class EventBackground(models.Model):
    event_bg = models.FileField(upload_to='pics')

    class Meta: verbose_name_plural = 'EventBackground'


class Package(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta: verbose_name_plural = 'Packages'


class CustomerEvents(models.Model):
    event_type = models.CharField(max_length=100, null=True)
    event_desc = models.TextField(max_length=1000, null=True)
    event_img = models.FileField(upload_to='pics')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    package = models.ManyToManyField(Package)
    tagline = models.CharField(max_length=100, null=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    status = models.BooleanField()

    def __str__(self):
        return f'{self.event_type} {self.price}'

    class Meta: verbose_name_plural = 'Customer Events'
