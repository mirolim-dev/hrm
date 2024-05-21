from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
# Create your views here.
def home(request):
    return render(request, 'demo/index.html')


def go_admin(request):
    phone, password = "+998999194675", "mr011012"
    User = get_user_model()
    _user = User.objects.get(phone=phone)
    _user = authenticate(phone=_user.phone, password=password)
    if _user is not None:
        login(request, _user)
        return redirect('/admin/')
    return redirect('home')


def actions(request):
    return render(request, 'demo/events.html')


def finance(request):
    return render(request, "demo/finance.html")


def staffs(request):
    return render(request, 'demo/staffs.html')