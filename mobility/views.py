from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from mobility.settings import *
# from mobility.models import User, Senior, Supporter, Job, Rating, Application
from mobility import models
from faker import Faker
from random import choice, randint
import datetime
from mobility import forms
from mobility import models
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

    user_id = request.user.id
    senior_id = models.Senior.objects.filter(user_id=user_id)[0].id

    if request.method == 'POST':
        form = request.POST

        job_type = form['job_type']

        obj = models.Job.objects.create(
                    senior_id = senior_id,
                    rated = False,
                    status = 'draft',
                    job_type = job_type,
        )

        id = obj.id

        return HttpResponseRedirect('/senior/trip/create/step_2/' + str(id) )

    return render(request, 'mobility/trip_create_1_senior.html', context={})

@login_required
# @is_senior
def trip_create_2_senior(request, id):

    if request.method == 'POST':

        form = request.POST

        start_loc = form['start_location']
        end_loc = form['end_location']

        start_lat = form['start_lat']
        start_lng = form['start_lng']
        end_lat = form['end_lat']
        end_lng = form['end_lng']

        # update latest job object
        models.Job.objects.filter(id=id).update(
                                start_loc = start_loc,
                                end_loc = end_loc,
                                start_lat = start_lat,
                                start_lng = start_lng,
                                end_lat = end_lat,
                                end_lng = end_lng,
        )

        return HttpResponseRedirect('/senior/trip/create/step_3/' + str(id) )

    return render(request, 'mobility/trip_create_2_senior.html', context={})

@login_required
# @is_senior
def trip_create_3_senior(request, id):

    if request.method == 'POST':
        form = request.POST

        start_time_type = form['start_time_type']

        # update job object
        models.Job.objects.filter(id=id).update(start_time_type = start_time_type)

        if start_time_type == 'flexible':
            return HttpResponseRedirect('/senior/trip/create/step_4_2_1/' + str(id) )
        else: # == fixed
            return HttpResponseRedirect('/senior/trip/create/step_4_1/' + str(id) )

    return render(request, 'mobility/trip_create_3_senior.html', context={})

@login_required
# @is_senior
def trip_create_4_1_senior(request, id): # fixed
    if request.method == 'POST':
        form = request.POST

        date = form['date']

        dt_obj = datetime.datetime.strptime(date, '%b %d, %Y')
        django_date_format = dt_obj.strftime('%Y-%m-%d')

        # update job object
        models.Job.objects.filter(id=id).update(date=django_date_format)

        time = form['time']

        # update job object
        models.Job.objects.filter(id=id).update(time=time)

        return HttpResponseRedirect('/senior/trip/create/step_5/' + str(id) )

    return render(request, 'mobility/trip_create_4_1_senior.html', context={})

@login_required
# @is_senior
def trip_create_4_2_1_senior(request, id): # flexible
    if request.method == 'POST':
        form = request.POST

        date = form['date']

        dt_obj = datetime.datetime.strptime(date, '%b %d, %Y')
        django_date_format = dt_obj.strftime('%Y-%m-%d')

        models.Job.objects.filter(id=id).update(date=django_date_format)

        return HttpResponseRedirect('/senior/trip/create/step_4_2_2/' + str(id) )


    return render(request, 'mobility/trip_create_4_2_1_senior.html', context={})

@login_required
# @is_senior
def trip_create_4_2_2_senior(request, id): # time slot preference

    if request.method == 'POST':
        form = request.POST

        time_slot = form['time_slot']

        models.Job.objects.filter(id=id).update(time_slot=time_slot)

        return HttpResponseRedirect('/senior/trip/create/step_5/' + str(id) )

    return render(request, 'mobility/trip_create_4_2_2_senior.html', context={})

@login_required
# @is_senior
def trip_create_5_senior(request, id):

    trip = models.Job.objects.filter(id=id).values('job_type', 'start_loc', 'end_loc', 'start_time_type', 'date', 'time', 'time_slot')[0]

    # changes status from draft to pending
    if request.method == 'POST':
        models.Job.objects.filter(id=id).update(status='pending')

        return HttpResponseRedirect('/senior/creation_confirmation/' + str(id) )

    return render(request, 'mobility/trip_create_5_senior.html', context={'trip': trip})

@login_required
# @is_senior
def trip_creation_confirmation_senior(request, id):
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

    card_dict = {}

    for trip in trips:
        card_dict[trip.id] = {}
        trip_dict = card_dict[trip.id]
        trip_dict["trip"] = trip.job_type
        trip_dict["date"] = trip.date
        if trip.time != None:
            trip_dict["time"] = trip.time
        else:
            trip_dict["time_slot"] = trip.time_slot
            trip_dict["senior_id"] = trip.senior_id

            senior = models.Senior.objects.filter(id=trip.senior_id)[0]

            # trip_dict["name"] = user.first_name
            # trip_dict["image_url"] = user.profile_image

            context = {
            "trips": card_dict
            }
            year = choice(list(range(1985, 2000)))
        return datetime.date(year, 3, 13)

    def generate_bio():
        return choice(["Prone to fits of apathy. Creator. Beer fanatic. Lifelong tv lover. Certified food expert. Extreme zombie enthusiast.",
                        "Lifelong bacon advocate. Unapologetic tv geek. Travel scholar. Friendly gamer. Wannabe writer. Web practitioner.",
                        "Extreme coffee maven. Internet geek. Evil social media trailblazer. Travel nerd. Food aficionado.",
                        "Certified analyst. Infuriatingly humble internet guru. Tv junkie. Coffee buff. Extreme social media practitioner.",
                        "Hipster-friendly zombieaholic. Certified troublemaker. Thinker. Total introvert.",
                        "Certified twitter aficionado. Infuriatingly humble internet trailblazer. Professional tv fanatic. Web geek.",
                        "Web fanatic. Entrepreneur. Alcohol guru. Award-winning tv fanatic. Incurable reader. Food junkie. Music aficionado. Zombie lover. Hardcore travel expert."
                        "Certified writer. Beer enthusiast. Total introvert. Proud organizer. Hipster-friendly thinker.",
                        "Twitter buff. General pop culture practitioner. Award-winning coffee enthusiast. Bacon nerd. Infuriatingly humble problem solver.",
                        "Travel fanatic. Incurable problem solver. Beer fan. Professional pop culture ninja. Hardcore web advocate. Total thinker. Freelance tv fanatic."])

    def generate_phone():
        return '+' + str(randint(111111111, 999999999))

    f = Faker()

    def generate_seed():
      for _ in range(N_users):
          user = User.objects.create(first_name=f.first_name(),
                                     last_name=f.last_name(),
                                     email=f.email())

          profile = 0
          sen_lat, sen_lng = generate_location()
          senior = Senior.objects.create(user_id=user.id,
                                         first_name=user.first_name,
                                         last_name=user.last_name,
                                         profile_image='https://source.unsplash.com/user/erondu',
                                         birth_date=generate_birthdate('senior'),
                                         lat=sen_lat,
                                         lng=sen_lng,
                                         bio=generate_bio(),
                                         phone=generate_phone())
          for __ in range(3):
              job_lat, job_lng = generate_location()
              job = Job.objects.create(senior_id=senior.user_id,
                                       status=choice(['draft', 'pending',
                                                      'confirmed', 'done',
                                                      'expired']),
                                      job_type=choice(['one_way', 'round_trip']),
                                      start_lat=senior.lat,
                                      start_lng=senior.lng,
                                      end_lat=job_lat,
                                      end_lng=job_lng,
                                      start_time_type=choice(['fixed', 'flexible']),
                                      date=datetime.date(2018, 10, choice([5, 6, 7])),
                                      # time=datetime.time(randint(12, 22), 00, 00),
                                      time_slot=choice(['morning', 'noon', 'afternoon', 'evening']),
                                      )

    generate_seed()


    return render(request, 'mobility/discover_trips_supporter.html', context=context)

@login_required
# @is_supporter
def my_trips_supporter(request):
    return render(request, 'mobility/my_trips_supporter.html', context={})

@login_required
# @is_supporter
def trip_details_supporter(request, id):
    return render(request, 'mobility/trip_details_supporter.html', context={})

@login_required
# @is_supporter
def trip_application_confirmation_supporter(request, id):
    return render(request, 'mobility/trip_application_confirmation_supporter.html', context={})

@login_required
# @is_supporter
def profile_supporter_success(request):
    return render(request, 'mobility/profile_supporter_success.html', context={})
