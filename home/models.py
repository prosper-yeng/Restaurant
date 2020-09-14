from django.db import models
from util.views import validate_file_size


class BackgroundImages(models.Model):
    img_url = models.FileField(upload_to='pics', validators=[validate_file_size])
    logo_url = models.FileField(upload_to='pics', validators=[validate_file_size])
    tagline = models.CharField(max_length=200)
    status = models.BooleanField()
    restaurant_name = models.CharField(max_length=200)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Background Images'

    def __str__(self):
        return '%s %s' % (self.restaurant_name, self.tagline)


