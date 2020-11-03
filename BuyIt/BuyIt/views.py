from django.http import HttpResponse, HttpResponseRedirect 
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        context['form'] = LoginForm()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['form'] = LoginForm()
            return redirect("/")
        else:
            pass
    return render(request,"auth/login_page.html",context)

User = get_user_model()
def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form":form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        new_user = User.objects.create_user(username,email,password)
        context['form'] = RegisterForm()
        login(request, new_user)
        return redirect('/')
    return render(request,"auth/register_page.html",context)

def logout_page(request):
    logout(request)
    return redirect("/")