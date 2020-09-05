from django.db import models

# Create your models here.

class BackgroundImages(models.Model):
    img_url = models.FileField(upload_to='pics')
    logo_url = models.FileField(upload_to='pics', null=True)
    tagline = models.CharField(max_length=200, null=True)
    status = models.BooleanField()
    restaurant_name = models.CharField(max_length=200, null=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    modified_on = models.DateField(auto_now=True)

    class Meta: verbose_name_plural = 'Background Images'

    def __str__(self):
        return f'{self.restaurant_name} {self.tagline}'


