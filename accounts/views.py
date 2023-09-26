from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import UserForm
from accounts.models import User


def signup(request):
    if request.method == "POST":
        print(request.POST)
        form = UserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            account = form.save(commit=False)
            username = form.cleaned_data.get('username')
            nickname = form.cleaned_data.get('nickname')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, email=email, password=raw_password, nickname=nickname)
            if user is not None:
                login(request, user)
            account.save()
            return redirect('common:login')
    else:
        form = UserForm()
    return render(request, 'accounts/sign_up.html', {'form': form})
