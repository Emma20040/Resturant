from django.shortcuts import render, redirect
from .models import Customer
from .forms import Register, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest, HttpResponseForbidden
# hompage view
def home_page(request):
    return render(request, 'base/about.html')

# view to signup users
def register(request):
    form = Register()
    if request.method =='POST':
        form = Register(request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            user.save()
            return redirect('home')
    context ={'form': form}
    return render(request, 'base/register.html', context)

# view for the login 
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('emial')

        user = authenticate(request, username=username, password = password, email = email)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponseForbidden('invader')
    form = LoginForm(request.POST)
    context ={"form":form}
    return render(request, 'base/login.html', context)

def logout_view(request):
    # if request.method == 'POST':
    logout(request)
    return HttpResponse("Logout sucessfull")
        # return redirect('home')