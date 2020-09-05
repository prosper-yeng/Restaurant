from django.db import models

# Create your models here.
category_choice = (
    ('Starter', 'Starter'),
    ('Main Course', 'Main Course'),
    ('Course Meal', 'Course Meal'),
    ('Dessert', 'Dessert'),
    ('Drink', 'Drink'),

)


class DrinkType(models.Model):
    drinkType = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'drink Type'

    def __str__(self):
        return f'{self.drinkType}'


class MenuSchedule(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    time_range = models.CharField(max_length=100, null=True, blank=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    status = models.BooleanField()

    class Meta: verbose_name_plural = 'Menu Schedule'

    def __str__(self):
        return f'{self.name}'


# class MenuSubCategory(models.Model):
#     if MenuCategory.menu_category == 'Drink':
#         menuCategory = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, null=True, blank=True,
#                                          choices=category_choices)
#     else:
#         MenuSubCategory = models.ForeignKey(MenuCategory, on_delete=models.CASCADE, null=True, blank=True)
#
#     created_on = models.DateField(auto_now_add=True, null=True)
#     status = models.BooleanField()
#
#     class Meta:
#         verbose_name_plural = 'Menu Category Type'
#
#     def __str__(self):
#         return f'{self.menu_type}'

class MenuItems(models.Model):
    menu_name = models.CharField(max_length=100, null=True)
    menu_desc = models.TextField(max_length=1000, null=True, blank=True)
    menuImage = models.FileField(upload_to='pics')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    menu_category = models.CharField(max_length=100, null=True, choices=category_choice)
    # if menu_category.choices == 'Drinks':
    drinkType = models.ForeignKey(DrinkType, on_delete=models.CASCADE, null=True, blank=True)

    # menuCategory = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    menuSchedule = models.ForeignKey(MenuSchedule, on_delete=models.CASCADE, null=True, blank=True)
    created_on = models.DateField(auto_now_add=True, null=True)
    childrenMenu = models.BooleanField(default=False)
    status = models.BooleanField()

    def __str__(self):
        return f'{self.menu_category} {self.menu_name} {self.price}'

    class Meta: verbose_name_plural = 'Menu Items'


class Spetials(models.Model):
    name = models.CharField(max_length=100, null=True)
    title = models.TextField(max_length=200, null=True)
    tagline = models.TextField(max_length=200, null=True)
    desc = models.TextField(max_length=200, null=True)
    menuImage = models.FileField(upload_to='pics')
    created_on = models.DateField(auto_now_add=True, null=True)
    status = models.BooleanField()

    def __str__(self):
        return f'{self.name} {self.title} {self.tagline}'

    class Meta: verbose_name_plural = 'Specials'
