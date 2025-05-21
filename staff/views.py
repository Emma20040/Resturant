from django.shortcuts import render, redirect
from .models import Food
from .forms import UploadLoadFood


# view to upload food
def upload_food(request):
    form= Food()
    if request.user =='POST':
        form = Food(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')
        
        else:
            form = Food()

    context = {'form':form}
    return render(request, 'staff/upload_food.html', context)

