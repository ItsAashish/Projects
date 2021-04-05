# import cuser
from cuser.models import CustomUser
from django.db import models
# Create your models here.

class UserInfo(models.Model):
    """ The model is OneToOne extension of the UserAdmin
    with extended fields firstName LastName & address """
    user        = models.OneToOneField(CustomUser,
                on_delete = models.CASCADE,
                null = True,
                blank = True,
                )
    firstName   = models.CharField(max_length = 30, null= True, blank= True)
    lastName    = models.CharField(max_length = 30, null= True, blank= True)
    address     = models.CharField(max_length = 30, null= True, blank = True)

    def __str__(self):
        return f'{ self.firstName } {self.lastName}'

class Category(models.Model):
    """ This stores the data required to define category of Recipe """
    c_type      = models.CharField(max_length= 30)
    region      = models.CharField(max_length=30)
    is_veg      = models.BooleanField(blank= False, null= False)

    def __str__(self):
        return f'{ self.c_type }'

class Recipe(models.Model):
    """ The model consists of all the information about Recipes"""
    recipe_name     = models.CharField(max_length= 100, blank = False, null= False)
    description     = models.TextField(blank= False, null= False)
    quantity        = models.CharField(max_length= 30, null=True, blank= True)
    date_added      = models.DateTimeField(auto_now_add= True, blank= False)
    recipe_type     = models.ForeignKey('Category',
                            blank= True, null= True,
                            on_delete = models.CASCADE
                            )
    created_by      = models.ForeignKey(
                    CustomUser,
                    on_delete=models.CASCADE
        )
    def __str__(self):
        return f'{ self.recipe_name }'



# The models to be made after recipe

class Comment(models.Model):
    """ The model consists of comments made by user in Recipes """
    description     = models.CharField(max_length = 255, null = False, blank = False)
    recipe          = models.ForeignKey(Recipe, on_delete = models.CASCADE)
    created_by      = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    is_appropriate  = models.BooleanField(default= True)
    def __str__(self):
        return f'Id: {self.is_appropriate}'


class Report(models.Model):
    """ The model consists of Reports to the Recipes """
    title           = models.CharField(max_length= 30, blank= False, null= False)
    description     = models.CharField(max_length = 255, null = False, blank = False)
    recipe          = models.ForeignKey('Recipe', on_delete = models.CASCADE)
    created_by      = models.ForeignKey('UserInfo', on_delete= models.CASCADE)
    is_repeated     = models.BooleanField(default= False)

    def __str__(self):
        return f'{ self.title }'

class Ingredient(models.Model):
    """ This model containsinfo about ingredients """
    ingredient_name     = models.CharField(max_length=100, unique= True)
    ingredient_type     = models.CharField(max_length=30)
    measurement_scale   = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{ self.ingredient_name }'

class Recipe_Ingredient(models.Model):
    recipe      = models.ForeignKey('Recipe',
                    blank= True, null= False,
                    on_delete = models.CASCADE)
    ingredient  = models.ForeignKey('Ingredient',
                    blank = False, null= False,
                    on_delete = models.CASCADE)
    amount      = models.FloatField(null=False, blank= False)

    def __str__(self):
        return f'{self.recipe} {self.ingredient}'

