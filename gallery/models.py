from django.db import models
from util.views import validate_file_size


class Gallery(models.Model):
    img_url = models.FileField(upload_to='pics', validators=[validate_file_size])
    status = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Gallery'

    def __str__(self):
        return '%s %s' % (self.img_url, self.status)
