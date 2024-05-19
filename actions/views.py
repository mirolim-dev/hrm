from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
# Create your views here.
def home(request):
    if request.POST:
        phone, password = "+998999194675", "mr011012"
        User = get_user_model()
        _user = User.objects.get(phone=phone)
        print("USer1", _user)
        _user = authenticate(phone=_user.phone, password=password)
        print("USer", _user)
        if _user is not None:
            login(request, _user)
            return redirect('/admin/')
    return render(request, 'home.html')