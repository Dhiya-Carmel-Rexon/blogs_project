from django.shortcuts import render,redirect
from .models import blogs
from .forms import Form

# Create your views here.

def home(request):
    posts = blogs.objects.all()
    context = {"p_no": posts}
    return render(request,'templates/home.html', context)

def basic(request):
    if request.method == 'POST':
        forms = Form(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('home')
    else:
        form = Form()
    
    return render(request, 'templates/basic.html',{'forms': forms})



