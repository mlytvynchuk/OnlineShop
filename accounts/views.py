from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login

# Create your views here.
from django.urls import reverse

from accounts.forms import UserRegisterForm, UserLoginForm


def authview(request):
    login_form = UserLoginForm()
    form = UserRegisterForm()
    if request.method == "POST" and "sign_in" in request.POST:
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            # username = login_form.cleaned_data.get("username")
            # password = login_form.cleaned_data.get("password")
            # user = authenticate(username=username, password=password)
            # login(request,user)
            # login_form.save()
            user = login_form.get_user()
            login(request,user)

            message = "success"
            print("Success")
            # return HttpResponseRedirect("products:home")
            return redirect(reverse("orders:checkout"))


    elif request.method == "POST" and "sign_up" in request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, '%s %s' % ('Your account has been created. Please login as',username))
            user = form.save()
            # user = authenticate(username=username, password=password)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect(reverse('products:home'))

    return render(request, "login.html", context={'login_form':login_form,'reg_form':form})





@login_required
def logout(request):
    django_logout(request)
    messages.info(request,"You have logged out")
    return redirect(reverse('login'))