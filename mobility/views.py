from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from mobility import forms

from mobility import utils
import os

boto_key = os.environ.get("BOTO_PUB_KEY")
boto_s_key = os.environ.get("BOTO_SECRET_KEY")

def index(request):
    return render(request, 'mobility/index.html')

# # # # # # # # # # # # # # #
#                           #
#  SENIORS' VIEWS BEGIN     #
#                           #
# # # # # # # # # # # # # # #

@login_required
# @is_senior <-- implement decorator
def create_profile_senior(request):
    return render(request, 'mobility/create_profile_senior.html', context={})

@login_required
# @is_senior
def profile_senior(request):
    return render(request, 'mobility/profile_senior.html', context={})

@login_required
# @is_senior
def my_trips_senior(request):
    return render(request, 'mobility/my_trips_senior.html', context={})

@login_required
# @is_senior
def trip_details_senior(request):
    return render(request, 'mobility/trip_details_senior.html', context={})

@login_required
# @is_senior
def trip_create_1_senior(request):
    return render(request, 'mobility/trip_create_1_senior.html', context={})

@login_required
# @is_senior
def trip_create_2_senior(request):
    return render(request, 'mobility/trip_create_2_senior.html', context={})

@login_required
# @is_senior
def trip_create_3_senior(request):
    return render(request, 'mobility/trip_create_3_senior.html', context={})

@login_required
# @is_senior
def trip_create_4_1_senior(request):
    return render(request, 'mobility/trip_create_4_1_senior.html', context={})

@login_required
# @is_senior
def trip_create_4_2_1_senior(request):
    return render(request, 'mobility/trip_create_4_2_1_senior.html', context={})

@login_required
# @is_senior
def trip_create_4_2_2_senior(request):
    return render(request, 'mobility/trip_create_4_2_2_senior.html', context={})

@login_required
# @is_senior
def trip_create_5_senior(request):
    return render(request, 'mobility/trip_create_5_senior.html', context={})

@login_required
# @is_senior
def trip_creation_confirmation_senior(request):
    return render(request, 'mobility/trip_creation_confirmation_senior.html', context={})

# # # # # # # # # # # # # # #
#                           #
#  SUPPORTERS' VIEWS BEGIN  #
#                           #
# # # # # # # # # # # # # # #

@login_required
# @is_supporter
def create_profile_supporter(request):
    form = forms.SupporterProfileForm()
    user_id = request.user.id
    return render(request, 'mobility/create_profile_supporter.html', context={'form': form, 'user_id': user_id})

@login_required
# @is_supporter
def profile_supporter(request):
    return render(request, 'mobility/profile_supporter.html', context={})

@login_required
# @is_supporter
def discover_trips_supporter(request):
    return render(request, 'mobility/discover_trips_supporter.html', context={})

@login_required
# @is_supporter
def my_trips_supporter(request):
    return render(request, 'mobility/my_trips_supporter.html', context={})

@login_required
# @is_supporter
def trip_details_supporter(request):
    return render(request, 'mobility/trip_details_supporter.html', context={})

@login_required
# @is_supporter
def trip_application_confirmation_supporter(request):
    return render(request, 'mobility/trip_application_confirmation_supporter.html', context={})

@login_required
# @is_supporter
def profile_supporter_success(request):
    return render(request, 'mobility/profile_supporter_success.html', context={})
