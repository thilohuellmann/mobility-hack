from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
import datetime
from accounts.forms import SignUpForm
from accounts.models import User

# create your views here

def SeniorSignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # save subscription info in backend
            login(request, user)
            now = datetime.datetime.now()
            today = now.date()
            next_month = today + datetime.timedelta(days=+30)

            return redirect('create_profile_senior')
            # return HttpResponseRedirect('/')

    else:
        # show message
        form = SignUpForm()

    return render(request, 'senior_signup.html', {'form': form})

def SupporterSignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            # save subscription info in backend
            login(request, user)
            now = datetime.datetime.now()
            today = now.date()
            next_month = today + datetime.timedelta(days=+30)

            return redirect('create_profile_supporter')
            # return HttpResponseRedirect('/')

    else:
        # show message
        form = SignUpForm()

    return render(request, 'supporter_signup.html', {'form': form})
