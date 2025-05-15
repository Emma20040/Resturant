from django.shortcuts import render, redirect
from .models import Customer
from django.contrib import messages
from .forms import Register, LoginForm, CustomerUserForm, CustomLoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpRequest, HttpResponseForbidden
# hompage view
def home_page(request):
    return render(request, 'base/about.html')

# view to signup users
def register(request):
    form = CustomerUserForm()
    if request.method =='POST':
        form = CustomerUserForm(request.POST)
        if form.is_valid():
            user =form.save(commit=False)
            user.save()
            
             # Specify the authentication backend when logging in
            backend = 'django.contrib.auth.backends.ModelBackend'  # custom backend
            login(request, user, backend=backend)
            
            return redirect('home')
        else:
            messages.error(request, 'invalid information, please enter your info again')
    context ={'form': form}
    return render(request, 'base/register.html', context)

# view for the login 
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data = request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('emial')

        user = authenticate(request, username=username, password = password, email = email)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, 'Invalid username/email or password.')

    form = CustomLoginForm(request.POST)
    context ={"form":form}
    return render(request, 'base/login.html', context)

def logout_view(request):
    # if request.method == 'POST':
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('home')