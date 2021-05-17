from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from .form import RegisterForm

# Create your views here.
def home(request):
    return HttpResponse('This is the home route')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data.get('username')
            return redirect(home)
    else:
        form = RegisterForm()

    return render (request, 'form1/register.html', {
        'form': form
    })
