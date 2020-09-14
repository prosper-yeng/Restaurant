from django.db import models
from util.views import validate_file_size


category_choice = (
    ('Starter', 'Starter'),
    ('Main Course', 'Main Course'),
    ('Course Meal', 'Course Meal'),
    ('Dessert', 'Dessert'),
    ('Drink', 'Drink'),

)


class DrinkType(models.Model):
    drinkType = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    status = models.BooleanField()

    class Meta:
        verbose_name_plural = 'drink Type'

    def __str__(self):
        return self.drinkType


class MenuSchedule(models.Model):
    name = models.CharField(max_length=100)
    time_range = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Menu Schedule'

    def __str__(self):
        return self.name


class MenuItems(models.Model):
    menu_name = models.CharField(max_length=100)
    menu_desc = models.TextField(max_length=1000, null=True, blank=True)
    menuImage = models.FileField(upload_to='pics', validators=[validate_file_size])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    menu_category = models.CharField(max_length=100, choices=category_choice)
    # if menu_category.choices == 'Drinks':
    drinkType = models.ForeignKey(DrinkType, on_delete=models.CASCADE, null=True, blank=True)

    # menuCategory = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    menuSchedule = models.ForeignKey(MenuSchedule, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    childrenMenu = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s %s' % (self.menu_category, self.menu_name, self.price)

    class Meta:
        verbose_name_plural = 'Menu Items'


class Spetials(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField(max_length=200)
    tagline = models.TextField(max_length=200)
    desc = models.TextField(max_length=200, null=True)
    menuImage = models.FileField(upload_to='pics', validators=[validate_file_size])
    created_on = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s %s' % (self.name, self.title, self.tagline)

    class Meta:
        verbose_name_plural = 'Specials'
