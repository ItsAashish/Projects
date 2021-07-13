from django.contrib import admin
from django.urls import path,include
from .views import (
    RegisterUser,
    index,
    UserLogin,
    AddRecipe,
    viewRecipe,
    updateRecipe,
    RecipeDeleteView,
    userDetails,
    createReport,
    reviews,
    all_recipes,
    logoutV,
)
app_name = 'app_recipe'
urlpatterns = [
    path('',index, name = 'index_page'),
    path('login/', UserLogin.as_view(), name = "login_view"),
    path('register/', RegisterUser, name = 'user_registration' ),
    path('add/', AddRecipe, name = 'add_recipe'),
    path('view/<int:id>/', viewRecipe, name = 'view_recipe'),
    path('view/<int:id>/update/', updateRecipe, name = 'update_recipe'),
    path('view/<pk>/delete/', RecipeDeleteView.as_view(), name = 'delete_recipe'),
    path('user/<int:id>', userDetails, name = 'user_data'),
    path('view/<pk>/report', createReport, name = 'create_report'),
    path('reviews/', reviews, name = 'reviews'),
    path('view/', all_recipes,name = 'all_recipes'),
    path('logout/',logoutV, name = 'logout_view'),

]
