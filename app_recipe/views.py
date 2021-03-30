from django.shortcuts import render
from cuser.forms import RegisterForm
from .forms import UserForm

# Create your views here.

def RegisterUser(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST or None)
        customer_form = UserForm(request.POST or None)
        if user_form.is_valid() and customer_form.is_valid():
            print(user_form)
            user = user_form.save(commit= False)
            customer= customer_form.save(commit = False)
            customer.user = user
            user.save()
            customer.save()

    else:
        user_form = RegisterForm()
        customer_form = UserForm()
    return render(request, 'cuser/create_customer.html', {
        'form1' : user_form,
        'form2' : customer_form
    })

