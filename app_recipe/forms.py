from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import ( 
    UserInfo,
    Category, 
    Recipe,
    Comment,
    Report,
    Recipe_Ingredient,
)
from cuser.models import CustomUser

class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = ('user',)


class RecipeForm(forms.ModelForm):
    class Meta:
        model   = Recipe
        fields  = ('recipe_name', 'description', 'quantity', 'recipe_type', 'image_file')

class RIForm(forms.ModelForm):
    class Meta:
        model   = Recipe_Ingredient
        exclude = ('recipe',)

class CommentForm(forms.ModelForm):
    class Meta:
        model   = Comment
        exclude = ('recipe', 'created_by', 'is_appropriate',)

class ReportForm(forms.ModelForm):
    class Meta:
        model   = Report
        exclude = ('recipe', 'created_by','is_repeated')