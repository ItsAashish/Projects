from django.contrib import admin
from django.urls import path,include
from .views import (
    RegisterUser,
    index,
    UserLogin,
    AddRecipe,
    viewRecipe,
)
app_name = 'app_recipe'
urlpatterns = [
    path('',index, name = 'index_page'),
    path('login/', UserLogin.as_view(), name = "login_view"),
    path('register/', RegisterUser, name = 'user_registration' ),
    path('add/', AddRecipe, name = 'add_recipe'),
    path('view/<int:id>/', viewRecipe, name = 'view_recipe')
]