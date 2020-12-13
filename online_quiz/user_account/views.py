from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password

from .forms import RegisterForm, LoginForm


class Register(View):
    def get(self, request):
        context = {'reg_form': RegisterForm}
        return render(request, 'user_account/register.html', context)

    def post(self, request):
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            user = reg_form.save(commit=False)
            user.password = make_password(reg_form.cleaned_data.get('password'))
            user.save()
            login(request, user)
            return redirect('quiz:list')
        else:
            context = {'reg_form': reg_form}
            return render(request, 'user_account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('account:login')


class LoginView(View):
    def get(self, request):
        return render(request, 'user_account/login.html', {'login_form': LoginForm})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data.get('email')
            password = login_form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('quiz:list')
        else:
            context = {'login_form': login_form}
            return render(request, 'user_account/login.html', context)