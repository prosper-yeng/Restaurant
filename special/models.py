from django.db import models


# Create your models here.
class Special(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    other_info = models.TextField(max_length=1000)
    img_url = models.FileField(upload_to='pics', null=True)
    status = models.BooleanField(null=True)
    created_on = models.DateField(auto_now_add=True)
    modified_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name + ' ' + self.title
