# Django imports

from math import sin, cos, sqrt, atan2, radians, asin
import os
from django.db import models
from django.db.models import F
from django.contrib.auth import get_user_model
from datetime import date
import boto
from .models import Job, Application, Senior, Supporter

User = get_user_model()

boto_key = os.environ.get("BOTO_PUB_KEY")
boto_s_key = os.environ.get("BOTO_SECRET_KEY")

# conn = boto.connect_s3(boto_key, boto_s_key)
# bucket = conn.get_bucket('mobility-hack-new')
# k = Key(bucket)

def s3_delete(user_id, file_name):
    k.key = '/datasets/user_{0}/{1}'.format(user_id, file_name)
    k.delete()


def s3_upload(file, user_id, has_header, file_name):
    """Uploads a user's file to the user folder in S3"""

    k.key = '/datasets/user_{0}/{1}'.format(user_id, file_name)
    k.set_contents_from_filename(file_name)  # /from_file...


def get_trips_in_radius(radius, supporter_lat=0, supporter_lng=0):
    # get all jobs
    try:
        jobs = Job.objects.all()
    except IndexError:
        jobs = []

    jobs_in_range = {}
    for j in jobs:
        dist = haversine(j.lng, j.lat, supporter_lng, supporter_lat)
        if  dist <= radius:
            jobs_in_range[j.id] = dist
    return jobs_in_range

def haversine(lng_1, lat_1, lng_2, lat_2):

    lng_1, lat_1, lng_2, lat_2 = map(radians, [lng_1, lat_1, lng_2, lat_2])

    dlon = lng_2 - lng_1
    dlat = lat_2 - lat_1
    a = sin(dlat/2)**2 + cos(lat_1) * cos(lat_2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r

def average_rating(user):
    ratings = Rating.objects.filter(user=user)
    rating_sum = 0
    try:
        for it, r in enumerate(ratings):
            rating_sum += r.rating
    except Exception:
        return 3.0 #FIXME
    return rating_sum/(it+1)


def birthdate_to_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))



def get_trip_list_by_status(status, user_id, iterations=20):


    applications = Application.objects.filter(supporter_id=user_id).filter(application_status=status)

    i = 0

    cards_list = []
    for application in applications:

        trip = Job.objects.filter(id=application.job_id)[0]

        if i == iterations:
            break

        trip_dict = {}
        trip_dict["status"] = status
        trip_dict["trip_id"] = trip.id

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
            senior = Senior.objects.filter(id=trip.senior_id)[0]
            trip_dict["name"] = "{0} {1}".format(senior.first_name, senior.last_name)
            trip_dict["image_url"] = senior.profile_image
            trip_dict["age"] = birthdate_to_age(senior.birth_date)
        except IndexError:
            pass

        cards_list.append(trip_dict)

        i += 1

    return cards_list

def get_trip_list_by_status_senior(status, user_id, iterations=20):

    applications = Application.objects.filter(supporter_id=user_id).filter(application_status=status)

    trips = Job.objects.filter(senior_id=user_id).filter(status=status)

    i = 0

    cards_list = []
    for trip in trips:

        # trip = Job.objects.filter(id=application.job_id)[0]

        if i == iterations:
            break

        trip_dict = {}
        trip_dict["status"] = status
        trip_dict["trip_id"] = trip.id

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

        # try:
        #     senior = Senior.objects.filter(id=trip.senior_id)[0]
        #     trip_dict["name"] = "{0} {1}".format(senior.first_name, senior.last_name)
        #     trip_dict["image_url"] = senior.profile_image
        #     trip_dict["age"] = get_age(senior.birth_date)
        # except IndexError:
        #     pass

        cards_list.append(trip_dict)

        i += 1

    return cards_list
