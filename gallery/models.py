from django.db import models


# Create your models here.
class Gallery(models.Model):
    img_url = models.FileField(upload_to='pics')
    status = models.BooleanField()
    created_on = models.DateField(auto_now_add=True, null=True)
    modified_on = models.DateField(auto_now=True)

    class Meta: verbose_name_plural = 'Gallery'

    def __str__(self):
        return f'{self.img_url}{self.status}'
