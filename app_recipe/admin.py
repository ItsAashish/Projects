from django.contrib import admin
from .models import (
    UserInfo,
    Category,
    Recipe,
    Comment,
    Report,
    Recipe_Ingredient,
    Ingredient
)


# Register your models here.
admin.site.register(UserInfo)
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Report)
admin.site.register(Ingredient)
admin.site.register(Recipe_Ingredient)
