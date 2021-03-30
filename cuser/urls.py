from django.urls import path
from .views import verify_user, RegisterUser, CreateUser, UserLogin

app_name = 'cuser'

urlpatterns = [
    path('', verify_user, name = 'verify'),
    path('from/', RegisterUser.as_view(), name = 'register'),
    path('create/', CreateUser),
    path('login/', UserLogin.as_view(), name = 'login_user')

]