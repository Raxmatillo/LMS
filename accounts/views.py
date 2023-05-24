from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout

from accounts.forms import NewUserForm

# Create your views here.


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Muafaqqiyatli ro'yhatdan o'tdingiz.")
            return redirect("home")
        messages.error(
            request, "Muvaffaqiyatsiz ro'yxatdan o'tish. Yaroqsiz maʼlumot.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


def login_request(request):
    msg = str()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(
                    request, "Foydalanuvchi nomi yoki parol noto‘g‘ri.")
                msg = "Foydalanuvchi nomi yoki parol noto‘g‘ri."
        else:
            messages.error(
                request, "Foydalanuvchi nomi yoki parol noto‘g‘ri..")
            msg = "Foydalanuvchi nomi yoki parol noto‘g‘ri."

    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form, "msg": msg})


def logout_request(request):
    logout(request)
    return redirect("login")
