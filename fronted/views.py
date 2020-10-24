from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import login as do_login
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from admin_drf.settings import base

# Create your views here.
@login_required(login_url='login')
def tasksList(request):
    context = {
    }
    return render(request, 'fronted/tasksList.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect(base.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        form = AuthenticationForm(data= request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                do_login(request, user)
                return redirect(base.LOGIN_REDIRECT_URL)

    return render(request, 'account/login.html')


def logout(request):
    do_logout(request)
    return redirect(base.ACCOUNT_LOGOUT_REDIRECT_URL)