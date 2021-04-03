from django.shortcuts import render,redirect,reverse
from cuser.forms import RegisterForm
from .forms import UserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'app_recipe/cookit.html')

class UserLogin(LoginView):
    template_name = 'app_recipe/login.html'
    # success_url = 'app_recipe:index_page'
    # LOGIN_REDIRECT_URL = 'app_recipe:index_page'

# def userLogin(request):
#     if request.user.is_authenticated:
#         return redirect(reverse('app_recipe:index_page'))
    
#     if request.method == 'POST':
#         loginData = LoginForm(request.POST or None)
#         if loginData.is_valid():
#             user = authenticate(request, user = loginData.cleaned_data.get('email'), password = loginData.cleaned_data.get('password'))
#             print(user)
#             if user is not None:
#                 login(request, user)
#                 return redirect(reverse('app_recipe:index_page'))
#             else:
#                 return render(request, 'app_recipe/login.html',
#                             {'form' : LoginForm, 'message' : "Invalid Credentials"})
#     return render(request, 'app_recipe/login.html',
#                             {'form' : LoginForm, 'message' : "Enter your credentials"})

def RegisterUser(request):
    if request.method == 'POST':
        reg_form = RegisterForm(request.POST or None)
        user_form = UserForm(request.POST or None)
        if user_form.is_valid() and reg_form.is_valid():
            print(user_form.cleaned_data, reg_form.cleaned_data)
            reg_user    = reg_form.save()
            user_data   = user_form.save(commit= False)
            user_data.user = reg_user
            user_data.save()

        # redirect to login page

    else:
        reg_form = RegisterForm()
        user_form = UserForm()
    return render(request, 'app_recipe/register.html', {
        'form1' : reg_form,
        'form2' : user_form,
    })

