from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import UserAuthForm
from django.contrib import messages
from django.contrib.auth.models import Group

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, "udało się zalogować")
            if user.groups.filter(name='manager').exists():
                return redirect("order_display:order_list")
            elif user.groups.filter(name='Worker').exists():
                return redirect("worker_app:order_list")
                
        else:
            messages.error(request, "nie poprawne hasło lub nazwa urzytkownika")
            form = UserAuthForm(request.POST)
            return render(request, 'users/login.html', {'login_form':form})
    else:
        form = UserAuthForm()
        return render(request, 'users/login.html', {'login_form':form})
    
    
def logout_view(request):
    logout(request)
    messages.success(request, "wylogowano")
    return redirect('users:login')
    
    
    