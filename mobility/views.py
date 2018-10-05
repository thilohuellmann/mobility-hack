from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from mobility.settings import *
from mobility.models import User, Senior, Supporter, Job, Rating, Application
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
    senior_id = 123 # models.Senior.objects.filter(user_id=user_id)[0]

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
    #senior_id = 123 # models.Senior.objects.filter(user_id=user_id)[0]

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

    jobs = utils.get_trips_in_radius()
    N_users = 10


    def generate_location():
        lat = float('50.40{}72'.format(choice(list(range(99)))))
        lng = float('7.61{}96'.format(choice(list(range(99)))))
        return lat, lng

    def generate_birthdate(kind='senior'):
        if kind == 'senior':
            year = choice(list(range(1928, 1945)))
        else:
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
            # Ratings for seniors
            for x_ in range(randind(10, 20)):
                rating = Rating.objects.create(user_id=user.user_id,
                                            rating=randint(3, 5))
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
                                        start_time_type=choice(['fixed', 'flexibel']),
                                        date=datetime.date(2018, 10, choice([5, 6, 7])),
                                        # time=datetime.time(randint(12, 22), 00, 00),
                                        time_slot=choice(['morning', 'noon', 'afternoon', 'evening']),
                                        )
                for ___ in range(randint(1, 3)):
                    user_ = User.objects.create(first_name=f.first_name(),
                                                last_name=f.last_name(),
                                                email=f.email())
                    sup_lat, sup_lng = generate_location()
                    supp = Supporter.objects.create(user_id=user_.user_id,
                                                    first_name=user_.first_name,
                                                    last_name=user_.last_name,
                                                    profile_image='https://source.unsplash.com/user/erondu',
                                                    gender=choice(['m', 'f']),
                                                    birth_date=generate_birthdate('supporter'),
                                                    lat=sup_lat,
                                                    lng=sup_lng,
                                                    bio=generate_bio(),
                                                    phone=generate_phone(),
                                                    radius=choice([1, 2, 5, 10]))
                    # Ratings for supporters
                    for x in range(randint(10, 20)):
                        rating_ = Rating.objects.create(user_id=user_.user_id,
                                                        rating=randint(3, 5))
                    app = Application.objects.create(job_id=job.id,
                                                     supporter_id=supp.user_id,
                                                     senior_id=senior.user_id,
                                                     application_status=choice(['applied', 'confirmed', 'rejected']))





    generate_seed()




    context = {
        "jobs": jobs
    }

    return render(request, 'mobility/discover_trips_supporter.html', context=context)

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
