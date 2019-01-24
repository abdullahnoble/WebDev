from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template.context import RequestContext
from django.views import generic
from .models import info
from .forms import Info_form


@login_required
def home(request):
    return render(request, 'mysite/home.html', context_instance=RequestContext(request))



from mysite.forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('mysite/home.html')
    else:
        form = SignUpForm()
    return render(request, 'mysite/signup.html', {'form': form})

def AddProfile(request):
    if request.method == "POST":
        form = Info_form(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            return redirect('mysite/prof_detail', pk=post.pk)
    else:
        form = Info_form()
    return render(request, 'mysite/form-template.html', {'form': form})




