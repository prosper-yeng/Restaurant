from django.db import models

class CoreValue(models.Model):
    name = models.CharField(max_length=30)
    status = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True, null=True)

    class Meta: verbose_name_plural = 'Core Values'

    def __str__(self):
        return f'{self.name}'

class AboutUs(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    vision = models.CharField(max_length=500, null=True)
    mission = models.CharField(max_length=500, null=True)
    img_url = models.FileField(upload_to='pics')
    status = models.BooleanField()
    created_on = models.DateField(auto_now_add=True, null=True)

    class Meta: verbose_name_plural = 'About Us'

    def __str__(self):
        return f'{self.title}'

class WhyUs(models.Model):
    id = models.CharField(max_length=10, null=False, primary_key=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    status = models.BooleanField()
    created_on = models.DateField(auto_now_add=True, null=True)

    class Meta: verbose_name_plural = 'Why Us'

    def __str__(self):
        return f'{self.id} {self.title}'