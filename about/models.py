from django.db import models

class CoreValue(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)

    class Meta: verbose_name_plural = 'Core Values'

    def __str__(self):
        return self.name

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    vision = models.CharField(max_length=500)
    mission = models.CharField(max_length=500)
    img_url = models.FileField(upload_to='pics')
    status = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    class Meta: verbose_name_plural = 'About Us'

    def __str__(self):
        return self.title


class WhyUs(models.Model):
    id = models.CharField(max_length=10, null=False, primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200, null=True)
    status = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Why Us'

    def __str__(self):
        return '%s %s' % (self.id, self.title)
