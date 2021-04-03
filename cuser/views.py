# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from .models import CustomUser
# from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.views import LoginView
# from django.views.generic import CreateView
# # import json
# from .forms import RegisterForm

# # Create your views here.

# def verify_user(request):
#     # a = CustomUser.objects.get(email= 'hp@gmail.com')
#     # print(a.password)
#     # print(a)
#     a = CustomUser.objects.all()
    
#     a_user = {
#         "id" : a[0].id,
#         'email' : '' ,
#     }
#     # json.dumps(a_user)
#     user = authenticate(email = 'hp@gmail.com', password = '123456')
#     login(request,user)
#     if user.is_authenticated :
#         print(user, user.is_authenticated)
#     return JsonResponse(a_user)

# class RegisterUser(CreateView):
#     template_name = 'cuser/index.html'
#     form_class = RegisterForm
#     success_url = '/'
    
#     # def form_valid(self, form):
#     #     # This method is called when valid form data has been POSTed.
#     #     # It should return an HttpResponse.
#     #     # form.send_email()
#     #     return super().form_valid(form)

# # def CreateUser(request):
# #         print(request.user.id)
# #         # qs = Customer.objects.get(address= 'nepal')
# #         # print(qs.user)
# #         user        = RegisterForm(request.POST or None)
# #         # if user.is_valid():
# #         customer    = CustomerForm(request.POST or None)
# #         # if user.is_valid():
# #         #     user.save()
# #         #     print(user.cleaned_data['email'])
# #         if customer.is_valid():
# #             # email = user.cleaned_data['email']
# #             # userid = CustomUser.objects.get(email = "mkk@gmail.com")
# #             # userid = CustomUser.objects.get(email = 'mk@gmail.com')
# #             customer.user = userid
            
# #             customer.save()
# #         return render(request,'cuser/create_customer.html',{"form1":RegisterForm, "form2" : CustomerForm})
 
    
# # def CreateUser(request):
# #     if request.method == 'POST':
# #         user_form = RegisterForm(request.POST or None)
# #         customer_form = CustomerForm(request.POST or None)
# #         if user_form.is_valid() and customer_form.is_valid():
# #             print(user_form)
# #             user = user_form.save(commit= False)
# #             customer= customer_form.save(commit = False)
# #             customer.user = user
# #             user.save()
# #             customer.save()

# #     else:
# #         user_form = RegisterForm()
# #         customer_form = CustomerForm()
# #     return render(request, 'cuser/create_customer.html', {
# #         'form1' : user_form,
# #         'form2' : customer_form
# #     })

# class UserLogin(LoginView):
#     template_name = 'cuser/login_user.html'
#     # success_url = 'cuser:verify'
#     LOGIN_REDIRECT_URL = 'cuser:verify'

