from django.db import models


# Create your models here.
class Menus(models.Model):
    menu_category = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True, null=True)
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'Menus'
    def __str__(self):
        return f'{self.menu_category}'

class MenuItems(models.Model):
    menu_name = models.CharField(max_length=100, null=True)
    menu_desc = models.TextField(max_length=1000, null=True)
    menuImage = models.FileField(upload_to='pics')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    menus= models.ForeignKey(Menus, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True, null=True)
    status = models.BooleanField()

    def __str__(self):
        return f'{self.menus} {self.menu_name} {self.price}'

    class Meta: verbose_name_plural = 'MenuItems'

class Spetials(models.Model):
    name = models.CharField(max_length=100, null=True)
    title = models.TextField(max_length=200, null=True)
    tagline = models.TextField(max_length=200, null=True)
    desc=models.TextField(max_length=200, null=True)
    menuImage = models.FileField(upload_to='pics')
    created_on = models.DateField(auto_now_add=True, null=True)
    status = models.BooleanField()

    def __str__(self):
        return f'{self.name} {self.title} {self.tagline}'

    class Meta: verbose_name_plural = 'Specials'