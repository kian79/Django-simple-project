from django.shortcuts import render
from myApp.models import *
from myApp.forms import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index_render(request):
    return render(request, 'index.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def base_render(request):
    return render(request, 'base.html')


@login_required
def special(request):
    return HttpResponse("You are logged in!")


def register_render(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'registration.html',
                  {'profile_form': profile_form, 'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        print("amaaaad")
        username = request.POST.get('username')  # get username input name from form
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE!!!")
        else:
            print("some one failed logging in!")
            print("username : {} and password : {}".format(username, password))
            return HttpResponse("INVALID LOGIN DETAILS!")
    else:
        return render(request, 'login.html',)
