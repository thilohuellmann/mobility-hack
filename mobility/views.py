from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from mobility.settings import *
from mobility import models
from faker import Faker
from random import choice, randint
import datetime
from mobility import forms
from mobility import models
from mobility import utils
import os
import itertools


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

    user_id = request.user.id
    senior_id = models.Senior.objects.get(user_id=request.user.id).id
    pending_status_applied = utils.get_trip_list_by_status_senior("pending", senior_id)
    confirmed_status_applied = utils.get_trip_list_by_status_senior("confirmed", senior_id)
    done_status_applied = utils.get_trip_list_by_status_senior("done", senior_id)
    expired_status_applied = utils.get_trip_list_by_status_senior("expired", senior_id)

    context = {
        "pending": pending_status_applied,
        "confirmed": confirmed_status_applied,
        "done": done_status_applied,
        "expired": expired_status_applied
    }

    return render(request, 'mobility/my_trips_senior.html', context=context)

@login_required
# @is_senior
def trip_details_senior(request):
    return render(request, 'mobility/trip_details_senior.html', context={})

@login_required
# @is_senior
def trip_create_1_senior(request):

    user_id = request.user.id

    if request.method == 'POST':
        form = request.POST

        job_type = form['job_type']

        models.Job.objects.create(
                    senior_id = senior_id,
                    rated = False,
                    status = 'draft',
                    job_type = job_type,
        )

        return HttpResponseRedirect('/senior/trip/create/step_2')

    return render(request, 'mobility/trip_create_1_senior.html', context={})

@login_required
# @is_senior
def trip_create_2_senior(request):
    #user_id = request.user.id

    # get latest created job
    #job_id = models.Job.objects.filter(senior_id=123).order_by('-created_at')[0]

    start = 'no start'

    if request.method == 'POST':
        form = request.POST
        start = form['start_lat'] + ',' + form['start_lng'] + ',' + form['end_lat'] + ',' + form['end_lng']

    return render(request, 'mobility/trip_create_2_senior.html', context={'start': start})

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

    user = request.user.id
    trips = models.Job.objects.all()

    cards_list = []

    iterations = 20
    i = 0

    for trip in trips:
        if i == iterations:
            break
        trip_dict = {}

            #trip_dict = card_dict[trip.id]
        trip_dict["trip"] = trip.job_type
        if trip.date == None:
            pass
        else:
            trip_dict["date"] = trip.date
        if trip.time != None:
            trip_dict["time"] = trip.time
            trip_dict["reward"] = round(8.5*3,2)
        elif trip.time_slot != None:
            trip_dict["time"] = trip.time_slot
        else:
            pass

        trip_dict["senior_id"] = trip.senior_id

        try:
            senior = models.Senior.objects.filter(id=trip.senior_id)[0]
            trip_dict["name"] = "{0} {1}".format(senior.first_name, senior.last_name)
            trip_dict["image_url"] = senior.profile_image
            trip_dict["age"] = utils.get_age(senior.birth_date)
        except IndexError:
            continue

        cards_list.append(trip_dict)

        i += 1

    context = {
        "trips": cards_list[:20]
    }

    return render(request, 'mobility/discover_trips_supporter.html', context=context)

@login_required
# @is_supporter
def my_trips_supporter(request):

    supporter_id = models.Supporter.objects.get(user_id=request.user.id).id

    application_status_applied = utils.get_trip_list_by_status("applied", supporter_id)
    confirmed_status_applied = utils.get_trip_list_by_status("confirmed", supporter_id)
    rejected_status_applied = utils.get_trip_list_by_status("rejected", supporter_id)

    context = {
        "applied": application_status_applied,
        "confirmed": confirmed_status_applied,
        "rejected": rejected_status_applied,
    }

    return render(request, 'mobility/my_trips_supporter.html', context=context)

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
